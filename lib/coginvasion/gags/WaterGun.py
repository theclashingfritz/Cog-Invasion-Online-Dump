# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.WaterGun
from panda3d.core import Point3, VBase3
from direct.interval.IntervalGlobal import Sequence, Parallel, Wait, Func, ActorInterval
from lib.coginvasion.globals import CIGlobals
from SquirtGag import SquirtGag
import GagGlobals

class WaterGun(SquirtGag):

    def __init__(self):
        SquirtGag.__init__(self, CIGlobals.WaterGun, 'phase_4/models/props/water-gun.bam', 12, GagGlobals.NULL_SFX, GagGlobals.WATERGUN_SFX, GagGlobals.NULL_SFX, 'squirt', 0, 0)
        self.setHealth(GagGlobals.WATERGLASS_HEAL)
        self.setImage('phase_3.5/maps/water-gun.png')
        self.anim = 'squirt'
        self.sprayScale = 0.2
        self.scale = 1.0
        self.holdTime = 0.0
        self.shootSfx = None
        self.timeout = 3.0
        return

    def build(self):
        SquirtGag.build(self)
        self.gag.setPos(Point3(0.28, 0.1, 0.08))
        self.gag.setHpr(VBase3(85.6, -4.44, 94.43))

    def start(self):
        SquirtGag.start(self)
        self.origin = self.getSprayStartPos()
        self.release()

    def release(self):
        if self.isLocal():
            self.startTimeout()

        def doSpray():
            if self.avatar.isEmpty():
                return
            self.sprayRange = self.avatar.getPos(render) + Point3(0, GagGlobals.SELTZER_RANGE, 0)
            self.doSpray(self.sprayScale, self.holdTime, self.sprayScale, horizScale=0.5, vertScale=0.5)
            if self.isLocal():
                base.localAvatar.sendUpdate('usedGag', [self.id])

        track = Parallel(Sequence(ActorInterval(self.avatar, 'squirt', startFrame=48, endFrame=58), Wait(1.0), ActorInterval(self.avatar, 'squirt', startFrame=107, endFrame=126, playRate=3)), Sequence(Wait(0.1), Func(doSpray)))
        track.start()
        self.tracks = track

    def getSprayStartPos(self):
        self.sprayJoint = self.gag.find('**/joint_nozzle')
        point = self.sprayJoint.getPos(render)
        return point