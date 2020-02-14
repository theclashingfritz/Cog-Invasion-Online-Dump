# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.BambooCane
from lib.coginvasion.gags.ToonUpGag import ToonUpGag
from lib.coginvasion.gags import GagGlobals
from lib.coginvasion.globals import CIGlobals
from direct.interval.IntervalGlobal import Sequence, Wait, Func, Parallel, ActorInterval
from panda3d.core import Point3

class BambooCane(ToonUpGag):

    def __init__(self):
        ToonUpGag.__init__(self, CIGlobals.BambooCane, 'phase_5/models/props/cane.bam', 40, 45, 100, GagGlobals.BAMBOO_CANE_SFX, 1)
        self.setImage('phase_3.5/maps/bamboo-cane.png')
        self.hatPath = 'phase_5/models/props/hat.bam'
        self.hat = None
        self.track = None
        self.scaleDuration = 0.5
        self.scaleUp = None
        self.scaleDown = None
        self.soundInterval = None
        self.timeout = 5.0
        return

    def buildHat(self):
        self.cleanupHat()
        self.hat = loader.loadModel(self.hatPath)

    def cleanupHat(self):
        if self.hat:
            self.hat.removeNode()

    def buildScaleTracks(self):
        props = []
        props.append(self.hat)
        props.append(self.gag)
        self.scaleUp = self.getScaleTrack(props, self.scaleDuration, self.PNTNEARZERO, self.PNTNORMAL)
        self.scaleDown = self.getScaleTrack(props, self.scaleDuration, self.PNTNORMAL, self.PNTNEARZERO)

    def start(self):
        super(BambooCane, self).start()
        if not self.hat:
            self.buildHat()
        if not self.gag:
            self.build()
        self.setupHandJoints()
        if not self.scaleUp:
            self.buildScaleTracks()
        self.placeProp(self.handJoint, self.hat, Point3(0.23, 0.09, 0.69), Point3(180, 0, 0))
        self.placeProp(self.lHandJoint, self.gag, Point3(-0.28, 0.0, 0.14), Point3(0.0, 0.0, -150.0))
        self.soundInterval = self.getSoundTrack(0.2, self.gag, 6.4)
        propInterval = Sequence()
        propInterval.append(self.scaleUp)
        propInterval.append(Wait(base.localAvatar.getDuration('happy-dance') - 2))
        if self.avatar == base.localAvatar:
            propInterval.append(Func(self.setHealAmount))
            propInterval.append(Func(self.healNearbyAvatars, 25))
        propInterval.append(self.scaleDown)
        propInterval.append(Func(self.cleanupGag))
        propInterval.append(Func(self.reset))
        self.track = Parallel(propInterval, ActorInterval(self.avatar, 'happy-dance'), Func(self.soundInterval.start))
        self.track.start()

    def equip(self):
        super(BambooCane, self).equip()
        self.build()
        self.buildHat()
        self.buildScaleTracks()

    def unEquip(self):
        if self.track:
            self.soundInterval.finish()
            self.track.finish()
            self.track = None
        self.reset()
        if self.scaleDown:
            Sequence(self.scaleDown, Func(self.cleanupGag)).start()
        return

    def cleanupGag(self):
        if self.gag:
            self.gag.removeNode()
        self.cleanupHat()