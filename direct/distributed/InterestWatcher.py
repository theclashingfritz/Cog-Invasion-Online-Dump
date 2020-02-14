# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.InterestWatcher
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.DirectObject import DirectObject
from direct.showbase.EventGroup import EventGroup

class InterestWatcher(DirectObject):
    notify = directNotify.newCategory('InterestWatcher')

    def __init__(self, interestMgr, name, doneEvent=None, recurse=True, start=True, mustCollect=False, doCollectionMgr=None):
        DirectObject.__init__(self)
        self._interestMgr = interestMgr
        if doCollectionMgr is None:
            doCollectionMgr = interestMgr
        self._doCollectionMgr = doCollectionMgr
        self._eGroup = EventGroup(name, doneEvent=doneEvent)
        self._doneEvent = self._eGroup.getDoneEvent()
        self._gotEvent = False
        self._recurse = recurse
        if self._recurse:
            self.closingParent2zones = {}
        if start:
            self.startCollect(mustCollect)
        return

    def startCollect(self, mustCollect=False):
        self._mustCollect = mustCollect
        self.accept(self._interestMgr._getAddInterestEvent(), self._handleInterestOpenEvent)
        self.accept(self._interestMgr._getRemoveInterestEvent(), self._handleInterestCloseEvent)

    def stopCollect(self):
        self.ignore(self._interestMgr._getAddInterestEvent())
        self.ignore(self._interestMgr._getRemoveInterestEvent())
        mustCollect = self._mustCollect
        del self._mustCollect
        if not self._gotEvent:
            if mustCollect:
                logFunc = self.notify.error
            else:
                logFunc = self.notify.warning
            logFunc('%s: empty interest-complete set' % self.getName())
            self.destroy()
            messenger.send(self.getDoneEvent())
        else:
            self.accept(self.getDoneEvent(), self.destroy)

    def destroy(self):
        if hasattr(self, '_eGroup'):
            self._eGroup.destroy()
            del self._eGroup
            del self._gotEvent
            del self._interestMgr
            self.ignoreAll()

    def getName(self):
        return self._eGroup.getName()

    def getDoneEvent(self):
        return self._doneEvent

    def _handleInterestOpenEvent(self, event):
        self._gotEvent = True
        self._eGroup.addEvent(event)

    def _handleInterestCloseEvent(self, event, parentId, zoneIdList):
        self._gotEvent = True
        self._eGroup.addEvent(event)