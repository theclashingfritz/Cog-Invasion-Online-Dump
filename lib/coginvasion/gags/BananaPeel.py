# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.BananaPeel
from lib.coginvasion.gags.ActivateTrapGag import ActivateTrapGag
from lib.coginvasion.gags import GagGlobals
from lib.coginvasion.globals import CIGlobals
from direct.interval.IntervalGlobal import Parallel, Sequence, Wait, LerpPosInterval, LerpScaleInterval, ActorInterval, SoundInterval
from panda3d.core import Point3

class BananaPeel(ActivateTrapGag):

    def __init__(self):
        ActivateTrapGag.__init__(self, CIGlobals.BananaPeel, 'phase_5/models/props/banana-peel-mod.bam', 10, GagGlobals.BANANA_SFX, 2.0, mode=1, anim='phase_5/models/props/banana-peel-chan.bam', activateSfx=GagGlobals.FALL_SFX, autoRelease=True)
        self.slipSfx = None
        self.setImage('phase_3.5/maps/banana-peel.png')
        if game.process == 'client':
            self.slipSfx = base.audio3d.loadSfx(GagGlobals.PIE_WOOSH_SFX)
        return

    def onActivate(self, entity, suit):
        ActivateTrapGag.onActivate(self, entity, suit)
        slidePos = entity.getPos(render)
        slidePos.setY(slidePos.getY() - 5.1)
        moveTrack = Sequence(Wait(0.1), LerpPosInterval(self.gag, 0.1, slidePos))
        animTrack = Sequence(ActorInterval(self.gag, 'banana', startTime=3.1), Wait(1.1), LerpScaleInterval(self.gag, 1, Point3(0.01, 0.01, 0.01)))
        suitTrack = ActorInterval(suit, 'slip-backward')
        soundTrack = Sequence(SoundInterval(self.slipSfx, duration=0.55, node=suit), SoundInterval(self.activateSfx, node=suit))
        Parallel(moveTrack, animTrack, suitTrack, soundTrack).start()

    def equip(self):
        ActivateTrapGag.equip(self)
        self.build()
        self.gag.reparentTo(self.handJoint)