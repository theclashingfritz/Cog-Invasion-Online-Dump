# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.ThreeUpShow
__all__ = [
 'ThreeUpShow']
import ShowBase

class ThreeUpShow(ShowBase.ShowBase):

    def __init__(self):
        ShowBase.ShowBase.__init__(self)

    def makeCamera(self, win, chan=None, layer=None, layerSort=0, scene=None, displayRegion=(0, 1, 0, 1), aspectRatio=None):
        self.camRS = ShowBase.ShowBase.makeCamera(self, win, displayRegion=(0.5, 1,
                                                                            0, 1), aspectRatio=0.67, camName='camRS')
        self.camLL = ShowBase.ShowBase.makeCamera(self, win, displayRegion=(0, 0.5,
                                                                            0, 0.5), camName='camLL')
        self.camUR = ShowBase.ShowBase.makeCamera(self, win, displayRegion=(0, 0.5,
                                                                            0.5,
                                                                            1), camName='camUR')
        return self.camUR