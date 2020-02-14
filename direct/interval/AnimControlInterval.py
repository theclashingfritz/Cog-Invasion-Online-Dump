# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.interval.AnimControlInterval
__all__ = [
 'AnimControlInterval']
from panda3d.core import *
from panda3d.direct import *
from direct.directnotify.DirectNotifyGlobal import *
import Interval, math

class AnimControlInterval(Interval.Interval):
    notify = directNotify.newCategory('AnimControlInterval')
    animNum = 1

    def __init__(self, controls, loop=0, constrainedLoop=0, duration=None, startTime=None, endTime=None, startFrame=None, endFrame=None, playRate=1.0, name=None):
        id = 'AnimControl-%d' % AnimControlInterval.animNum
        AnimControlInterval.animNum += 1
        if isinstance(controls, AnimControlCollection):
            self.controls = controls
            if config.GetBool('strict-anim-ival', 0):
                checkSz = self.controls.getAnim(0).getNumFrames()
                for i in range(1, self.controls.getNumAnims()):
                    if checkSz != self.controls.getAnim(i).getNumFrames():
                        self.notify.error("anim controls don't have the same number of frames!")

        else:
            if isinstance(controls, AnimControl):
                self.controls = AnimControlCollection()
                self.controls.storeAnim(controls, '')
            else:
                self.notify.error('invalid input control(s) for AnimControlInterval')
        self.loopAnim = loop
        self.constrainedLoop = constrainedLoop
        self.playRate = playRate
        if name == None:
            name = id
        self.frameRate = self.controls.getAnim(0).getFrameRate() * abs(playRate)
        if startFrame != None:
            self.startFrame = startFrame
        else:
            if startTime != None:
                self.startFrame = startTime * self.frameRate
            else:
                self.startFrame = 0
        if endFrame != None:
            self.endFrame = endFrame
        else:
            if endTime != None:
                self.endFrame = endTime * self.frameRate
            else:
                if duration != None:
                    if startTime == None:
                        startTime = float(self.startFrame) / float(self.frameRate)
                    endTime = startTime + duration
                    self.endFrame = duration * self.frameRate
                else:
                    numFrames = self.controls.getAnim(0).getNumFrames()
                    self.endFrame = numFrames - 1
        self.reverse = playRate < 0
        if self.endFrame < self.startFrame:
            self.reverse = 1
            t = self.endFrame
            self.endFrame = self.startFrame
            self.startFrame = t
        self.numFrames = self.endFrame - self.startFrame + 1
        self.implicitDuration = 0
        if duration == None:
            self.implicitDuration = 1
            duration = float(self.numFrames) / self.frameRate
        Interval.Interval.__init__(self, name, duration)
        return

    def getCurrentFrame(self):
        retval = None
        if not self.isStopped():
            framesPlayed = self.numFrames * self.currT
            retval = self.startFrame + framesPlayed
        return retval

    def privStep(self, t):
        frameCount = t * self.frameRate
        if self.constrainedLoop:
            frameCount = frameCount % self.numFrames
        if self.reverse:
            absFrame = self.endFrame - frameCount
        else:
            absFrame = self.startFrame + frameCount
        intFrame = int(math.floor(absFrame + 0.0001))
        numFrames = self.controls.getAnim(0).getNumFrames()
        if self.loopAnim:
            frame = intFrame % numFrames + (absFrame - intFrame)
        else:
            frame = max(min(absFrame, numFrames - 1), 0)
        self.controls.poseAll(frame)
        self.state = CInterval.SStarted
        self.currT = t

    def privFinalize(self):
        if self.implicitDuration and not self.loopAnim:
            if self.reverse:
                self.controls.poseAll(self.startFrame)
            else:
                self.controls.poseAll(self.endFrame)
        else:
            self.privStep(self.getDuration())
        self.state = CInterval.SFinal
        self.intervalDone()