# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.Snowball
from panda3d.core import NodePath, CollisionNode, CollisionSphere, BitMask32, CollisionHandlerEvent
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.IntervalGlobal import ProjectileInterval
from direct.showbase.DirectObject import DirectObject
from lib.coginvasion.globals import CIGlobals

class Snowball(NodePath, DirectObject):
    notify = directNotify.newCategory('Snowball')

    def __init__(self, mg, index):
        self.mg = mg
        self.index = index
        self.model = None
        self.collNP = None
        self.isAirborne = False
        self.owner = None
        self.throwIval = None
        self.impactSound = base.loadSfx('phase_4/audio/sfx/snowball_hit.ogg')
        NodePath.__init__(self, 'snowball')
        return

    def load(self):
        self.model = loader.loadModel('phase_5/models/props/snowball.bam')
        self.model.reparentTo(self)
        base.audio3d.attachSoundToObject(self.impactSound, self)
        sphere = CollisionSphere(0, 0, 0, 0.35)
        sphere.setTangible(0)
        node = CollisionNode('snowball-coll-' + str(id(self)))
        node.addSolid(sphere)
        node.setFromCollideMask(CIGlobals.WallBitmask | CIGlobals.FloorBitmask)
        self.collNP = self.attachNewNode(node)
        self.collNP.setCollideMask(BitMask32(0))
        self.collNP.setZ(0.35)
        event = CollisionHandlerEvent()
        event.set_in_pattern('%fn-into')
        event.set_out_pattern('%fn-out')
        base.cTrav.add_collider(self.collNP, event)

    def setOwner(self, owner):
        self.owner = owner

    def getOwner(self):
        return self.owner

    def hasOwner(self):
        return self.owner is not None

    def b_throw(self):
        p = camera.getP(render)
        self.d_throw(p)
        self.throw(p)

    def d_throw(self, p):
        self.mg.sendUpdate('throw', [self.index, p])

    def throw(self, p):
        self.isAirborne = True
        self.owner.avatar.play('pie', partName='torso', fromFrame=60)
        base.playSfx(self.owner.throwSound, node=self.owner.avatar)
        start = NodePath('StartPath')
        start.reparentTo(self.owner.avatar)
        start.setScale(render, 1)
        start.setPos(0, 0, 0)
        start.setP(p)
        end = NodePath('ThrowPath')
        end.reparentTo(start)
        end.setScale(render, 1)
        end.setPos(0, 160, -90)
        end.setHpr(90, -90, 90)
        self.wrtReparentTo(render)
        self.setScale(1.0)
        self.throwIval = ProjectileInterval(self, startPos=self.owner.avatar.find('**/def_joint_right_hold').getPos(render), endPos=end.getPos(render), gravityMult=0.9, duration=3)
        self.throwIval.start()
        if self.owner.avId == base.localAvatar.doId:
            self.accept('snowball-coll-' + str(id(self)) + '-into', self.__handleSnowballCollision)
        start.removeNode()
        del start
        end.removeNode()
        del end

    def pauseThrowIval(self):
        if self.owner:
            if self.owner.throwSound:
                self.owner.throwSound.stop()
        if self.throwIval:
            self.throwIval.pause()
            self.throwIval = None
        return

    def handleHitWallOrPlayer(self):
        self.pauseThrowIval()
        self.reparentTo(render)
        self.setPos(self.mg.SnowballData[self.index])
        self.setHpr(0, 0, 0)
        self.isAirborne = False
        self.owner = None
        return

    def handleHitGround(self):
        self.pauseThrowIval()
        self.reparentTo(render)
        self.setZ(0.5)
        self.setHpr(0, 0, 0)
        self.isAirborne = False
        self.owner = None
        return

    def __handleSnowballCollision(self, entry):
        intoNP = entry.getIntoNodePath()
        avNP = intoNP.getParent()
        name = intoNP.getName()
        if 'barrier' in name:
            return
        self.ignore('snowball-coll-' + str(id(self)) + '-into')
        self.pauseThrowIval()
        if self.owner.avId == base.localAvatar.doId:
            self.mg.firstPerson.mySnowball = None
            self.mg.firstPerson.hasSnowball = False
        self.isAirborne = False
        self.owner = None
        base.playSfx(self.impactSound, node=self, volume=1.5)
        if 'wall' in name or 'fence' in name:
            self.mg.sendUpdate('snowballHitWall', [self.index])
            self.handleHitWallOrPlayer()
        else:
            if 'floor' in name or 'ground' in name or name == 'team_divider':
                self.mg.sendUpdate('snowballHitGround', [self.index])
                self.handleHitGround()
            else:
                for av in self.mg.remoteAvatars:
                    if av.avatar.getKey() == avNP.getKey():
                        self.handleHitWallOrPlayer()
                        friendly = int(av.team == self.mg.team)
                        if friendly:
                            av.unFreeze()
                        else:
                            av.freeze()
                        self.mg.sendUpdate('snowballHitPlayer', [av.avId, self.mg.team, self.index])

        return

    def b_pickup(self):
        self.d_pickup(self.mg.cr.localAvId)
        self.pickup(self.mg.getMyRemoteAvatar())

    def d_pickup(self, avId):
        self.mg.sendUpdate('snowballPickup', [self.index, avId])

    def pickup(self, remoteAv):
        self.setPosHpr(0, 0, 0, 0, 0, 0)
        self.reparentTo(remoteAv.avatar.find('**/def_joint_right_hold'))
        self.owner = remoteAv
        self.isAirborne = False

    def removeNode(self):
        self.pauseThrowIval()
        if self.model:
            self.model.removeNode()
            self.model = None
        if self.collNP:
            self.collNP.removeNode()
            self.collNP = None
        self.isAirborne = None
        self.owner = None
        self.mg = None
        NodePath.removeNode(self)
        return