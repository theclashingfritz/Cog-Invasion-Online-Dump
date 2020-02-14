# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogtropolis.CTPlayground
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.IntervalGlobal import Sequence, Wait, Func
from direct.gui.DirectGui import DirectButton, DirectLabel
from lib.coginvasion.hood import Playground
import random

class CTPlayground(Playground.Playground):
    notify = directNotify.newCategory('CTPlayground')
    LightningRange = [
     15, 30]

    def enter(self, rs):
        Playground.Playground.enter(self, rs)
        self.loader.rain.start(parent=camera, renderParent=self.loader.rainRender)
        base.playSfx(self.loader.soundRain, looping=1)
        render.setFog(self.loader.fog)
        waitTime = random.uniform(self.LightningRange[0], self.LightningRange[1])
        taskMgr.doMethodLater(waitTime, self.__lightningTask, 'CTPlayground.LightningTask')
        self.lightningTrack = None
        return

    def __lightningTask(self, task):
        sound = random.choice(self.loader.thunderSounds)
        sound.play()
        self.lightningTrack = Sequence()
        numStrikes = random.randint(1, 3)
        for _ in range(numStrikes):
            self.lightningTrack.append(Func(self.loader.fog.setColor, 1.0, 1.0, 1.0))
            self.lightningTrack.append(Wait(0.1))
            self.lightningTrack.append(Func(self.loader.fog.setColor, 0.3, 0.3, 0.3))
            self.lightningTrack.append(Wait(0.1))

        self.lightningTrack.start()
        waitTime = random.uniform(self.LightningRange[0], self.LightningRange[1])
        task.delayTime = waitTime
        return task.again

    def exit(self):
        taskMgr.remove('CTPlayground.LightningTask')
        if self.lightningTrack:
            self.lightningTrack.finish()
            self.lightningTrack = None
        render.clearFog()
        self.loader.soundRain.stop()
        self.loader.rain.cleanup()
        Playground.Playground.exit(self)
        return