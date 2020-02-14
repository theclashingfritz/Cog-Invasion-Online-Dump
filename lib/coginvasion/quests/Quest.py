# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.quests.Quest


class Quest:

    def __init__(self, type, subject, area, reward, progress, goal, rewardValue, index):
        self.type = type
        self.subject = subject
        self.area = area
        self.reward = reward
        self.progress = progress
        self.goal = goal
        self.rewardValue = rewardValue
        self.index = index

    def isComplete(self):
        return self.progress >= self.goal

    def cleanup(self):
        del self.type
        del self.subject
        del self.area
        del self.reward
        del self.progress
        del self.goal
        del self.rewardValue