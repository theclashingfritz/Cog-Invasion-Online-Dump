# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.interval.ParticleInterval
__all__ = [
 'ParticleInterval']
from panda3d.core import *
from panda3d.direct import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from Interval import Interval

class ParticleInterval(Interval):
    particleNum = 1
    notify = directNotify.newCategory('ParticleInterval')

    def __init__(self, particleEffect, parent, worldRelative=1, renderParent=None, duration=0.0, softStopT=0.0, cleanup=False, name=None):
        id = 'Particle-%d' % ParticleInterval.particleNum
        ParticleInterval.particleNum += 1
        if name == None:
            name = id
        self.particleEffect = particleEffect
        self.cleanup = cleanup
        if parent != None:
            self.particleEffect.reparentTo(parent)
        if worldRelative:
            renderParent = render
        if renderParent:
            for particles in self.particleEffect.getParticlesList():
                particles.setRenderParent(renderParent.node())

        self.__softStopped = False
        if softStopT == 0.0:
            self.softStopT = duration
        else:
            if softStopT < 0.0:
                self.softStopT = duration + softStopT
            else:
                self.softStopT = softStopT
        Interval.__init__(self, name, duration)
        return

    def __step(self, dt):
        if self.particleEffect:
            self.particleEffect.accelerate(dt, 1, 0.05)

    def __softStart(self):
        if self.particleEffect:
            self.particleEffect.softStart()
        self.__softStopped = False

    def __softStop(self):
        if self.particleEffect:
            self.particleEffect.softStop()
        self.__softStopped = True

    def privInitialize(self, t):
        if self.state != CInterval.SPaused:
            self.__softStart()
            if self.particleEffect:
                self.particleEffect.clearToInitial()
            self.currT = 0
        if self.particleEffect:
            for forceGroup in self.particleEffect.getForceGroupList():
                forceGroup.enable()

        Interval.privInitialize(self, t)

    def privInstant(self):
        self.privInitialize(self.getDuration())
        self.privFinalize()

    def privStep(self, t):
        if self.state == CInterval.SPaused or t < self.currT:
            self.privInitialize(t)
        else:
            if not self.__softStopped and t > self.softStopT:
                self.__step(self.softStopT - self.currT)
                self.__softStop()
                self.__step(t - self.softStopT)
            else:
                self.__step(t - self.currT)
            Interval.privStep(self, t)

    def privFinalize(self):
        Interval.privFinalize(self)
        if self.cleanup and self.particleEffect:
            self.particleEffect.cleanup()
            self.particleEffect = None
        return