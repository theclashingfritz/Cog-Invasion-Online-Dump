# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cog.Suit
from lib.coginvasion.avatar.Avatar import Avatar
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.cog import SuitGlobals
from lib.coginvasion.cog import Variant
from lib.coginvasion.cog import Voice
from lib.coginvasion.cog.SuitAttacks import SuitAttacks
from lib.coginvasion.toon import ParticleLoader
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.IntervalGlobal import Sequence, Parallel, ActorInterval, SoundInterval, Wait, Func
from lib.coginvasion.distributed import DelayDelete
from direct.actor.Actor import Actor
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.showbase.Audio3DManager import Audio3DManager
from direct.task.Task import Task
from panda3d.core import Vec4, VBase4, Texture
import random

class Suit(Avatar):
    notify = directNotify.newCategory('Suit')
    audio3d = Audio3DManager(base.sfxManagerList[0], camera)
    audio3d.setDistanceFactor(25)
    audio3d.setDropOffFactor(audio3d.getDistanceFactor() / 1000)

    def __init__(self):
        Avatar.__init__(self)
        self.name = None
        self.dept = None
        self.suit = None
        self.head = None
        self.headModel = None
        self.variant = None
        self.handColor = None
        self.voice = None
        self.chat = None
        self.chatDial = None
        self.shadow = None
        self.propeller = None
        self.smallExp = None
        self.largeExp = None
        self.explosion = None
        self.hasSpawned = False
        self.suitTrack = None
        self.timestampAnimTrack = None
        self.propellerSounds = {}
        self.healthBar = None
        self.healthBarGlow = None
        self.condition = 0
        self.avatarType = CIGlobals.Suit
        self.suitPlan = None
        self.animFSM = ClassicFSM('Suit', [
         State('off', self.enterOff, self.exitOff),
         State('neutral', self.enterNeutral, self.exitNeutral),
         State('walk', self.enterWalk, self.exitWalk),
         State('die', self.enterDie, self.exitDie),
         State('win', self.enterWin, self.exitWin),
         State('attack', self.enterAttack, self.exitAttack),
         State('flail', self.enterFlail, self.exitFlail),
         State('flyDown', self.enterFlyDown, self.exitFlyDown),
         State('flyAway', self.enterFlyAway, self.exitFlyAway),
         State('flyNeutral', self.enterFlyNeutral, self.exitFlyNeutral),
         State('trayWalk', self.enterTrayWalk, self.exitTrayWalk),
         State('trayNeutral', self.enterTrayNeutral, self.exitTrayNeutral)], 'off', 'off')
        self.animFSM.enterInitialState()
        self.initializeBodyCollisions()
        return

    def getNametagJoints(self):
        return []

    def enterOff(self, ts=0):
        self.anim = None
        return

    def exitOff(self):
        pass

    def exitGeneral(self):
        self.stop()

    def enterTrayWalk(self, ts=0):
        self.show()
        self.loop('tray-walk')

    def exitTrayWalk(self):
        self.exitGeneral()

    def enterTrayNeutral(self, ts=0):
        self.loop('tray-neutral')

    def exitTrayNeutral(self):
        self.stop()

    def enterNeutral(self, ts=0):
        self.show()
        self.loop('neutral')

    def exitNeutral(self):
        self.exitTimestampAnimTrack()
        self.exitGeneral()

    def enterWalk(self, ts=0):
        self.show()
        self.loop('walk')
        self.disableShadowRay()

    def exitWalk(self):
        self.exitTimestampAnimTrack()
        self.exitGeneral()
        self.enableShadowRay()

    def enterFlail(self, ts=0):
        self.pingpong('flail', fromFrame=30, toFrame=35)

    def exitFlail(self):
        self.stop()

    def exitTimestampAnimTrack(self):
        if self.timestampAnimTrack:
            self.timestampAnimTrack.pause()
            self.timestampAnimTrack = None
        return

    def enterAttack(self, attack, target, ts=0):
        self.show()
        if hasattr(self, 'uniqueName'):
            doneEvent = self.uniqueName('suitAttackDone')
        else:
            doneEvent = 'suitAttackDone'
        self.suitAttackState = SuitAttacks(doneEvent, self, target)
        self.suitAttackState.load(attack)
        self.suitAttackState.enter(ts)
        self.headsUp(target)
        self.acceptOnce(doneEvent, self.handleSuitAttackDone)

    def handleSuitAttackDone(self):
        self.exitAttack()

    def exitAttack(self):
        if hasattr(self, 'uniqueName'):
            self.ignore(self.uniqueName('suitAttackDone'))
        else:
            self.ignore('suitAttackDone')
        if hasattr(self, 'suitAttackState'):
            self.suitAttackState.exit()
        if hasattr(self, 'suitAttackState'):
            self.suitAttackState.unload()
        if hasattr(self, 'suitAttackState'):
            del self.suitAttackState

    def interruptAttack(self):
        if hasattr(self, 'suitAttackState'):
            self.suitAttackState.currentAttack.interruptAttack()
            self.clearChatbox()

    def handleWeaponTouch(self):
        if hasattr(self, 'suitAttackState'):
            currentAttack = self.suitAttackState.currentAttack
            if hasattr(currentAttack, 'handleWeaponTouch'):
                currentAttack.handleWeaponTouch()

    def enterFlyNeutral(self, ts=0):
        self.disableRay()
        if not self.propeller:
            self.generatePropeller()
        sfx = self.propellerSounds['neutral']
        sfx.setLoop(True)
        base.playSfx(sfx, node=self)
        self.propeller.loop('chan', fromFrame=0, toFrame=3)
        self.setPlayRate(0.8, 'land')
        self.pingpong('land', fromFrame=0, toFrame=10)

    def exitFlyNeutral(self):
        self.cleanupPropeller()

    def enterFlyDown(self, ts=0):
        self.disableRay()
        if not self.propeller:
            self.generatePropeller()
        sfx = self.propellerSounds['in']
        base.playSfx(sfx, node=self)
        groundF = 28
        dur = self.getDuration('land')
        fr = self.getFrameRate('land')
        if fr:
            animTimeInAir = groundF / fr
        else:
            animTimeInAir = groundF
        impactLength = dur - animTimeInAir
        timeTillLanding = 6.5 - impactLength
        waitTime = timeTillLanding - animTimeInAir
        lastSpinFrame = 8
        propDur = self.propeller.getDuration('chan')
        fr = self.propeller.getFrameRate('chan')
        spinTime = lastSpinFrame / fr
        openTime = (lastSpinFrame + 1) / fr
        if hasattr(self, 'uniqueName'):
            name = self.uniqueName('enterFlyDown')
        else:
            name = 'enterFlyDown'
        animTrack = Sequence(Func(self.pose, 'land', 0), Wait(waitTime), ActorInterval(self, 'land', duration=dur))
        propTrack = Parallel(SoundInterval(sfx, duration=waitTime + dur, node=self), Sequence(ActorInterval(self.propeller, 'chan', constrainedLoop=1, duration=waitTime + spinTime, startTime=0.0, endTime=spinTime), ActorInterval(self.propeller, 'chan', duration=propDur - openTime, startTime=openTime)))
        self.suitTrack = Parallel(animTrack, propTrack, name=self.taskName('flyDown'))
        if not self.hasSpawned:
            self.show()
            fadeInTrack = Sequence(Func(self.setTransparency, 1), self.colorScaleInterval(1, colorScale=VBase4(1, 1, 1, 1), startColorScale=VBase4(1, 1, 1, 0)), Func(self.clearColorScale), Func(self.clearTransparency))
            self.hasSpawned = True
            self.suitTrack.append(fadeInTrack)
        self.suitTrack.setDoneEvent(self.suitTrack.getName())
        self.acceptOnce(self.suitTrack.getDoneEvent(), self.exitFlyDown)
        self.suitTrack.delayDelete = DelayDelete.DelayDelete(self, name)
        self.suitTrack.start(ts)

    def exitFlyDown(self):
        self.initializeRay(self.avatarType, 2)
        if self.suitTrack != None:
            self.ignore(self.suitTrack.getDoneEvent())
            self.suitTrack.finish()
            DelayDelete.cleanupDelayDeletes(self.suitTrack)
            self.suitTrack = None
        self.exitGeneral()
        self.cleanupPropeller()
        return

    def enterFlyAway(self, ts=0, doFadeOut=0):
        self.show()
        if not self.propeller:
            self.generatePropeller()
        sfx = self.propellerSounds['out']
        if hasattr(self, 'uniqueName'):
            name = self.uniqueName('enterFlyAway')
        else:
            name = 'enterFlyAway'
        dur = self.getDuration('land')
        actInt = ActorInterval(self, 'land', loop=0, startTime=dur, endTime=0.0)
        lastSpinFrame = 8
        propDur = self.propeller.getDuration('chan')
        fr = self.propeller.getFrameRate('chan')
        spinTime = lastSpinFrame / fr
        openTime = (lastSpinFrame + 1) / fr
        propTrack = Parallel(SoundInterval(sfx, node=self), Sequence(Func(self.propeller.show), ActorInterval(self.propeller, 'chan', endTime=openTime, startTime=propDur), ActorInterval(self.propeller, 'chan', constrainedLoop=1, duration=propDur - openTime, startTime=spinTime, endTime=0.0)))
        self.suitTrack = Parallel(actInt, propTrack, name=self.taskName('trackName'))
        if doFadeOut:
            fadeOut = Sequence(Wait(4.0), Func(self.setTransparency, 1), self.colorScaleInterval(1, colorScale=VBase4(1, 1, 1, 0), startColorScale=VBase4(1, 1, 1, 1)), Func(self.clearColorScale), Func(self.clearTransparency), Func(self.reparentTo, hidden))
            self.suitTrack.append(fadeOut)
        self.suitTrack.setDoneEvent(self.suitTrack.getName())
        self.acceptOnce(self.suitTrack.getDoneEvent(), self.exitFlyAway)
        self.suitTrack.delayDelete = DelayDelete.DelayDelete(self, name)
        self.suitTrack.start(ts)
        self.disableRay()

    def exitFlyAway(self):
        if self.suitTrack:
            self.ignore(self.suitTrack.getDoneEvent())
            self.suitTrack.finish()
            DelayDelete.cleanupDelayDeletes(self.suitTrack)
            self.suitTrack = None
        self.cleanupPropeller()
        self.exitGeneral()
        return

    def enterDie(self, ts=0):
        self.show()
        self.generateCog(isLose=1)
        self.nametag.clearChatText()
        self.deleteNameTag()
        deathSound = base.audio3d.loadSfx('phase_3.5/audio/sfx/Cog_Death_Full.ogg')
        base.audio3d.attachSoundToObject(deathSound, self)
        trackName = self.uniqueName('enterDie')
        smallGears = ParticleLoader.loadParticleEffect('phase_3.5/etc/gearExplosionSmall.ptf')
        smallGears.getParticlesNamed('particles-1').setPoolSize(30)
        singleGear = ParticleLoader.loadParticleEffect('phase_3.5/etc/gearExplosion.ptf')
        singleGear.getParticlesNamed('particles-1').setPoolSize(1)
        smallGearExplosion = ParticleLoader.loadParticleEffect('phase_3.5/etc/gearExplosion.ptf')
        smallGearExplosion.getParticlesNamed('particles-1').setPoolSize(10)
        bigGearExplosion = ParticleLoader.loadParticleEffect('phase_3.5/etc/gearExplosionBig.ptf')
        bigGearExplosion.getParticlesNamed('particles-1').setPoolSize(30)
        smallGears.setDepthWrite(False)
        singleGear.setDepthWrite(False)
        smallGearExplosion.setDepthWrite(False)
        bigGearExplosion.setDepthWrite(False)
        self.smallGears = smallGears
        self.smallGears.setPos(self.find('**/joint_head').getPos() + (0, 0, 2))
        self.singleGear = singleGear
        self.smallGearExp = smallGearExplosion
        self.bigGearExp = bigGearExplosion
        gearTrack = Sequence(Wait(0.7), Func(self.doSingleGear), Wait(1.5), Func(self.doSmallGears), Wait(3.0), Func(self.doBigExp))
        self.suitTrack = Parallel(Sequence(Wait(0.8), SoundInterval(deathSound, node=self, duration=deathSound.length() / 2)), Sequence(Wait(0.7), Func(self.doSingleGear), Wait(4.3), Func(self.suitExplode), Wait(1.0), Func(self.disableBodyCollisions), Func(self.__cleanupExplosion)), gearTrack, Sequence(ActorInterval(self, 'lose', duration=6), Func(self.getGeomNode().hide)), name=trackName)
        self.suitTrack.setDoneEvent(self.suitTrack.getName())
        self.acceptOnce(self.suitTrack.getName(), self.exitDie)
        self.suitTrack.delayDelete = DelayDelete.DelayDelete(self, trackName)
        self.suitTrack.start(ts)
        del deathSound

    def doSingleGear(self):
        self.singleGear.start(self.getGeomNode())

    def doSmallGears(self):
        self.smallGears.start(self.getGeomNode())

    def doSmallExp(self):
        self.smallGearExp.start(self.getGeomNode())

    def doBigExp(self):
        self.bigGearExp.start(self.getGeomNode())

    def suitExplode(self):
        self.explosion = loader.loadModel('phase_3.5/models/props/explosion.bam')
        self.explosion.setScale(0.5)
        self.explosion.reparentTo(render)
        self.explosion.setBillboardPointEye()
        if self.variant == Variant.SKELETON:
            self.explosion.setPos(self.getPart('body').find('**/joint_head').getPos(render) + (0,
                                                                                               0,
                                                                                               2))
        else:
            self.explosion.setPos(self.headModel.getPos(render) + (0, 0, 2))

    def __cleanupExplosion(self):
        if self.explosion:
            self.explosion.removeNode()
            self.explosion = None
        return

    def exitDie(self):
        if self.suitTrack != None:
            self.ignore(self.suitTrack.getName())
            self.suitTrack.finish()
            DelayDelete.cleanupDelayDeletes(self.suitTrack)
            self.suitTrack = None
        if hasattr(self, 'singleGear'):
            self.singleGear.cleanup()
            del self.singleGear
        if hasattr(self, 'smallGears'):
            self.smallGears.cleanup()
            del self.smallGears
        if hasattr(self, 'smallGearExp'):
            self.smallGearExp.cleanup()
            del self.smallGearExp
        if hasattr(self, 'bigGearExp'):
            self.bigGearExp.cleanup()
            del self.bigGearExp
        self.__cleanupExplosion()
        return

    def enterWin(self, ts=0):
        self.play('win')

    def exitWin(self):
        self.exitGeneral()

    def generate(self, suitPlan, variant, voice=None, hideFirst=True):
        self.suitPlan = suitPlan
        self.suit = suitPlan.getSuitType()
        self.head = suitPlan.getHead()
        self.dept = suitPlan.getDept()
        self.handColor = suitPlan.getHandColor()
        self.variant = variant
        self.setVoice(voice)
        self.generateCog()
        if hideFirst:
            self.hide()

    def __blinkRed(self, task):
        self.healthBar.setColor(SuitGlobals.healthColors[3], 1)
        self.healthBarGlow.setColor(SuitGlobals.healthGlowColors[3], 1)
        if self.condition == 5:
            self.healthBar.setScale(1.17)
        return Task.done

    def __blinkGray(self, task):
        if not self.healthBar:
            return
        self.healthBar.setColor(SuitGlobals.healthColors[4], 1)
        self.healthBarGlow.setColor(SuitGlobals.healthGlowColors[4], 1)
        if self.condition == 5:
            self.healthBar.setScale(1.0)
        return Task.done

    def generateHealthBar(self):
        self.removeHealthBar()
        button = loader.loadModel('phase_3.5/models/gui/matching_game_gui.bam').find('**/minnieCircle')
        button.setScale(3.0)
        button.setH(180)
        button.setColor(SuitGlobals.healthColors[0])
        chestNull = self.find('**/def_joint_attachMeter')
        if chestNull.isEmpty():
            chestNull = self.find('**/joint_attachMeter')
        button.reparentTo(chestNull)
        self.healthBar = button
        self.healthBarGlow = loader.loadModel('phase_3.5/models/props/glow.bam')
        self.healthBarGlow.reparentTo(self.healthBar)
        self.healthBarGlow.setScale(0.28)
        self.healthBarGlow.setPos(-0.005, 0.01, 0.015)
        self.healthBarGlow.setColor(SuitGlobals.healthGlowColors[0])
        button.flattenLight()
        self.condition = 0
        if hasattr(self, 'getHealth'):
            self.updateHealthBar(self.getHealth())

    def updateHealthBar(self, hp):
        if not self.healthBar:
            return
        if hp > self.health:
            self.health = hp
        health = 0.0
        try:
            health = float(hp) / float(self.maxHealth)
        except:
            pass

        if health > 0.95:
            condition = 0
        else:
            if health > 0.7:
                condition = 1
            else:
                if health > 0.3:
                    condition = 2
                else:
                    if health > 0.05:
                        condition = 3
                    else:
                        if health > 0.0:
                            condition = 4
                        else:
                            condition = 5
        if self.condition != condition:
            if condition == 4:
                blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.75), Task(self.__blinkGray), Task.pause(0.1))
                taskMgr.add(blinkTask, self.taskName('blink-task'))
            else:
                if condition == 5:
                    if self.condition == 4:
                        taskMgr.remove(self.taskName('blink-task'))
                    blinkTask = Task.loop(Task(self.__blinkRed), Task.pause(0.25), Task(self.__blinkGray), Task.pause(0.1))
                    taskMgr.add(blinkTask, self.taskName('blink-task'))
                else:
                    self.healthBar.setColor(SuitGlobals.healthColors[condition], 1)
                    self.healthBarGlow.setColor(SuitGlobals.healthGlowColors[condition], 1)
            self.condition = condition

    def removeHealthBar(self):
        if self.healthBar:
            self.healthBar.removeNode()
            self.healthBar = None
        if self.condition == 4 or self.condition == 5:
            taskMgr.remove(self.taskName('blink-task'))
        self.healthCondition = 0
        return

    def initializeLocalCollisions(self, name):
        self.notify.info('Initializing Local Collisions!')
        Avatar.initializeLocalCollisions(self, 1, 3, name)

    def initializeBodyCollisions(self):
        self.notify.info('Initializing Body Collisions!')
        Avatar.initializeBodyCollisions(self, self.avatarType, 6, 2)
        self.initializeRay(self.avatarType, 2)

    def hideSuit(self):
        self.hide()

    def showSuit(self):
        self.show()
        fadeIn = Sequence(Func(self.setTransparency, 1), self.colorScaleInterval(0.6, colorScale=Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0)), Func(self.clearColorScale), Func(self.clearTransparency), Func(self.reparentTo, render))
        fadeIn.start()

    def generateCog(self, isLose=0):
        self.cleanup()
        if not isLose:
            if self.variant == Variant.SKELETON or self.variant == Variant.ZOMBIE:
                self.loadModel('phase_5/models/char/cog%s_robot-zero.bam' % str(self.suit), 'body')
            else:
                self.loadModel('phase_3.5/models/char/suit%s-mod.bam' % str(self.suit), 'body')
            animations = SuitGlobals.animations
            anims = {}
            for anim in animations:
                if self.suit not in anim.getSuitTypes():
                    continue
                path = 'phase_%s/models/char/suit%s-%s.bam' % (anim.getPhase(), self.suit, anim.getFile())
                anims[anim.getName()] = path

            self.loadAnims(anims, 'body')
            self.generateHealthBar()
            self.generatePropeller()
        else:
            if self.variant == Variant.SKELETON or self.variant == Variant.ZOMBIE:
                self.loadModel('phase_5/models/char/cog%s_robot-lose-mod.bam' % str(self.suit), 'body')
            else:
                self.loadModel('phase_4/models/char/suit%s-lose-mod.bam' % str(self.suit), 'body')
            self.loadAnims({'lose': 'phase_4/models/char/suit%s-lose.bam' % str(self.suit)}, 'body')
        if self.variant != Variant.SKELETON:
            self.headModel = self.head.generate()
            self.headModel.reparentTo(self.find('**/joint_head'))
        if self.suitPlan.getName() == SuitGlobals.VicePresident:
            self.headModel.setScale(0.35)
            self.headModel.setHpr(270, 0, 270)
            self.headModel.setZ(-0.1)
            self.headModel.loop('neutral')
        self.setClothes()
        self.setAvatarScale(self.suitPlan.getScale() / SuitGlobals.scaleFactors[self.suit])
        self.setHeight(self.suitPlan.getHeight())
        self.setupNameTag()
        Avatar.initShadow(self)

    def cleanup(self):
        self.cleanupPropeller()
        self.clearChatbox()
        if self.shadow:
            self.deleteShadow()
        if self.getPart('body'):
            self.removePart('body')
        if self.headModel:
            self.headModel.removeNode()
            self.headModel = None
        self.timestampAnimTrack = None
        return

    def generatePropeller(self):
        self.cleanupPropeller()
        self.propeller = Actor('phase_4/models/props/propeller-mod.bam', {'chan': 'phase_4/models/props/propeller-chan.bam'})
        self.propeller.reparentTo(self.find('**/joint_head'))
        self.propellerSounds['in'] = self.audio3d.loadSfx(SuitGlobals.propellerInSfx)
        self.propellerSounds['out'] = self.audio3d.loadSfx(SuitGlobals.propellerOutSfx)
        self.propellerSounds['neutral'] = self.audio3d.loadSfx(SuitGlobals.propellerNeutSfx)
        for sound in self.propellerSounds.values():
            self.audio3d.attachSoundToObject(sound, self.propeller)

    def cleanupPropeller(self):
        for sound in self.propellerSounds.values():
            self.audio3d.detachSound(sound)
            sound.stop()

        self.propellerSounds = {}
        if self.propeller:
            self.propeller.cleanup()
            self.propeller = None
        return

    def setVoice(self, voice):
        if not voice:
            if self.variant == Variant.SKELETON or self.variant == Variant.ZOMBIE:
                self.voice = Voice.SKELETON
            else:
                self.voice = Voice.NORMAL
        else:
            self.voice = voice

    def setClothes(self):
        if self.variant == Variant.SKELETON:
            parts = self.findAllMatches('**/pPlane*')
            for partNum in range(0, parts.getNumPaths()):
                bb = parts.getPath(partNum)
                bb.setTwoSided(1)

            tie = loader.loadTexture('phase_5/maps/cog_robot_tie_%s.jpg' % self.dept.getTie())
            tie.setMinfilter(Texture.FTLinearMipmapLinear)
            tie.setMagfilter(Texture.FTLinear)
            self.find('**/tie').setTexture(tie, 1)
        else:
            prefix = 'phase_3.5/maps/' + self.dept.getClothingPrefix() + '_%s.jpg'
            if self.variant == Variant.WAITER:
                prefix = 'phase_3.5/maps/waiter_m_%s.jpg'
            self.find('**/legs').setTexture(loader.loadTexture(prefix % 'leg'), 1)
            self.find('**/arms').setTexture(loader.loadTexture(prefix % 'sleeve'), 1)
            self.find('**/torso').setTexture(loader.loadTexture(prefix % 'blazer'), 1)
            self.find('**/hands').setColor(self.handColor)

    def setName(self, nameString, charName):
        Avatar.setName(self, nameString, avatarType=self.avatarType, charName=charName, createNow=1)

    def setupNameTag(self, tempName=None):
        Avatar.setupNameTag(self, tempName=tempName)
        if self.nametag:
            if self.level > 0:
                self.nametag.setText(self.nametag.getText() + '\n%s\nLevel %s' % (self.dept.getName(), self.level))
            else:
                self.nametag.setText(self.nametag.getText() + '\n%s' % self.dept.getName())

    def setChat(self, chat):
        self.clearChatbox()
        Avatar.setChat(self, chat)
        self.chat = chat
        chatDial = None
        questionDial = self.voice.getSoundFile('question')
        question02Dial = None
        gruntDial = self.voice.getSoundFile('grunt')
        statementDial = self.voice.getSoundFile('statement')
        if self.voice == Voice.NORMAL:
            question02Dial = self.voice.getSoundFile('question_2')
        if '!' in self.chat:
            chatDial = self.audio3d.loadSfx(gruntDial)
        else:
            if '?' in self.chat:
                questionDials = [
                 questionDial]
                if self.voice == Voice.NORMAL:
                    questionDials.append(question02Dial)
                chatDial = self.audio3d.loadSfx(random.choice(questionDials))
            else:
                chatDial = self.audio3d.loadSfx(statementDial)
        self.chatDial = chatDial
        if self.variant == Variant.SKELETON:
            self.audio3d.attachSoundToObject(self.chatDial, self)
        else:
            self.audio3d.attachSoundToObject(self.chatDial, self.headModel)
        base.playSfx(self.chatDial, node=self)
        return

    def clearChatbox(self):
        self.clearChat()
        self.chat = None
        if self.chatDial:
            self.chatDial.stop()
            self.chatDial = None
        return

    def getDept(self):
        return self.dept

    def getVariant(self):
        return self.variant

    def disable(self):
        if self.suitTrack:
            self.suitTrack.finish()
            DelayDelete.cleanupDelayDeletes(self.suitTrack)
            self.suitTrack = None
        self.animFSM.requestFinalState()
        self.cleanup()
        Avatar.disable(self)
        return

    def delete(self):
        Avatar.delete(self)
        self.cleanup()