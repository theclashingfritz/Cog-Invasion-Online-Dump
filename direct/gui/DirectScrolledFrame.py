# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.gui.DirectScrolledFrame
__all__ = [
 'DirectScrolledFrame']
from panda3d.core import *
import DirectGuiGlobals as DGG
from DirectFrame import *
from DirectScrollBar import *

class DirectScrolledFrame(DirectFrame):

    def __init__(self, parent=None, **kw):
        optiondefs = (
         (
          'pgFunc', PGScrollFrame, None),
         (
          'frameSize', (-0.5, 0.5, -0.5, 0.5), None),
         (
          'canvasSize', (-1, 1, -1, 1), self.setCanvasSize),
         (
          'manageScrollBars', 1, self.setManageScrollBars),
         (
          'autoHideScrollBars', 1, self.setAutoHideScrollBars),
         ('scrollBarWidth', 0.08, None),
         (
          'borderWidth', (0.01, 0.01), self.setBorderWidth))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        w = self['scrollBarWidth']
        self.verticalScroll = self.createcomponent('verticalScroll', (), None, DirectScrollBar, (self,), borderWidth=self['borderWidth'], frameSize=(
         -w / 2.0, w / 2.0, -1, 1), orientation=DGG.VERTICAL)
        self.horizontalScroll = self.createcomponent('horizontalScroll', (), None, DirectScrollBar, (self,), borderWidth=self['borderWidth'], frameSize=(
         -1, 1, -w / 2.0, w / 2.0), orientation=DGG.HORIZONTAL)
        self.guiItem.setVerticalSlider(self.verticalScroll.guiItem)
        self.guiItem.setHorizontalSlider(self.horizontalScroll.guiItem)
        self.canvas = NodePath(self.guiItem.getCanvasNode())
        self.initialiseoptions(DirectScrolledFrame)
        return

    def setCanvasSize(self):
        f = self['canvasSize']
        self.guiItem.setVirtualFrame(f[0], f[1], f[2], f[3])

    def getCanvas(self):
        return self.canvas

    def setManageScrollBars(self):
        self.guiItem.setManagePieces(self['manageScrollBars'])

    def setAutoHideScrollBars(self):
        self.guiItem.setAutoHide(self['autoHideScrollBars'])

    def commandFunc(self):
        if self['command']:
            apply(self['command'], self['extraArgs'])

    def destroy(self):
        for child in self.canvas.getChildren():
            childGui = self.guiDict.get(child.getName())
            if childGui:
                childGui.destroy()
            else:
                parts = child.getName().split('-')
                simpleChildGui = self.guiDict.get(parts[-1])
                if simpleChildGui:
                    simpleChildGui.destroy()

        self.verticalScroll.destroy()
        self.horizontalScroll.destroy()
        del self.verticalScroll
        del self.horizontalScroll
        DirectFrame.destroy(self)