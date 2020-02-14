# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.GridChild
from direct.distributed.DistributedSmoothNodeBase import DistributedSmoothNodeBase
from direct.distributed.GridParent import GridParent

class GridChild:

    def __init__(self):
        try:
            self.__initiallized
        except AttributeError:
            self._gridParent = None
            self._gridInterestEnabled = False
            self._gridInterests = {}

        return

    def delete(self):
        self.__setGridParent(None)
        self.enableGridInterest(False)
        return

    @report(types=['args'], dConfigParam='smoothnode')
    def setGridCell(self, grid, zoneId):
        if not hasattr(self, 'getParent'):
            return
        if grid is None:
            self.__setGridParent(None)
            self.__clearGridInterest()
        else:
            if not self._gridParent:
                self.__setGridParent(GridParent(self))
            self._gridParent.setGridCell(grid, zoneId)
            self.updateGridInterest(grid, zoneId)
        return

    def updateGridInterest(self, grid, zoneId):
        self.__setGridInterest(grid, zoneId)

    def enableGridInterest(self, enabled=True):
        self._gridInterestEnabled = enabled
        if enabled and self.isOnAGrid():
            for currGridId, interestInfo in self._gridInterests.items():
                currGrid = getBase().getRepository().doId2do.get(currGridId)
                if currGrid:
                    self.__setGridInterest(currGrid, interestInfo[1])
                else:
                    self.notify.warning('unknown grid interest %s' % currGridId)

        else:
            for currGridId, interestInfo in self._gridInterests.items():
                self.cr.removeTaggedInterest(interestInfo[0])

    def isOnAGrid(self):
        return self._gridParent is not None

    def getGrid(self):
        if self._gridParent:
            return self._gridParent.getGrid()
        return
        return

    def getGridZone(self):
        if self._gridParent:
            return self._gridParent.getGridZone()
        return
        return

    def __setGridParent(self, gridParent):
        if self._gridParent and self._gridParent is not gridParent:
            self._gridParent.delete()
        self._gridParent = gridParent

    def __setGridInterest(self, grid, zoneId):
        if self.cr.noNewInterests():
            self.notify.warning('startProcessVisibility(%s): tried to open a new interest during logout' % self.doId)
            return
        gridDoId = grid.getDoId()
        existingInterest = self._gridInterests.get(gridDoId)
        if self._gridInterestEnabled:
            if existingInterest and existingInterest[0]:
                self.cr.alterInterest(existingInterest[0], grid.getDoId(), zoneId)
                existingInterest[1] = zoneId
            else:
                newInterest = self.cr.addTaggedInterest(gridDoId, zoneId, self.cr.ITAG_GAME, self.uniqueName('gridvis'))
                self._gridInterests[gridDoId] = [newInterest, zoneId]
        else:
            if game.process == 'client':
                self._gridInterests[gridDoId] = [None, zoneId]
        return

    def getGridInterestIds(self):
        return self._gridInterests.keys()

    def getGridInterestZoneId(self, gridDoId):
        return self._gridInterests.get(gridDoId, [None, None])[1]

    def __clearGridInterest(self):
        if self._gridInterestEnabled:
            for currGridId, interestInfo in self._gridInterests.items():
                self.cr.removeTaggedInterest(interestInfo[0])

        self._gridInterests = {}


class SmoothGridChild(GridChild):

    def __init__(self):
        GridChild.__init__(self)

    @report(types=['args'], dConfigParam='smoothnode')
    def setGridCell(self, grid, zoneId):
        GridChild.setGridCell(self, grid, zoneId)
        if grid and self.isGenerated():
            self.cnode.setEmbeddedVal(zoneId)

    @report(types=['args'], dConfigParam='smoothnode')
    def transformTelemetry(self, x, y, z, h, p, r, e):
        if self.isOnAGrid():
            self.setGridCell(self.getGrid(), e)
        return (
         x, y, z, h, p, r)