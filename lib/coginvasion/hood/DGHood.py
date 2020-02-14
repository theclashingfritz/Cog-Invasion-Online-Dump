# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.DGHood
from panda3d.core import TransparencyAttrib
from direct.directnotify.DirectNotifyGlobal import directNotify
from ToonHood import ToonHood
import SkyUtil
from DGSafeZoneLoader import DGSafeZoneLoader
import DGTownLoader
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.holiday.HolidayManager import HolidayType

class DGHood(ToonHood):
    notify = directNotify.newCategory('DGHood')

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = CIGlobals.DaisyGardens
        self.safeZoneLoader = DGSafeZoneLoader
        self.townLoader = DGTownLoader.DGTownLoader
        self.skyUtil = SkyUtil.SkyUtil()
        self.storageDNAFile = 'phase_8/dna/storage_DG.pdna'
        self.holidayDNAFile = None
        if base.cr.holidayManager.getHoliday() == HolidayType.CHRISTMAS:
            self.holidayDNAFile = 'phase_8/dna/winter_storage_DG.pdna'
        self.skyFilename = 'phase_3.5/models/props/TT_sky.bam'
        self.spookySkyFile = 'phase_3.5/models/props/BR_sky.bam'
        self.titleColor = (0.4, 0.67, 0.18, 1.0)
        self.loaderDoneEvent = 'DGHood-loaderDone'
        return

    def load(self):
        ToonHood.load(self)
        self.parentFSM.getStateNamed('DGHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('DGHood').removeChild(self.fsm)
        ToonHood.unload(self)

    def startSuitEffect(self):
        ToonHood.startSuitEffect(self)
        if base.cr.playGame.getPlace():
            base.cr.playGame.getPlace().stopBirds()

    def stopSuitEffect(self, newSky=1):
        if base.cr.playGame.getPlace():
            base.cr.playGame.getPlace().startBirds()
        ToonHood.stopSuitEffect(self, newSky)

    def startSky(self):
        ToonHood.startSky(self)
        self.sky.setTransparency(TransparencyAttrib.MDual, 1)
        self.skyUtil.startSky(self.sky)

    def stopSky(self):
        ToonHood.stopSky(self)
        self.skyUtil.stopSky()