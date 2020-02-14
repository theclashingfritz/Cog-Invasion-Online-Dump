# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gui.MoneyGui
from panda3d.core import *
from direct.gui.DirectGui import *

class MoneyGui:

    def createGui(self):
        self.deleteGui()
        self.frame = DirectFrame(parent=base.a2dBottomLeft, pos=(0.45, 0, 0.155))
        gui = loader.loadModel('phase_3.5/models/gui/jar_gui.bam')
        self.jar = OnscreenImage(image=gui, scale=0.5, parent=self.frame)
        mf = loader.loadFont('phase_3/models/fonts/MickeyFont.bam')
        self.money_lbl = DirectLabel(text='', text_font=mf, text_fg=(1, 1, 0, 1), parent=self.jar, text_scale=0.2, relief=None, pos=(0,
                                                                                                                                     0,
                                                                                                                                     -0.1))
        gui.remove_node()
        return

    def deleteGui(self):
        if hasattr(self, 'jar'):
            self.jar.destroy()
            del self.jar
        if hasattr(self, 'money_lbl'):
            self.money_lbl.destroy()
            del self.money_lbl
        if hasattr(self, 'frame'):
            self.frame.destroy()
            del self.frame

    def update(self, moneyAmt):
        if hasattr(self, 'money_lbl'):
            if moneyAmt <= 0:
                self.money_lbl['text_fg'] = (0.9, 0, 0, 1)
            else:
                self.money_lbl['text_fg'] = (1, 1, 0, 1)
            self.money_lbl['text'] = str(moneyAmt)