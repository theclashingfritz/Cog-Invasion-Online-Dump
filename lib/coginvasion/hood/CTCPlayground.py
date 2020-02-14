# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.CTCPlayground
import Playground
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.SoundInterval import SoundInterval
import random

class CTCPlayground(Playground.Playground):
    notify = directNotify.newCategory('TTPlayground')

    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.birdSfx = None
        return

    def load(self):
        Playground.Playground.load(self)

    def unload(self):
        Playground.Playground.unload(self)

    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)
        self.startBirds()

    def startBirds(self):
        taskMgr.add(self.birdTask, 'CTCPlayground-birdTask')

    def stopBirds(self):
        taskMgr.remove('CTCPlayground-birdTask')
        if self.birdSfx:
            self.birdSfx.finish()
            self.birdSfx = None
        return

    def birdTask(self, task):
        noiseFile = random.choice(self.loader.birdNoises)
        noise = base.loadSfx(noiseFile)
        if self.birdSfx:
            self.birdSfx.finish()
            self.birdSfx = None
        self.birdSfx = SoundInterval(noise)
        self.birdSfx.start()
        task.delayTime = random.random() * 20 + 1
        return task.again

    def exit(self):
        self.stopBirds()
        Playground.Playground.exit(self)