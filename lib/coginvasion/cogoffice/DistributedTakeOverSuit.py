# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogoffice.DistributedTakeOverSuit
from panda3d.core import Point3
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.interval.IntervalGlobal import LerpPosInterval, Parallel, Sequence, Wait, Func
from direct.distributed.ClockDelta import globalClockDelta
from lib.coginvasion.cog.DistributedSuit import DistributedSuit

class DistributedTakeOverSuit(DistributedSuit):
    notify = directNotify.newCategory('DistributedTakeOverSuit')
    StartPosFromDoor = Point3(1.6, -10, -0.5)
    AtDoorPos = Point3(1.6, -1, 0)

    def __init__(self, cr):
        DistributedSuit.__init__(self, cr)
        self.doorDoId = None
        self.door = None
        self.takeOverTrack = None
        self.fsm = ClassicFSM('DTOS-fsm', [
         State('off', self.enterOff, self.exitOff),
         State('takeOver', self.enterTakeOver, self.exitTakeOver)], 'off', 'off')
        self.fsm.enterInitialState()
        return

    def interruptTakeOver(self):
        if self.takeOverTrack:
            self.takeOverTrack.pause()
            self.takeOverTrack = None
        return

    def setState(self, state, timestamp):
        ts = globalClockDelta.localElapsedTime(timestamp)
        self.fsm.request(state, [ts])

    def disable(self):
        taskMgr.remove('posTask')
        self.fsm.requestFinalState()
        self.fsm = None
        self.doorDoId = None
        self.door = None
        if self.takeOverTrack:
            self.takeOverTrack.finish()
            self.takeOverTrack = None
        DistributedSuit.disable(self)
        return

    def setDoorDoId(self, doId):
        self.doorDoId = doId
        self.door = self.cr.doId2do.get(doId)
        if self.door is None:
            taskMgr.add(self.__pollDoor, self.uniqueName('pollDoor'))
        return

    def stateAndTimestamp(self, state, timestamp):
        self.setState(state, timestamp)

    def __pollDoor(self, task):
        self.door = self.cr.doId2do.get(self.doorDoId)
        if self.door:
            self.sendUpdate('requestStateAndTimestamp')
            return task.done
        return task.cont

    def getDoorDoId(self):
        return self.doorDoId

    def enterOff(self, ts=0):
        pass

    def exitOff(self):
        pass

    def enterTakeOver(self, ts=0):
        if not self.door:
            return
        self.stopSmooth()
        self.hasSpawned = False
        self.reparentTo(self.door.doorNode)
        self.setHpr(0, 0, 0)
        self.takeOverTrack = Parallel(Sequence(Func(self.animFSM.request, 'flyDown', [ts]), Wait(6.834), Func(self.setAnimState, 'neutral'), Wait(0.5), Func(self.setAnimState, 'walk'), LerpPosInterval(self, duration=2.0, pos=DistributedTakeOverSuit.AtDoorPos, startPos=DistributedTakeOverSuit.StartPosFromDoor), Func(self.setAnimState, 'neutral'), Wait(0.3), Func(self.setAnimState, 'walk'), LerpPosInterval(self, duration=0.5, pos=self.door.enterDoorWalkBackNode.getPos(), startPos=DistributedTakeOverSuit.AtDoorPos), Func(self.setAnimState, 'neutral'), Wait(1.0), Func(self.setAnimState, 'walk'), LerpPosInterval(self, duration=1.0, pos=self.door.enterDoorWalkInNode.getPos(), startPos=self.door.enterDoorWalkBackNode.getPos())), LerpPosInterval(self, duration=4.375, pos=DistributedTakeOverSuit.StartPosFromDoor, startPos=DistributedTakeOverSuit.StartPosFromDoor + (0, 0, 31.2)))
        self.takeOverTrack.start(ts)

    def exitTakeOver(self):
        if self.takeOverTrack:
            self.takeOverTrack.pause()
            self.takeOverTrack = None
        return