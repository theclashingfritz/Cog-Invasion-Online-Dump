# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.CartesianGridBase
from pandac.PandaModules import Vec3

class CartesianGridBase:

    def isValidZone(self, zoneId):

        def checkBounds(self=self, zoneId=zoneId):
            if zoneId < self.startingZone or zoneId > self.startingZone + self.gridSize * self.gridSize - 1:
                return 0
            return 1

        if self.style == 'Cartesian':
            return checkBounds()
        if self.style == 'CartesianStated':
            if zoneId >= 0 and zoneId < self.startingZone:
                return 1
            return checkBounds()
        else:
            return 0

    def getZoneFromXYZ(self, pos, wantRowAndCol=False):
        dx = self.cellWidth * self.gridSize * 0.5
        x = pos[0] + dx
        y = pos[1] + dx
        col = x // self.cellWidth
        row = y // self.cellWidth
        zoneId = int(self.startingZone + (row * self.gridSize + col))
        if wantRowAndCol:
            return (zoneId, col, row)
        return zoneId

    def getGridSizeFromSphereRadius(self, sphereRadius, cellWidth, gridRadius):
        sphereRadius = max(sphereRadius, gridRadius * cellWidth)
        return 2 * (sphereRadius // cellWidth)

    def getGridSizeFromSphere(self, sphereRadius, spherePos, cellWidth, gridRadius):
        xMax = abs(spherePos[0]) + sphereRadius
        yMax = abs(spherePos[1]) + sphereRadius
        sphereRadius = Vec3(xMax, yMax, 0).length()
        return max(2 * (sphereRadius // cellWidth), 1)

    def getZoneCellOrigin(self, zoneId):
        dx = self.cellWidth * self.gridSize * 0.5
        zone = zoneId - self.startingZone
        row = zone // self.gridSize
        col = zone % self.gridSize
        x = col * self.cellWidth - dx
        y = row * self.cellWidth - dx
        return (
         x, y, 0)

    def getZoneCellOriginCenter(self, zoneId):
        dx = self.cellWidth * self.gridSize * 0.5
        center = self.cellWidth * 0.5
        zone = zoneId - self.startingZone
        row = zone // self.gridSize
        col = zone % self.gridSize
        x = col * self.cellWidth - dx + center
        y = row * self.cellWidth - dx + center
        return (
         x, y, 0)

    def getConcentricZones(self, zoneId, radius):
        zones = []
        zone = zoneId - self.startingZone
        row = zone // self.gridSize
        col = zone % self.gridSize
        leftOffset = min(col, radius)
        rightOffset = min(self.gridSize - (col + 1), radius)
        topOffset = min(row, radius)
        bottomOffset = min(self.gridSize - (row + 1), radius)
        ulZone = zoneId - leftOffset - topOffset * self.gridSize
        for currCol in range(int(rightOffset + leftOffset + 1)):
            if currCol == 0 and leftOffset == radius or currCol == rightOffset + leftOffset and rightOffset == radius:
                possibleRows = range(int(bottomOffset + topOffset + 1))
            else:
                possibleRows = []
                if topOffset == radius:
                    possibleRows.append(0)
                if bottomOffset == radius:
                    possibleRows.append(bottomOffset + topOffset)
            for currRow in possibleRows:
                newZone = ulZone + currRow * self.gridSize + currCol
                zones.append(int(newZone))

        return zones