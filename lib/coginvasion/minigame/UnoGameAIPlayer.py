# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.UnoGameAIPlayer
from lib.coginvasion.npc import NPCGlobals
from lib.coginvasion.toon.ToonDNA import ToonDNA
from lib.coginvasion.minigame import UnoGameGlobals as UGG
import random

class UnoGameAIPlayer(ToonDNA):

    def __init__(self, npc_name, doId, uno_ai):
        ToonDNA.__init__(self)
        self.game = uno_ai
        self.name = npc_name
        self.dna = NPCGlobals.NPC_DNA[npc_name]
        self.cards = []
        self.dealingCards = []
        self.strategicCards = []
        self.startingCards = []
        self.doId = doId
        self.drawsThisTurn = 0
        self.maxDrawsPerTurn = -1

    def generate(self):
        self.setDNAStrand(self.dna)

    def organizeStrategicCards(self):
        strategyCards = [
         str(UGG.CARD_DRAW_TWO), str(UGG.CARD_SKIP), str(UGG.CARD_WILD), str(UGG.CARD_WILD_DRAW_FOUR)]
        self.strategicCards = []
        for card in self.cards:
            if card[:2] in strategyCards:
                self.strategicCards.append(card)

    def hasStrategicCard(self):
        if len(self.strategicCards) > 0:
            return True
        return False

    def getRandomStrategicCard(self):
        card = None
        if self.hasStrategicCard():
            card = self.strategicCards[random.randint(0, len(self.strategicCards) - 1)]
        return card

    def addStartingCard(self, card):
        self.startingCards.append(card)

    def getStartingCards(self):
        return self.startingCards

    def addCard(self, card):
        self.cards.append(card)
        self.game.d_updateHeadPanelValue(self.doId, 1)
        self.organizeStrategicCards()

    def removeCard(self, card):
        if card in self.cards:
            self.cards.remove(card)
            self.game.d_updateHeadPanelValue(self.doId, 0)
            self.drawsThisTurn = 0
            self.organizeStrategicCards()

    def getCards(self):
        return self.cards

    def addDealingCard(self, card):
        self.dealingCards.append(card)

    def removeDealingCard(self, card):
        self.dealingCards.remove(card)

    def getDealingCards(self):
        return self.dealingCards

    def setDrawsThisTurn(self, draws):
        self.drawsThisTurn = draws

    def getDrawsThisTurn(self):
        return self.drawsThisTurn

    def setMaxDrawsPerTurn(self, maxDraws):
        self.maxDrawsPerTurn = maxDraws

    def getMaxDrawsPerTurn(self):
        return self.maxDrawsPerTurn

    def getName(self):
        return self.name

    def getID(self):
        return self.doId