# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.quest.CogObjective
from direct.directnotify.DirectNotifyGlobal import directNotify

class CogObjective:
    notify = directNotify.newCategory('CogObjective')

    def __init__(self, amount, level=None, levelRange=None, name=None, variant=None, dept=None):
        self.neededAmount = amount
        self.amount = 0
        self.level = level
        self.levelRange = levelRange
        self.name = name
        self.dept = dept
        self.variant = variant

    def handleCogDeath(self, cog):
        if not self.location or self.isOnLocation(cog.zoneId):
            if self.level and not cog.getLevel() == self.level:
                return
            if self.levelRange and not self.isInLevelRange(cog.getLevel()):
                return
            if self.name and not cog.getName() == self.name:
                return
            if self.dept and not cog.getDept() == self.dept:
                return
            if self.variant and not cog.getVariant() == self.variant:
                return
            self.amount += 1
            self.updateQuest()

    def finished(self):
        return self.amount == self.neededAmount

    def isInLevelRange(self, level):
        if self.levelRange:
            return self.levelRange[0] <= level and self.levelRange[1] >= level
        return False