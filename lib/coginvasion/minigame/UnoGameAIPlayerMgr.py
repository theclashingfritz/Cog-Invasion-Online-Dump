# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.UnoGameAIPlayerMgr
from lib.coginvasion.npc import NPCGlobals
from lib.coginvasion.minigame.UnoGameAIPlayer import UnoGameAIPlayer
from panda3d.core import UniqueIdAllocator
import random

class UnoGameAIPlayerMgr:

    def __init__(self, uno_game):
        self.game = uno_game
        self.players = []
        self.idAllocator = UniqueIdAllocator(1, 4)

    def createPlayer(self, difficulty=None):
        npc_name = random.choice(NPCGlobals.NPC_DNA.keys())
        player = UnoGameAIPlayer(npc_name, self.idAllocator.allocate(), self.game)
        player.generate()
        self.players.append(player)
        return player

    def removePlayer(self, player):
        self.players.remove(player)

    def getPlayers(self):
        return self.players

    def getPlayerByID(self, doId):
        for player in self.players:
            if player.getID() == doId:
                return player

        return

    def generateHeadPanels(self):
        for avatar in self.players:
            gender = avatar.getGender()
            animal = avatar.getAnimal()
            head, color = avatar.getHeadStyle()
            r, g, b, a = color
            self.game.d_generateHeadPanel(gender, animal, head, [r, g, b], avatar.getID(), avatar.getName())