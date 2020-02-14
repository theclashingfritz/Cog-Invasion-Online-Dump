# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.quests.QuestManager
from direct.showbase.DirectObject import DirectObject
from lib.coginvasion.globals import CIGlobals
from QuestManagerBase import QuestManagerBase
import QuestNote, Quests, QuestGlobals
from lib.coginvasion.hood import ZoneUtil

class QuestManager(QuestManagerBase):

    def makeQuestsFromData(self):
        QuestManagerBase.makeQuestsFromData(self, base.localAvatar)

    def makeQuestNotes(self, quests=None):
        notes = []
        if not quests:
            quests = self.quests.values()
        for quest in quests:
            objective = quest.currentObjective
            note = QuestNote.QuestNote(quest.index)
            isDefeatObjective = objective.type in (Quests.DefeatCog, Quests.DefeatCogDept,
             Quests.DefeatCogInvasion, Quests.DefeatCogTournament, Quests.DefeatCogLevel)
            heading = None
            if isDefeatObjective:
                heading = Quests.DefeatText
            else:
                if objective.type in [Quests.VisitNPC, Quests.VisitHQOfficer]:
                    heading = Quests.VisitText
            note.setHeading(heading)
            taskInfo = None
            if isDefeatObjective:
                if objective.goal > 1:
                    taskInfo = '%d ' % objective.goal
                else:
                    taskInfo = 'a '
                if objective.type == Quests.DefeatCog:
                    if objective.subject == Quests.Any:
                        taskInfo += CIGlobals.Suits
                    elif objective.goal > 1:
                        taskInfo += QuestGlobals.makePlural(CIGlobals.SuitNames[objective.subject])
                    else:
                        taskInfo += CIGlobals.SuitNames[objective.subject]
                else:
                    if objective.type in (Quests.DefeatCogInvasion, Quests.DefeatCogTournament, Quests.DefeatCogDept):
                        if objective.goal > 1:
                            if objective.type == Quests.DefeatCogDept:
                                taskInfo += QuestGlobals.AbbrToDept[objective.subject]
                            elif objective.type == Quests.DefeatCogInvasion:
                                taskInfo += QuestGlobals.QuestSubjects[1]
                            elif objective.type == Quests.DefeatCogTournament:
                                taskInfo += QuestGlobals.QuestSubjects[6]
                        elif objective.type == Quests.DefeatCogDept:
                            taskInfo += QuestGlobals.makeSingular(QuestGlobals.AbbrToDept[objective.subject])
                        elif objective.type == Quests.DefeatCogInvasion:
                            taskInfo += QuestGlobals.makeSingular(QuestGlobals.QuestSubjects[1])
                        elif objective.type == Quests.DefeatCogTournament:
                            taskInfo += QuestGlobals.makeSingular(QuestGlobals.QuestSubjects[6])
                    else:
                        if objective.type == Quests.DefeatCogLevel:
                            if objective.goal > 1:
                                taskInfo += 'Level %d+ %s' % (objective.minCogLevel, CIGlobals.Suits)
                            else:
                                taskInfo += 'Level %d+ %s' % (objective.minCogLevel, CIGlobals.Suit)
                if objective.area == Quests.Any:
                    taskInfo += '\nAnywhere'
                else:
                    taskInfo += '\nin ' + ZoneUtil.getHoodId(objective.area)
            else:
                if objective.type == Quests.VisitNPC:
                    nameOfNPC = CIGlobals.NPCToonNames[objective.npcId]
                    placeOfNPC = CIGlobals.zone2TitleDict[objective.npcZone][0]
                    taskInfo = nameOfNPC + '\nat ' + placeOfNPC
                else:
                    if objective.type == Quests.VisitHQOfficer:
                        taskInfo = 'an HQ Officer\nat a Toon HQ'
            note.setTaskInfo(taskInfo)
            progress = ''
            if isDefeatObjective:
                if not objective.isComplete():
                    if isDefeatObjective:
                        progress = '%d of %d ' % (objective.progress, objective.goal) + QuestGlobals.makePastTense(Quests.DefeatText)
                        note.setProgress(progress)
                else:
                    note.setCompleted(1)
            else:
                if objective.type == Quests.VisitNPC:
                    streetZone = ZoneUtil.getBranchZone(objective.npcZone)
                    if streetZone % 1000 >= 100:
                        streetName = CIGlobals.BranchZone2StreetName[streetZone]
                    else:
                        streetName = 'the Playground'
                    hoodName = ZoneUtil.getHoodId(streetZone, 1)
                    progress = 'on %s\nin %s' % (streetName, hoodName)
                    note.setProgress(progress)
                else:
                    if objective.type == Quests.VisitHQOfficer:
                        progress = 'Any Street\nAny Playground'
                        note.setProgress(progress)
            reward = ''
            if quest.rewardType == Quests.RewardJellybeans:
                reward = 'For %d jellybeans'
            else:
                if quest.rewardType == Quests.RewardHealth:
                    reward = 'For a %d point Laff boost'
                else:
                    if quest.rewardType == Quests.RewardAccess:
                        reward = 'For access to %s'
                    else:
                        if quest.rewardType == Quests.RewardNone:
                            reward = 'For no reward'
            if '%s' in reward or '%d' in reward:
                note.setReward(reward % quest.rewardValue)
            else:
                note.setReward(reward)
            notes.append(note)

        return notes