# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogoffice.CogOfficeSuitAttackBehavior
from direct.distributed.ClockDelta import globalClockDelta
from lib.coginvasion.cog.SuitAttackBehavior import SuitAttackBehavior
from lib.coginvasion.cog import SuitAttacks
import random

class CogOfficeSuitAttackBehavior(SuitAttackBehavior):

    def __init__(self, suit, target):
        SuitAttackBehavior.__init__(self, suit)
        self.target = target
        self.targetToon = self.suit.air.doId2do.get(target)
        self.maxAttacksPerSession = random.choice([1, 2])

    def unload(self):
        del self.targetToon
        SuitAttackBehavior.unload(self)

    def startAttacking(self, task=None):
        target = self.targetToon
        self.suit.b_setAnimState('neutral')
        self.suit.headsUp(target)
        attack = random.choice(self.suit.suitPlan.getAttacks())
        attackIndex = SuitAttacks.SuitAttackLengths.keys().index(attack)
        timestamp = globalClockDelta.getFrameNetworkTime()
        if self.suit.isDead():
            self.stopAttacking()
            return
        self.suit.sendUpdate('doAttack', [attackIndex, target.doId, timestamp])
        self.isAttacking = True
        self.attacksThisSession += 1
        self.attacksDone += 1
        self.ATTACK_COOLDOWN = SuitAttacks.SuitAttackLengths[attack]
        if self.attacksThisSession < self.maxAttacksPerSession:
            taskMgr.doMethodLater(self.ATTACK_COOLDOWN, self.startAttacking, self.suit.uniqueName('attackTask'))
        else:
            taskMgr.doMethodLater(self.ATTACK_COOLDOWN, self.stopAttacking, self.suit.uniqueName('finalAttack'))
        if task:
            return task.done