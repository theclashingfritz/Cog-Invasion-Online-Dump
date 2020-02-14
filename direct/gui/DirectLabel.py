# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.gui.DirectLabel
__all__ = [
 'DirectLabel']
from panda3d.core import *
from DirectFrame import *

class DirectLabel(DirectFrame):

    def __init__(self, parent=None, **kw):
        optiondefs = (
         (
          'pgFunc', PGItem, None),
         ('numStates', 1, None),
         (
          'state', self.inactiveInitState, None),
         (
          'activeState', 0, self.setActiveState))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.initialiseoptions(DirectLabel)
        return

    def setActiveState(self):
        self.guiItem.setState(self['activeState'])