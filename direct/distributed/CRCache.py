# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.CRCache
from direct.directnotify import DirectNotifyGlobal
import DistributedObject

class CRCache:
    notify = DirectNotifyGlobal.directNotify.newCategory('CRCache')

    def __init__(self, maxCacheItems=10):
        self.maxCacheItems = maxCacheItems
        self.storedCacheItems = maxCacheItems
        self.dict = {}
        self.fifo = []

    def isEmpty(self):
        return len(self.fifo) == 0

    def flush(self):
        CRCache.notify.debug('Flushing the cache')
        messenger.send('clientCleanup')
        delayDeleted = []
        for distObj in self.dict.values():
            distObj.deleteOrDelay()
            if distObj.getDelayDeleteCount() != 0:
                delayDeleted.append(distObj)
            if distObj.getDelayDeleteCount() <= 0:
                distObj.detectLeaks()

        delayDeleteLeaks = []
        for distObj in delayDeleted:
            if distObj.getDelayDeleteCount() != 0:
                delayDeleteLeaks.append(distObj)

        if len(delayDeleteLeaks):
            s = 'CRCache.flush:'
            for obj in delayDeleteLeaks:
                s += '\n  could not delete %s (%s), delayDeletes=%s' % (
                 safeRepr(obj), itype(obj), obj.getDelayDeleteNames())

            self.notify.error(s)
        self.dict = {}
        self.fifo = []

    def cache(self, distObj):
        doId = distObj.getDoId()
        success = False
        if doId in self.dict:
            CRCache.notify.warning('Double cache attempted for distObj ' + str(doId))
        else:
            distObj.disableAndAnnounce()
            self.fifo.append(distObj)
            self.dict[doId] = distObj
            success = True
            if len(self.fifo) > self.maxCacheItems:
                oldestDistObj = self.fifo.pop(0)
                del self.dict[oldestDistObj.getDoId()]
                oldestDistObj.deleteOrDelay()
                if oldestDistObj.getDelayDeleteCount() <= 0:
                    oldestDistObj.detectLeaks()
        return success

    def retrieve(self, doId):
        if doId in self.dict:
            distObj = self.dict[doId]
            del self.dict[doId]
            self.fifo.remove(distObj)
            return distObj
        return
        return

    def contains(self, doId):
        return doId in self.dict

    def delete(self, doId):
        distObj = self.dict[doId]
        del self.dict[doId]
        self.fifo.remove(distObj)
        distObj.deleteOrDelay()
        if distObj.getDelayDeleteCount() <= 0:
            distObj.detectLeaks()

    def checkCache(self):
        from pandac.PandaModules import NodePath
        for obj in self.dict.values():
            if isinstance(obj, NodePath):
                continue

        return 1

    def turnOff(self):
        self.flush()
        self.storedMaxCache = self.maxCacheItems
        self.maxCacheItems = 0

    def turnOn(self):
        self.maxCacheItems = self.storedMaxCache