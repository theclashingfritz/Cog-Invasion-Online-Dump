# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.QuietZoneState
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.fsm.StateData import StateData
from lib.coginvasion.distributed.CogInvasionMsgTypes import *

class QuietZoneState(StateData):

    def __init__(self, doneEvent, moveOn=1):
        StateData.__init__(self, doneEvent)
        self.fsm = ClassicFSM('quietZone', [
         State('off', self.enterOff, self.exitOff, [
          'waitForQuietZoneResponse']),
         State('waitForQuietZoneResponse', self.enterWaitForQuietZoneResponse, self.exitWaitForQuietZoneResponse, [
          'waitForSetZoneResponse']),
         State('waitForSetZoneResponse', self.enterWaitForSetZoneResponse, self.exitWaitForSetZoneResponse, [
          'waitForSetZoneComplete']),
         State('waitForSetZoneComplete', self.enterWaitForSetZoneComplete, self.exitWaitForSetZoneComplete, [
          'off'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.moveOn = moveOn

    def getSetZoneCompleteEvent(self):
        return 'setZoneComplete-%s' % id(self)

    def getQuietZoneResponseEvent(self):
        return 'quietZoneResponse-%s' % id(self)

    def getEnterWaitForSetZoneResponseMsg(self):
        return 'enterWaitForSetZoneResponse-%s' % id(self)

    def unload(self):
        StateData.unload(self)
        del self.fsm

    def enter(self, requestStatus):
        StateData.enter(self)
        self._requestStatus = requestStatus
        base.localAvatar.b_setAnimState('off')
        self.fsm.request('waitForQuietZoneResponse')

    def exit(self):
        StateData.exit(self)
        if self._requestStatus.get('how', None) != 'doorOut':
            base.transitions.noTransitions()
        del self._requestStatus
        self.fsm.request('off')
        return

    def getDoneStatus(self):
        return self._requestStatus

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def handleWaitForQuietZoneResponse(self, msgType, di):
        if msgType == CLIENT_ENTER_OBJECT_REQUIRED:
            base.cr.handleQuietZoneGenerateWithRequired(di)
        else:
            if msgType == CLIENT_ENTER_OBJECT_REQUIRED_OTHER:
                base.cr.handleQuietZoneGenerateWithRequiredOther(di)
            else:
                if msgType == CLIENT_OBJECT_SET_FIELD:
                    base.cr.handleQuietZoneUpdateField(di)
                else:
                    base.cr.astronHandle(di)

    def enterWaitForQuietZoneResponse(self):
        self.setZoneDoneEvent = base.cr.getNextSetZoneDoneEvent()
        self.acceptOnce(self.setZoneDoneEvent, self._handleQuietZoneResponse)
        base.cr.sendQuietZoneRequest()

    def _handleQuietZoneResponse(self):
        if self.moveOn:
            self.fsm.request('waitForSetZoneResponse')
        else:
            messenger.send('enteredQuietZone')

    def exitWaitForQuietZoneResponse(self):
        self.ignore(self.setZoneDoneEvent)
        del self.setZoneDoneEvent

    def enterWaitForZoneRedirect(self):
        self.fsm.request('waitForSetZoneResponse')

    def exitWaitForZoneRedirect(self):
        pass

    def enterWaitForSetZoneResponse(self):
        zoneId = self._requestStatus['zoneId']
        base.cr.sendSetZoneMsg(zoneId)
        self.fsm.request('waitForSetZoneComplete')

    def exitWaitForSetZoneResponse(self):
        pass

    def enterWaitForSetZoneComplete(self):
        self.setZoneDoneEvent = base.cr.getLastSetZoneDoneEvent()
        self.acceptOnce(self.setZoneDoneEvent, self._announceDone)

    def exitWaitForSetZoneComplete(self):
        self.ignore(self.setZoneDoneEvent)
        del self.setZoneDoneEvent

    def _announceDone(self):
        doneEvent = self.doneEvent
        requestStatus = self._requestStatus
        messenger.send(self.getSetZoneCompleteEvent(), [requestStatus])
        messenger.send(doneEvent)

    def getRequestStatus(self):
        return self._requestStatus