# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.gui.OnscreenImage
__all__ = [
 'OnscreenImage']
from panda3d.core import *
from direct.showbase.DirectObject import DirectObject
import types

class OnscreenImage(DirectObject, NodePath):

    def __init__(self, image=None, pos=None, hpr=None, scale=None, color=None, parent=None, sort=0):
        NodePath.__init__(self)
        if parent == None:
            parent = aspect2d
        self.setImage(image, parent=parent, sort=sort)
        if isinstance(pos, types.TupleType) or isinstance(pos, types.ListType):
            apply(self.setPos, pos)
        else:
            if isinstance(pos, VBase3):
                self.setPos(pos)
        if isinstance(hpr, types.TupleType) or isinstance(hpr, types.ListType):
            apply(self.setHpr, hpr)
        else:
            if isinstance(hpr, VBase3):
                self.setHpr(hpr)
        if isinstance(scale, types.TupleType) or isinstance(scale, types.ListType):
            apply(self.setScale, scale)
        else:
            if isinstance(scale, VBase3):
                self.setScale(scale)
            else:
                if isinstance(scale, types.FloatType) or isinstance(scale, types.IntType):
                    self.setScale(scale)
        if color:
            self.setColor(color[0], color[1], color[2], color[3])
        return

    def setImage(self, image, parent=NodePath(), transform=None, sort=0):
        if not self.isEmpty():
            parent = self.getParent()
            if transform == None:
                transform = self.getTransform()
            sort = self.getSort()
        self.removeNode()
        if isinstance(image, NodePath):
            self.assign(image.copyTo(parent, sort))
        else:
            if isinstance(image, types.StringTypes) or isinstance(image, Texture):
                if isinstance(image, Texture):
                    tex = image
                else:
                    tex = loader.loadTexture(image)
                cm = CardMaker('OnscreenImage')
                cm.setFrame(-1, 1, -1, 1)
                self.assign(parent.attachNewNode(cm.generate(), sort))
                self.setTexture(tex)
            else:
                if type(image) == type(()):
                    model = loader.loadModel(image[0])
                    if model:
                        node = model.find(image[1])
                        if node:
                            self.assign(node.copyTo(parent, sort))
                        else:
                            print 'OnscreenImage: node %s not found' % image[1]
                    else:
                        print 'OnscreenImage: model %s not found' % image[0]
        if transform and not self.isEmpty():
            self.setTransform(transform)
        return

    def getImage(self):
        return self

    def configure(self, option=None, **kw):
        for option, value in kw.items():
            try:
                setter = getattr(self, 'set' + option[0].upper() + option[1:])
                if (setter == self.setPos or setter == self.setHpr or setter == self.setScale) and (isinstance(value, types.TupleType) or isinstance(value, types.ListType)):
                    apply(setter, value)
                else:
                    setter(value)
            except AttributeError:
                print 'OnscreenImage.configure: invalid option:', option

    def __setitem__(self, key, value):
        apply(self.configure, (), {key: value})

    def cget(self, option):
        getter = getattr(self, 'get' + option[0].upper() + option[1:])
        return getter()

    __getitem__ = cget

    def destroy(self):
        self.removeNode()