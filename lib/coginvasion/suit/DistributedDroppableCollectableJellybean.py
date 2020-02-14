# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.DistributedDroppableCollectableJellybean
from panda3d.core import VBase4, Vec3, Vec4, Point3
from direct.directnotify.DirectNotifyGlobal import directNotify
from DistributedDroppableCollectableJellybeans import DistributedDroppableCollectableJellybeans
from direct.interval.IntervalGlobal import SoundInterval, Sequence, LerpPosInterval, LerpHprInterval, Func
from direct.interval.MetaInterval import ParallelEndTogether
from direct.interval.LerpInterval import LerpColorScaleInterval
import random

class DistributedDroppableCollectableJellybean(DistributedDroppableCollectableJellybeans):
    notify = directNotify.newCategory('DistributedDroppableCollectableJellybean')

    def __init__(self, cr):
        DistributedDroppableCollectableJellybeans.__init__(self, cr)
        self.bean = None
        self.spinIval = None
        self.flyTrack = None
        self.tickSfx = None
        return

    def loadObject(self):
        self.removeObject()
        self.bean = loader.loadModel('phase_5.5/models/estate/jellyBean.bam')
        self.bean.setTwoSided(1)
        self.bean.setScale(1.5)
        self.bean.setZ(1.5)
        self.bean.reparentTo(self)
        self.bean.setColor(VBase4(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 1.0))
        self.spin()

    def removeObject(self):
        if self.bean:
            self.bean.removeNode()
            self.bean = None
        return

    def handleCollisions(self, entry):
        self.sendUpdate('requestGrab', [])

    def handlePickup(self, avId):
        avatar = self.cr.doId2do[avId]
        avatarGoneName = avatar.uniqueName('disable')
        self.accept(avatarGoneName, self.unexpectedExit)
        flyTime = 1.0
        self.stopSpin()
        self.spinIval = Sequence(LerpHprInterval(self.bean, duration=1.5, hpr=Vec3(360, 0, 0), startHpr=self.bean.getHpr()))
        self.spinIval.loop()
        self.actuallyCollect(avId, 1.2)
        track = ParallelEndTogether(Sequence(LerpPosInterval(self.bean, flyTime, pos=Point3(0, 0, 3), startPos=self.bean.getPos(avatar), blendType='easeInOut'), Func(self.bean.detachNode), Func(self.ignore, avatarGoneName)), LerpColorScaleInterval(self.bean, flyTime, Vec4(0, 0, 0, 0.1), Vec4(1, 1, 1, 1)))
        self.flyTrack = Sequence(track, name='treasureFlyTrack')
        self.bean.reparentTo(avatar)
        self.flyTrack.start()

    def actuallyCollect(self, avId, wait=None):
        DistributedDroppableCollectableJellybeans.handleCollisions(self, avId, wait)
        SoundInterval(self.tickSfx).start()

    def unexpectedExit(self):
        self.cleanupFlyTrack()

    def cleanupFlyTrack(self):
        if self.flyTrack:
            self.flyTrack.pause()
            self.flyTrack = None
        return

    def load(self):
        self.tickSfx = base.loadSfx('phase_3.5/audio/sfx/tick_counter.ogg')
        self.collectSfx = base.loadSfx('phase_3.5/audio/sfx/tt_s_gui_sbk_cdrSuccess.ogg')
        DistributedDroppableCollectableJellybeans.load(self)

    def unload(self):
        self.tickSfx = None
        self.stopSpin()
        self.cleanupFlyTrack()
        DistributedDroppableCollectableJellybeans.unload(self)
        return

    def spin(self):
        self.stopSpin()
        self.spinIval = LerpHprInterval(self.bean, duration=3.0, hpr=Vec3(360, 0, 0), startHpr=(0,
                                                                                                0,
                                                                                                0))
        self.spinIval.loop()

    def stopSpin(self):
        if self.spinIval:
            self.spinIval.finish()
            self.spinIval = None
        return