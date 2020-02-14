# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogtropolis.CTHood
from direct.directnotify.DirectNotifyGlobal import directNotify
from lib.coginvasion.hood import ToonHood
from lib.coginvasion.globals import CIGlobals
import CTSafeZoneLoader

class CTHood(ToonHood.ToonHood):
    notify = directNotify.newCategory('CTHood')

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = CIGlobals.CogTropolis
        self.safeZoneLoader = CTSafeZoneLoader.CTSafeZoneLoader
        self.storageDNAFile = None
        self.holidayDNAFile = None
        self.skyFilename = 'phase_9/models/cogHQ/cog_sky.bam'
        self.spookySkyFile = 'phase_9/models/cogHQ/cog_sky.bam'
        self.titleColor = (0.5, 0.5, 0.5, 1.0)
        self.loaderDoneEvent = 'CTHood-loaderDone'
        return

    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('CTHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('CTHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)