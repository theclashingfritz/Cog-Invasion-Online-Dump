# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.margins.MarginManager
from panda3d.core import PandaNode
import random
from MarginCell import MarginCell

class MarginManager(PandaNode):

    def __init__(self):
        PandaNode.__init__(self, 'margins')
        self.cells = set()
        self.visibles = set()

    def addCell(self, x, y, a2dMarker):
        cell = MarginCell()
        cell.reparentTo(a2dMarker)
        cell.setPos(x, 0, y)
        cell.setScale(0.2)
        cell.setActive(True)
        self.cells.add(cell)
        self.reorganize()
        return cell

    def removeCell(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)
            self.reorganize()

    def addVisible(self, visible):
        self.visibles.add(visible)
        self.reorganize()

    def removeVisible(self, visible):
        if visible in self.visibles:
            self.visibles.remove(visible)
            self.reorganize()

    def getActiveCells(self):
        return [ cell for cell in self.cells if cell.getActive() ]

    def reorganize(self):
        activeCells = self.getActiveCells()
        visibles = list(self.visibles)
        visibles.sort(key=lambda visible: visible.getPriority(), reverse=True)
        visibles = visibles[:len(activeCells)]
        emptyCells = []
        for cell in activeCells:
            content = cell.getContent()
            if content in visibles:
                visibles.remove(content)
                continue
            else:
                if content is not None:
                    cell.setContent(None)
            emptyCells.append(cell)

        for visible in visibles:
            cell = visible.getLastCell()
            if cell not in emptyCells:
                cell = random.choice(emptyCells)
            cell.setContent(visible)
            emptyCells.remove(cell)

        return