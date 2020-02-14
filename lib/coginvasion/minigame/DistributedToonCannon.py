# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.DistributedToonCannon
from panda3d.core import Vec4
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedNode import DistributedNode
from direct.interval.IntervalGlobal import Sequence, Parallel, LerpScaleInterval, LerpColorScaleInterval, Func

class DistributedToonCannon(DistributedNode):
    notify = directNotify.newCategory('DistributedToonCannon')

    def __init__(self, cr):
        DistributedNode.__init__(self, cr)
        self.cannon = None
        self.avatarInTurret = None
        return

    def makeCannon(self):
        if self.cannon:
            self.cannon.removeNode()
            self.cannon = None
        self.cannon = loader.loadModel('phase_4/models/minigames/toon_cannon.bam')
        self.cannon.reparentTo(self)
        return

    def putAvatarInTurret(self, avId):
        av = self.cr.doId2do.get(avId)
        if av:
            av.getPart('legs').hide()
            av.getPart('torso').hide()
            av.getPart('head').show()

    def setBarrelOrientation(self, h, p):
        self.find('**/cannon').setHpr(h, p, 0)

    def d_setBarrelOrientation(self, h, p):
        self.sendUpdate('setBarrelOrientation', [h, p])

    def shoot(self):
        smoke = loader.loadModel('phase_4/models/props/test_clouds.bam')
        smoke.setBillboardPointEye()
        smoke.reparentTo(self.find('**/cannon'))
        smoke.setPos(0, 6, -3)
        smoke.setScale(0.5)
        smoke.wrtReparentTo(render)
        track = Sequence(Parallel(LerpScaleInterval(smoke, 0.5, 3), LerpColorScaleInterval(smoke, 0.5, Vec4(2, 2, 2, 0))), Func(smoke.removeNode))
        track.start()
        sfx = base.audio3d.loadSfx('phase_4/audio/sfx/MG_cannon_fire_alt.ogg')
        base.audio3d.attachSoundToObject(sfx, self)
        base.playSfx(sfx)

    def d_shoot(self):
        self.sendUpdate('shoot', [])

    def removeCannon(self):
        if self.cannon:
            self.cannon.removeNode()
            self.cannon = None
        return

    def announceGenerate(self):
        DistributedNode.announceGenerate(self)
        self.makeCannon()

    def disable(self):
        if self.avatarInTurret:
            self.avatarInTurret.getPart('legs').show()
            self.avatarInTurret.getPart('torso').show()
            self.avatarInTurret.getPart('head').show()
            self.avatarInTurret = None
        self.removeCannon()
        DistributedNode.disable(self)
        return