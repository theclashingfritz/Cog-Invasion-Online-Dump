# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.DistancePhasedNode
from direct.showbase.DirectObject import DirectObject
from panda3d.core import *
from PhasedObject import PhasedObject

class DistancePhasedNode(PhasedObject, DirectObject, NodePath):
    notify = directNotify.newCategory('DistancePhasedObject')
    __InstanceSequence = 0
    __InstanceDeque = []

    @staticmethod
    def __allocateId():
        if DistancePhasedNode.__InstanceDeque:
            return DistancePhasedNode.__InstanceDeque.pop(0)
        id = DistancePhasedNode.__InstanceSequence
        DistancePhasedNode.__InstanceSequence += 1
        DistancePhasedNode.__InstanceSequence &= 65535
        return id

    @staticmethod
    def __deallocateId(id):
        DistancePhasedNode.__InstanceDeque.append(id)

    def __init__(self, name, phaseParamMap={}, autoCleanup=True, enterPrefix='enter', exitPrefix='exit', phaseCollideMask=BitMask32.allOn(), fromCollideNode=None):
        NodePath.__init__(self, name)
        self.phaseParamMap = phaseParamMap
        self.phaseParamList = sorted(phaseParamMap.items(), key=lambda x: x[1], reverse=True)
        PhasedObject.__init__(self, dict([ (alias, phase) for phase, alias in enumerate([ item[0] for item in self.phaseParamList ]) ]))
        self.__id = self.__allocateId()
        self.autoCleanup = autoCleanup
        self.enterPrefix = enterPrefix
        self.exitPrefix = exitPrefix
        self.phaseCollideMask = phaseCollideMask
        self.cTrav = base.cTrav
        self.fromCollideNode = fromCollideNode
        self._colSpheres = []
        self.reset()

    def __del__(self):
        self.__deallocateId(self.__id)

    def __repr__(self):
        outStr = 'DistancePhasedObject('
        outStr += '%s' % repr(self.getName())
        for param, value in zip(('phaseParamMap', 'autoCleanup', 'enterPrefix', 'exitPrefix',
                                 'phaseCollideMask', 'fromCollideNode'), ('{}', 'True',
                                                                          "'enter'",
                                                                          "'exit'",
                                                                          'BitMask32.allOn()',
                                                                          'None')):
            outStr += eval("(', " + param + " = %s' % repr(self." + param + "),'')[self." + param + ' == ' + value + ']')

        outStr += ')'
        return outStr

    def __str__(self):
        return "%s in phase '%s'" % (NodePath.__str__(self), self.getPhase())

    def cleanup(self):
        self.__disableCollisions(cleanup=True)
        for sphere in self._colSpheres:
            sphere.remove()

        self._colSpheres = []
        PhasedObject.cleanup(self)

    def setPhaseCollideMask(self, mask):
        self.phaseCollideMask = mask
        for sphere in self._colSpheres:
            self.colSphere.node().setIntoCollideMask(self.phaseCollideMask)

    def reset(self):
        self.cleanup()
        self.__oneTimeCollide()
        for name, dist in self.phaseParamList:
            cSphere = CollisionSphere(0.0, 0.0, 0.0, dist)
            cSphere.setTangible(0)
            cName = 'PhaseNode%s-%d' % (name, self.__id)
            cSphereNode = CollisionNode(cName)
            cSphereNode.setIntoCollideMask(self.phaseCollideMask)
            cSphereNode.setFromCollideMask(BitMask32.allOff())
            cSphereNode.addSolid(cSphere)
            cSphereNodePath = self.attachNewNode(cSphereNode)
            cSphereNodePath.stash()
            self._colSpheres.append(cSphereNodePath)

        if self.fromCollideNode:
            self.cTrav = CollisionTraverser()
            cHandler = CollisionHandlerEvent()
            cHandler.addInPattern(self.enterPrefix + '%in')
            cHandler.addOutPattern(self.exitPrefix + '%in')
            self.cTrav.addCollider(self.fromCollideNode, cHandler)
        self.__enableCollisions(-1)

    def setPhase(self, aPhase):
        phase = self.getAliasPhase(aPhase)
        PhasedObject.setPhase(self, aPhase)
        self.__disableCollisions()
        self.__enableCollisions(phase)
        if phase == -1 and self.autoCleanup:
            self.cleanup()
        else:
            self.__oneTimeCollide()

    def __getEnterEvent(self, phaseName):
        return '%sPhaseNode%s-%d' % (self.enterPrefix, phaseName, self.__id)

    def __getExitEvent(self, phaseName):
        return '%sPhaseNode%s-%d' % (self.exitPrefix, phaseName, self.__id)

    def __enableCollisions(self, phase):
        if 0 <= phase:
            phaseName = self.getPhaseAlias(phase)
            self.accept(self.__getExitEvent(phaseName), self.__handleExitEvent, extraArgs=[
             phaseName])
            self._colSpheres[phase].unstash()
        if 0 <= phase + 1 < len(self._colSpheres):
            phaseName = self.getPhaseAlias(phase + 1)
            self.accept(self.__getEnterEvent(phaseName), self.__handleEnterEvent, extraArgs=[
             phaseName])
            self._colSpheres[phase + 1].unstash()

    def __disableCollisions(self, cleanup=False):
        for x, sphere in enumerate(self._colSpheres):
            phaseName = self.getPhaseAlias(x)
            self.ignore(self.__getEnterEvent(phaseName))
            if x > 0 or not self.autoCleanup or cleanup:
                sphere.stash()
                self.ignore(self.__getExitEvent(phaseName))

    def __handleEnterEvent(self, phaseName, cEntry):
        self.setPhase(phaseName)

    def __handleExitEvent(self, phaseName, cEntry):
        phase = self.getAliasPhase(phaseName) - 1
        self.setPhase(phase)

    def __oneTimeCollide(self):
        if self.cTrav:
            if self.cTrav is base.cTrav:
                self.cTrav.traverse(render)
            else:
                self.cTrav.traverse(self)
            base.eventMgr.doEvents()


