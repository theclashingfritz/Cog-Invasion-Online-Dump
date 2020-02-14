# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.quest.Objective
from direct.directnotify.DirectNotifyGlobal import directNotify

class Objective:
    notify = directNotify.newCategory('Objective')

    def __init__(self, quest, location, assignDialog):
        self.quest = quest
        self.location = location
        self.assignDialog = assignDialog

    def setAssignDialog(self, dialog):
        self.assignDialog = dialog

    def getAssignDialog(self, dialog):
        return self.assignDialog

    def isOnLocation(self, zoneId):
        if not isinstance(self.location, (list, tuple)):
            return self.location == zoneId
        return zoneId in self.location

    def updateQuest(self):
        pass

    def finished(self):
        pass