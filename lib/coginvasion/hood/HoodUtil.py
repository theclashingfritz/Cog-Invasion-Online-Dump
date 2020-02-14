# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.HoodUtil
from direct.showbase.DirectObject import DirectObject
from lib.coginvasion.hood.TTCHood import TTCHood
from lib.coginvasion.hood.MinigameHood import MinigameHood
from lib.coginvasion.hood import HoodGui
from lib.coginvasion.gui.ToontownProgressScreen import ToontownProgressScreen
from lib.coginvasion.globals import CIGlobals

class HoodUtil(DirectObject):

    def __init__(self, cr=None):
        DirectObject.__init__(self)
        self.cr = cr
        self.centralHood = TTCHood(self.cr)
        self.minigameHood = MinigameHood(self.cr)
        self.progressScreen = ToontownProgressScreen()

    def load(self, hood, AI=0):
        if hood == 'TT':
            if not AI:
                loader.beginBulkLoad(hood, CIGlobals.ToontownCentral, 20, 2, self.progressScreen)
            self.centralHood.createHood(AI=AI)
            self.setCurrentHood(self.centralHood)
            if not AI:
                loader.endBulkLoad(hood)
        else:
            if hood == 'minigamearea':
                if not AI:
                    loader.beginBulkLoad(hood, CIGlobals.MinigameArea, 20, 3, self.progressScreen)
                self.minigameHood.createHood()
                self.setCurrentHood(self.minigameHood)
                if not AI:
                    loader.endBulkLoad(hood)
        self.announceHood(hood)

    def setCurrentHood(self, hood):
        if self.cr is not None:
            self.cr.setCurrentHood(hood)
        return

    def announceHood(self, hood):
        if hood == 'TT':
            HoodGui.announceHood(CIGlobals.ToontownCentral)
        else:
            if hood == 'minigamearea':
                HoodGui.announceHood(CIGlobals.MinigameArea)

    def unload(self, hood):
        if hood == 'TT':
            self.centralHood.unloadHood()
        else:
            if hood == 'minigamearea':
                self.minigameHood.unloadHood()

    def enableSuitEffect(self, size):
        self.centralHood.enableSuitEffect(size)

    def disableSuitEffect(self):
        self.centralHood.disableSuitEffect()