# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.MLHood
from direct.directnotify.DirectNotifyGlobal import directNotify
from ToonHood import ToonHood
from MLSafeZoneLoader import MLSafeZoneLoader
from MLTownLoader import MLTownLoader
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.holiday.HolidayManager import HolidayType

class MLHood(ToonHood):
    notify = directNotify.newCategory('MLHood')

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = CIGlobals.MinniesMelodyland
        self.safeZoneLoader = MLSafeZoneLoader
        self.townLoader = MLTownLoader
        self.storageDNAFile = 'phase_6/dna/storage_MM.pdna'
        self.holidayDNAFile = None
        if base.cr.holidayManager.getHoliday() == HolidayType.CHRISTMAS:
            self.holidayDNAFile = 'phase_6/dna/winter_storage_MM.pdna'
        self.skyFilename = 'phase_6/models/props/MM_sky.bam'
        self.spookySkyFile = 'phase_3.5/models/props/BR_sky.bam'
        self.titleColor = (0.945, 0.54, 1.0, 1.0)
        self.loaderDoneEvent = 'MLHood-loaderDone'
        return

    def load(self):
        ToonHood.load(self)
        self.parentFSM.getStateNamed('MLHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('MLHood').removeChild(self.fsm)
        ToonHood.unload(self)