# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.DistributedNode
from pandac.PandaModules import NodePath
from direct.showbase.ShowBaseGlobal import *
from direct.task import Task
import GridParent, DistributedObject, types

class DistributedNode(DistributedObject.DistributedObject, NodePath):

    def __init__(self, cr):
        try:
            self.DistributedNode_initialized
        except:
            self.DistributedNode_initialized = 1
            self.gotStringParentToken = 0
            DistributedObject.DistributedObject.__init__(self, cr)
            if not self.this:
                NodePath.__init__(self, 'DistributedNode')
            self.gridParent = None

        return

    def disable(self):
        if self.activeState != DistributedObject.ESDisabled:
            if not self.isEmpty():
                self.reparentTo(hidden)
            DistributedObject.DistributedObject.disable(self)

    def delete(self):
        try:
            self.DistributedNode_deleted
        except:
            self.DistributedNode_deleted = 1
            if not self.isEmpty():
                self.removeNode()
            if self.gridParent:
                self.gridParent.delete()
            DistributedObject.DistributedObject.delete(self)

    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.gotStringParentToken = 0

    def setLocation(self, parentId, zoneId, teleport=0):
        DistributedObject.DistributedObject.setLocation(self, parentId, zoneId)
        parentObj = self.cr.doId2do.get(parentId)
        if parentObj:
            if parentObj.isGridParent() and zoneId >= parentObj.startingZone:
                if not self.gridParent:
                    self.gridParent = GridParent.GridParent(self)
                self.gridParent.setGridParent(parentObj, zoneId, teleport)
            elif self.gridParent:
                self.gridParent.delete()
                self.gridParent = None
        else:
            if self.gridParent:
                self.gridParent.delete()
                self.gridParent = None
        return

    def __cmp__(self, other):
        if self is other:
            return 0
        return 1

    def b_setParent(self, parentToken):
        if type(parentToken) == types.StringType:
            self.setParentStr(parentToken)
        else:
            self.setParent(parentToken)
        self.d_setParent(parentToken)

    def d_setParent(self, parentToken):
        if type(parentToken) == types.StringType:
            self.sendUpdate('setParentStr', [parentToken])
        else:
            self.sendUpdate('setParent', [parentToken])

    def setParentStr(self, parentTokenStr):
        if len(parentTokenStr) > 0:
            self.do_setParent(parentTokenStr)
            self.gotStringParentToken = 1

    def setParent(self, parentToken):
        justGotRequiredParentAsStr = not self.isGenerated() and self.gotStringParentToken
        if not justGotRequiredParentAsStr:
            if parentToken != 0:
                self.do_setParent(parentToken)
        self.gotStringParentToken = 0

    def do_setParent(self, parentToken):
        if not self.isDisabled():
            self.cr.parentMgr.requestReparent(self, parentToken)

    def d_setX(self, x):
        self.sendUpdate('setX', [x])

    def d_setY(self, y):
        self.sendUpdate('setY', [y])

    def d_setZ(self, z):
        self.sendUpdate('setZ', [z])

    def d_setH(self, h):
        self.sendUpdate('setH', [h])

    def d_setP(self, p):
        self.sendUpdate('setP', [p])

    def d_setR(self, r):
        self.sendUpdate('setR', [r])

    def setXY(self, x, y):
        self.setX(x)
        self.setY(y)

    def d_setXY(self, x, y):
        self.sendUpdate('setXY', [x, y])

    def setXZ(self, x, z):
        self.setX(x)
        self.setZ(z)

    def d_setXZ(self, x, z):
        self.sendUpdate('setXZ', [x, z])

    def d_setPos(self, x, y, z):
        self.sendUpdate('setPos', [x, y, z])

    def d_setHpr(self, h, p, r):
        self.sendUpdate('setHpr', [h, p, r])

    def setXYH(self, x, y, h):
        self.setX(x)
        self.setY(y)
        self.setH(h)

    def d_setXYH(self, x, y, h):
        self.sendUpdate('setXYH', [x, y, h])

    def setXYZH(self, x, y, z, h):
        self.setPos(x, y, z)
        self.setH(h)

    def d_setXYZH(self, x, y, z, h):
        self.sendUpdate('setXYZH', [x, y, z, h])

    def d_setPosHpr(self, x, y, z, h, p, r):
        self.sendUpdate('setPosHpr', [x, y, z, h, p, r])