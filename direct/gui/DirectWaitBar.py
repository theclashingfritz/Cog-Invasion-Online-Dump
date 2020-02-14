# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.gui.DirectWaitBar
__all__ = [
 'DirectWaitBar']
from panda3d.core import *
import DirectGuiGlobals as DGG
from DirectFrame import *
import types

class DirectWaitBar(DirectFrame):

    def __init__(self, parent=None, **kw):
        optiondefs = (
         (
          'pgFunc', PGWaitBar, None),
         (
          'frameSize', (-1, 1, -0.08, 0.08), None),
         (
          'borderWidth', (0, 0), None),
         (
          'range', 100, self.setRange),
         (
          'value', 0, self.setValue),
         (
          'barBorderWidth', (0, 0), self.setBarBorderWidth),
         (
          'barColor', (1, 0, 0, 1), self.setBarColor),
         (
          'barTexture', None, self.setBarTexture),
         (
          'barRelief', DGG.FLAT, self.setBarRelief),
         (
          'sortOrder', NO_FADE_SORT_INDEX, None))
        if 'text' in kw:
            textoptiondefs = (('text_pos', (0, -0.025), None),
             ('text_scale', 0.1, None))
        else:
            textoptiondefs = ()
        self.defineoptions(kw, optiondefs + textoptiondefs)
        DirectFrame.__init__(self, parent)
        self.barStyle = PGFrameStyle()
        self.initialiseoptions(DirectWaitBar)
        self.updateBarStyle()
        return

    def destroy(self):
        self.barStyle = None
        DirectFrame.destroy(self)
        return

    def setRange(self):
        self.guiItem.setRange(self['range'])

    def setValue(self):
        self.guiItem.setValue(self['value'])

    def getPercent(self):
        return self.guiItem.getPercent()

    def updateBarStyle(self):
        if not self.fInit:
            self.guiItem.setBarStyle(self.barStyle)

    def setBarRelief(self):
        self.barStyle.setType(self['barRelief'])
        self.updateBarStyle()

    def setBarBorderWidth(self):
        self.barStyle.setWidth(*self['barBorderWidth'])
        self.updateBarStyle()

    def setBarColor(self):
        color = self['barColor']
        self.barStyle.setColor(color[0], color[1], color[2], color[3])
        self.updateBarStyle()

    def setBarTexture(self):
        texture = self['barTexture']
        if isinstance(texture, types.StringTypes):
            texture = loader.loadTexture(texture)
        if texture:
            self.barStyle.setTexture(texture)
        else:
            self.barStyle.clearTexture()
        self.updateBarStyle()

    def update(self, value):
        self['value'] = value
        base.graphicsEngine.renderFrame()

    def finish(self, N=10):
        remaining = self['range'] - self['value']
        if remaining:
            step = max(1, int(remaining / N))
            count = self['value']
            while count != self['range']:
                count += step
                if count > self['range']:
                    count = self['range']
                self.update(count)