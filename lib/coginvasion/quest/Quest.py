# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.quest.Quest
from direct.directnotify.DirectNotifyGlobal import directNotify

class Quest:
    notify = directNotify.newCategory('Quest')

    def __init__(self, name, requirement, tier, reward):
        self.name = name
        self.requirement = requirement
        self.tier = tier
        self.reward = reward
        self.objectives = []
        self.completedObjectives = []
        self.currentObjective = None
        self.assignByStrangerDialog = []
        self.assignByOwnerDialog = []
        return

    def setObjectives(self, objectives):
        self.objectives = objectives

    def addObjective(self, objective):
        if objective:
            self.objectives.append(objective)
        else:
            self.notify.warning('Attempted to add a None objective to a quest!')

    def getNextObjective(self):
        objectiveIndex = self.getObjectiveIndex(self.currentObjective)
        if not self.currentObjective:
            if len(self.objectives) > 0:
                return self.objectives[0]
            self.notify.warning('Quest is empty and has no objectives!')
            return
        else:
            if objectiveIndex and len(self.objectives) - 1 != objectiveIndex:
                return self.objectives[objectiveIndex + 1]
        return

    def getCurrentObjective(self):
        return self.currentObjective

    def getCompletedObjectives(self):
        return self.completedObjectives

    def getObjectiveIndex(self, objective):
        return self.objectives.index(objective)

    def isCompleted(self):
        finishedObjectives = 0
        for objective in self.objectives:
            if objective.finished():
                finishedObjectives += 1

        return len(self.objectives) == finishedObjectives

    def getName(self):
        return self.name

    def getTier(self):
        return self.tier

    def getRequirement(self):
        return self.requirement

    def getReward(self):
        return self.reward