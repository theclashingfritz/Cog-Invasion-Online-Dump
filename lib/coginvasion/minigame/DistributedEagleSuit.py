# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.DistributedEagleSuit
from panda3d.core import CollisionSphere, CollisionNode
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task import Task
from direct.actor.Actor import Actor
from direct.fsm.State import State
from direct.interval.IntervalGlobal import LerpPosInterval, Sequence, Wait, Func
from FlightProjectileInterval import FlightProjectileInterval
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.cog.DistributedSuit import DistributedSuit
from lib.coginvasion.npc.NPCWalker import NPCWalkInterval
import EagleGameGlobals as EGG, random

class DistributedEagleSuit(DistributedSuit):
    notify = directNotify.newCategory('DistributedEagleSuit')

    def __init__(self, cr):
        DistributedSuit.__init__(self, cr)
        self.eagleCry = base.audio3d.loadSfx('phase_5/audio/sfx/tt_s_ara_cfg_eagleCry.ogg')
        base.audio3d.attachSoundToObject(self.eagleCry, self)
        self.fallWhistle = base.audio3d.loadSfx('phase_5/audio/sfx/incoming_whistleALT.ogg')
        base.audio3d.attachSoundToObject(self.fallWhistle, self)
        self.explode = base.audio3d.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.ogg')
        base.audio3d.attachSoundToObject(self.explode, self)
        self.eventSphereNodePath = None
        self.fallingPropeller = None
        self.fallingPropProjectile = None
        self.mg = None
        self.flySpeed = 0.0
        return

    def enterNeutral(self, ts=0):
        self.show()
        self.timestampAnimTrack = Sequence(Wait(ts), Func(self.loop, 'flyNeutral'))
        self.timestampAnimTrack.start()

    def makeStateDict(self):
        self.suitFSM.addState(State('eagleFly', self.enterEagleFly, self.exitEagleFly))
        self.suitFSM.addState(State('eagleFall', self.enterEagleFall, self.exitEagleFall))
        self.stateIndex2suitState = {0: self.suitFSM.getStateNamed('off'), 
           1: self.suitFSM.getStateNamed('walking'), 
           2: self.suitFSM.getStateNamed('flyingDown'), 
           3: self.suitFSM.getStateNamed('flyingUp'), 
           4: self.suitFSM.getStateNamed('lured'), 
           5: self.suitFSM.getStateNamed('eagleFly'), 
           6: self.suitFSM.getStateNamed('eagleFall')}
        self.suitState2stateIndex = {}
        for stateId, state in self.stateIndex2suitState.items():
            self.suitState2stateIndex[state.getName()] = stateId

    def setFlySpeed(self, value):
        self.flySpeed = value

    def getFlySpeed(self):
        return self.flySpeed

    def enterEagleFly(self, startIndex, endIndex, ts=0.0):
        durationFactor = self.getFlySpeed()
        if startIndex > -1:
            startPos = EGG.EAGLE_FLY_POINTS[startIndex]
        else:
            startPos = self.getPos(render)
        endPos = EGG.EAGLE_FLY_POINTS[endIndex]
        if self.moveIval:
            self.moveIval.pause()
            self.moveIval = None
        self.moveIval = NPCWalkInterval(self, endPos, durationFactor=durationFactor, startPos=startPos, fluid=1)
        self.moveIval.start(ts)
        return

    def exitEagleFly(self):
        if self.moveIval:
            self.moveIval.pause()
            self.moveIval = None
        return

    def enterEagleFall(self, startIndex, endIndex, ts=0.0):
        self.moveIval = LerpPosInterval(self, duration=4.0, pos=self.getPos(render) - (0,
                                                                                       0,
                                                                                       75), startPos=self.getPos(render), blendType='easeIn')
        self.moveIval.start(ts)

    def exitEagleFall(self):
        if self.moveIval:
            self.moveIval.finish()
            self.moveIval = None
        return

    def fallAndExplode(self):
        self.cleanupPropeller()
        self.fallingPropeller = Actor('phase_4/models/props/propeller-mod.bam', {'chan': 'phase_4/models/props/propeller-chan.bam'})
        self.fallingPropeller.reparentTo(render)
        self.fallingPropeller.loop('chan', fromFrame=0, toFrame=3)
        parentNode = self.attachNewNode('fallingPropParentNode')
        h = random.randint(0, 359)
        parentNode.setH(h)
        dummyNode = parentNode.attachNewNode('dummyNode')
        dummyNode.setPos(0, 10, -50)
        self.fallingPropProjectile = FlightProjectileInterval(self.fallingPropeller, startPos=self.find('**/joint_head').getPos(render), endPos=dummyNode.getPos(render), duration=5.0, gravityMult=0.25)
        self.fallingPropProjectile.start()
        dummyNode.removeNode()
        del dummyNode
        parentNode.removeNode()
        del parentNode
        self.updateHealthBar(0)
        self.ignoreHit()
        base.playSfx(self.fallWhistle, node=self)
        taskMgr.doMethodLater(4.0, self.doExplodeSound, self.uniqueName('DEagleSuit-doExplodeSound'))

    def doExplodeSound(self, task):
        base.playSfx(self.explode, node=self)
        return Task.done

    def __initializeEventSphere(self):
        sphere = CollisionSphere(0, 0, 0, 2)
        sphere.setTangible(0)
        node = CollisionNode(self.uniqueName('DEagleSuit-eventSphere'))
        node.addSolid(sphere)
        node.setCollideMask(CIGlobals.WallBitmask)
        np = self.attachNewNode(node)
        np.setSz(2.5)
        np.setZ(5.5)
        self.eventSphereNodePath = np

    def removeEventSphere(self):
        if self.eventSphereNodePath:
            self.eventSphereNodePath.removeNode()
            self.eventSphereNodePath = None
        return

    def acceptHit(self):
        self.acceptOnce('enter' + self.eventSphereNodePath.node().getName(), self.__handleHit)

    def ignoreHit(self):
        self.ignore('enter' + self.eventSphereNodePath.node().getName())

    def __handleHit(self, entry):
        messenger.send(EGG.EAGLE_HIT_EVENT, [self.doId])

    def setSuit(self, arg, variant):
        DistributedSuit.setSuit(self, arg, 3)
        self.deleteShadow()
        self.disableBodyCollisions()
        self.disableRay()
        self.__initializeEventSphere()
        self.show()
        self.setAnimState('flyNeutral')

    def __doEagleCry(self, task):
        base.playSfx(self.eagleCry, node=self)
        task.delayTime = random.uniform(3, 30)
        return Task.again

    def announceGenerate(self):
        DistributedSuit.announceGenerate(self)
        taskMgr.doMethodLater(random.uniform(5, 25), self.__doEagleCry, self.uniqueName('DEagleSuit-doEagleCry'))
        self.acceptHit()

    def disable(self):
        self.ignoreHit()
        self.removeEventSphere()
        taskMgr.remove(self.uniqueName('DEagleSuit-doExplodeSound'))
        taskMgr.remove(self.uniqueName('DEagleSuit-doEagleCry'))
        if self.fallingPropProjectile:
            self.fallingPropProjectile.finish()
            self.fallingPropProjectile = None
        if self.fallingPropeller:
            self.fallingPropeller.cleanup()
            self.fallingPropeller = None
        base.audio3d.detachSound(self.fallWhistle)
        del self.fallWhistle
        base.audio3d.detachSound(self.explode)
        del self.explode
        base.audio3d.detachSound(self.eagleCry)
        del self.eagleCry
        self.mg = None
        DistributedSuit.disable(self)
        return