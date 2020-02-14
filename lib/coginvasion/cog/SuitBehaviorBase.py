# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cog.SuitBehaviorBase
from direct.showbase.DirectObject import DirectObject

class SuitBehaviorBase(DirectObject):

    def __init__(self, suit, doneEvent=None):
        if doneEvent == None:
            doneEvent = 'suit%s-behaviorDone' % suit.doId
        self.doneEvent = doneEvent
        self.suit = suit
        return

    def isAvatarReachable(self, var, exitFSM=False):
        if var == None or var.isEmpty():
            if hasattr(self, 'fsm') and exitFSM:
                self.fsm.enterInitialState()
                self.suit.getBrain().exitCurrentBehavior()
            return False
        return True

    def enter(self):
        if self.isEntered == 1:
            return
        self.isEntered = 1

    def exit(self):
        if self.isEntered == 1:
            self.isEntered = 0
            messenger.send(self.doneEvent)
            if self.suit and self.suit.brain:
                if self.suit.brain.currentBehavior == self:
                    self.suit.brain.currentBehavior = None
        return

    def canEnter(self):
        return not self.isEntered

    def load(self):
        pass

    def unload(self):
        if hasattr(self, 'suit'):
            self.suit = None
            del self.suit
        del self.isEntered
        del self.doneEvent
        return

    def shouldStart(self):
        pass

    def isActive(self):
        return self.isEntered

    def getDoneEvent(self):
        return self.doneEvent