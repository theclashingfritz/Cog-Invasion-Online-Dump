# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gui.KOTHGui
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import DirectFrame, OnscreenText, OnscreenImage
from lib.coginvasion.globals import CIGlobals

class KOTHGui(DirectFrame):
    notify = directNotify.newCategory('KOTHGui')
    pointsSfx = None
    points = None

    def __init__(self):
        DirectFrame.__init__(self, parent=base.a2dTopLeft, relief=None, pos=(0.275,
                                                                             1, -0.7), sortOrder=0)
        self.pointsSfx = loader.loadSfx('phase_4/audio/sfx/MG_maze_pickup.ogg')
        self.points = 0
        gui = loader.loadModel('phase_4/models/gui/purchase_gui.bam')
        panel = gui.find('**/yellowPanel')
        self.bg = OnscreenImage(image=panel, parent=self)
        self.title = OnscreenText(text='Capture Points', font=CIGlobals.getMinnieFont(), parent=self, scale=0.0475, pos=(0,
                                                                                                                         0.18), fg=(1,
                                                                                                                                    0,
                                                                                                                                    0,
                                                                                                                                    1), shadow=(0.2,
                                                                                                                                                0.2,
                                                                                                                                                0.2,
                                                                                                                                                1))
        self.amt_label = OnscreenText(text=str(self.points), font=CIGlobals.getToonFont(), parent=self, scale=0.15, pos=(0,
                                                                                                                         0.03525), shadow=(0.5,
                                                                                                                                           0.5,
                                                                                                                                           0.5,
                                                                                                                                           0.6))
        self.info = OnscreenText(text='First Toon to 100 points wins!\nEarn points by standing on the\nhill after capturing it.', parent=self, font=CIGlobals.getToonFont(), scale=0.035, pos=(0,
                                                                                                                                                                                               -0.05), fg=(1.5,
                                                                                                                                                                                                           0,
                                                                                                                                                                                                           0,
                                                                                                                                                                                                           1), shadow=(0.2,
                                                                                                                                                                                                                       0.2,
                                                                                                                                                                                                                       0.2,
                                                                                                                                                                                                                       1))
        self.hide()
        return

    def show(self):
        self.title.show()
        self.amt_label.show()
        self.info.show()
        self.bg.show()

    def hide(self):
        self.title.hide()
        self.amt_label.hide()
        self.info.hide()
        self.bg.hide()

    def destroy(self):
        self.title.destroy()
        self.amt_label.destroy()
        self.info.destroy()
        self.bg.destroy()
        self.title = None
        self.amt_label = None
        self.info = None
        self.bg = None
        self.pointsSfx.stop()
        self.pointsSfx = None
        self.points = None
        DirectFrame.destroy(self)
        return

    def setPoints(self, points):
        self.points = points
        self.amt_label.setText(str(self.points))
        self.pointsSfx.play()

    def getPoints(self):
        return self.points