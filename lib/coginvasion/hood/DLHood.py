# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.DLHood
from direct.directnotify.DirectNotifyGlobal import directNotify
from ToonHood import ToonHood
from DLSafeZoneLoader import DLSafeZoneLoader
from DLTownLoader import DLTownLoader
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.holiday.HolidayManager import HolidayType

class DLHood(ToonHood):
    notify = directNotify.newCategory('DLHood')

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = CIGlobals.DonaldsDreamland
        self.safeZoneLoader = DLSafeZoneLoader
        self.townLoader = DLTownLoader
        self.storageDNAFile = 'phase_8/dna/storage_DL.pdna'
        self.holidayDNAFile = None
        if base.cr.holidayManager.getHoliday() == HolidayType.CHRISTMAS:
            self.holidayDNAFile = 'phase_8/dna/winter_storage_DL.pdna'
        self.skyFilename = 'phase_8/models/props/DL_sky.bam'
        self.spookySkyFile = 'phase_3.5/models/props/BR_sky.bam'
        self.titleColor = (0.443, 0.21, 1.0, 1.0)
        self.loaderDoneEvent = 'DLHood-loaderDone'
        return

    def load(self):
        ToonHood.load(self)
        self.parentFSM.getStateNamed('DLHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('DLHood').removeChild(self.fsm)
        ToonHood.unload(self)