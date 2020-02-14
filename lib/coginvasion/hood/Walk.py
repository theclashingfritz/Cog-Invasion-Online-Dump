# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.Walk
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.StateData import StateData
from direct.fsm.State import State
from direct.directnotify.DirectNotifyGlobal import directNotify

class Walk(StateData):
    notify = directNotify.newCategory('Walk')

    def __init__(self, doneEvent):
        StateData.__init__(self, doneEvent)
        self.fsm = ClassicFSM('Walk', [
         State('off', self.enterOff, self.exitOff, ['walking', 'deadWalking']),
         State('walking', self.enterWalking, self.exitWalking),
         State('deadWalking', self.enterDeadWalking, self.exitDeadWalking)], 'off', 'off')
        self.fsm.enterInitialState()

    def load(self):
        pass

    def unload(self):
        del self.fsm

    def enter(self):
        base.localAvatar.startPosHprBroadcast()
        base.localAvatar.d_broadcastPositionNow()
        base.localAvatar.startBlink()
        base.localAvatar.attachCamera()
        base.localAvatar.startSmartCamera()
        base.localAvatar.collisionsOn()
        base.localAvatar.enableAvatarControls()

    def exit(self):
        base.localAvatar.lastState = None
        self.fsm.request('off')
        base.localAvatar.disableAvatarControls()
        base.localAvatar.detachCamera()
        base.localAvatar.stopSmartCamera()
        base.localAvatar.stopPosHprBroadcast()
        base.localAvatar.stopBlink()
        base.localAvatar.collisionsOff()
        base.localAvatar.controlManager.placeOnFloor()
        return

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterWalking(self):
        if base.localAvatar.getHealth() > 0:
            base.localAvatar.startTrackAnimToSpeed()
            base.localAvatar.setWalkSpeedNormal()
        else:
            self.fsm.request('deadWalking')

    def exitWalking(self):
        base.localAvatar.stopTrackAnimToSpeed()

    def enterDeadWalking(self):
        base.localAvatar.startTrackAnimToSpeed()
        base.localAvatar.setWalkSpeedSlow()
        base.taskMgr.add(self.__watchForPositiveHP, base.localAvatar.uniqueName('watchforPositiveHP'))

    def __watchForPositiveHP(self, task):
        if base.localAvatar.getHealth() > 0:
            self.fsm.request('walking')
            return task.done
        return task.cont

    def exitDeadWalking(self):
        base.taskMgr.remove(base.localAvatar.uniqueName('watchforPositiveHP'))
        base.localAvatar.stopTrackAnimToSpeed()