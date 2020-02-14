# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.fsm.FSM
__all__ = [
 'FSMException', 'FSM']
from direct.showbase.DirectObject import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import PythonUtil
from direct.stdpy.threading import RLock
import types

class FSMException(Exception):
    pass


class AlreadyInTransition(FSMException):
    pass


class RequestDenied(FSMException):
    pass


class FSM(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('FSM')
    SerialNum = 0
    defaultTransitions = None

    def __init__(self, name):
        self.fsmLock = RLock()
        self._name = name
        self.stateArray = []
        self._serialNum = FSM.SerialNum
        FSM.SerialNum += 1
        self._broadcastStateChanges = False
        self._state = 'Off'
        self.__requestQueue = []

    def cleanup(self):
        self.fsmLock.acquire()
        try:
            if self._state != 'Off':
                self.__setState('Off')
        finally:
            self.fsmLock.release()

    def setBroadcastStateChanges(self, doBroadcast):
        self._broadcastStateChanges = doBroadcast

    def getStateChangeEvent(self):
        return 'FSM-%s-%s-stateChange' % (self._serialNum, self._name)

    def getCurrentFilter(self):
        if not self._state:
            error = 'FSM cannot determine current filter while in transition (%s -> %s).' % (self.oldState, self.newState)
            raise AlreadyInTransition, error
        filter = getattr(self, 'filter' + self._state, None)
        if not filter:
            filter = self.defaultFilter
        return filter

    def getCurrentOrNextState(self):
        self.fsmLock.acquire()
        try:
            if self._state:
                return self._state
            return self.newState
        finally:
            self.fsmLock.release()

    def getCurrentStateOrTransition(self):
        self.fsmLock.acquire()
        try:
            if self._state:
                return self._state
            return '%s -> %s' % (self.oldState, self.newState)
        finally:
            self.fsmLock.release()

    def isInTransition(self):
        self.fsmLock.acquire()
        try:
            return self._state == None
        finally:
            self.fsmLock.release()

        return

    def forceTransition(self, request, *args):
        self.fsmLock.acquire()
        try:
            self.notify.debug('%s.forceTransition(%s, %s' % (
             self._name, request, str(args)[1:]))
            if not self._state:
                self.__requestQueue.append(PythonUtil.Functor(self.forceTransition, request, *args))
                return
            self.__setState(request, *args)
        finally:
            self.fsmLock.release()

    def demand(self, request, *args):
        self.fsmLock.acquire()
        try:
            self.notify.debug('%s.demand(%s, %s' % (
             self._name, request, str(args)[1:]))
            if not self._state:
                self.__requestQueue.append(PythonUtil.Functor(self.demand, request, *args))
                return
            if not self.request(request, *args):
                raise RequestDenied, '%s (from state: %s)' % (request, self._state)
        finally:
            self.fsmLock.release()

    def request(self, request, *args):
        self.fsmLock.acquire()
        try:
            self.notify.debug('%s.request(%s, %s' % (
             self._name, request, str(args)[1:]))
            filter = self.getCurrentFilter()
            result = filter(request, args)
            if result:
                if isinstance(result, types.StringTypes):
                    result = (
                     result,) + args
                self.__setState(*result)
            return result
        finally:
            self.fsmLock.release()

    def defaultEnter(self, *args):
        pass

    def defaultExit(self):
        pass

    def defaultFilter(self, request, args):
        if request == 'Off':
            return (
             request,) + args
        if self.defaultTransitions is None:
            if request[0].isupper():
                return (request,) + args
        else:
            if request in self.defaultTransitions.get(self._state, []):
                return (
                 request,) + args
        if request[0].isupper():
            raise RequestDenied, '%s (from state: %s)' % (request, self._state)
        return

    def filterOff(self, request, args):
        if request[0].isupper():
            return (request,) + args
        return self.defaultFilter(request, args)

    def setStateArray(self, stateArray):
        self.fsmLock.acquire()
        try:
            self.stateArray = stateArray
        finally:
            self.fsmLock.release()

    def requestNext(self, *args):
        self.fsmLock.acquire()
        try:
            if self.stateArray:
                if self._state not in self.stateArray:
                    self.request(self.stateArray[0])
                else:
                    cur_index = self.stateArray.index(self._state)
                    new_index = (cur_index + 1) % len(self.stateArray)
                    self.request(self.stateArray[new_index], args)
        finally:
            self.fsmLock.release()

    def requestPrev(self, *args):
        self.fsmLock.acquire()
        try:
            if self.stateArray:
                if self.state not in self.stateArray:
                    self.request(self.stateArray[0])
                else:
                    cur_index = self.stateArray.index(self._state)
                    new_index = (cur_index - 1) % len(self.stateArray)
                    self.request(self.stateArray[new_index], args)
        finally:
            self.fsmLock.release()

    def __setState(self, newState, *args):
        self.oldState = self._state
        self.newState = newState
        self._state = None
        try:
            if not self.__callFromToFunc(self.oldState, self.newState, *args):
                self.__callExitFunc(self.oldState)
                self.__callEnterFunc(self.newState, *args)
        except:
            self._state = 'InternalError'
            del self.oldState
            del self.newState
            raise

        if self._broadcastStateChanges:
            messenger.send(self.getStateChangeEvent())
        self._state = newState
        del self.oldState
        del self.newState
        if self.__requestQueue:
            request = self.__requestQueue.pop(0)
            request()
        return

    def __callEnterFunc(self, name, *args):
        func = getattr(self, 'enter' + name, None)
        if not func:
            func = self.defaultEnter
        func(*args)
        return

    def __callFromToFunc(self, oldState, newState, *args):
        func = getattr(self, 'from%sTo%s' % (oldState, newState), None)
        if func:
            func(*args)
            return True
        return False

    def __callExitFunc(self, name):
        func = getattr(self, 'exit' + name, None)
        if not func:
            func = self.defaultExit
        func()
        return

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        self.fsmLock.acquire()
        try:
            className = self.__class__.__name__
            if self._state:
                str = '%s FSM:%s in state "%s"' % (className, self._name, self._state)
            else:
                str = "%s FSM:%s in transition from '%s' to '%s'" % (className, self._name, self.oldState, self.newState)
            return str
        finally:
            self.fsmLock.release()