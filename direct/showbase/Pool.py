# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.Pool
__all__ = [
 'Pool']
from direct.directnotify import DirectNotifyGlobal

class Pool:
    notify = DirectNotifyGlobal.directNotify.newCategory('Pool')

    def __init__(self, free=None):
        if free:
            self.__free = free
        else:
            self.__free = []
        self.__used = []

    def add(self, item):
        self.__free.append(item)

    def remove(self, item):
        if item in self.__free:
            self.__free.remove(item)
        else:
            if item in self.__used:
                self.__used.remove(item)
            else:
                self.notify.error('item not in pool')

    def checkout(self):
        if not self.__free:
            self.notify.error('no items are free')
        item = self.__free.pop()
        self.__used.append(item)
        return item

    def checkin(self, item):
        if item not in self.__used:
            self.notify.error('item is not checked out')
        self.__used.remove(item)
        self.__free.append(item)

    def reset(self):
        self.__free.extend(self.__used)
        self.__used = []

    def hasFree(self):
        return len(self.__free) != 0

    def isFree(self, item):
        return item in self.__free

    def isUsed(self, item):
        return item in self.__used

    def getNumItems(self):
        return (
         len(self.__free), len(self.__used))

    def cleanup(self, cleanupFunc=None):
        if cleanupFunc:
            allItems = self.__free + self.__used
            for item in allItems:
                cleanupFunc(item)

        del self.__free
        del self.__used

    def __repr__(self):
        return 'free = %s\nused = %s' % (self.__free, self.__used)