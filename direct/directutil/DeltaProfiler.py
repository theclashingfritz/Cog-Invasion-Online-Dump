# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.directutil.DeltaProfiler
from time import time

class DeltaProfiler:

    def __init__(self, name=''):
        self.name = name
        self.priorLabel = ''
        self.priorTime = 0
        self.active = 0

    def printDeltaTime(self, label):
        if self.active:
            deltaTime = time() - self.priorTime
            print '%s DeltaTime %-25s to %-25s: %3.5f' % (
             self.name,
             self.priorLabel,
             label,
             deltaTime)
            self.priorLabel = label
            self.priorTime = time()