# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogoffice.DistributedCogOfficeElevator
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObject import DistributedObject
from direct.interval.IntervalGlobal import Sequence, Func
from lib.coginvasion.hood import ZoneUtil
from ElevatorConstants import *
from ElevatorUtils import *
from DistributedElevator import DistributedElevator

class DistributedCogOfficeElevator(DistributedElevator):
    notify = directNotify.newCategory('DistributedCogOfficeElevator')

    def __init__(self, cr):
        DistributedElevator.__init__(self, cr)
        self.index = None
        return

    def setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self.index

    def getLeftDoor(self):
        return self.thebldg.elevators[self.index].getLeftDoor()

    def getRightDoor(self):
        return self.thebldg.elevators[self.index].getRightDoor()

    def postAnnounceGenerate(self):
        DistributedElevator.postAnnounceGenerate(self)
        self.thebldg.elevatorReady()
        self.accept(self.thebldg.uniqueName('prepareElevator'), self.__prepareElevator)

    def disable(self):
        self.ignore(self.thebldg.uniqueName('prepareElevator'))
        DistributedElevator.disable(self)

    def __prepareElevator(self):
        self.countdownTextNP.reparentTo(self.getElevatorModel())
        self.elevatorSphereNodePath.reparentTo(self.getElevatorModel())
        self.openDoors = getOpenInterval(self, self.getLeftDoor(), self.getRightDoor(), self.openSfx, None, self.type)
        self.closeDoors = getCloseInterval(self, self.getLeftDoor(), self.getRightDoor(), self.closeSfx, None, self.type)
        self.closeDoors = Sequence(self.closeDoors, Func(self.onDoorCloseFinish))
        closeDoors(self.getLeftDoor(), self.getRightDoor())
        return

    def putToonsInElevator(self):
        for i in xrange(len(self.thebldg.avatars)):
            avId = self.thebldg.avatars[i]
            toon = self.cr.doId2do.get(avId)
            if toon:
                toon.stopSmooth()
                toon.animFSM.request('neutral')
                toon.reparentTo(self.getElevatorModel())
                if self.thebldg.currentFloor == 0:
                    toon.setPos(ElevatorPoints[i])
                toon.setHpr(180, 0, 0)

    def onDoorCloseFinish(self):
        if self.index == 1:
            if self.localAvOnElevator:
                base.transitions.fadeScreen(1)
                self.thebldg.d_readyForNextFloor()
                self.localAvOnElevator = False
            else:
                requestStatus = {'zoneId': ZoneUtil.getZoneId(ZoneUtil.getHoodId(self.zoneId, street=1)), 'hoodId': self.cr.playGame.hood.hoodId, 
                   'where': 'playground', 
                   'avId': base.localAvatar.doId, 
                   'loader': 'safeZoneLoader', 
                   'shardId': None, 
                   'wantLaffMeter': 1, 
                   'world': base.cr.playGame.getCurrentWorldName(), 
                   'how': 'teleportIn'}
                self.cr.playGame.getPlace().doneStatus = requestStatus
                messenger.send(self.cr.playGame.getPlace().doneEvent)
        return

    def getElevatorModel(self):
        return self.thebldg.elevators[self.index].getElevatorModel()