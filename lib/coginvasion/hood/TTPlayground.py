# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.TTPlayground
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.SoundInterval import SoundInterval
from lib.coginvasion.holiday.HolidayManager import HolidayType
import Playground, random

class TTPlayground(Playground.Playground):
    notify = directNotify.newCategory('TTPlayground')

    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.birdSfx = None
        self.christmasTree = None
        return

    def load(self):
        Playground.Playground.load(self)
        if base.cr.holidayManager.getHoliday() == HolidayType.CHRISTMAS:
            self.christmasTree = loader.loadModel('phase_4/models/props/winter_tree_Christmas.bam')
            self.christmasTree.reparentTo(self.loader.geom)
            self.christmasTree.setPos(0.651558, 23.0954, 0.00864142)
            self.christmasTree.setH(-183.108)
            winterTxt = loader.loadTexture('winter/maps/tt_winter_ground.png')
            self.loader.geom.find('**/ground_center').setTexture(winterTxt, 1)

    def unload(self):
        Playground.Playground.unload(self)
        if self.christmasTree:
            self.christmasTree.removeNode()
            self.christmasTree = None
        return

    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)
        self.startBirds()

    def startBirds(self):
        taskMgr.add(self.birdTask, 'TTPlayground-birdTask')

    def stopBirds(self):
        taskMgr.remove('TTPlayground-birdTask')
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