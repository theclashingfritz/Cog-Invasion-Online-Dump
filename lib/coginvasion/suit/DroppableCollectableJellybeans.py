# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.DroppableCollectableJellybeans
from direct.directnotify.DirectNotifyGlobal import directNotify
from DroppableCollectableObject import DroppableCollectableObject

class DroppableCollectableJellybeans(DroppableCollectableObject):
    notify = directNotify.newCategory('DroppableCollectableJellybeans')

    def __init__(self):
        DroppableCollectableObject.__init__(self)

    def unload(self):
        self.collectSfx = None
        DroppableCollectableObject.unload(self)
        return