class BufferedDistancePhasedNode(DistancePhasedNode):
    notify = directNotify.newCategory('BufferedDistancePhasedObject')

    def __init__(self, name, bufferParamMap={}, autoCleanup=True, enterPrefix='enter', exitPrefix='exit', phaseCollideMask=BitMask32.allOn(), fromCollideNode=None):
        self.bufferParamMap = bufferParamMap
        self.bufferParamList = sorted(bufferParamMap.items(), key=lambda x: x[1], reverse=True)
        sParams = dict(bufferParamMap)
        for key in sParams:
            sParams[key] = sParams[key][0]

        DistancePhasedNode.__init__(self, name=name, phaseParamMap=sParams, autoCleanup=autoCleanup, enterPrefix=enterPrefix, exitPrefix=exitPrefix, phaseCollideMask=phaseCollideMask, fromCollideNode=fromCollideNode)

    def __repr__(self):
        outStr = 'BufferedDistancePhasedNode('
        outStr += '%s' % repr(self.getName())
        for param, value in zip(('bufferParamMap', 'autoCleanup', 'enterPrefix', 'exitPrefix',
                                 'phaseCollideMask', 'fromCollideNode'), ('{}', 'True',
                                                                          "'enter'",
                                                                          "'exit'",
                                                                          'BitMask32.allOn()',
                                                                          'None')):
            outStr += eval("(', " + param + " = %s' % repr(self." + param + "),'')[self." + param + ' == ' + value + ']')

        outStr += ')'
        return outStr

    def __str__(self):
        return "%s in phase '%s'" % (NodePath.__str__(self), self.getPhase())

    def setPhase(self, aPhase):
        DistancePhasedNode.setPhase(self, aPhase)
        phase = self.getAliasPhase(aPhase)
        self.__adjustCollisions(phase)

    def __adjustCollisions(self, phase):
        for x, sphere in enumerate(self._colSpheres[:phase + 1]):
            sphere.node().modifySolid(0).setRadius(self.bufferParamList[x][1][1])
            sphere.node().markInternalBoundsStale()

        for x, sphere in enumerate(self._colSpheres[phase + 1:]):
            sphere.node().modifySolid(0).setRadius(self.bufferParamList[x + phase + 1][1][0])
            sphere.node().markInternalBoundsStale()


if __debug__ and 0:
    cSphere = CollisionSphere(0, 0, 0, 0.1)
    cNode = CollisionNode('camCol')
    cNode.addSolid(cSphere)
    cNodePath = NodePath(cNode)
    cNodePath.reparentTo(base.cam)
    base.cTrav = CollisionTraverser()
    eventHandler = CollisionHandlerEvent()
    eventHandler.addInPattern('enter%in')
    eventHandler.addOutPattern('exit%in')
    base.cTrav.addCollider(cNodePath, eventHandler)
    p = BufferedDistancePhasedNode('p', {'At': (10, 20), 'Near': (100, 200), 'Far': (1000, 1020)}, autoCleanup=False, fromCollideNode=cNodePath)
    p.reparentTo(render)
    p._DistancePhasedNode__oneTimeCollide()
    base.eventMgr.doEvents()