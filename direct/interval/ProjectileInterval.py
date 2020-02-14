# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.interval.ProjectileInterval
__all__ = [
 'ProjectileInterval']
from panda3d.core import *
from panda3d.direct import *
from direct.directnotify.DirectNotifyGlobal import *
from Interval import Interval
from direct.showbase import PythonUtil

class ProjectileInterval(Interval):
    notify = directNotify.newCategory('ProjectileInterval')
    projectileIntervalNum = 1
    gravity = 32.0

    def __init__(self, node, startPos=None, endPos=None, duration=None, startVel=None, endZ=None, wayPoint=None, timeToWayPoint=None, gravityMult=None, name=None, collNode=None):
        self.node = node
        self.collNode = collNode
        if self.collNode:
            if isinstance(self.collNode, NodePath):
                self.collNode = self.collNode.node()
        if name == None:
            name = '%s-%s' % (self.__class__.__name__,
             self.projectileIntervalNum)
            ProjectileInterval.projectileIntervalNum += 1
        args = (startPos, endPos, duration, startVel, endZ,
         wayPoint, timeToWayPoint, gravityMult)
        self.implicitStartPos = 0
        if startPos is None:
            if duration is None:
                self.notify.error('must provide either startPos or duration')
            self.duration = duration
            self.trajectoryArgs = args
            self.implicitStartPos = 1
        else:
            self.trajectoryArgs = args
            self.__calcTrajectory(*args)
        Interval.__init__(self, name, self.duration)
        return

    def __calcTrajectory(self, startPos=None, endPos=None, duration=None, startVel=None, endZ=None, wayPoint=None, timeToWayPoint=None, gravityMult=None):
        if startPos is None:
            startPos = self.node.getPos()

        def doIndirections(*items):
            result = []
            for item in items:
                if callable(item):
                    item = item()
                result.append(item)

            return result

        startPos, endPos, startVel, endZ, gravityMult, wayPoint, timeToWayPoint = doIndirections(startPos, endPos, startVel, endZ, gravityMult, wayPoint, timeToWayPoint)
        self.startPos = startPos
        self.zAcc = -self.gravity
        if gravityMult:
            self.zAcc *= gravityMult

        def calcStartVel(startPos, endPos, duration, zAccel):
            if duration == 0:
                return Point3(0, 0, 0)
            return Point3((endPos[0] - startPos[0]) / duration, (endPos[1] - startPos[1]) / duration, (endPos[2] - startPos[2] - 0.5 * zAccel * duration * duration) / duration)

        def calcTimeOfImpactOnPlane(startHeight, endHeight, startVel, accel):
            return PythonUtil.solveQuadratic(accel * 0.5, startVel, startHeight - endHeight)

        def calcTimeOfLastImpactOnPlane(startHeight, endHeight, startVel, accel):
            time = calcTimeOfImpactOnPlane(startHeight, endHeight, startVel, accel)
            if not time:
                return None
            if type(time) == type([]):
                time = max(*time)
            return time

        if None not in (endPos, duration):
            self.duration = duration
            self.endPos = endPos
            self.startVel = calcStartVel(self.startPos, self.endPos, self.duration, self.zAcc)
        else:
            if None not in (startVel, duration):
                self.duration = duration
                self.startVel = startVel
                self.endPos = None
            else:
                if None not in (startVel, endZ):
                    self.startVel = startVel
                    time = calcTimeOfLastImpactOnPlane(self.startPos[2], endZ, self.startVel[2], self.zAcc)
                    if time is None:
                        self.notify.error('projectile never reaches plane Z=%s' % endZ)
                    self.duration = time
                    self.endPos = None
                else:
                    if None not in (wayPoint, timeToWayPoint, endZ):
                        self.startVel = calcStartVel(self.startPos, wayPoint, timeToWayPoint, self.zAcc)
                        time = calcTimeOfLastImpactOnPlane(self.startPos[2], endZ, self.startVel[2], self.zAcc)
                        if time is None:
                            self.notify.error('projectile never reaches plane Z=%s' % endZ)
                        self.duration = time
                        self.endPos = None
                    else:
                        self.notify.error('invalid set of inputs to ProjectileInterval')
        self.parabola = LParabola(VBase3(0, 0, 0.5 * self.zAcc), self.startVel, self.startPos)
        if not self.endPos:
            self.endPos = self.__calcPos(self.duration)
        return

    def __initialize(self):
        if self.implicitStartPos:
            self.__calcTrajectory(*self.trajectoryArgs)

    def testTrajectory(self):
        try:
            self.__calcTrajectory(*self.trajectoryArgs)
        except StandardError:
            return False

        return True

    def privInitialize(self, t):
        self.__initialize()
        if self.collNode:
            self.collNode.clearSolids()
            csolid = CollisionParabola(self.parabola, 0, 0)
            self.collNode.addSolid(csolid)
        Interval.privInitialize(self, t)

    def privInstant(self):
        self.__initialize()
        Interval.privInstant(self)
        if self.collNode:
            self.collNode.clearSolids()
            csolid = CollisionParabola(self.parabola, 0, self.duration)
            self.collNode.addSolid(csolid)

    def __calcPos(self, t):
        return self.parabola.calcPoint(t)

    def privStep(self, t):
        if self.node:
            if self.node.isEmpty():
                self.pause()
                return
        else:
            return
        self.node.setFluidPos(self.__calcPos(t))
        Interval.privStep(self, t)
        if self.collNode and self.collNode.getNumSolids() > 0:
            csolid = self.collNode.modifySolid(0)
            csolid.setT1(csolid.getT2())
            csolid.setT2(t)