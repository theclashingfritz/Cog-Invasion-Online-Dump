# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.DroppableCollectableObject
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.DirectObject import DirectObject
from direct.controls.ControlManager import CollisionHandlerRayStart
from panda3d.core import *
from lib.coginvasion.globals import CIGlobals

class DroppableCollectableObject(DirectObject, NodePath):
    notify = directNotify.newCategory('DroppableCollectableObject')

    def __init__(self):
        NodePath.__init__(self, 'droppableCollectableObject')
        self.collSensorNodePath = None
        self.collRayNodePath = None
        return

    def loadObject(self):
        pass

    def removeObject(self):
        pass

    def loadCollisions(self):
        sphere = CollisionSphere(0, 0, 0, 1)
        sphere.setTangible(0)
        node = CollisionNode('objectCollNode')
        node.addSolid(sphere)
        node.setCollideMask(CIGlobals.WallBitmask)
        self.collSensorNodePath = self.attachNewNode(node)
        ray = CollisionRay(0.0, 0.0, CollisionHandlerRayStart, 0.0, 0.0, -1.0)
        rayNode = CollisionNode('objectRayNode')
        rayNode.addSolid(ray)
        rayNode.setFromCollideMask(CIGlobals.FloorBitmask)
        rayNode.setIntoCollideMask(BitMask32.allOff())
        self.collRayNodePath = self.attachNewNode(rayNode)
        lifter = CollisionHandlerFloor()
        lifter.addCollider(self.collRayNodePath, self)
        base.cTrav.addCollider(self.collRayNodePath, lifter)

    def removeCollisions(self):
        if self.collSensorNodePath:
            self.collSensorNodePath.removeNode()
            self.collSensorNodePath = None
        if self.collRayNodePath:
            self.collRayNodePath.removeNode()
            self.collRayNodePath = None
        return

    def load(self):
        print 'loading droppableCollectableObject'
        self.loadObject()
        self.loadCollisions()

    def unload(self):
        print 'unloading...'
        self.removeCollisions()
        self.removeObject()
        self.removeNode()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()