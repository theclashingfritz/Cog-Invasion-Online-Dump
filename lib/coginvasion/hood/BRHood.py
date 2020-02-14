# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.BRHood
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.holiday.HolidayManager import HolidayType
import BRSafeZoneLoader, BRTownLoader, ToonHood

class BRHood(ToonHood.ToonHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = CIGlobals.TheBrrrgh
        self.safeZoneLoader = BRSafeZoneLoader.BRSafeZoneLoader
        self.townLoader = BRTownLoader.BRTownLoader
        self.storageDNAFile = 'phase_8/dna/storage_BR.pdna'
        self.skyFilename = 'phase_3.5/models/props/BR_sky.bam'
        self.spookySkyFile = 'phase_3.5/models/props/BR_sky.bam'
        self.holidayDNAFile = None
        self.titleColor = (0.25, 0.25, 1.0, 1.0)
        self.loaderDoneEvent = 'BRHood-loaderDone'
        return

    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('BRHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('BRHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)