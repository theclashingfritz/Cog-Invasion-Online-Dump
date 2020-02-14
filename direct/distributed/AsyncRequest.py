# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.AsyncRequest
from otp.ai.AIBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.DirectObject import DirectObject
from ConnectionRepository import *
ASYNC_REQUEST_DEFAULT_TIMEOUT_IN_SECONDS = 8.0
ASYNC_REQUEST_INFINITE_RETRIES = -1
ASYNC_REQUEST_DEFAULT_NUM_RETRIES = 0

class AsyncRequest(DirectObject):
    _asyncRequests = {}
    notify = DirectNotifyGlobal.directNotify.newCategory('AsyncRequest')

    def __init__(self, air, replyToChannelId=None, timeoutTime=ASYNC_REQUEST_DEFAULT_TIMEOUT_IN_SECONDS, numRetries=ASYNC_REQUEST_DEFAULT_NUM_RETRIES):
        AsyncRequest._asyncRequests[id(self)] = self
        self.deletingMessage = 'AsyncRequest-deleting-%s' % id(self)
        self.air = air
        self.replyToChannelId = replyToChannelId
        self.timeoutTask = None
        self.neededObjects = {}
        self._timeoutTime = timeoutTime
        self._initialNumRetries = numRetries
        return

    def delete(self):
        del AsyncRequest._asyncRequests[id(self)]
        self.ignoreAll()
        self._resetTimeoutTask(False)
        messenger.send(self.deletingMessage, [])
        del self.neededObjects
        del self.air
        del self.replyToChannelId

    def askForObjectField(self, dclassName, fieldName, doId, key=None, context=None):
        if key is None:
            key = fieldName
        if context is None:
            context = self.air.allocateContext()
        self.air.contextToClassName[context] = dclassName
        self.acceptOnce('doFieldResponse-%s' % (context,), self._checkCompletion, [key])
        self.neededObjects[key] = None
        self.air.queryObjectField(dclassName, fieldName, doId, context)
        self._resetTimeoutTask()
        return

    def askForObjectFields(self, dclassName, fieldNames, doId, key=None, context=None):
        if key is None:
            key = fieldNames[0]
        if context is None:
            context = self.air.allocateContext()
        self.air.contextToClassName[context] = dclassName
        self.acceptOnce('doFieldResponse-%s' % (context,), self._checkCompletion, [key])
        self.air.queryObjectFields(dclassName, fieldNames, doId, context)
        self._resetTimeoutTask()
        return

    def askForObjectFieldsByString(self, dbId, dclassName, objString, fieldNames, key=None, context=None):
        if key is None:
            key = fieldNames
        if context is None:
            context = self.air.allocateContext()
        self.air.contextToClassName[context] = dclassName
        self.acceptOnce('doFieldResponse-%s' % (context,), self._checkCompletion, [key])
        self.air.queryObjectStringFields(dbId, dclassName, objString, fieldNames, context)
        self._resetTimeoutTask()
        return

    def askForObject(self, doId, context=None):
        if context is None:
            context = self.air.allocateContext()
        self.acceptOnce('doRequestResponse-%s' % (context,), self._checkCompletion, [None])
        self.air.queryObjectAll(doId, context)
        self._resetTimeoutTask()
        return

    def createObject(self, name, className, databaseId=None, values=None, context=None):
        self.neededObjects[name] = None
        if context is None:
            context = self.air.allocateContext()
        self.accept(self.air.getDatabaseGenerateResponseEvent(context), self._doCreateObject, [name, className, values])
        self.air.requestDatabaseGenerate(className, context, databaseId=databaseId, values=values)
        self._resetTimeoutTask()
        return

    def createObjectId(self, name, className, values=None, context=None):
        self.neededObjects[name] = None
        if context is None:
            context = self.air.allocateContext()
        self.accept(self.air.getDatabaseGenerateResponseEvent(context), self._checkCompletion, [name, None])
        self.air.requestDatabaseGenerate(className, context, values=values)
        self._resetTimeoutTask()
        return

    def finish(self):
        self.delete()

    def _doCreateObject(self, name, className, values, doId):
        isInDoId2do = doId in self.air.doId2do
        distObj = self.air.generateGlobalObject(doId, className, values)
        if not isInDoId2do and game.name == 'uberDog':
            self.air.doId2do.pop(doId, None)
        self._checkCompletion(name, None, distObj)
        return

    def _checkCompletion(self, name, context, distObj):
        if name is not None:
            self.neededObjects[name] = distObj
        else:
            self.neededObjects[distObj.doId] = distObj
        for i in self.neededObjects.values():
            if i is None:
                return

        self.finish()
        return

    def _resetTimeoutTask(self, createAnew=True):
        if self.timeoutTask:
            taskMgr.remove(self.timeoutTask)
            self.timeoutTask = None
        if createAnew:
            self.numRetries = self._initialNumRetries
            self.timeoutTask = taskMgr.doMethodLater(self._timeoutTime, self.timeout, 'AsyncRequestTimer-%s' % id(self))
        return

    def timeout(self, task):
        if self.numRetries > 0:
            self.numRetries -= 1
            return Task.again
        self.delete()
        return Task.done


def cleanupAsyncRequests():
    for asyncRequest in AsyncRequest._asyncRequests:
        asyncRequest.delete()