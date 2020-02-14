# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.DistributedDroppableCollectableJellybeanJar
from direct.directnotify.DirectNotifyGlobal import directNotify
from DistributedDroppableCollectableJellybeans import DistributedDroppableCollectableJellybeans
from direct.interval.IntervalGlobal import SoundInterval

class DistributedDroppableCollectableJellybeanJar(DistributedDroppableCollectableJellybeans):
    notify = directNotify.newCategory('DistributedDroppableCollectableJellybeanJar')

    def __init__(self, cr):
        DistributedDroppableCollectableJellybeans.__init__(self, cr)
        self.jar = None
        self.tickSfx = None
        return

    def loadObject(self):
        self.removeObject()
        self.jar = loader.loadModel('phase_5.5/models/estate/jellybeanJar.bam')
        self.jar.setZ(1.0)
        self.jar.setTwoSided(1)
        self.jar.reparentTo(self)

    def removeObject(self):
        if self.jar:
            self.jar.removeNode()
            self.jar = None
        return

    def handleCollisions(self, entry):
        SoundInterval(self.tickSfx, startTime=0.05, volume=2.0).start()
        DistributedDroppableCollectableJellybeans.handleCollisions(self, base.localAvatar.doId)

    def load(self):
        self.tickSfx = base.loadSfx('phase_4/audio/sfx/MG_maze_pickup.ogg')
        self.collectSfx = base.loadSfx('phase_4/audio/sfx/MG_pos_buzzer.ogg')
        DistributedDroppableCollectableJellybeans.load(self)

    def unload(self):
        self.tickSfx = None
        DistributedDroppableCollectableJellybeans.unload(self)
        return