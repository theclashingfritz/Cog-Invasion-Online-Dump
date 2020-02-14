# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.margins.MarginVisible


class MarginVisible:

    def __init__(self):
        self.marginManager = None
        self.visible = False
        self.priority = 0
        self.lastCell = None
        self.cell = None
        return

    def manage(self, marginManager):
        if self.marginManager is not None:
            self.unmanage(self.marginManager)
        self.marginManager = marginManager
        if self.visible:
            self.marginManager.addVisible(self)
        return

    def unmanage(self, marginManager):
        if marginManager != self.marginManager:
            return
        if self.marginManager is None:
            return
        if self.visible:
            self.marginManager.removeVisible(self)
        self.marginManager = None
        return

    def setVisible(self, visible):
        if visible == self.visible:
            return
        self.visible = visible
        if self.marginManager is not None:
            if self.visible:
                self.marginManager.addVisible(self)
            else:
                self.marginManager.removeVisible(self)
        return

    def getVisible(self):
        return self.visible

    def setPriority(self, priority):
        self.priority = priority
        if self.marginManager is not None and self.visible:
            self.marginManager.reorganize()
        return

    def getPriority(self):
        return self.priority

    def setLastCell(self, cell):
        self.lastCell = cell

    def getLastCell(self):
        return self.lastCell

    def setCell(self, cell):
        self.cell = cell

    def getCell(self):
        return self.cell

    def marginVisibilityChanged(self):
        pass