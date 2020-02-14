# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.MLTownLoader
import TownLoader, MLStreet
from lib.coginvasion.globals import CIGlobals

class MLTownLoader(TownLoader.TownLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = MLStreet.MLStreet
        self.musicFile = 'phase_6/audio/bgm/MM_SZ.mid'
        self.interiorMusicFile = 'phase_6/audio/bgm/MM_SZ_activity.mid'
        self.townStorageDNAFile = 'phase_6/dna/storage_MM_town.pdna'

    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        zone4File = str(self.branchZone)
        dnaFile = 'phase_6/dna/minnies_melody_land_' + zone4File + '.pdna'
        self.createHood(dnaFile)

    def unload(self):
        TownLoader.TownLoader.unload(self)