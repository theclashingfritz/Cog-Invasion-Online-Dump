# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.quests.QuestManagerBase
import Quests
from lib.coginvasion.globals import CIGlobals

class QuestManagerBase:

    def __init__(self):
        self.quests = {}

    def cleanup(self):
        del self.quests

    def getQuestAndIdWhereCurrentObjectiveIsToVisit(self, npcId):
        for questId, quest in self.quests.items():
            currObjective = quest.getCurrentObjective()
            if currObjective.type == Quests.VisitNPC:
                if currObjective.npcId == npcId:
                    return [questId, quest]
            elif currObjective.type == Quests.VisitHQOfficer:
                if CIGlobals.NPCToonDict[npcId][3] == CIGlobals.NPC_HQ:
                    return [questId, quest]

        return

    def makeQuestsFromData(self, avatar):
        for quest in self.quests.values():
            quest.cleanup()

        self.quests = {}
        questData = avatar.getQuests()
        for i in xrange(len(questData[0])):
            questId = questData[0][i]
            currentObjectiveIndex = questData[1][i]
            currentObjectiveProg = questData[2][i]
            quest = Quests.Quest(questId, currentObjectiveIndex, currentObjectiveProg, i)
            self.quests[questId] = quest