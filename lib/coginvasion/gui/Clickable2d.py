# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gui.Clickable2d
from panda3d.core import Point3
from Clickable import Clickable

class Clickable2d(Clickable):

    def setClickRegionFrame(self, left, right, bottom, top):
        mat = self.contents.getNetTransform().getMat()
        left, _, top = mat.xformPoint(Point3(left, 0, top))
        right, _, bottom = mat.xformPoint(Point3(right, 0, bottom))
        self.region.setFrame(left, right, bottom, top)