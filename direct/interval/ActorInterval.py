# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.interval.ActorInterval
__all__ = [
 'ActorInterval', 'LerpAnimInterval']
from panda3d.core import *
from panda3d.direct import *
from direct.directnotify.DirectNotifyGlobal import *
import Interval, math

class ActorInterval(Interval.Interval):
    notify = directNotify.newCategory('ActorInterval')
    animNum = 1

    def __init__(self, actor, animName, loop=0, constrainedLoop=0, duration=None, startTime=None, endTime=None, startFrame=None, endFrame=None, playRate=1.0, name=None, forceUpdate=0, partName=None, lodName=None):
        id = 'Actor-%s-%d' % (animName, ActorInterval.animNum)
        ActorInterval.animNum += 1
        self.actor = actor
        self.animName = animName
        self.controls = self.actor.getAnimControls(self.animName, partName=partName, lodName=lodName)
        self.loopAnim = loop
        self.constrainedLoop = constrainedLoop
        self.forceUpdate = forceUpdate
        self.playRate = playRate
        if name == None:
            name = id
        if len(self.controls) == 0:
            self.notify.warning('Unknown animation for actor: %s' % self.animName)
            self.frameRate = 1.0
            self.startFrame = 0
            self.endFrame = 0
        else:
            self.frameRate = self.controls[0].getFrameRate() * abs(playRate)
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
                        maxFrames = self.controls[0].getNumFrames()
                        warned = 0
                        for i in range(1, len(self.controls)):
                            numFrames = self.controls[i].getNumFrames()
                            if numFrames != maxFrames and numFrames != 1 and not warned:
                                self.notify.warning("Animations '%s' on %s have an inconsistent number of frames." % (animName, actor.getName()))
                                warned = 1
                            maxFrames = max(maxFrames, numFrames)

                        self.endFrame = maxFrames - 1
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
        for control in self.controls:
            numFrames = control.getNumFrames()
            if self.loopAnim:
                frame = intFrame % numFrames + (absFrame - intFrame)
            else:
                frame = max(min(absFrame, numFrames - 1), 0)
            control.pose(frame)

        if self.forceUpdate:
            self.actor.update()
        self.state = CInterval.SStarted
        self.currT = t

    def privFinalize(self):
        if self.implicitDuration and not self.loopAnim:
            if self.reverse:
                for control in self.controls:
                    control.pose(self.startFrame)

            else:
                for control in self.controls:
                    control.pose(self.endFrame)

            if self.forceUpdate:
                self.actor.update()
        else:
            self.privStep(self.getDuration())
        self.state = CInterval.SFinal
        self.intervalDone()

    def resetControls(self, partName, lodName=None):
        self.controls = self.actor.getAnimControls(self.animName, partName=partName, lodName=lodName)


class LerpAnimInterval(CLerpAnimEffectInterval):
    lerpAnimNum = 1

    def __init__(self, actor, duration, startAnim, endAnim, startWeight=0.0, endWeight=1.0, blendType='noBlend', name=None, partName=None, lodName=None):
        if name == None:
            name = 'LerpAnimInterval-%d' % LerpAnimInterval.lerpAnimNum
            LerpAnimInterval.lerpAnimNum += 1
        blendType = self.stringBlendType(blendType)
        CLerpAnimEffectInterval.__init__(self, name, duration, blendType)
        if startAnim != None:
            controls = actor.getAnimControls(startAnim, partName=partName, lodName=lodName)
            for control in controls:
                self.addControl(control, startAnim, 1.0 - startWeight, 1.0 - endWeight)

        if endAnim != None:
            controls = actor.getAnimControls(endAnim, partName=partName, lodName=lodName)
            for control in controls:
                self.addControl(control, endAnim, startWeight, endWeight)

        return