# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogoffice.CogOfficeSuitWalkBehavior
from panda3d.core import Point3
from lib.coginvasion.cog.SuitPathBehavior import SuitPathBehavior
from CogOfficeConstants import *

class CogOfficeSuitWalkBehavior(SuitPathBehavior):

    def __init__(self, suit, spot):
        SuitPathBehavior.__init__(self, suit)
        self.spot = spot

    def unload(self):
        del self.spot
        SuitPathBehavior.unload(self)

    def enter(self):
        SuitPathBehavior.enter(self)
        self.createPath()

    def createPath(self):
        if self.suit.battle.currentFloor in self.suit.battle.UNIQUE_FLOORS:
            points = POINTS[self.suit.battle.deptClass][self.suit.battle.currentFloor]['battle']
        else:
            points = POINTS[self.suit.battle.currentFloor]['battle']
        path = Point3(points[self.spot][0], points[self.spot][1], points[self.spot][2])
        durationFactor = 0.1
        startIndex = -1
        endIndex = self.spot
        pathList = [[path.getX(), path.getY()]]
        self.startPath(pathList, 0, durationFactor)