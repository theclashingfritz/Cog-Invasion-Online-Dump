# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.gui.DirectCheckBox
from direct.gui.DirectGui import *
from panda3d.core import *

class DirectCheckBox(DirectButton):

    def __init__(self, parent=None, **kw):
        optiondefs = (
         (
          'pgFunc', PGButton, None),
         ('numStates', 4, None),
         (
          'state', DGG.NORMAL, None),
         (
          'relief', DGG.RAISED, None),
         (
          'invertedFrames', (1, ), None),
         ('command', None, None),
         (
          'extraArgs', [], None),
         (
          'commandButtons', (DGG.LMB,), self.setCommandButtons),
         (
          'rolloverSound', DGG.getDefaultRolloverSound(), self.setRolloverSound),
         (
          'clickSound', DGG.getDefaultClickSound(), self.setClickSound),
         (
          'pressEffect', 1, DGG.INITOPT),
         ('uncheckedImage', None, None),
         ('checkedImage', None, None),
         (
          'isChecked', False, None))
        self.defineoptions(kw, optiondefs)
        DirectButton.__init__(self, parent)
        self.initialiseoptions(DirectCheckBox)
        return

    def commandFunc(self, event):
        self['isChecked'] = not self['isChecked']
        if self['isChecked']:
            self['image'] = self['checkedImage']
        else:
            self['image'] = self['uncheckedImage']
        self.setImage()
        if self['command']:
            apply(self['command'], [self['isChecked']] + self['extraArgs'])