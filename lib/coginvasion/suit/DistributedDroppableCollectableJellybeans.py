# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.DistributedDroppableCollectableJellybeans
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.IntervalGlobal import SoundInterval
from DistributedDroppableCollectableObject import DistributedDroppableCollectableObject

class DistributedDroppableCollectableJellybeans(DistributedDroppableCollectableObject):
    notify = directNotify.newCategory('DistributedDroppableCollectableJellybeans')

    def __init__(self, cr):
        DistributedDroppableCollectableObject.__init__(self, cr)

    def handleCollisions(self, avId, wait=0):
        SoundInterval(self.collectSfx).start()
        DistributedDroppableCollectableObject.handleCollisions(self, avId, wait)

    def unload(self):
        self.collectSfx = None
        DistributedDroppableCollectableObject.unload(self)
        return