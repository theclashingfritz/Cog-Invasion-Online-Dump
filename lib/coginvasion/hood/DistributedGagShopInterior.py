# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.DistributedGagShopInterior
from direct.directnotify.DirectNotifyGlobal import directNotify
from libpandadna import *
import ZoneUtil, ToonInteriorColors, DistributedToonInterior, random

class DistributedGagShopInterior(DistributedToonInterior.DistributedToonInterior):
    notify = directNotify.newCategory('DistributedGagShopInterior')

    def makeInterior(self, roomIndex=None):
        self.dnaStore = self.cr.playGame.dnaStore
        self.generator = random.Random()
        self.generator.seed(self.zoneId)
        self.interior = loader.loadModel('phase_4/models/modules/gagShop_interior.bam')
        self.interior.reparentTo(render)
        hoodId = ZoneUtil.getHoodId(self.zoneId, 1)
        self.colors = ToonInteriorColors.colors[hoodId]
        self.replaceRandomInModel(self.interior)
        door = self.dnaStore.findNode('door_double_round_ur')
        doorOrigin = render.find('**/door_origin;+s')
        doorNP = door.copyTo(doorOrigin)
        doorOrigin.setScale(0.8, 0.8, 0.8)
        doorOrigin.setPos(doorOrigin, 0, -0.025, 0)
        doorColor = self.generator.choice(self.colors['TI_door'])
        DNADoor.setupDoor(doorNP, self.interior, doorOrigin, self.dnaStore, self.block, doorColor)
        doorFrame = doorNP.find('door_*_flat')
        doorFrame.wrtReparentTo(self.interior)
        doorFrame.setColor(doorColor)
        del self.colors
        del self.dnaStore
        del self.generator
        self.interior.flattenMedium()