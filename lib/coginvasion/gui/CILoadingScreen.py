# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gui.CILoadingScreen
from direct.gui.DirectGui import OnscreenText
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.Transitions import Transitions
from lib.coginvasion.base import FileUtility
loadernotify = directNotify.newCategory('CILoadingScreen')

class CILoadingScreen:

    def __init__(self):
        self.transitions = Transitions(loader)

    def createMenu(self):
        base.graphicsEngine.renderFrame()
        base.graphicsEngine.renderFrame()
        self.version_lbl = OnscreenText(text='ver-' + game.version, scale=0.06, pos=(-1.32,
                                                                                     -0.97,
                                                                                     -0.97), align=TextNode.ALeft, fg=(0.9,
                                                                                                                       0.9,
                                                                                                                       0.9,
                                                                                                                       7))

    def beginLoadGame(self):
        phasesToScan = [
         'models', 'phase_3/models', 'phase_3.5/models', 'phase_4/models']
        self.models = FileUtility.findAllModelFilesInVFS(phasesToScan)
        for model in self.models:
            loader.loadModel(model)
            loader.progressScreen.tick()

        doneInitLoad()
        self.destroy()

    def loadModelDone(self, array):
        self.modelsLoaded += 1
        if self.modelsLoaded == len(self.models):
            doneInitLoad()
            self.destroy()

    def destroy(self):
        self.version_lbl.destroy()