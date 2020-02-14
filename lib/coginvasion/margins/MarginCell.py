# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.margins.MarginCell
from panda3d.core import NodePath

class MarginCell(NodePath):

    def __init__(self):
        NodePath.__init__(self, 'cell')
        self.active = False
        self.content = None
        self.contentNodePath = None
        return

    def setActive(self, active):
        if not active:
            self.setContent(None)
        self.active = active
        return

    def getActive(self):
        return self.active

    def setContent(self, content):
        if self.content is not None:
            self.content.setCell(None)
            self.content.marginVisibilityChanged()
            self.content = None
        if self.contentNodePath is not None:
            self.contentNodePath.removeNode()
            self.contentNodePath = None
        if content is not None:
            content.setLastCell(self)
            content.setCell(self)
            self.contentNodePath = self.attachNewNode(content)
            content.marginVisibilityChanged()
        self.content = content
        return

    def getContent(self):
        return self.content