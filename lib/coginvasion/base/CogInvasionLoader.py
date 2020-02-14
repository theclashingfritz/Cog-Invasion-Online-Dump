# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.base.CogInvasionLoader
from panda3d.core import *
from direct.showbase import Loader
from lib.coginvasion.gui.CIProgressScreen import CIProgressScreen
from lib.coginvasion.dna.DNALoader import *

class CogInvasionLoader(Loader.Loader):
    TickPeriod = 0.0

    def __init__(self, base):
        Loader.Loader.__init__(self, base)
        self.inBulkBlock = None
        self.blockName = None
        self.progressScreen = CIProgressScreen()
        self.wantAutoTick = False
        return

    def beginBulkLoad(self, name, hood, range, wantGui=1, autoTick=True):
        self.wantAutoTick = autoTick
        self._loadStartT = globalClock.getRealTime()
        if self.inBulkBlock:
            self.notify.warning("tried to start a block ('%s'), but we're already in block ('%s')" % (name, self.blockName))
            return
        self.inBulkBlock = 1
        self._lastTickT = globalClock.getRealTime()
        self.blockName = name
        self.progressScreen.begin(hood, range, wantGui)
        return

    def endBulkLoad(self, name):
        if not self.inBulkBlock:
            self.notify.warning("attempted to end block ('%s'), but we're not in any block." % name)
            return
        if name != self.blockName:
            self.notify.warning("attempted to end block ('%s'), other than the current one ('%s')" % (name, self.blockName))
            return
        self.inBulkBlock = None
        self.wantAutoTick = False
        self.progressScreen.end()
        return

    def tick(self):
        if self.inBulkBlock:
            self.progressScreen.tick()
            try:
                base.cr.considerHeartbeat()
            except:
                pass

    def loadDNAFile(self, dnaStore, filename):
        return loadDNAFile(dnaStore, filename)

    def loadModel(self, *args, **kw):
        ret = Loader.Loader.loadModel(self, *args, **kw)
        self.tick()
        return ret

    def loadFont(self, *args, **kw):
        ret = Loader.Loader.loadFont(self, *args, **kw)
        self.tick()
        return ret

    def loadTexture(self, texturePath, alphaPath=None, okMissing=False):
        ret = Loader.Loader.loadTexture(self, texturePath, alphaPath, okMissing=okMissing)
        self.tick()
        if alphaPath:
            self.tick()
        return ret

    def loadSfx(self, soundPath):
        ret = Loader.Loader.loadSfx(self, soundPath)
        self.tick()
        return ret

    def loadMusic(self, soundPath):
        ret = Loader.Loader.loadMusic(self, soundPath)
        self.tick()
        return ret

    def destroy(self):
        Loader.Loader.destroy(self)

    try:
        self.progressScreen.destroy()
        del self.progressScreen
    except:
        pass