# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.CTCHood
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.holiday.HolidayManager import HolidayType
from panda3d.core import TransparencyAttrib
import ToonHood, CTCSafeZoneLoader, TTTownLoader, SkyUtil

class CTCHood(ToonHood.ToonHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = CIGlobals.BattleTTC
        self.safeZoneLoader = CTCSafeZoneLoader.CTCSafeZoneLoader
        self.townLoader = TTTownLoader.TTTownLoader
        self.skyUtil = SkyUtil.SkyUtil()
        self.storageDNAFile = 'phase_4/dna/storage_TT.pdna'
        self.holidayDNAFile = None
        if base.cr.holidayManager.getHoliday() == HolidayType.CHRISTMAS:
            self.holidayDNAFile = 'phase_4/dna/winter_storage_TT.pdna'
        self.skyFilename = 'phase_3.5/models/props/TT_sky.bam'
        self.spookySkyFile = 'phase_3.5/models/props/BR_sky.bam'
        self.titleColor = (1.0, 0.5, 0.4, 1.0)
        self.loaderDoneEvent = 'CTCHood-loaderDone'
        return

    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('CTCHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('CTCHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)

    def enter(self, requestStatus):
        ToonHood.ToonHood.enter(self, requestStatus)

    def exit(self):
        ToonHood.ToonHood.exit(self)

    def startSuitEffect(self):
        ToonHood.ToonHood.startSuitEffect(self)
        if base.cr.playGame.getPlace():
            if hasattr(base.cr.playGame.getPlace(), 'stopBirds'):
                base.cr.playGame.getPlace().stopBirds()

    def stopSuitEffect(self, newSky=1):
        if base.cr.playGame.getPlace():
            if hasattr(base.cr.playGame.getPlace(), 'startBirds'):
                base.cr.playGame.getPlace().startBirds()
        ToonHood.ToonHood.stopSuitEffect(self, newSky)

    def startSky(self):
        ToonHood.ToonHood.startSky(self)
        self.sky.setTransparency(TransparencyAttrib.MDual, 1)
        self.skyUtil.startSky(self.sky)

    def stopSky(self):
        ToonHood.ToonHood.stopSky(self)
        self.skyUtil.stopSky()