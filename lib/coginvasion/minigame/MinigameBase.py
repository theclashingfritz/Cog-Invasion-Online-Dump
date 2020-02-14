# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.MinigameBase
from direct.showbase.DirectObject import DirectObject
from lib.coginvasion.globals import CIGlobals
from DistributedRaceGameAI import DistributedRaceGameAI
from DistributedUnoGameAI import DistributedUnoGameAI
from DistributedGunGameAI import DistributedGunGameAI
from DistributedMinigameAI import DistributedMinigameAI
from DistributedFactorySneakGameAI import DistributedFactorySneakGameAI
from DistributedCameraShyGameAI import DistributedCameraShyGameAI
from DistributedEagleGameAI import DistributedEagleGameAI
from DistributedDeliveryGameAI import DistributedDeliveryGameAI
from DistributedDodgeballGameAI import DistributedDodgeballGameAI

class MinigameBase(DirectObject):

    def __init__(self, cr):
        DirectObject.__init__(self)
        self.minigame = None
        self.zoneId = None
        self.cr = cr
        return

    def createMinigame(self, game, numPlayers, avatars):
        self.zoneId = base.air.allocateZone()
        gameClass = DistributedMinigameAI
        if game == CIGlobals.RaceGame:
            gameClass = DistributedRaceGameAI
        else:
            if game == CIGlobals.UnoGame:
                gameClass = DistributedUnoGameAI
            else:
                if game == CIGlobals.GunGame:
                    gameClass = DistributedGunGameAI
                else:
                    if game == CIGlobals.FactoryGame:
                        gameClass = DistributedFactorySneakGameAI
                    else:
                        if game == CIGlobals.CameraShyGame:
                            gameClass = DistributedCameraShyGameAI
                        else:
                            if game == CIGlobals.EagleGame:
                                gameClass = DistributedEagleGameAI
                            else:
                                if game == CIGlobals.DeliveryGame:
                                    gameClass = DistributedDeliveryGameAI
                                else:
                                    if game == CIGlobals.DodgeballGame:
                                        gameClass = DistributedDodgeballGameAI
        self.minigame = gameClass(self.cr)
        self.minigame.generateWithRequired(self.zoneId)
        self.minigame.setNumPlayers(numPlayers)
        for avatar in avatars:
            self.minigame.appendAvatar(avatar)

        taskMgr.add(self.monitorAvatars, self.cr.uniqueName('monitorAvatars'))

    def monitorAvatars(self, task):
        for avatar in self.minigame.avatars:
            if avatar not in self.cr.doId2do.values():
                self.minigame.d_abort()
                self.handleEmptyMinigame()
                return task.done

        return task.cont

    def handleEmptyMinigame(self):
        taskMgr.remove(self.cr.uniqueName('monitorAvatars'))
        base.air.deallocateZone(self.zoneId)
        self.minigame.requestDelete()
        self.delete()

    def delete(self):
        del self.minigame
        del self.zoneId
        del self.cr