# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.ActivateTrapGag
from lib.coginvasion.gags.TrapGag import TrapGag
from lib.coginvasion.gags.LocationGag import LocationGag
from lib.coginvasion.gags import GagGlobals
from lib.coginvasion.globals import CIGlobals
from direct.interval.IntervalGlobal import Sequence, SoundInterval, Wait, Func, LerpScaleInterval, ActorInterval, ProjectileInterval
from direct.task.Task import Task
from direct.actor.Actor import Actor
from panda3d.core import Point3, CollisionSphere, BitMask32, CollisionNode, CollisionHandlerEvent, NodePath

class ActivateTrapGag(TrapGag, LocationGag):

    def __init__(self, name, model, damage, hitSfx, collRadius, mode=0, anim=None, autoRelease=True, activateSfx=None):
        TrapGag.__init__(self, name, model, damage, hitSfx, anim, doesAutoRelease=autoRelease)
        LocationGag.__init__(self, 10, 50, shadowScale=0.25)
        self.trapMode = mode
        self.entities = []
        self.lifeTime = 120
        self.minSafeDistance = 5
        self.collRadius = collRadius
        self.activateSfx = None
        self.entityTrack = None
        if game.process == 'client':
            if activateSfx:
                self.activateSfx = base.audio3d.loadSfx(activateSfx)
        return

    def __clearEntity(self, entity, task):
        if entity:
            self.__doDustClear(entity)
        return Task.done

    def __doDustClear(self, entity):
        dustTrack = Sequence()
        dust = self.buildDust()
        dust.setBillboardPointEye()
        dust.setScale(Point3(0.1, 0.9, 1))
        dust.setPos(entity.getPos(render))
        entity.removeNode()
        self.removeEntity(entity)
        dustTrack.append(Func(dust.reparentTo, render))
        dustTrack.append(ActorInterval(dust, 'chan'))
        dustTrack.append(Func(dust.cleanup))
        dustTrack.start()

    def buildProjCollisions(self):
        gagSph = CollisionSphere(0, 0, 0, 1)
        gagSph.setTangible(0)
        gagNode = CollisionNode('projSensor')
        gagNode.addSolid(gagSph)
        gagNP = self.gag.attach_new_node(gagNode)
        gagNP.setScale(0.75, 0.8, 0.75)
        gagNP.setPos(0.0, 0.1, 0.5)
        gagNP.setCollideMask(BitMask32.bit(0))
        gagNP.node().setFromCollideMask(CIGlobals.FloorBitmask)
        event = CollisionHandlerEvent()
        event.set_in_pattern('%fn-into')
        event.set_out_pattern('%fn-out')
        base.cTrav.addCollider(gagNP, event)

    def buildCollisions(self):
        TrapGag.buildCollisions(self)
        gagSph = CollisionSphere(0, 0, 0, self.collRadius)
        gagSph.setTangible(0)
        gagNode = CollisionNode('gagSensor')
        gagNode.addSolid(gagSph)
        gagNP = self.gag.attachNewNode(gagNode)
        gagNP.setScale(0.75, 0.8, 0.75)
        gagNP.setPos(0.0, 0.1, 0.5)
        gagNP.setCollideMask(BitMask32.bit(0))
        gagNP.node().setFromCollideMask(CIGlobals.WallBitmask | CIGlobals.FloorBitmask)
        event = CollisionHandlerEvent()
        event.set_in_pattern('%fn-into')
        event.set_out_pattern('%fn-out')
        base.cTrav.addCollider(gagNP, event)
        if self.isLocal():
            self.avatar.accept('gagSensor-into', self.onCollision)

    def damageSuit(self, suit):
        if self.isLocal():
            suit.sendUpdate('hitByGag', [self.getID()])

    def onActivate(self, entity, suit):
        self.removeEntity(entity)

    def onProjCollision(self, entry):
        if not self.gag:
            self.build()
        x, y, z = self.gag.getPos(render)
        self.avatar.sendUpdate('setGagPos', [self.getID(), x, y, z])
        self.avatar.b_gagRelease(self.getID())

    def onCollision(self, entry):
        intoNP = entry.getIntoNodePath()
        avNP = intoNP.getParent()
        if self.avatar.doId == base.localAvatar.doId:
            for key in base.cr.doId2do.keys():
                obj = base.cr.doId2do[key]
                if obj.__class__.__name__ in CIGlobals.SuitClasses:
                    if obj.getKey() == avNP.getKey():
                        if obj.getHealth() > 0:
                            index = self.getEntityIndex(entry.getFromNodePath().getParent())
                            if not index == None:
                                self.avatar.b_trapActivate(self.getID(), self.avatar.doId, index, obj.doId)

        return

    def buildDust(self):
        dust = Actor('phase_5/models/props/dust-mod.bam', {'chan': 'phase_5/models/props/dust-chan.bam'})
        objBin = 110
        for cloudNum in range(1, 12):
            cloudName = '**/cloud' + str(cloudNum)
            cloud = dust.find(cloudName)
            cloud.setBin('fixed', objBin)
            objBin -= 10

        return dust

    def getSplicedLerpAnimsTrack(self, av, animName, origDuration, newDuration, startTime=0, fps=30):
        track = Sequence()
        addition = 0
        numIvals = int(origDuration * fps)
        timeInterval = newDuration / numIvals
        animInterval = origDuration / numIvals
        for _ in range(0, numIvals):
            track.append(Wait(timeInterval))
            track.append(ActorInterval(av, animName, startTime=startTime + addition, duration=animInterval))
            addition += animInterval

        return track

    def start(self):
        TrapGag.startTrap(self)
        if self.trapMode == 0:
            LocationGag.start(self, self.avatar)
        else:
            if self.trapMode == 1:
                if not self.gag:
                    self.build()
                    self.setHandJoint()
                self.gag.reparentTo(self.handJoint)
                self.avatar.play('toss', fromFrame=22)

    def startEntity(self):
        if self.entityTrack:
            self.entityTrack.pause()
            self.entityTrack = None
        if self.getLocation():
            x, y, z = self.getLocation()
            self.gag.setPos(x, y, z - 0.45)
        if not self.gag:
            self.build()
        self.gag.setScale(GagGlobals.PNT3NEAR0)
        self.gag.reparentTo(render)
        LerpScaleInterval(self.gag, 1.2, Point3(1.7, 1.7, 1.7)).start()
        track = Sequence(Wait(0.7))
        if self.isSafeLocation(self.gag):
            self.entities.append(self.gag)
            suits = []
            for obj in base.cr.doId2do.values():
                if obj.__class__.__name__ == 'DistributedSuit':
                    if obj.getPlace() == base.localAvatar.zoneId:
                        suits.append(obj)

            nearestCog = self.getClosestObject(self.gag, suits)
            suits = []
            if nearestCog and nearestCog.getDistance(self.gag) <= self.minSafeDistance:
                self.onActivate(self.gag, nearestCog)
            else:
                track.append(SoundInterval(self.hitSfx, duration=0.5, node=self.gag))
                base.taskMgr.doMethodLater(self.lifeTime, self.__clearEntity, 'Clear Entity', extraArgs=[self.gag], appendTask=True)
                self.gag = None
        else:
            self.cleanupGag()
            for ent in [self.gag, self.getClosestObject(self.gag, self.entities)]:
                if ent:
                    self.__doDustClear(ent)

        track.append(Func(self.completeTrap))
        track.start()
        self.entityTrack = track
        return

    def throw(self):
        if not self.gag and not self.isLocal():
            self.setHandJoint()
            self.build()
        if self.gag and self.getLocation():
            self.startEntity()
        else:
            if self.gag and self.trapMode == 1:
                throwPath = NodePath('ThrowPath')
                throwPath.reparentTo(self.avatar)
                throwPath.setScale(render, 1)
                throwPath.setPos(0, 160, -120)
                throwPath.setHpr(0, 90, 0)
                self.gag.setScale(self.gag.getScale(render))
                self.gag.reparentTo(render)
                self.gag.setHpr(throwPath.getHpr(render))
                self.setHandJoint()
                self.track = ProjectileInterval(self.gag, startPos=self.handJoint.getPos(render), endPos=throwPath.getPos(render), gravityMult=0.9, duration=3)
                self.track.start()
                self.buildProjCollisions()
                self.reset()
                self.avatar.acceptOnce('projSensor-into', self.onProjCollision)

    def completeTrap(self):
        LocationGag.complete(self)
        self.reset()

    def release(self):
        TrapGag.release(self)
        if self.trapMode == 0:
            LocationGag.release(self)
            self.build()
            self.buildCollisions()
            actorTrack = LocationGag.getActorTrack(self)
            if actorTrack:
                LocationGag.getSoundTrack(self).start()
                if self.isLocal():
                    actorTrack.append(Func(self.avatar.b_gagThrow, self.getID()))
                actorTrack.start()
        else:
            if self.trapMode == 1:
                self.startEntity()

    def setEndPos(self, x, y, z):
        LocationGag.setDropLoc(self, x, y, z + 0.25)

    def getClosestObject(self, entity, objects):
        distances = []
        entities = {}
        for ent in objects:
            entities.update({ent: ent.getDistance(entity) / 100})

        for dist in entities.values():
            distances.append(dist)

        distances.sort()
        for ent in entities.keys():
            if ent.getDistance(entity) / 100 == distances[0]:
                entities = {}
                distances = []
                return ent

    def isSafeLocation(self, entity):
        for ent in self.entities:
            distance = ent.getDistance(entity) / 100
            if distance < self.minSafeDistance:
                return False

        return True

    def getEntityIndex(self, entity):
        for i in range(len(self.entities)):
            ent = self.entities[i]
            if ent == entity:
                return i

    def removeEntity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)

    def getEntities(self):
        return self.entities

    def equip(self):
        TrapGag.equip(self)

    def unEquip(self):
        TrapGag.unEquip(self)
        LocationGag.cleanupLocationSeeker(self)