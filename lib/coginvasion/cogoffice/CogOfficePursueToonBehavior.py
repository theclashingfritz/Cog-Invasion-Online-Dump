# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogoffice.CogOfficePursueToonBehavior
from direct.directnotify.DirectNotifyGlobal import directNotify
from lib.coginvasion.cog.SuitPathBehavior import SuitPathBehavior
from lib.coginvasion.cog.SuitPursueToonBehavior import SuitPursueToonBehavior
import random

class CogOfficePursueToonBehavior(SuitPursueToonBehavior):
    notify = directNotify.newCategory('CogOfficePursueToonBehavior')

    def enter(self):
        SuitPathBehavior.enter(self)
        self.pickTarget()
        self.attackSafeDistance = random.uniform(5.0, 19.0)
        self.fsm.request('pursue')

    def pickTarget(self):
        avIds = list(self.suit.battle.avIds)
        avIds.sort(key=lambda avId: len(self.suit.battle.toonId2suitsTargeting[avId]))
        self.targetId = avIds[0]
        self.target = self.air.doId2do.get(self.targetId)
        self.suit.battle.toonId2suitsTargeting[self.targetId].append(self.suit.doId)

    def exit(self):
        if self.targetId is not None and self.targetId in self.suit.battle.toonId2suitsTargeting.keys() and self.suit.doId in self.suit.battle.toonId2suitsTargeting[self.targetId]:
            self.suit.battle.toonId2suitsTargeting[self.targetId].remove(self.suit.doId)
        SuitPursueToonBehavior.exit(self)
        return