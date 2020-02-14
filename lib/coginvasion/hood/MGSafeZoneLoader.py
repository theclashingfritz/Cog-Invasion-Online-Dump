# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.MGSafeZoneLoader
from direct.directnotify.DirectNotifyGlobal import directNotify
import SafeZoneLoader, MGPlayground

class MGSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    notify = directNotify.newCategory('MGSafeZoneLoader')

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playground = MGPlayground.MGPlayground
        self.pgMusicFilename = 'phase_13/audio/bgm/minigame_area.ogg'
        self.interiorMusicFilename = None
        self.battleMusicFile = None
        self.invasionMusicFiles = None
        self.tournamentMusicFiles = None
        self.bossBattleMusicFile = None
        self.dnaFile = 'phase_13/dna/party_sz.pdna'
        self.szStorageDNAFile = 'phase_13/dna/storage_party_sz.pdna'
        return