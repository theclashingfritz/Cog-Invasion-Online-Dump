# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.DistributedToonHQInterior
from panda3d.core import ModelNode, NodePath
import DistributedToonInterior, ToonInteriorColors
from lib.coginvasion.hood import ZoneUtil
from libpandadna import *
from lib.coginvasion.globals import CIGlobals
import random

class DistributedToonHQInterior(DistributedToonInterior.DistributedToonInterior):

    def makeInterior(self):
        self.dnaStore = self.cr.playGame.dnaStore
        self.generator = random.Random()
        self.generator.seed(self.zoneId)
        self.interior = loader.loadModel('phase_3.5/models/modules/HQ_interior.bam')
        self.interior.reparentTo(render)
        self.colors = ToonInteriorColors.colors[CIGlobals.ToontownCentral]
        doorModelName = 'door_double_round_ul'
        if doorModelName[-1:] == 'r':
            doorModelName = doorModelName[:-1] + 'l'
        else:
            doorModelName = doorModelName[:-1] + 'r'
        door = self.dnaStore.findNode(doorModelName)
        color = self.generator.choice(self.colors['TI_door'])
        doorOrigins = render.findAllMatches('**/door_origin*')
        numDoorOrigins = doorOrigins.getNumPaths()
        for npIndex in xrange(numDoorOrigins):
            doorOrigin = doorOrigins[npIndex]
            doorOriginNPName = doorOrigin.getName()
            doorOriginIndexStr = doorOriginNPName[len('door_origin_'):]
            newNode = ModelNode('door_' + doorOriginIndexStr)
            newNodePath = NodePath(newNode)
            newNodePath.reparentTo(self.interior)
            doorNP = door.copyTo(newNodePath)
            doorOrigin.setScale(0.8, 0.8, 0.8)
            doorOrigin.setPos(doorOrigin, 0, -0.025, 0)
            doorColor = self.generator.choice(self.colors['TI_door'])
            triggerId = str(self.block) + '0' + doorOriginIndexStr
            triggerId = int(triggerId)
            DNADoor.setupDoor(doorNP, newNodePath, doorOrigin, self.dnaStore, triggerId, doorColor)
            doorFrame = doorNP.find('door_*_flat')
            doorFrame.setColor(doorColor)

        del self.dnaStore
        del self.colors
        del self.generator
        self.interior.flattenMedium()