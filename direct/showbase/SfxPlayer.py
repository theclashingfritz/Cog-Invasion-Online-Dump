# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.SfxPlayer
__all__ = [
 'SfxPlayer']
import math
from panda3d.core import *

class SfxPlayer:
    UseInverseSquare = 0

    def __init__(self):
        self.cutoffVolume = 0.02
        if SfxPlayer.UseInverseSquare:
            self.setCutoffDistance(300.0)
        else:
            self.setCutoffDistance(120.0)

    def setCutoffDistance(self, d):
        self.cutoffDistance = d
        rawCutoffDistance = math.sqrt(1.0 / self.cutoffVolume)
        self.distanceScale = rawCutoffDistance / self.cutoffDistance

    def getCutoffDistance(self):
        return self.cutoffDistance

    def getLocalizedVolume(self, node, listenerNode=None, cutoff=None):
        d = None
        if not node.isEmpty():
            if listenerNode and not listenerNode.isEmpty():
                d = node.getDistance(listenerNode)
            else:
                d = node.getDistance(base.cam)
        if d == None or d > cutoff:
            volume = 0
        else:
            if SfxPlayer.UseInverseSquare:
                sd = d * self.distanceScale
                volume = min(1, 1 / (sd * sd or 1))
            else:
                volume = 1 - d / (cutoff or 1)
        return volume

    def playSfx(self, sfx, looping=0, interrupt=1, volume=None, time=0.0, node=None, listenerNode=None, cutoff=None):
        if sfx:
            if not cutoff:
                cutoff = self.cutoffDistance
            self.setFinalVolume(sfx, node, volume, listenerNode, cutoff)
            if interrupt or sfx.status() != AudioSound.PLAYING:
                sfx.setTime(time)
                sfx.setLoop(looping)
                sfx.play()

    def setFinalVolume(self, sfx, node, volume, listenerNode, cutoff=None):
        if node or volume is not None:
            if node:
                finalVolume = self.getLocalizedVolume(node, listenerNode, cutoff)
            else:
                finalVolume = 1
            if volume is not None:
                finalVolume *= volume
            if node is not None:
                finalVolume *= node.getNetAudioVolume()
            sfx.setVolume(finalVolume)
        return