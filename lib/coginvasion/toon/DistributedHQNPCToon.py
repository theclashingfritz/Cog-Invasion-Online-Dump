# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.toon.DistributedHQNPCToon
from panda3d.core import Vec4
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import DirectFrame, DirectButton, DGG
import DistributedNPCToon
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.quests import Quests, QuestNote

class DistributedHQNPCToon(DistributedNPCToon.DistributedNPCToon):
    notify = directNotify.newCategory('DistributedHQNPCToon')

    def __init__(self, cr):
        DistributedNPCToon.DistributedNPCToon.__init__(self, cr)
        self.questFrame = None
        self.questBtns = None
        self.questNotes = None
        return

    def makePickableQuests(self, list):
        quests = []
        for questId in list:
            quests.append(Quests.Quest(questId, 0, 0, list.index(questId)))

        positions = [
         (0, 0, 0.6), (0, 0, 0), (0, 0, -0.6)]
        self.questNotes = base.localAvatar.questManager.makeQuestNotes(quests=quests)
        self.questFrame = DirectFrame(parent=base.a2dLeftCenter, relief=None, pos=(0.5,
                                                                                   0,
                                                                                   0), geom=DGG.getDefaultDialogGeom(), geom_color=Vec4(0.8, 0.6, 0.4, 1), geom_scale=(1.85,
                                                                                                                                                                       1,
                                                                                                                                                                       0.9), geom_hpr=(0,
                                                                                                                                                                                       0,
                                                                                                                                                                                       -90))
        self.questBtns = []
        for i in xrange(len(self.questNotes)):
            note = self.questNotes[i]
            note.setPos(0, 0, 0)
            if quests[i].currentObjective.type in Quests.DefeatObjectives:
                note.progressText.hide()
            btn = DirectButton(geom=note, parent=self.questFrame, pos=positions[i], command=self.d_pickedQuest, extraArgs=[quests[i]], relief=None)
            btn.setScale(1.15)
            note.reparentTo(btn.stateNodePath[0], 20)
            note.instanceTo(btn.stateNodePath[1], 20)
            note.instanceTo(btn.stateNodePath[2], 20)
            note.show()
            self.questBtns.append(btn)

        return

    def removePickableQuests(self):
        if self.questNotes:
            for note in self.questNotes:
                note.destroy()

            self.questNotes = None
        if self.questBtns:
            for btn in self.questBtns:
                btn.destroy()

            self.questBtns = None
        if self.questFrame:
            self.questFrame.destroy()
            self.questFrame = None
        return

    def d_pickedQuest(self, quest):
        self.removePickableQuests()
        self.sendUpdate('pickedQuest', [quest.questId])
        self.currentQuestId = quest.questId
        self.currentQuestObjective = 0
        self.currentChatIndex = 0
        self.doNPCChat(Quests.QuestHQOfficerDialogue)

    def disable(self):
        self.removePickableQuests()
        DistributedNPCToon.DistributedNPCToon.disable(self)