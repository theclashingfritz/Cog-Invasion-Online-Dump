# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.toon.LabelScaler
import math

class LabelScaler:
    SCALING_MINDIST = 1
    SCALING_MAXDIST = 50

    def __init__(self, factor=0.06):
        self.SCALING_FACTOR = factor

    def resize(self, node):
        self.node = node
        taskMgr.add(self.resizeTask, 'resizeTask')

    def resizeTask(self, task):
        if self.node.isEmpty():
            return task.done
        distance = self.node.getDistance(camera)
        distance = max(min(distance, self.SCALING_MAXDIST), self.SCALING_MINDIST)
        self.node.setScale(math.sqrt(distance) * self.SCALING_FACTOR)
        return task.cont