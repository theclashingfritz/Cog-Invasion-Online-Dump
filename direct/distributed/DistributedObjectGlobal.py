# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.DistributedObjectGlobal
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObject import DistributedObject

class DistributedObjectGlobal(DistributedObject):
    notify = directNotify.newCategory('DistributedObjectGlobal')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.parentId = 0
        self.zoneId = 0