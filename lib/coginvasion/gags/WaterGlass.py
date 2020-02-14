# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.WaterGlass
from panda3d.core import Point3
from direct.interval.IntervalGlobal import Sequence, Wait, Func
from lib.coginvasion.globals import CIGlobals
from SquirtGag import SquirtGag
import GagGlobals

class WaterGlass(SquirtGag):

    def __init__(self):
        SquirtGag.__init__(self, CIGlobals.WaterGlass, 'phase_5/models/props/glass-mod.bam', 8, GagGlobals.NULL_SFX, GagGlobals.NULL_SFX, GagGlobals.NULL_SFX, 'spit', 82, 110)
        self.setHealth(GagGlobals.WATERGLASS_HEAL)
        self.setImage('phase_3.5/maps/water-glass.png')
        self.anim = 'spit'
        self.sprayScale = 0.1
        self.scale = 3.5
        self.holdTime = 0.0
        self.spitSfx = None
        self.track = None
        self.timeout = 4.0
        return

    def delete(self):
        if self.track:
            self.track.pause()
            self.track = None
        SquirtGag.delete(self)
        return

    def start(self):
        SquirtGag.start(self)
        if self.isLocal():
            self.startTimeout()
        self.origin = self.getSprayStartPos()
        self.spitSfx = base.loadSfx(GagGlobals.SPIT_SFX)

        def playSpit():
            base.playSfx(self.spitSfx, node=self.avatar)

        self.track = Sequence(Wait(1.7), Func(playSpit), Wait(1.75), Func(self.release))
        self.track.start()

    def release(self):
        if self.avatar.isEmpty():
            return
        self.sprayRange = self.avatar.getPos(render) + Point3(0, GagGlobals.SELTZER_RANGE, 0)
        self.doSpray(self.sprayScale, self.holdTime, self.sprayScale, horizScale=0.3, vertScale=0.3)
        if self.isLocal():
            base.localAvatar.sendUpdate('usedGag', [self.id])

    def getSprayStartPos(self):
        self.sprayJoint = self.avatar.find('**/joint_head')
        if self.sprayJoint.isEmpty():
            self.sprayJoint = self.avatar.find('**/def_head')
        startNode = hidden.attachNewNode('pointInFrontOfHead')
        startNode.reparentTo(self.avatar)
        startNode.setPos(self.sprayJoint.getPos(self.avatar) + Point3(0, 0.3, -0.2))
        point = startNode.getPos(render)
        startNode.removeNode()
        del startNode
        return point