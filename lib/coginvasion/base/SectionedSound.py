# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.base.SectionedSound
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *

class AudioClip(DirectObject):
    notify = directNotify.newCategory('SectionedMusic')

    def __init__(self, chunks):
        DirectObject.__init__(self)
        self.ival = None
        self.chunks = chunks
        return

    def playFromIndex(self, startIndex):
        self.stop()
        self.ival = Sequence()
        index = 0
        for chunk in self.chunks:
            if index >= startIndex:
                self.ival.append(SoundInterval(chunk, volume=0.5, duration=chunk.length() / 2, taskChain='TournamentMusicThread'))
                if index < len(self.chunks) - 1:
                    self.ival.append(Func(messenger.send, 'AudioClip_partDone', [index]))
            index += 1

        self.ival.append(Func(messenger.send, 'AudioClip_clipDone'))
        self.ival.start()

    def playAllParts(self):
        self.stop()
        self.ival = Sequence()
        index = 0
        for chunk in self.chunks:
            self.ival.append(SoundInterval(chunk, volume=0.5, duration=chunk.length() / 2, taskChain='TournamentMusicThread'))
            if index < len(self.chunks) - 1:
                self.ival.append(Func(messenger.send, 'AudioClip_partDone', [index]))
            index += 1

        self.ival.append(Func(messenger.send, 'AudioClip_clipDone'))
        self.ival.start()

    def stop(self):
        if self.ival:
            self.ival.pause()
            self.ival = None
        return

    def cleanup(self):
        self.stop()
        self.chunks = None
        return