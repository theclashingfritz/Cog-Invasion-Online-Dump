# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.DistributedToonInterior
from panda3d.core import Mat4, Point3
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed import DistributedObject
from libpandadna import *
import ToonInteriorColors, ZoneUtil, random
SIGN_LEFT = -4
SIGN_RIGHT = 4
SIGN_BOTTOM = -3.5
SIGN_TOP = 1.5
FrameScale = 1.4

class DistributedToonInterior(DistributedObject.DistributedObject):
    notify = directNotify.newCategory('DistributedToonInterior')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.interior = None
        self.block = None
        return

    def randomDNAItem(self, category, findFunc):
        codeCount = self.dnaStore.getNumCatalogCodes(category)
        index = self.generator.randint(0, codeCount - 1)
        code = self.dnaStore.getCatalogCode(category, index)
        return findFunc(code)

    def replaceRandomInModel(self, model):
        baseTag = 'random_'
        npc = model.findAllMatches('**/' + baseTag + '???_*')
        for i in xrange(npc.getNumPaths()):
            np = npc.getPath(i)
            name = np.getName()
            b = len(baseTag)
            category = name[b + 4:]
            key1 = name[b]
            key2 = name[b + 1]
            if key1 == 'm':
                model = self.randomDNAItem(category, self.dnaStore.findNode)
                newNP = model.copyTo(np)
                c = render.findAllMatches('**/collision')
                c.stash()
                if key2 == 'r':
                    self.replaceRandomInModel(newNP)
            else:
                if key1 == 't':
                    texture = self.randomDNAItem(category, self.dnaStore.findTexture)
                    np.setTexture(texture, 100)
                    newNP = np
            if key2 == 'c':
                if category == 'TI_wallpaper' or category == 'TI_wallpaper_border':
                    self.generator.seed(self.zoneId)
                    newNP.setColorScale(self.generator.choice(self.colors[category]))
                else:
                    newNP.setColorScale(self.generator.choice(self.colors[category]))

    def makeInterior(self, roomIndex=None):
        self.dnaStore = self.cr.playGame.dnaStore
        self.generator = random.Random()
        self.generator.seed(self.zoneId)
        if roomIndex == None:
            interior = self.randomDNAItem('TI_room', self.dnaStore.findNode)
        else:
            interior = self.dnaStore.findNode(self.dnaStore.getCatalogCode('TI_room', roomIndex))
        self.interior = interior.copyTo(render)
        hoodId = ZoneUtil.getHoodId(self.zoneId, 1)
        self.colors = ToonInteriorColors.colors[hoodId]
        self.replaceRandomInModel(self.interior)
        doorModelName = 'door_double_round_ul'
        if doorModelName[-1:] == 'r':
            doorModelName = doorModelName[:-1] + 'l'
        else:
            doorModelName = doorModelName[:-1] + 'r'
        door = self.dnaStore.findNode(doorModelName)
        door_origin = render.find('**/door_origin;+s')
        doorNP = door.copyTo(door_origin)
        door_origin.setScale(0.8, 0.8, 0.8)
        door_origin.setPos(door_origin, 0, -0.025, 0)
        color = self.generator.choice(self.colors['TI_door'])
        DNADoor.setupDoor(doorNP, self.interior, door_origin, self.dnaStore, self.block, color)
        doorFrame = doorNP.find('door_*_flat')
        doorFrame.wrtReparentTo(self.interior)
        doorFrame.setColor(color)
        sign = hidden.find('**/tb%s:*_landmark_*_DNARoot/**/sign;+s' % (self.block,))
        if not sign.isEmpty():
            signOrigin = self.interior.find('**/sign_origin;+s')
            newSignNP = sign.copyTo(signOrigin)
            newSignNP.setDepthWrite(1, 1)
            inv = Mat4(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            newSignNP.setMat(inv)
            newSignNP.flattenLight()
            ll = Point3()
            ur = Point3()
            newSignNP.calcTightBounds(ll, ur)
            width = ur[0] - ll[0]
            height = ur[2] - ll[2]
            if width != 0 and height != 0:
                xScale = (SIGN_RIGHT - SIGN_LEFT) / width
                zScale = (SIGN_TOP - SIGN_BOTTOM) / height
                scale = min(xScale, zScale)
                xCenter = (ur[0] + ll[0]) / 2.0
                zCenter = (ur[2] + ll[2]) / 2.0
                newSignNP.setPosHprScale((SIGN_RIGHT + SIGN_LEFT) / 2.0 - xCenter * scale, -0.1, (SIGN_TOP + SIGN_BOTTOM) / 2.0 - zCenter * scale, 0.0, 0.0, 0.0, scale, scale, scale)
        del self.generator
        del self.dnaStore
        del self.colors
        self.interior.flattenMedium()
        return

    def setBlock(self, block):
        self.block = block

    def getBlock(self):
        return self.block

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.makeInterior()

    def disable(self):
        if self.interior:
            self.interior.removeNode()
            self.interior = None
        DistributedObject.DistributedObject.disable(self)
        return