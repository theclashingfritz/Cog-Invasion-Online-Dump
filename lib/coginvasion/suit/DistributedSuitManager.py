# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.DistributedSuitManager
from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify.DirectNotifyGlobal import directNotify
from lib.coginvasion.globals import CIGlobals, ChatGlobals
from lib.coginvasion.gui.WhisperPopup import WhisperPopup
from lib.coginvasion.suit.CogTournamentMusicManager import CogTournamentMusicManager
import random

class DistributedSuitManager(DistributedObject):
    notify = directNotify.newCategory('DistributedSuitManager')

    def __init__(self, cr):
        try:
            self.DistributedSuitManager_initialized
            return
        except:
            self.DistributedSuitManager_initialized = 1

        DistributedObject.__init__(self, cr)
        self.hood = cr.playGame.hood
        self.spawnerStatus = 0

    def spawner(self, onOrOff):
        self.spawnerStatus = bool(onOrOff)
        if self.cr.playGame.getPlace():
            self.cr.playGame.getPlace().maybeUpdateAdminPage()

    def getSpawner(self):
        return self.spawnerStatus

    def d_requestSuitInfo(self):
        self.notify.info("sending update 'requestSuitInfo'")
        self.sendUpdate('requestSuitInfo', [])

    def systemMessage(self, message):
        whisper = WhisperPopup('Toon HQ: ' + message, CIGlobals.getToonFont(), ChatGlobals.WTSystem)
        whisper.manage(base.marginManager)

    def noSuits(self):
        self.notify.info('There are no suits!')
        if not hasattr(self.hood, 'loader'):
            return
        if self.hood.loader.music.status() == self.hood.loader.music.READY:
            self.notify.info('playing noSuits music.')
            if self.hood.loader.battleMusic:
                self.hood.loader.battleMusic.stop()
            if self.hood.loader.invasionMusic:
                self.hood.loader.invasionMusic.stop()
            if self.hood.loader.tournamentMusic:
                self.hood.loader.tournamentMusic.stop()
                base.cr.music = None
            self.hood.loader.bossBattleMusic.stop()
            base.playMusic(self.hood.loader.music, looping=1, volume=0.9)
        self.hood.stopSuitEffect()
        return

    def newSuit(self):
        self.notify.info('There are active Suits!')
        if not hasattr(self.hood, 'loader'):
            return
        if not self.hood.loader.battleMusic or self.hood.loader.battleMusic.status() == self.hood.loader.battleMusic.READY:
            self.notify.info('playing newSuit music.')
            self.hood.loader.music.stop()
            self.hood.loader.bossBattleMusic.stop()
            self.hood.loader.battleMusic.stop()
            if self.hood.loader.tournamentMusic:
                self.hood.loader.tournamentMusic.stop()
                self.hood.loader.tournamentMusic = None
            if self.hood.loader.invasionMusic:
                self.hood.loader.invasionMusic.stop()
                self.hood.loader.invasionMusic = None
            base.playMusic(self.hood.loader.battleMusic, looping=1, volume=0.9)
        self.hood.startSuitEffect()
        return

    def bossSpawned(self):
        if not hasattr(self.hood, 'loader'):
            return
        if not self.hood.loader.bossBattleMusic or self.hood.loader.bossBattleMusic.status() == self.hood.loader.bossBattleMusic.READY:
            self.notify.info('playing bossSpawned music.')
            self.hood.loader.music.stop()
            self.hood.loader.battleMusic.stop()
            if self.hood.loader.invasionMusic:
                self.hood.loader.invasionMusic.stop()
                self.hood.loader.invasionMusic = None
            if self.hood.loader.tournamentMusic:
                self.hood.loader.tournamentMusic.stop()
                self.hood.loader.tournamentMusic = None
                base.cr.music = None
            base.playMusic(self.hood.loader.bossBattleMusic, looping=1, volume=0.9)
        return

    def invasionSpawned(self):
        if not hasattr(self.hood, 'loader'):
            return
        if not self.hood.loader.invasionMusic or self.hood.loader.invasionMusic.status() == self.hood.loader.invasionMusic.READY:
            self.notify.info('playing invasionSpawned music.')
            self.hood.loader.music.stop()
            self.hood.loader.bossBattleMusic.stop()
            self.hood.loader.battleMusic.stop()
            if self.hood.loader.tournamentMusic:
                self.hood.loader.tournamentMusic.stop()
            if self.hood.loader.invasionMusic:
                self.hood.loader.invasionMusic.stop()
            self.hood.loader.invasionMusic = None
            choice = random.choice(self.hood.loader.invasionMusicFiles)
            if 'BossBot_CEO_v1' in choice:
                volume = 1.7
            else:
                volume = 0.9
            self.hood.loader.invasionMusic = base.loadMusic(choice)
            base.playMusic(self.hood.loader.invasionMusic, looping=1, volume=volume)
        return

    def tournamentSpawned(self):
        if not hasattr(self.hood, 'loader'):
            return
        if not self.hood.loader.tournamentMusic or self.hood.loader.tournamentMusic.status() == self.hood.loader.tournamentMusic.READY:
            self.hood.loader.music.stop()
            self.hood.loader.bossBattleMusic.stop()
            self.hood.loader.battleMusic.stop()
            if self.hood.loader.tournamentMusic:
                self.hood.loader.tournamentMusic.stop()
            if self.hood.loader.invasionMusic:
                self.hood.loader.invasionMusic.stop()
            self.hood.loader.tournamentMusic = None
            self.hood.loader.tournamentMusic = base.loadMusic(random.choice(self.hood.loader.tournamentMusicFiles))
            base.cr.music = self.hood.loader.tournamentMusic
            base.playMusic(self.hood.loader.tournamentMusic, looping=1, volume=0.9)
        return

    def invasionInProgress(self):
        self.systemMessage(CIGlobals.SuitInvasionInProgMsg)

    def tournamentInProgress(self):
        self.systemMessage(CIGlobals.SuitTournamentInProgMsg)

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        base.cr.playGame.suitManager = self

    def disable(self):
        base.cr.playGame.suitManager = None
        base.cr.music = None
        del self.hood
        del self.spawnerStatus
        DistributedObject.disable(self)
        return