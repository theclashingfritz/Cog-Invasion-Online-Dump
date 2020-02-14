# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogtropolis.NURBSMopath
from panda3d.core import *

class NURBSMopath:

    def __init__(self, curve, name=None):
        if name == None:
            name = 'nurbsmopath'
        self.name = name
        self.duration = 1.0
        self.node = None
        self.loop = False
        self.cnpRef = None
        self.rope = None
        self.evaluator = None
        self.nurbs = None
        self.tDisplace = 0
        self.tCurrent = 0
        self.loopNum = 0
        if curve:
            if isinstance(curve, str):
                self.loadCurves(curve)
            elif isinstance(curve, NodePath):
                self.cnpRef = curve
                self.__extractCurves(curve)
            elif isinctance(curve, RopeNode):
                self.setCurve(curve)
        print self.name
        return

    def loadCurves(self, fname, parent=render):
        if self.cnpRef:
            self.cnpRef.detachNode()
        self.cnpRef = loader.loadModel(fname, noCache=True)
        self.cnpRef.reparentTo(parent)
        self.cnpRef.ls()
        if self.cnpRef:
            if not self.__extractCurves(self.cnpRef):
                print "NURBSMopath: can't find any curves in file: %s" % fname
        else:
            print 'NURBSMopath: no data in file: %s' % fname

    def setCurve(self, curve):
        self.rope = NodePath(curve)
        self.evaluator = curve.getCurve()
        self.nurbs = self.evaluator.evaluate()

    def __extractCurves(self, np):
        node = np.node()
        if isinstance(node, RopeNode):
            self.setCurve(node)
            return True
        for ch in np.getChildren():
            if self.__extractCurves(ch):
                return True

    def __playTask(self, task):
        start, stop = self.getRange()
        delta = stop - start
        scaled_duration = delta * self.duration
        self.loopNum = int(task.time / scaled_duration)
        if not self.loop and self.loopNum > 0:
            self.finish()
            messenger.send(self.name + '-done')
            self.node = None
            return task.done
        t = self.nurbs.getStartT() + (task.time - self.loopNum * scaled_duration) / self.duration + self.tDisplace
        self.tCurrent = t
        self.goto(t)
        return task.cont

    def getRange(self):
        if self.nurbs:
            return (self.nurbs.getStartT(), self.nurbs.getEndT())
        return (0, 0)

    def goto(self, t):
        if self.node:
            p = Point3()
            v = Vec3()
            self.nurbs.evalPoint(t, p)
            self.node.setPos(self.rope, p)
            self.nurbs.evalTangent(t, v)
            v = render.getRelativeVector(self.rope, v)
            self.node.lookAt(self.node.getPos() + v)

    def play(self, node, duration=1.0, resume=False, loop=False):
        if self.nurbs:
            if not resume:
                self.lastTime = 0
            self.node = node
            self.duration = duration
            self.loop = loop
            self.stop()
            t = taskMgr.add(self.__playTask, self.name + '-play')
        else:
            print 'NURBSMopath: has no curve.'

    def stop(self):
        self.tDisplace = self.tCurrent
        taskMgr.remove(self.name + '-play')

    def finish(self):
        start, stop = self.getRange()
        self.tDisplace = 0
        taskMgr.remove(self.name + '-play')