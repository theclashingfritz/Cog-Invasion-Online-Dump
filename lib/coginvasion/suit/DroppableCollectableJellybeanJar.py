# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.DroppableCollectableJellybeanJar
from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from DroppableCollectableJellybeans import DroppableCollectableJellybeans

class DroppableCollectableJellybeanJar(DroppableCollectableJellybeans):
    notify = directNotify.newCategory('DroppableCollectableJellybeanJar')

    def __init__(self):
        DroppableCollectableJellybeans.__init__(self)
        self.jar = None
        return

    def loadObject(self):
        self.removeObject()
        self.jar = loader.loadModel('phase_5.5/models/estate/jellybeanJar.bam')
        self.jar.setZ(1.5)
        self.jar.setTwoSided(1)
        self.jar.reparentTo(self)

    def removeObject(self):
        if self.jar:
            self.jar.removeNode()
            self.jar = None
        return

    def load(self):
        self.collectSfx = base.loadSfx('phase_3.5/audio/sfx/ci_s_money_bigBucks.ogg')
        DroppableCollectableJellybeans.load(self)