# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.DLTownLoader
import TownLoader, DLStreet
from lib.coginvasion.globals import CIGlobals

class DLTownLoader(TownLoader.TownLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = DLStreet.DLStreet
        self.musicFile = 'phase_8/audio/bgm/DL_SZ.mid'
        self.interiorMusicFile = 'phase_8/audio/bgm/DL_SZ_activity.mid'
        self.townStorageDNAFile = 'phase_8/dna/storage_DL_town.pdna'

    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        zone4File = str(self.branchZone)
        dnaFile = 'phase_8/dna/donalds_dreamland_' + zone4File + '.pdna'
        self.createHood(dnaFile)