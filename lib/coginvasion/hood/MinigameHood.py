# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.MinigameHood
from lib.coginvasion.hood.SkyUtil import SkyUtil
from lib.coginvasion.dna.DNAParser import *
from panda3d.core import NodePath

class MinigameHood:

    def __init__(self, cr):
        self.cr = cr
        self.isLoaded = 0
        self.dnaStore = DNAStorage()

    def createHood(self, loadStorage=1):
        if loadStorage:
            loadDNAFile(self.dnaStore, 'phase_13/dna/storage_party_sz.dna')
        self.node = loadDNAFile(self.dnaStore, 'phase_13/dna/party_sz.dna')
        if self.node.getNumParents() == 1:
            self.geom = NodePath(self.node.getParent(0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(self.node)
        gsg = base.win.getGsg()
        if gsg:
            self.geom.prepareScene(gsg)
        self.geom.setName('minigames')
        base.hoodBGM = base.loadMusic('phase_13/audio/bgm/party_original_theme.ogg')
        base.hoodBGM.setVolume(0.7)
        base.hoodBGM.setLoop(True)
        base.hoodBGM.play()
        self.sky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
        self.sky.reparentTo(self.geom)
        self.sky.setPos(9.15527e-05, -1.90735e-06, 2.6226e-06)
        self.sky.setH(-90)
        self.skyUtil = SkyUtil()
        self.skyUtil.startSky(self.sky)
        self.geom.reparentTo(render)
        self.isLoaded = 1
        messenger.send('loadedHood')

    def unloadHood(self):
        self.isLoaded = 0
        self.skyUtil.stopSky()
        self.geom.removeNode()
        base.hoodBGM.stop()