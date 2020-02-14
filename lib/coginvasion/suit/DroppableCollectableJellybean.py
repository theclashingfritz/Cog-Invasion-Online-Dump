# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.DroppableCollectableJellybean
from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from DroppableCollectableJellybeans import DroppableCollectableJellybeans
from direct.interval.IntervalGlobal import *
import random

class DroppableCollectableJellybean(DroppableCollectableJellybeans):
    notify = directNotify.newCategory('DroppableCollectableJellybean')

    def __init__(self):
        DroppableCollectableJellybeans.__init__(self)
        self.bean = None
        self.spinIval = None
        self.collectSfx = base.loadSfx('phase_3.5/audio/sfx/ci_s_money_smallBucks.ogg')
        return

    def loadObject(self):
        self.removeObject()
        self.bean = loader.loadModel('phase_5.5/models/estate/jellyBean.bam')
        self.bean.setTwoSided(1)
        self.bean.setScale(1.5)
        self.bean.setZ(1.0)
        self.bean.reparentTo(self)
        self.bean.setColor(VBase4(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 1.0))
        self.spin()

    def removeObject(self):
        if self.bean:
            self.bean.removeNode()
            self.bean = None
        return

    def load(self):
        print 'loading droppableCollectableJellybean'
        self.collectSfx = base.loadSfx('phase_3.5/audio/sfx/ci_s_money_smallBucks.ogg')
        DroppableCollectableJellybeans.load(self)

    def unload(self):
        self.stopSpin()
        DroppableCollectableJellybeans.unload(self)

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