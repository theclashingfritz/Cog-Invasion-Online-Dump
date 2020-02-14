# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.TossTrapGag
from lib.coginvasion.gags.TrapGag import TrapGag
from lib.coginvasion.globals import CIGlobals
from direct.particles.ParticleEffect import ParticleEffect
from direct.interval.IntervalGlobal import ProjectileInterval
from panda3d.core import NodePath, BitMask32, CollisionSphere, CollisionNode, CollisionHandlerEvent

class TossTrapGag(TrapGag):

    def __init__(self, name, model, damage, hitSfx, idleSfx=None, particlesFx=None, anim=None, wantParticles=True):
        TrapGag.__init__(self, name, model, damage, hitSfx, anim)
        self.wantParticles = wantParticles
        self.particles = None
        self.particlesFx = particlesFx
        self.idleSfx = None
        self.timeout = 5.0
        if game.process == 'client':
            if idleSfx:
                self.idleSfx = base.audio3d.loadSfx(idleSfx)
        return

    def startTrap(self):
        TrapGag.startTrap(self)
        if not self.gag:
            self.build()
            self.setHandJoint()
        self.gag.reparentTo(self.handJoint)
        self.avatar.play('toss', fromFrame=22)

    def build(self):
        TrapGag.build(self)
        self.buildParticles()
        self.setHandJoint()

    def buildParticles(self):
        self.cleanupParticles()
        if hasattr(self, 'wantParticles') and hasattr(self, 'particlesFx'):
            if self.wantParticles and self.particlesFx:
                self.particles = ParticleEffect()
                self.particles.loadConfig(self.particlesFx)

    def buildCollisions(self):
        TrapGag.buildCollisions(self)
        gagSph = CollisionSphere(0, 0, 0, 1)
        gagSph.setTangible(0)
        gagNode = CollisionNode('gagSensor')
        gagNode.addSolid(gagSph)
        gagNP = self.entity.attachNewNode(gagNode)
        gagNP.setScale(0.75, 0.8, 0.75)
        gagNP.setPos(0.0, 0.1, 0.5)
        gagNP.setCollideMask(BitMask32.bit(0))
        gagNP.node().setFromCollideMask(CIGlobals.FloorBitmask)
        event = CollisionHandlerEvent()
        event.setInPattern('%fn-into')
        event.setOutPattern('%fn-out')
        base.cTrav.addCollider(gagNP, event)
        self.avatar.acceptOnce('gagSensor-into', self.onCollision)

    def onCollision(self, entry):
        TrapGag.onCollision(self, entry)
        x, y, z = self.entity.getPos(render)
        base.localAvatar.sendUpdate('setGagPos', [self.getID(), x, y, z])

    def release(self):
        throwPath = NodePath('ThrowPath')
        throwPath.reparentTo(self.avatar)
        throwPath.setScale(render, 1)
        throwPath.setPos(0, 160, -120)
        throwPath.setHpr(0, 90, 0)
        if not self.gag:
            self.build()
        self.entity = self.gag
        self.gag = None
        self.entity.wrtReparentTo(render)
        self.entity.setHpr(throwPath.getHpr(render))
        self.setHandJoint()
        self.track = ProjectileInterval(self.entity, startPos=self.handJoint.getPos(render), endPos=throwPath.getPos(render), gravityMult=0.9, duration=3)
        self.track.start()
        if self.isLocal():
            self.startTimeout()
            self.buildCollisions()
            self.avatar.acceptOnce('gagSensor-into', self.onCollision)
        self.reset()
        TrapGag.release(self)
        return

    def delete(self):
        TrapGag.delete(self)
        self.cleanupParticles()

    def unEquip(self):
        TrapGag.unEquip(self)
        self.cleanupParticles()

    def cleanupParticles(self):
        if self.particles:
            self.particles.cleanup()
            self.particles = None
        return