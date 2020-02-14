# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.backpack.Backpack
from lib.coginvasion.gags.GagManager import GagManager
from lib.coginvasion.gags.GagState import GagState
from lib.coginvasion.gags import GagGlobals
import types

class Backpack:

    def __init__(self, avatar):
        self.gags = {}
        self.loadout = []
        self.activeGag = -1
        self.currentGag = -1
        self.loadoutGUI = None
        self.gagManager = GagManager()
        self.avatar = avatar
        return

    def setCurrentGag(self, gagId=-1):
        if not self.currentGag == -1 and self.hasGag(self.currentGag):
            self.gags.get(self.currentGag)[0].unEquip()
            self.currentGag = -1
        if not gagId == -1 and self.hasGag(gagId):
            self.currentGag = gagId

    def getCurrentGag(self):
        return self.getGagByID(self.currentGag)

    def setActiveGag(self, gagId):
        if not self.activeGag == -1:
            state = self.gags.get(self.activeGag)[0].getState()
            if state in [GagState.LOADED, GagState.RECHARGING]:
                self.activeGag = -1
        if self.activeGag == -1 and self.hasGag(gagId):
            self.activeGag = gagId

    def getActiveGag(self):
        return self.getGagByID(self.activeGag)

    def addGag(self, gagId, curSupply=0, maxSupply=0):
        if gagId not in self.gags.keys():
            gagName = GagGlobals.getGagByID(gagId)
            if gagName is not None:
                gag = self.gagManager.getGagByName(gagName)
                gag.setAvatar(self.avatar)
                self.gags.update({gagId: [gag, curSupply, maxSupply]})
        return

    def setLoadout(self, gagIds):
        self.loadout = gagIds
        if self.avatar.doId == base.localAvatar.doId:
            playGame = base.cr.playGame
            if playGame and playGame.getPlace() and playGame.getPlace().fsm.getCurrentState().getName() == 'walk':
                base.localAvatar.disableGags()
                base.localAvatar.enableGags(1)

    def addLoadoutGag(self, gagId):
        if len(self.loadout) < 4 and self.hasGag(gagId) and gagId not in self.loadout:
            self.loadout.append(gagId)
            if self.loadoutGUI:
                self.loadoutGUI.updateLoadout()

    def removeLoadoutGag(self, gagId):
        if len(self.loadout) > 0 and gagId in self.loadout:
            self.loadout.remove(gagId)
            if self.loadoutGUI:
                self.loadoutGUI.updateLoadout()

    def getLoadout(self):
        return self.loadout

    def getLoadoutInIds(self):
        ids = []
        for gag in self.loadout:
            ids.append(gag.getID())

        return ids

    def setMaxSupply(self, gagId, maxSupply):
        if self.hasGag(gagId) and 0 <= maxSupply <= 255:
            values = self.gags.get(gagId)
            gag = values[0]
            supply = values[1]
            self.gags.update({gagId: [gag, supply, maxSupply]})
            if self.loadoutGUI:
                self.loadoutGUI.update()
            return True
        return False

    def getMaxSupply(self, arg=-1):
        if type(arg) == types.IntType and self.hasGag(arg):
            return self.gags.get(arg)[2]
        if arg != -1:
            for values in self.gags.values():
                if values[0].getName() == arg:
                    return values[2]

        else:
            if arg == -1:
                if self.currentGag > -1:
                    return self.gags.get(self.currentGag)[2]
        return -1

    def setSupply(self, gagId, supply):
        if self.hasGag(gagId) and 0 <= supply <= 255:
            values = self.gags.get(gagId)
            gag = values[0]
            maxSupply = values[2]
            self.gags.update({gagId: [gag, supply, maxSupply]})
            if self.loadoutGUI:
                self.loadoutGUI.update()
            return True
        return False

    def getSupply(self, arg=-1):
        if type(arg) == types.IntType and self.hasGag(arg):
            return self.gags.get(arg)[1]
        if arg != -1:
            for values in self.gags.values():
                if values[0].getName() == arg:
                    return values[1]

        else:
            if arg == -1:
                if self.currentGag > -1:
                    return self.gags.get(self.currentGag)[1]
        return -1

    def hasGag(self, gagId):
        return gagId in self.gags.keys()

    def getGagByID(self, gagId):
        if self.hasGag(gagId):
            return self.gags.get(gagId)[0]
        return

    def getGagByIndex(self, index):
        return self.gags.get(self.gags.keys()[index])[0]

    def getGags(self):
        return self.gags

    def cleanup(self):
        for _, data in self.gags.iteritems():
            gag = data[0]
            gag.delete()

        del self.gags
        del self.loadout
        del self.currentGag
        del self.activeGag
        del self.loadoutGUI
        del self.gagManager
        del self.avatar