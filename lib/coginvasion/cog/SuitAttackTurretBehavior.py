# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cog.SuitAttackTurretBehavior
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.IntervalGlobal import Sequence, Wait, Func
from SuitHabitualBehavior import SuitHabitualBehavior
from SuitType import SuitType
import SuitAttacks, SuitUtils, SuitGlobals

class SuitAttackTurretBehavior(SuitHabitualBehavior):
    notify = directNotify.newCategory('SuitAttackTurretBehavior')
    MAX_DISTANCE = 40.0

    def __init__(self, suit):
        SuitHabitualBehavior.__init__(self, suit)
        self.isEntered = 0
        self.targetId = None
        self.target = None
        self.suitAttackTurretTrack = None
        self.air = self.suit.air
        self.mgr = self.suit.getManager()
        self.battle = self.mgr.getBattle()
        self.turretMgr = self.battle.getTurretManager()
        return

    def getSortedTurretList(self):
        turrets = self.turretMgr.turretId2turret.values()
        turrets.sort(key=lambda turret: turret.getDistance(self.suit))
        return turrets

    def enter(self):
        SuitHabitualBehavior.enter(self)
        self.target = self.getSortedTurretList()[0]
        self.targetId = self.target.doId
        taskMgr.add(self._doAttack, self.suit.uniqueName('doAttackTurret'))

    def _doAttack(self, task):
        if self.target.isEmpty():
            self.exit()
            return task.done
        attack = SuitUtils.attack(self.suit, self.target)
        distance = self.suit.getDistance(self.target)
        speed = 50.0
        if attack == 'glowerpower':
            speed = 100.0
        timeUntilRelease = distance / speed
        if attack != 'glowerpower':
            if self.suit.getSuit()[0].getSuitType() == SuitType.C:
                timeUntilRelease += 2.2
            else:
                timeUntilRelease += 3.0
        else:
            timeUntilRelease += 1.0
        hp = int(self.suit.getMaxHealth() / SuitAttacks.SuitAttackDamageFactors[attack])
        if self.suit.suitPlan.getName() == SuitGlobals.VicePresident:
            hp = int(200 / SuitAttacks.SuitAttackDamageFactors[attack])
        self.suitAttackTurretTrack = Sequence(Wait(timeUntilRelease), Func(self._damageTurret, hp))
        self.suitAttackTurretTrack.start()
        timeout = SuitAttacks.SuitAttackLengths[attack]
        task.delayTime = timeout
        return task.again

    def _damageTurret(self, damage):
        if not self.target.isEmpty():
            if not self.target.isDead():
                self.target.b_setHealth(self.target.getHealth() - damage)
                self.target.d_announceHealth(0, damage)
                self.suit.d_handleWeaponTouch()

    def exit(self):
        taskMgr.remove(self.suit.uniqueName('doAttackTurret'))
        if self.suitAttackTurretTrack:
            self.suitAttackTurretTrack.pause()
            self.suitAttackTurretTrack = None
        self.target = None
        self.targetId = None
        SuitHabitualBehavior.exit(self)
        return

    def unload(self):
        self.suitAttackTurretTrack = None
        self.target = None
        self.targetId = None
        self.air = None
        self.mgr = None
        self.battle = None
        self.turretMgr = None
        SuitHabitualBehavior.unload(self)
        return

    def shouldStart(self):
        turretList = self.getSortedTurretList()
        if len(turretList) == 0 or self.suit.getDistance(turretList[0]) > SuitAttackTurretBehavior.MAX_DISTANCE:
            return False
        return True