# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.StagedObject


class StagedObject:
    UNKNOWN = -1
    OFF = 0
    ON = 1

    def __init__(self, initState=UNKNOWN):
        self.__state = initState

    def goOnStage(self, *args, **kw):
        if not self.isOnStage():
            self.handleOnStage(*args, **kw)

    def handleOnStage(self):
        self.__state = StagedObject.ON

    def goOffStage(self, *args, **kw):
        if not self.isOffStage():
            self.handleOffStage(*args, **kw)

    def handleOffStage(self):
        self.__state = StagedObject.OFF

    def isOnStage(self):
        return self.__state == StagedObject.ON

    def isOffStage(self):
        return self.__state == StagedObject.OFF