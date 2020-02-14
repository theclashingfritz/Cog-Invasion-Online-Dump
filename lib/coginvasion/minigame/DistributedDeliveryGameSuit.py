# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.DistributedDeliveryGameSuit
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.IntervalGlobal import LerpPosInterval, Sequence, Wait
from lib.coginvasion.cog.DistributedSuit import DistributedSuit
from lib.coginvasion.npc.NPCWalker import NPCWalkInterval
import DeliveryGameGlobals as DGG, random

class DistributedDeliveryGameSuit(DistributedSuit):
    notify = directNotify.newCategory('DistributedDeliveryGameSuit')

    def __init__(self, cr):
        DistributedSuit.__init__(self, cr)
        self.truckIndex = 0

    def setTruckIndex(self, index):
        self.truckIndex = index

    def getTruckIndex(self):
        return self.truckIndex

    def enterFlyingDown(self, startIndex, endIndex, ts=0.0):
        startPos = DGG.SpawnPoints[startIndex] + (0, 0, 50)
        endPos = DGG.SpawnPoints[endIndex]
        duration = 3
        self.moveIval = LerpPosInterval(self, duration=duration, pos=endPos, startPos=startPos, fluid=1)
        self.moveIval.start(ts)
        self.animFSM.request('flyDown', [ts])
        yaw = random.uniform(0.0, 360.0)
        self.setH(yaw)

    def enterFlyingUp(self, startIndex, endIndex, ts=0.0):
        startPos = DGG.SpawnPoints[startIndex]
        endPos = DGG.SpawnPoints[endIndex] + (0, 0, 50)
        duration = 3
        self.moveIval = Sequence(Wait(1.7), LerpPosInterval(self, duration=duration, pos=endPos, startPos=startPos, fluid=1))
        self.moveIval.start(ts)
        self.animFSM.request('flyAway', [ts])

    def enterWalking(self, startIndex, endIndex, ts=0.0):
        durationFactor = 0.2
        if startIndex > -1:
            startPos = DGG.SpawnPoints[startIndex]
        else:
            startPos = self.getPos(render)
        if endIndex == DGG.WalkToTruckIndex:
            endPos = DGG.TruckSuitPointsByIndex[self.truckIndex]
        else:
            endPos = DGG.SpawnPoints[endIndex]
        self.stopMoving()
        self.moveIval = NPCWalkInterval(self, endPos, durationFactor, startPos, fluid=1)
        self.moveIval.start(ts)