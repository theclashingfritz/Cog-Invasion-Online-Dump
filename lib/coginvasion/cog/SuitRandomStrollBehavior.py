# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cog.SuitRandomStrollBehavior
from lib.coginvasion.cog.SuitPathBehavior import SuitPathBehavior

class SuitRandomStrollBehavior(SuitPathBehavior):

    def __init__(self, suit):
        SuitPathBehavior.__init__(self, suit)
        self.isEntered = 0

    def enter(self):
        SuitPathBehavior.enter(self)
        self.createPath(fromCurPos=True)

    def shouldStart(self):
        return True