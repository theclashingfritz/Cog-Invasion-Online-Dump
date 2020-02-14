# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.FactorySneakPlayer
from panda3d.core import Point3
from direct.showbase.DirectObject import DirectObject
from direct.directnotify.DirectNotifyGlobal import directNotify
from lib.coginvasion.gui.MoneyGui import MoneyGui
from FactorySneakGameToonFPS import FactorySneakGameToonFPS

class FactorySneakPlayer(DirectObject):
    notify = directNotify.newCategory('FactorySneakPlayer')
    SPAWN_POINT = Point3(21, 14.5, 3.73)

    def __init__(self, mg):
        DirectObject.__init__(self)
        self.actualAvatar = base.localAvatar
        self.beansCollected = 0
        self.moneyGui = None
        self.mg = mg
        self.toonFPS = FactorySneakGameToonFPS(mg)
        self.guardsPursuing = 0
        return

    def guardPursue(self):
        self.mg.gameWorld.showAlert('A guard has noticed you!')
        self.guardsPursuing += 1
        if self.guardsPursuing == 1:
            self.mg.gameWorld.playMusic(1)

    def guardStopPursue(self):
        self.guardsPursuing -= 1
        if self.guardsPursuing == 0:
            self.mg.gameWorld.playMusic(0)
            self.mg.gameWorld.showAlert("You've evaded the guards!")

    def startFPS(self, enableLookAround=True):
        self.toonFPS.load()
        self.toonFPS.start()
        if enableLookAround == False:
            self.disableLookAround()
        self.toonFPS.gui.hp_meter.hide()
        self.accept('guardPursue', self.guardPursue)
        self.accept('guardStopPursue', self.guardStopPursue)

    def enableLookAround(self):
        self.toonFPS.firstPerson.disableMouse()

    def disableLookAround(self):
        self.toonFPS.firstPerson.enableMouse()

    def enableControls(self):
        self.toonFPS.reallyStart()

    def disableControls(self):
        self.toonFPS.end()

    def cleanupFPS(self):
        self.ignore('guardPursue')
        self.ignore('guardStopPursue')
        self.toonFPS.reallyEnd()
        self.toonFPS.cleanup()

    def spawn(self):
        self.actualAvatar.setPos(self.SPAWN_POINT)

    def setupInterface(self):
        self.moneyGui = MoneyGui()
        self.moneyGui.createGui()
        self.moneyGui.frame.setPos(self.moneyGui.frame.getPos() + (-0.25, 0, 0.175))
        self.updateBeansCollected()

    def cleanup(self):
        self.actualAvatar = None
        self.beansCollected = None
        self.cleanupFPS()
        if self.moneyGui:
            self.moneyGui.deleteGui()
            self.moneyGui = None
        self.mg = None
        return

    def setBeansCollected(self, amt):
        self.beansCollected = amt
        self.updateBeansCollected()

    def getBeansCollected(self):
        return self.beansCollected

    def updateBeansCollected(self):
        self.moneyGui.update(self.beansCollected)