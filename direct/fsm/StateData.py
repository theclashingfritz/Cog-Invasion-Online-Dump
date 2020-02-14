# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.fsm.StateData
__all__ = [
 'StateData']
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.DirectObject import DirectObject
from direct.directnotify import DirectNotifyGlobal

class StateData(DirectObject):
    notify = directNotify.newCategory('StateData')

    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.doneStatus = None
        self.isLoaded = 0
        self.isEntered = 0
        return

    def enter(self):
        if self.isEntered:
            return 0
        if not self.isLoaded:
            self.notify.warning('entered StateData before it was loaded')
            self.load()
        self.isEntered = 1
        StateData.notify.debug('enter()')
        return 1

    def exit(self):
        if not self.isEntered:
            return 0
        self.isEntered = 0
        StateData.notify.debug('exit()')
        return 1

    def load(self):
        if self.isLoaded:
            return 0
        self.isLoaded = 1
        StateData.notify.debug('load()')
        return 1

    def unload(self):
        if not self.isLoaded:
            return 0
        if self.isEntered:
            self.notify.warning('unloaded StateData before it was exited')
            self.exit()
        self.isLoaded = 0
        StateData.notify.debug('unload()')
        return 1

    def getDoneStatus(self):
        return self.doneStatus