# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.EventManager
__all__ = [
 'EventManager']
from MessengerGlobal import *
from direct.directnotify.DirectNotifyGlobal import *
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import PStatCollector, EventQueue, EventHandler

class EventManager:
    notify = None
    PStatCollector = None

    def __init__(self, eventQueue=None):
        if EventManager.notify == None:
            EventManager.notify = directNotify.newCategory('EventManager')
        self.eventQueue = eventQueue
        self.eventHandler = None
        self._wantPstats = None
        return

    def doEvents(self):
        if self._wantPstats is None:
            self._wantPstats = config.GetBool('pstats-eventmanager', 0)
            EventManager.PStatCollector = PStatCollector
        if self._wantPstats:
            processFunc = self.processEventPstats
        else:
            processFunc = self.processEvent
        while not self.eventQueue.isQueueEmpty():
            processFunc(self.eventQueue.dequeueEvent())

        return

    def eventLoopTask(self, task):
        self.doEvents()
        messenger.send('event-loop-done')
        return task.cont

    def parseEventParameter(self, eventParameter):
        if eventParameter.isInt():
            return eventParameter.getIntValue()
        if eventParameter.isDouble():
            return eventParameter.getDoubleValue()
        if eventParameter.isString():
            return eventParameter.getStringValue()
        if eventParameter.isWstring():
            return eventParameter.getWstringValue()
        if eventParameter.isTypedRefCount():
            return eventParameter.getTypedRefCountValue()
        if eventParameter.isEmpty():
            return
        return eventParameter.getPtr()
        return

    def processEvent(self, event):
        eventName = event.getName()
        if eventName:
            paramList = []
            for i in range(event.getNumParameters()):
                eventParameter = event.getParameter(i)
                eventParameterData = self.parseEventParameter(eventParameter)
                paramList.append(eventParameterData)

            if EventManager.notify.getDebug() and eventName != 'NewFrame':
                EventManager.notify.debug('received C++ event named: ' + eventName + ' parameters: ' + repr(paramList))
            if paramList:
                messenger.send(eventName, paramList)
            else:
                messenger.send(eventName)
            if self.eventHandler:
                self.eventHandler.dispatchEvent(event)
        else:
            EventManager.notify.warning('unnamed event in processEvent')

    def processEventPstats(self, event):
        eventName = event.getName()
        if eventName:
            paramList = []
            for i in range(event.getNumParameters()):
                eventParameter = event.getParameter(i)
                eventParameterData = self.parseEventParameter(eventParameter)
                paramList.append(eventParameterData)

            if EventManager.notify.getDebug() and eventName != 'NewFrame':
                EventManager.notify.debug('received C++ event named: ' + eventName + ' parameters: ' + repr(paramList))
            if self._wantPstats:
                name = eventName
                hyphen = name.find('-')
                if hyphen >= 0:
                    name = name[0:hyphen]
                pstatCollector = EventManager.PStatCollector('App:Show code:eventManager:' + name)
                pstatCollector.start()
                if self.eventHandler:
                    cppPstatCollector = EventManager.PStatCollector('App:Show code:eventManager:' + name + ':C++')
            if paramList:
                messenger.send(eventName, paramList)
            else:
                messenger.send(eventName)
            if self.eventHandler:
                if self._wantPstats:
                    cppPstatCollector.start()
                self.eventHandler.dispatchEvent(event)
            if self._wantPstats:
                if self.eventHandler:
                    cppPstatCollector.stop()
                pstatCollector.stop()
        else:
            EventManager.notify.warning('unnamed event in processEvent')

    def restart(self):
        if self.eventQueue == None:
            self.eventQueue = EventQueue.getGlobalEventQueue()
        if self.eventHandler == None:
            if self.eventQueue == EventQueue.getGlobalEventQueue():
                self.eventHandler = EventHandler.getGlobalEventHandler()
            else:
                self.eventHandler = EventHandler(self.eventQueue)
        taskMgr.add(self.eventLoopTask, 'eventManager')
        return

    def shutdown(self):
        taskMgr.remove('eventManager')
        if self.eventQueue is not None:
            self.eventQueue.clear()
        return