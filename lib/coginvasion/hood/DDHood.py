# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.DDHood
from panda3d.core import Fog
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.holiday.HolidayManager import HolidayType
import DDTownLoader, DDSafeZoneLoader
from ToonHood import ToonHood

class DDHood(ToonHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = CIGlobals.DonaldsDock
        self.safeZoneLoader = DDSafeZoneLoader.DDSafeZoneLoader
        self.townLoader = DDTownLoader.DDTownLoader
        self.storageDNAFile = 'phase_6/dna/storage_DD.pdna'
        self.holidayDNAFile = None
        if base.cr.holidayManager.getHoliday() == HolidayType.CHRISTMAS:
            self.holidayDNAFile = 'phase_6/dna/winter_storage_DD.pdna'
        self.skyFilename = 'phase_3.5/models/props/BR_sky.bam'
        self.spookySkyFile = 'phase_3.5/models/props/BR_sky.bam'
        self.titleColor = (0.8, 0.6, 0.5, 1.0)
        self.loaderDoneEvent = 'DDHood-loaderDone'
        self.fog = None
        return

    def load(self):
        ToonHood.load(self)
        self.fog = Fog('DDFog')
        self.parentFSM.getStateNamed('DDHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('DDHood').removeChild(self.fsm)
        del self.fog
        ToonHood.unload(self)