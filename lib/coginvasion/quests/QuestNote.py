# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.quests.QuestNote
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import DirectFrame, OnscreenText
from lib.coginvasion.globals import CIGlobals

class QuestNote(DirectFrame):
    notify = directNotify.newCategory('QuestNote')
    spots = [
     (-0.45, 0, 0.3), (0.45, 0, 0.3), (0.45, 0, -0.25), (-0.45, 0, -0.25)]
    RewardTextPos = (0, -0.4)
    RewardTextScale = 0.06
    ProgressTextScale = 0.07
    ProgressTextPos = (0, -0.19)
    TaskInfoTextPos = (0, 0.05)
    NonHeadingTextScale = 0.08
    HeadingTextPos = (0, 0.23)
    HeadingTextScale = 0.1

    def __init__(self, index):
        DirectFrame.__init__(self, scale=0.5)
        stickergui = loader.loadModel('phase_3.5/models/gui/stickerbook_gui.bam')
        self['image'] = stickergui.find('**/paper_note')
        self.setPos(self.spots[index])
        self.headingText = OnscreenText(parent=self, text='', font=CIGlobals.getToonFont(), pos=self.HeadingTextPos, scale=self.HeadingTextScale)
        self.taskInfoText = OnscreenText(parent=self, text='', font=CIGlobals.getToonFont(), pos=self.TaskInfoTextPos, scale=self.NonHeadingTextScale)
        self.progressText = OnscreenText(parent=self, text='', font=CIGlobals.getToonFont(), pos=self.ProgressTextPos, scale=self.ProgressTextScale)
        self.rewardText = OnscreenText(parent=self, text='', font=CIGlobals.getToonFont(), pos=self.RewardTextPos, scale=self.RewardTextScale)
        self.hide()

    def setHeading(self, text):
        self.headingText.setText(text)

    def setTaskInfo(self, text):
        self.taskInfoText.setText(text)

    def setProgress(self, text):
        self.progressText.setText(text)

    def setReward(self, text):
        self.rewardText.setText(text)

    def setCompleted(self, value):
        if value:
            self.setProgress('Completed')
            self.progressText['fg'] = (0, 0.6, 0, 1)