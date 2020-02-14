# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.TrapDoor
from lib.coginvasion.gags.ActivateTrapGag import ActivateTrapGag
from lib.coginvasion.gags import GagGlobals
from lib.coginvasion.globals import CIGlobals
from direct.interval.IntervalGlobal import Sequence, Parallel, Wait, Func, LerpScaleInterval, LerpPosInterval, SoundInterval, ActorInterval
from panda3d.core import Vec4, Point3

class TrapDoor(ActivateTrapGag):

    def __init__(self):
        ActivateTrapGag.__init__(self, CIGlobals.TrapDoor, 'phase_5/models/props/trapdoor.bam', 70, GagGlobals.TRAP_DOOR_SFX, 2.5, activateSfx=GagGlobals.FALL_SFX)
        self.setImage('phase_3.5/maps/trap-door.png')

    def onActivate(self, entity, suit):
        ActivateTrapGag.onActivate(self, entity, suit)
        x, y, z = entity.getPos(render)
        sinkPos = Point3(x, y, z - 9.1)
        dropPos = Point3(x, y, z + 15)
        landPos = Point3(x, y, z)
        suit.d_disableMovement()
        suit.setPos(x, y, z)
        entTrack = Sequence(Wait(0.4), Func(entity.setColor, Vec4(0, 0, 0, 1)), Wait(0.4), LerpScaleInterval(entity, 0.8, GagGlobals.PNT3NEAR0))
        suitTrack = Sequence(self.getSplicedLerpAnimsTrack(suit, 'flail', 0.7, 0.25), Wait(0.2), LerpPosInterval(suit, 0.4, sinkPos), Func(suit.setPos, dropPos), Func(suit.hide), ActorInterval(suit, 'neutral', duration=0.5), Wait(0.75), Func(suit.show), Parallel(LerpPosInterval(suit, 0.3, landPos), Func(suit.play, 'slip-forward')), SoundInterval(self.activateSfx, node=suit), Func(self.damageSuit, suit), Func(suit.d_enableMovement))
        soundTrack = Sequence(SoundInterval(self.hitSfx, node=suit), Wait(0.8))
        Parallel(entTrack, suitTrack, soundTrack).start()