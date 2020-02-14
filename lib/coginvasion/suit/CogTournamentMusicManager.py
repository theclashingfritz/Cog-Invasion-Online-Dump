# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.CogTournamentMusicManager
from panda3d.core import TP_urgent
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.DirectObject import DirectObject
from lib.coginvasion.base.SectionedSound import AudioClip
from CTMusicData import *
import random
taskMgr.setupTaskChain('TournamentMusicThread', numThreads=1, frameSync=False, threadPriority=TP_urgent)
TournamentMusicChunks = {}
TournamentMusicClips = {}
Loaded = False

def loadMusic(task):
    global Loaded
    for songName, chunkData in ChunkData.items():
        TournamentMusicChunks[songName] = {}
        TournamentMusicClips[songName] = {}
        for chunkName, chunkRange in chunkData.items():
            TournamentMusicChunks[songName][chunkName] = []
            listIndex = 0
            for i in chunkRange:
                folder = 'tournament_music/' + songName + '/'
                filename = 'MW_Music{0}'
                extension = '.ogg'
                if i > 0:
                    filename = filename.format('_' + str(i))
                else:
                    filename = filename.format('')
                fullfile = folder + filename + extension
                song = base.loadMusic(fullfile)
                TournamentMusicChunks[songName][chunkName].insert(listIndex, song)
                listIndex += 1

            TournamentMusicClips[songName][chunkName] = AudioClip(TournamentMusicChunks[songName][chunkName])

    Loaded = True
    return task.done


class CogTournamentMusicManager(DirectObject):
    notify = directNotify.newCategory('CogTournamentMusicManager')

    def __init__(self):
        self.suitsSpawnedInLastSomeSeconds = 0
        self.suitsKilledInLastSomeSeconds = 0
        self.currentAudioClip = None
        self.currentClipName = None
        self.nextClipRequest = None
        self.songName = random.choice(TournamentMusicChunks.keys())
        return

    def startMusic(self):
        if not Loaded:
            print 'CogTournamentMusicManager: Cannot start the music before loading!'
            return
        baseOrOrch = random.choice(['base', 'orchestra'])
        self.playClip('intro_' + baseOrOrch)
        self.accept('AudioClip_partDone', self.__handlePartDone)
        self.accept('AudioClip_clipDone', self.__handleClipDone)

    def setClipRequest(self, request):
        print 'New clip request: ' + request
        self.nextClipRequest = request

    def __handleClipDone(self):
        self.__playNewClip()

    def __handlePartDone(self, partIndex):
        print partIndex
        if self.nextClipRequest is not None and self.nextClipRequest.split('_')[0] not in self.currentClipName:
            self.__playNewClip()
        else:
            if self.nextClipRequest is not None and self.nextClipRequest.split('_')[0] in self.currentClipName:
                print 'Starting from current part index'
                self.stopClip()
                print self.nextClipRequest
                ac = TournamentMusicClips[self.songName][self.nextClipRequest]
                ac.playFromIndex(partIndex + 1)
                self.currentClipName = self.nextClipRequest
                self.nextClipRequest = None
                self.currentAudioClip = ac
        return

    def __playNewClip(self):
        if self.nextClipRequest is None:
            randomClips = [
             'located_orchestra', 'located_base', '5050_orchestra', '5050_base',
             'running_away_base', 'running_away_orchestra',
             'getting_worse_orchestra', 'getting_worse_base']
            newClip = random.choice(randomClips)
        else:
            newClip = self.nextClipRequest
            self.nextClipRequest = None
        print 'Playing clip: ' + newClip
        self.playClip(newClip)
        return

    def playClip(self, clipName):
        self.stopClip()
        self.currentClipName = clipName
        ac = TournamentMusicClips[self.songName][clipName]
        ac.playAllParts()
        self.currentAudioClip = ac

    def stopClip(self):
        if self.currentAudioClip:
            self.currentAudioClip.stop()
            self.currentAudioClip = None
        self.currentClipName = None
        return

    def cleanup(self):
        self.stopClip()
        self.suitsSpawnedInLastSomeSeconds = None
        self.suitsKilledInLastSomeSeconds = None
        self.index = None
        self.clipNames = None
        self.currentAudioClip = None
        return