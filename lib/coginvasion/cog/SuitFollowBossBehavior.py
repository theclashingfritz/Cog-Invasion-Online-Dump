# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cog.SuitFollowBossBehavior
from lib.coginvasion.cog.SuitPathBehavior import SuitPathBehavior
from lib.coginvasion.cog.SuitHabitualBehavior import SuitHabitualBehavior
from lib.coginvasion.cog import SuitAttacks
from lib.coginvasion.globals import CIGlobals
from SuitFlyToRandomSpotBehavior import SuitFlyToRandomSpotBehavior
from SuitAttackBehavior import SuitAttackBehavior
import SuitPathDataAI, SuitUtils
from direct.fsm import ClassicFSM, State
from direct.task.Task import Task
from direct.interval.IntervalGlobal import Sequence, Wait, Func
from direct.distributed.ClockDelta import globalClockDelta
import random

class SuitFollowBossBehavior(SuitPathBehavior, SuitHabitualBehavior):
    LEEWAY_DISTANCE = 4
    MAX_BOSS_HELPERS = 5
    HEAL_SPEED = 50.0

    def __init__(self, suit, boss):
        SuitPathBehavior.__init__(self, suit, exitOnWalkFinish=False)
        self.fsm = ClassicFSM.ClassicFSM('SuitFollowBossBehavior', [State.State('off', self.enterOff, self.exitOff),
         State.State('follow', self.enterFollow, self.exitFollow),
         State.State('protect', self.enterProtect, self.exitProtect)], 'off', 'off')
        self.fsm.enterInitialState()
        self.boss = boss
        self.bossSpotKey = None
        self.healInProgress = False
        self.suitHealTrack = None
        self.followBossTaskName = self.suit.uniqueName('followBoss')
        self.pathFinder = SuitPathDataAI.getPathFinder(self.suit.hood)
        return

    def isHealing(self):
        return self.healInProgress

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enter(self):
        SuitPathBehavior.enter(self)
        self.fsm.request('follow')

    def exit(self):
        SuitPathBehavior.exit(self)
        self.fsm.requestFinalState()
        taskMgr.remove(self.followBossTaskName)

    def unload(self):
        SuitPathBehavior.unload(self)
        del self.boss
        del self.followBossTaskName
        del self.bossSpotKey
        del self.fsm
        del self.suitHealTrack
        del self.healInProgress

    def enterProtect(self):
        base.taskMgr.add(self.__protectTick, self.suit.uniqueName('protectBossTick'))

    def __protectTick(self, task):
        if self.boss.isDead():
            self.suit.b_setAnimState('neutral')
            self.exit()
            return task.done
        if self.bossSpotKey != self.boss.getCurrentPath():
            self.fsm.request('follow')
            return task.done
        if self.isHealing():
            return task.cont
        if self.boss.brain.currentBehavior.__class__ == SuitAttackBehavior:
            choice = random.randint(0, 1)
            if choice == 0:
                return task.cont
            if choice == 1:
                self.doHeal()
        return task.cont

    def __attemptToHealBoss(self, hp, currBossPos):
        if self.isBossAvailable():
            if (self.boss.getPos(render) - currBossPos).length() <= 1:
                self.boss.b_setHealth(self.boss.getHealth() + hp)
                self.boss.d_announceHealth(1, hp)
                self.suit.d_handleWeaponTouch()

    def isBossAvailable(self):
        if not self.boss.isEmpty() and not hasattr(self.boss, 'DELETED') and not self.boss.isDead():
            return True
        return False

    def __disableBoss(self):
        if self.isBossAvailable():
            if self.boss.getBrain():
                self.boss.getBrain().stopThinking()
            self.boss.b_setAnimState('neutral')

    def __enableBoss(self):
        if self.isBossAvailable():
            self.boss.getBrain().startThinking()

    def __toggleHeal(self):
        if self.healInProgress:
            self.healInProgress = False
        else:
            self.healInProgress = True

    def doHeal(self):
        self.__toggleHeal()
        attack = random.randint(0, 6)
        attackName = SuitAttacks.SuitAttackLengths.keys()[attack]
        timestamp = globalClockDelta.getFrameNetworkTime()
        self.suit.sendUpdate('doAttack', [attack, self.boss.doId, timestamp])
        distance = self.suit.getDistance(self.boss)
        timeUntilHeal = distance / self.HEAL_SPEED
        timeUntilRelease = 1.0
        self.suit.d_setChat(CIGlobals.SuitHealTaunt)
        hp = int(self.suit.maxHealth / SuitAttacks.SuitAttackDamageFactors[attackName])
        if hp == 0:
            hp = 1
        if self.boss.getHealth() + hp > self.boss.getMaxHealth():
            hp = self.boss.getMaxHealth() - self.boss.getHealth()
        if attackName != 'glowerpower':
            timeUntilRelease = 2.2
        self.suitHealTrack = Sequence(Wait(timeUntilRelease + timeUntilHeal), Func(self.__attemptToHealBoss, hp, self.boss.getPos(render)), Func(self.faceOtherDirection), Wait(3.0), Func(self.__toggleHeal))
        self.suitHealTrack.start()

    def faceOtherDirection(self):
        self.suit.b_setAnimState('neutral')
        self.suit.setH(self.suit.getH() - 180)
        self.suit.d_setH(self.suit.getH())

    def exitProtect(self):
        base.taskMgr.remove(self.suit.uniqueName('protectBossTick'))
        if self.suitHealTrack:
            self.suitHealTrack.pause()
            self.suitHealTrack = None
        return

    def enterFollow(self):
        self.__updatePath()
        taskMgr.add(self.__followBoss, self.followBossTaskName)

    def exitFollow(self):
        taskMgr.remove(self.followBossTaskName)

    def __updatePath(self):
        if self.boss.isDead():
            self.suit.b_setAnimState('neutral')
            self.exit()
            return task.done
        self.clearWalkTrack()
        if hasattr(self.boss, 'currentPath'):
            bossSpot = self.boss.getCurrentPath()
            self.bossSpotKey = bossSpot
            pos = self.boss.getPosFromCurrentPath()
            self.createPath(pos=(pos[0], pos[1]))
        else:
            self.exit()

    def __followBoss(self, task):
        if not hasattr(self, 'suit') or self.boss.isEmpty() or not self.boss.isEmpty() and self.boss.isDead():
            return Task.done
        if self.boss.getCurrentPath() != self.bossSpotKey:
            self.__updatePath()
        if self.suit.getDistance(self.boss) <= self.LEEWAY_DISTANCE and self.boss.brain.currentBehavior.__class__ != SuitFlyToRandomSpotBehavior:
            self.clearWalkTrack(andTurnAround=1)
            self.suit.b_setAnimState('neutral')
            self.suit.setH(self.suit.getH() - 180)
            self.suit.d_setH(self.suit.getH())
            self.fsm.request('protect')
            return Task.done
        return Task.cont

    def shouldAbandonFollow(self):
        suitsByBoss = self.getSuitsByBoss()
        backupCalledIn = self.getBackupCalledIn()
        if backupCalledIn == 0:
            backupCalledIn = 1
        return float(len(suitsByBoss)) / float(backupCalledIn) >= 0.4

    def getSuitsByBoss(self):
        suits = []
        for obj in base.air.doId2do.values():
            className = obj.__class__.__name__
            if className == 'DistributedSuitAI':
                if obj.zoneId == self.suit.zoneId:
                    if not obj.isDead() and not obj == self.boss and not obj == self.suit:
                        if obj.getDistance(self.boss) <= self.LEEWAY_DISTANCE * 3:
                            suits.append(obj)

        return suits

    def getBackupCalledIn(self):
        from lib.coginvasion.cog.SuitCallInBackupBehavior import SuitCallInBackupBehavior
        behaviorClass = SuitCallInBackupBehavior
        if hasattr(self.boss, 'DELETED') or not self.boss.getBrain():
            return 0
        behavior = self.boss.getBrain().getBehavior(behaviorClass)
        return behavior.getCalledInBackup()

    def isBossInManager(self):
        return self.boss in self.suit.getManager().suits.values()

    def shouldStart(self):
        if self.boss and not self.boss.isDead() and self.isBossInManager() and self.suit.getDistance(self.boss) > self.LEEWAY_DISTANCE:
            _helper_suits = 0
            for suit in self.suit.getManager().suits.values():
                if suit.doId != self.suit.doId:
                    if suit.brain:
                        if suit.brain.currentBehavior.__class__ == SuitFollowBossBehavior:
                            _helper_suits += 1

            if _helper_suits < self.MAX_BOSS_HELPERS:
                return True
        return False