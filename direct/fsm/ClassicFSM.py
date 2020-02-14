# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.fsm.ClassicFSM
__all__ = [
 'ClassicFSM']
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.DirectObject import DirectObject
import types, weakref

class ClassicFSM(DirectObject):
    notify = directNotify.newCategory('ClassicFSM')
    ALLOW = 0
    DISALLOW = 1
    DISALLOW_VERBOSE = 2
    ERROR = 3

    def __init__(self, name, states=[], initialStateName=None, finalStateName=None, onUndefTransition=DISALLOW_VERBOSE):
        self.setName(name)
        self.setStates(states)
        self.setInitialState(initialStateName)
        self.setFinalState(finalStateName)
        self.onUndefTransition = onUndefTransition
        self.inspecting = 0
        self.__currentState = None
        self.__internalStateInFlux = 0
        return

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        currentState = self.getCurrentState()
        if currentState:
            str = 'ClassicFSM ' + self.getName() + ' in state "' + currentState.getName() + '"'
        else:
            str = 'ClassicFSM ' + self.getName() + ' not in any state'
        return str

    def enterInitialState(self, argList=[]):
        if self.__currentState == self.__initialState:
            return
        self.__internalStateInFlux = 1
        self.__enter(self.__initialState, argList)

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getStates(self):
        return self.__states.values()

    def setStates(self, states):
        self.__states = {}
        for state in states:
            self.__states[state.getName()] = state

    def addState(self, state):
        self.__states[state.getName()] = state

    def getInitialState(self):
        return self.__initialState

    def setInitialState(self, initialStateName):
        self.__initialState = self.getStateNamed(initialStateName)

    def getFinalState(self):
        return self.__finalState

    def setFinalState(self, finalStateName):
        self.__finalState = self.getStateNamed(finalStateName)

    def requestFinalState(self):
        self.request(self.getFinalState().getName())

    def getCurrentState(self):
        return self.__currentState

    def getStateNamed(self, stateName):
        state = self.__states.get(stateName)
        if state:
            return state
        ClassicFSM.notify.warning('[%s]: getStateNamed: %s, no such state' % (
         self.__name, stateName))

    def hasStateNamed(self, stateName):
        result = False
        state = self.__states.get(stateName)
        if state:
            result = True
        return result

    def __exitCurrent(self, argList):
        self.__currentState.exit(argList)
        if self.inspecting:
            messenger.send(self.getName() + '_' + self.__currentState.getName() + '_exited')
        self.__currentState = None
        return

    def __enter(self, aState, argList=[]):
        stateName = aState.getName()
        if stateName in self.__states:
            self.__currentState = aState
            if self.inspecting:
                messenger.send(self.getName() + '_' + stateName + '_entered')
            self.__internalStateInFlux = 0
            aState.enter(argList)
        else:
            self.__internalStateInFlux = 0
            ClassicFSM.notify.error('[%s]: enter: no such state' % self.__name)

    def __transition(self, aState, enterArgList=[], exitArgList=[], exitCurrent=1):
        self.__internalStateInFlux = 1
        if exitCurrent == 1:
            self.__exitCurrent(exitArgList)
        self.__enter(aState, enterArgList)

    def request(self, aStateName, enterArgList=[], exitArgList=[], force=0, exitCurrent=1):
        if not self.__currentState:
            ClassicFSM.notify.warning('[%s]: request: never entered initial state' % self.__name)
            self.__currentState = self.__initialState
        if isinstance(aStateName, types.StringType):
            aState = self.getStateNamed(aStateName)
        else:
            aState = aStateName
            aStateName = aState.getName()
        if aState == None:
            ClassicFSM.notify.error('[%s]: request: %s, no such state' % (
             self.__name, aStateName))
        transitionDefined = self.__currentState.isTransitionDefined(aStateName)
        transitionAllowed = transitionDefined
        if self.onUndefTransition == ClassicFSM.ALLOW:
            transitionAllowed = 1
            if not transitionDefined:
                ClassicFSM.notify.warning('[%s]: performing undefined transition from %s to %s' % (
                 self.__name,
                 self.__currentState.getName(),
                 aStateName))
        if transitionAllowed or force:
            self.__transition(aState, enterArgList, exitArgList, exitCurrent)
            return 1
        if aStateName == self.__finalState.getName():
            if self.__currentState == self.__finalState:
                return 1
            self.__transition(aState, enterArgList, exitArgList, exitCurrent)
            return 1
        else:
            if aStateName == self.__currentState.getName():
                return 0
        msg = '[%s]: no transition exists from %s to %s' % (
         self.__name,
         self.__currentState.getName(),
         aStateName)
        if self.onUndefTransition == ClassicFSM.ERROR:
            ClassicFSM.notify.error(msg)
        else:
            if self.onUndefTransition == ClassicFSM.DISALLOW_VERBOSE:
                ClassicFSM.notify.warning(msg)
            return 0
        return

    def forceTransition(self, aStateName, enterArgList=[], exitArgList=[]):
        self.request(aStateName, enterArgList, exitArgList, force=1)

    def conditional_request(self, aStateName, enterArgList=[], exitArgList=[]):
        if not self.__currentState:
            ClassicFSM.notify.warning('[%s]: request: never entered initial state' % self.__name)
            self.__currentState = self.__initialState
        if isinstance(aStateName, types.StringType):
            aState = self.getStateNamed(aStateName)
        else:
            aState = aStateName
            aStateName = aState.getName()
        if aState == None:
            ClassicFSM.notify.error('[%s]: request: %s, no such state' % (
             self.__name, aStateName))
        transitionDefined = self.__currentState.isTransitionDefined(aStateName) or aStateName in [self.__currentState.getName(),
         self.__finalState.getName()]
        if transitionDefined:
            return self.request(aStateName, enterArgList, exitArgList)
        return 0
        return

    def view(self):
        from direct.tkpanels import FSMInspector
        FSMInspector.FSMInspector(self)

    def isInternalStateInFlux(self):
        return self.__internalStateInFlux