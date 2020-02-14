# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gui.Clickable3d
from panda3d.core import Quat, Point3, Point2
from Clickable import Clickable

class Clickable3d(Clickable):

    def setClickRegionFrame(self, left, right, bottom, top):
        transform = self.contents.getNetTransform()
        camTransform = base.cam.getNetTransform().getInverse()
        transform = camTransform.compose(transform)
        transform.setQuat(Quat())
        mat = transform.getMat()
        camSpaceTopLeft = mat.xformPoint(Point3(left, 0, top))
        camSpaceBottomRight = mat.xformPoint(Point3(right, 0, bottom))
        screenSpaceTopLeft = Point2()
        screenSpaceBottomRight = Point2()
        base.camLens.project(Point3(camSpaceTopLeft), screenSpaceTopLeft)
        base.camLens.project(Point3(camSpaceBottomRight), screenSpaceBottomRight)
        left, top = screenSpaceTopLeft
        right, bottom = screenSpaceBottomRight
        self.region.setFrame(left, right, bottom, top)