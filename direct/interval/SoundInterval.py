# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.interval.SoundInterval
__all__ = [
 'SoundInterval']
from panda3d.core import *
from panda3d.direct import *
from direct.directnotify.DirectNotifyGlobal import *
import Interval, random

class SoundInterval(Interval.Interval):
    soundNum = 1
    notify = directNotify.newCategory('SoundInterval')

    def __init__(self, sound, loop=0, duration=0.0, name=None, volume=1.0, startTime=0.0, node=None, seamlessLoop=True, listenerNode=None, cutOff=None):
        id = 'Sound-%d' % SoundInterval.soundNum
        SoundInterval.soundNum += 1
        self.sound = sound
        if sound:
            self.soundDuration = sound.length()
        else:
            self.soundDuration = 0
        self.fLoop = loop
        self.volume = volume
        self.startTime = startTime
        self.node = node
        self.listenerNode = listenerNode
        self.cutOff = cutOff
        self._seamlessLoop = seamlessLoop
        if self._seamlessLoop:
            self._fLoop = True
        self._soundPlaying = False
        self._reverse = False
        if float(duration) == 0.0 and self.sound != None:
            duration = max(self.soundDuration - self.startTime, 0)
        if name == None:
            name = id
        Interval.Interval.__init__(self, name, duration)
        return

    def privInitialize(self, t):
        self._reverse = False
        t1 = t + self.startTime
        if t1 < 0.1:
            t1 = 0.0
        if t1 < self.soundDuration and not (self._seamlessLoop and self._soundPlaying):
            base.sfxPlayer.playSfx(self.sound, self.fLoop, 1, self.volume, t1, self.node, listenerNode=self.listenerNode, cutoff=self.cutOff)
            self._soundPlaying = True
        self.state = CInterval.SStarted
        self.currT = t

    def privInstant(self):
        pass

    def privStep(self, t):
        if self.state == CInterval.SPaused:
            t1 = t + self.startTime
            if t1 < self.soundDuration:
                base.sfxPlayer.playSfx(self.sound, self.fLoop, 1, self.volume, t1, self.node, listenerNode=self.listenerNode)
        if self.listenerNode and not self.listenerNode.isEmpty() and self.node and not self.node.isEmpty():
            base.sfxPlayer.setFinalVolume(self.sound, self.node, self.volume, self.listenerNode, self.cutOff)
        self.state = CInterval.SStarted
        self.currT = t

    def finish(self, *args, **kArgs):
        self._inFinish = True
        Interval.Interval.finish(self, *args, **kArgs)
        del self._inFinish

    def privFinalize(self):
        if self._seamlessLoop and self._soundPlaying and self.getLoop() and not hasattr(self, '_inFinish'):
            base.sfxPlayer.setFinalVolume(self.sound, self.node, self.volume, self.listenerNode, self.cutOff)
            return
        if self.sound != None:
            self.sound.stop()
            self._soundPlaying = False
        self.currT = self.getDuration()
        self.state = CInterval.SFinal
        return

    def privReverseInitialize(self, t):
        self._reverse = True

    def privReverseInstant(self):
        self.state = CInterval.SInitial

    def privReverseFinalize(self):
        self._reverse = False
        self.state = CInterval.SInitial

    def privInterrupt(self):
        if self.sound != None:
            self.sound.stop()
            self._soundPlaying = False
        self.state = CInterval.SPaused
        return

    def loop(self, startT=0.0, endT=-1.0, playRate=1.0, stagger=False):
        self.fLoop = 1
        Interval.Interval.loop(self, startT, endT, playRate)
        if stagger:
            self.setT(random.random() * self.getDuration())