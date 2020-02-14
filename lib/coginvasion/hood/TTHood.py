# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.TTHood
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.holiday.HolidayManager import HolidayType
import ToonHood, TTSafeZoneLoader, TTTownLoader, SkyUtil
from panda3d.core import TransparencyAttrib

class TTHood(ToonHood.ToonHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = CIGlobals.ToontownCentral
        self.safeZoneLoader = TTSafeZoneLoader.TTSafeZoneLoader
        self.townLoader = TTTownLoader.TTTownLoader
        self.skyUtil = SkyUtil.SkyUtil()
        self.storageDNAFile = 'phase_4/dna/storage_TT.pdna'
        self.holidayDNAFile = None
        if base.cr.holidayManager.getHoliday() == HolidayType.CHRISTMAS:
            self.holidayDNAFile = 'phase_4/dna/winter_storage_TT.pdna'
        self.skyFilename = 'phase_3.5/models/props/TT_sky.bam'
        self.spookySkyFile = 'phase_3.5/models/props/BR_sky.bam'
        self.titleColor = (1.0, 0.5, 0.4, 1.0)
        self.loaderDoneEvent = 'TTHood-loaderDone'
        return

    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('TTHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('TTHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)

    def startSky(self):
        ToonHood.ToonHood.startSky(self)
        self.sky.setTransparency(TransparencyAttrib.MDual, 1)
        if not self.sky.find('**/cloud2').isEmpty():
            self.sky.find('**/cloud2').removeNode()
        self.sky.setScale(5)
        if not self.sky.find('**/cloud1').isEmpty():
            self.sky.find('**/cloud1').setSz(0.7)

    def stopSky(self):
        ToonHood.ToonHood.stopSky(self)
        self.skyUtil.stopSky()