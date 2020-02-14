# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.CameraShyLevelLoader
from direct.directnotify.DirectNotifyGlobal import directNotify
from panda3d.core import Point3, Vec3, NodePath, CompassEffect
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.hood.SkyUtil import SkyUtil
from lib.coginvasion.distributed.HoodMgr import HoodMgr
from lib.coginvasion.dna.DNALoader import *
hoodMgr = HoodMgr()

class CameraShyLevelLoader:
    notify = directNotify.newCategory('CameraShyLevelLoader')
    levelData = {'TT_maze': {'name': CIGlobals.ToontownCentral, 
                   'models': {'phase_4/models/minigames/maze_1player.bam': {'name': 'maze'}, 'phase_4/models/minigames/maze_1player_collisions.egg': {'name': 'maze_collisions'}}, 'sky': 'TT', 
                   'spawnPoints': [
                                 [
                                  Point3(0, 0, 0), Vec3(0, 0, 0)],
                                 [
                                  Point3(-23.89, 18.58, 0.0), Vec3(90.0, 0.0, 0.0)],
                                 [
                                  Point3(-23.89, 6.3, 0.0), Vec3(0.0, 0.0, 0.0)],
                                 [
                                  Point3(23.78, 6.3, 0.0), Vec3(0.0, 0.0, 0.0)],
                                 [
                                  Point3(8.12, -17.79, 0.0), Vec3(270.0, 0.0, 0.0)]]}, 
       'DG_playground': {'name': CIGlobals.DaisyGardens, 
                         'dna': [
                               'phase_8/dna/storage_DG.pdna',
                               'phase_8/dna/storage_DG_sz.pdna',
                               'phase_8/dna/daisys_garden_sz.pdna'], 
                         'sky': 'TT', 
                         'spawnPoints': hoodMgr.dropPoints[CIGlobals.DaisyGardens]}}
    skyData = {'TT': {'model': 'phase_3.5/models/props/TT_sky.bam', 
              'moving': 1}}

    def __init__(self):
        self.level = None
        self.dnaStore = DNAStorage()
        self.levelGeom = None
        self.skyUtil = None
        self.skyModel = None
        self.models = []
        return

    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        return self.level

    def load(self):
        if not self.level:
            self.notify.warning('Attempted to load a null level!')
            return

        def loadSky(sky):
            data = self.skyData[sky]
            if data:
                model = data['model']
                moving = 0
                if data.get('moving'):
                    moving = data['moving']
                self.skyModel = loader.loadModel(model)
                self.skyModel.reparentTo(camera)
                self.skyUtil = SkyUtil()
                self.skyUtil.startSky(self.skyModel)
                if moving:
                    compass = CompassEffect.make(NodePath(), CompassEffect.PRot | CompassEffect.PZ)
                    self.skyModel.node().setEffect(compass)

        self.unload()
        data = self.levelData[self.level]
        skyType = data['sky']
        if data.get('dna'):
            dnaFiles = data['dna']
            loadDNAFile(self.dnaStore, 'phase_4/dna/storage.pdna')
            for index in range(len(dnaFiles)):
                if 'storage' not in dnaFiles[index]:
                    node = loader.loadDNAFile(self.dnaStore, dnaFiles[index])
                    if node.getNumParents() == 1:
                        self.levelGeom = NodePath(node.getParent(0))
                        self.levelGeom.reparentTo(hidden)
                    else:
                        self.levelGeom = hidden.attachNewNode(node)
                    self.levelGeom.flattenMedium()
                    gsg = base.win.getGsg()
                    if gsg:
                        self.levelGeom.prepareScene(gsg)
                    self.levelGeom.reparentTo(render)
                else:
                    loadDNAFile(self.dnaStore, dnaFiles[index])

        else:
            if data.get('models'):
                models = data['models']
                for model, modifiers in models.items():
                    mdl = loader.loadModel(model)
                    if modifiers.get('name'):
                        mdl.setName(modifiers['name'])
                    if modifiers.get('hpr'):
                        mdl.setHpr(modifiers['hpr'])
                    if modifiers.get('pos'):
                        mdl.setPos(modifiers['pos'])
                    if modifiers.get('scale'):
                        mdl.setScale(modifiers['scale'])
                    if modifiers.get('parent'):
                        mdl.reparentTo(modifiers['parent'])
                    else:
                        mdl.reparentTo(render)
                    self.models.append(mdl)

            else:
                self.notify.warning('Attempted to load a level with no data on how to generate it. Level is empty!')
                return
        loadSky(skyType)
        self.levelLoaded()

    def unload(self):
        if self.models:
            if len(self.models) > 0:
                for model in self.models:
                    model.removeNode()

        self.models = []
        if self.levelGeom:
            self.levelGeom.removeNode()
            self.levelGeom = None
        if self.skyUtil:
            self.skyUtil.stopSky()
            self.skyUtil = None
        if self.skyModel:
            self.skyModel.removeNode()
            self.skyModel = None
        if self.dnaStore:
            self.dnaStore.reset_nodes()
            self.dnaStore.reset_hood_nodes()
            self.dnaStore.reset_place_nodes()
            self.dnaStore.reset_hood()
            self.dnaStore.reset_fonts()
            self.dnaStore.reset_DNA_vis_groups()
            self.dnaStore.reset_textures()
            self.dnaStore.reset_block_numbers()
            self.dnaStore.reset_block_zones()
            self.dnaStore.reset_suit_points()
        hoodMgr = None
        return

    def cleanup(self):
        try:
            self.CameraShyLevelLoader_deleted
        except:
            self.CameraShyLevelLoader_deleted = 1
            if self.dnaStore:
                self.unload()
            self.models = None
            self.levelGeom = None
            self.skyUtil = None
            self.skyModel = None
            self.dnaStore = None
            self.levelData = None

        return

    def levelLoaded(self):
        if self.level == 'TT_maze':
            for model in self.models:
                if model.getName() == 'maze':
                    model.find('**/maze_walls').setSz(1.5)
                elif model.getName() == 'maze_collisions':
                    model.hide()
                    model.setTransparency(1)
                    model.setColorScale(1, 1, 1, 0)
                    for node in model.findAllMatches('**'):
                        node.setSz(1.5)

    def getSpawnPoints(self):
        if self.level:
            points = self.levelData[self.level].get('spawnPoints')
            if points in hoodMgr.dropPoints.values():
                twoPointArray = []
                for posHpr in points:
                    twoPointArray.append(Point3(posHpr[0], posHpr[1], posHpr[2]), Vec3(posHpr[3], posHpr[4], posHpr[5]))

                points = twoPointArray
            return points
        self.notify.warning('Attempted to get spawn points of a null level!')
        return
        return