# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.DistributedObjectBase
from direct.showbase.DirectObject import DirectObject
from direct.directnotify import DirectNotifyGlobal

class DistributedObjectBase(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedObjectBase')

    def __init__(self, cr):
        self.cr = cr
        self.children = {}
        self.parentId = None
        self.zoneId = None
        return

    def getLocation(self):
        try:
            if self.parentId == 0 and self.zoneId == 0:
                return
            if self.parentId == 4294967295L and self.zoneId == 4294967295L:
                return
            return (self.parentId, self.zoneId)
        except AttributeError:
            return

        return

    def handleChildArrive(self, childObj, zoneId):
        pass

    def handleChildArriveZone(self, childObj, zoneId):
        pass

    def handleChildLeave(self, childObj, zoneId):
        pass

    def handleChildLeaveZone(self, childObj, zoneId):
        pass

    def handleQueryObjectChildrenLocalDone(self, context):
        pass

    def getParentObj(self):
        if self.parentId is None:
            return
        return self.cr.doId2do.get(self.parentId)

    def hasParentingRules(self):
        return self.dclass.getFieldByName('setParentingRules') != None

    def delete(self):
        pass