# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogtropolis.CTSafeZoneLoader
from panda3d.core import Point3, Vec3, Fog
from direct.directnotify.DirectNotifyGlobal import directNotify
from lib.coginvasion.hood.SafeZoneLoader import SafeZoneLoader
from lib.coginvasion.toon import ParticleLoader
import CTPlayground, TrafficLight

class CTSafeZoneLoader(SafeZoneLoader):
    notify = directNotify.newCategory('CTSafeZoneLoader')
    bldgPoints = [
     Point3(0, 0, 0),
     Point3(0, 95, 0),
     Point3(75, 0, 0),
     Point3(75, 95, 0),
     Point3(-110, 0, 0),
     Point3(-185, 0, 0),
     Point3(-110, 95, 0),
     Point3(-185, 95, 0),
     Point3(-296.5, 0, 0),
     Point3(-296.5, 95, 0),
     Point3(-372, 95, 0),
     Point3(-372, 0, 0),
     Point3(189, 0, 0),
     Point3(189, 95, 0),
     Point3(264, 95, 0),
     Point3(264, 0, 0),
     Point3(264, 221.5, 0),
     Point3(264, 318, 0),
     Point3(188, 318, 0),
     Point3(188, 221.5, 0),
     Point3(75, 221.5, 0),
     Point3(75, 318, 0),
     Point3(0, 221.5, 0),
     Point3(0, 318, 0),
     Point3(-110, 318, 0),
     Point3(-110, 221.5, 0),
     Point3(-185, 318, 0),
     Point3(-185, 221.5, 0),
     Point3(-296.5, 318, 0),
     Point3(-296.5, 221.5, 0),
     Point3(-372, 318, 0),
     Point3(-372, 221.5, 0)]
    bldgSectionData = [
     [
      Point3(0, 0, 0), Vec3(0, 0, 0)],
     [
      Point3(-38.59, -43.57, 0), Vec3(180, 0, 0)]]
    tLightData = [
     [
      (0.71, -2.06, 0.0), (0, 0, 0)],
     [
      (0.71, -226.17, -0.59), (0, 0, 0)],
     [
      (0.71, -451.44, 0.0), (0, 0, 0)],
     [
      (0.71, 221.32, 0), (0, 0, 0)],
     [
      (-39.05, 404.94, 0), (180, 0, 0)],
     [
      (-221.31, 404.94, 0.0), (180, 0, 0)],
     [
      (147.93, 404.94, 0), (180, 0, 0)],
     [
      (187.76, 221.68, 0), (0, 0, 0)],
     [
      (187.76, -1.82, 0), (0, 0, 0)],
     [
      (187.76, -227.4, -0.59), (0, 0, 0)],
     [
      (187.76, -451.28, 0), (0, 0, 0)],
     [
      (-185.21, -451.28, 0), (0, 0, 0)],
     [
      (-185.21, -226.94, 0), (0, 0, 0)],
     [
      (-185.21, -1.95, 0), (0, 0, 0)],
     [
      (-185.21, 221.7, 0), (0, 0, 0)]]

    def __init__(self, hood, parentFSMState, doneEvent):
        SafeZoneLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.playground = CTPlayground.CTPlayground
        self.pgMusicFilename = 'phase_12/audio/bgm/Bossbot_Entry_v1.mid'
        self.interiorMusicFilename = None
        self.battleMusicFile = None
        self.invasionMusicFiles = None
        self.tournamentMusicFiles = None
        self.bossBattleMusicFile = None
        self.dnaFile = None
        self.szStorageDNAFile = None
        self.buildingSectionNodes = []
        self.trafficLightNodes = []
        self.trafficLights = []
        self.fog = None
        self.rain = None
        self.rainRender = None
        self.soundRain = None
        self.thunderSounds = [base.loadSfx('phase_14/audio/sfx/big_thunder_1.ogg'),
         base.loadSfx('phase_14/audio/sfx/big_thunder_2.ogg'),
         base.loadSfx('phase_14/audio/sfx/big_thunder_3.ogg'),
         base.loadSfx('phase_14/audio/sfx/big_thunder_4.ogg'),
         base.loadSfx('phase_14/audio/sfx/big_thunder_5.ogg'),
         base.loadSfx('phase_14/audio/sfx/big_thunder_6.ogg'),
         base.loadSfx('phase_14/audio/sfx/big_thunder_7.ogg'),
         base.loadSfx('phase_14/audio/sfx/big_thunder_8.ogg'),
         base.loadSfx('phase_14/audio/sfx/big_thunder_9.ogg'),
         base.loadSfx('phase_14/audio/sfx/big_thunder_10.ogg')]
        return

    def load(self):
        SafeZoneLoader.load(self)
        self.soundRain = base.loadSfx('phase_14/audio/sfx/rain_ambient.ogg')
        self.rain = ParticleLoader.loadParticleEffect('phase_14/etc/rain.ptf')
        self.rain.setPos(0, 0, 5)
        self.rainRender = self.geom.attachNewNode('snowRender')
        self.rainRender.setDepthWrite(0)
        self.rainRender.setBin('fixed', 1)

    def unload(self):
        self.soundRain = None
        self.rain = None
        del self.rainRender
        SafeZoneLoader.unload(self)
        return

    def createSafeZone(self, foo):
        self.geom = loader.loadModel('phase_14/models/neighborhoods/cogtropolis.egg')
        self.geom.reparentTo(hidden)
        for i in range(2):
            bldgSectionNode = render.attachNewNode('bldgSection' + str(i))
            bldgSectionNode.setPos(self.bldgSectionData[i][0])
            bldgSectionNode.setHpr(self.bldgSectionData[i][1])
            for point in self.bldgPoints:
                bldg = loader.loadModel('phase_14/models/props/cogtropolis_big_building_1.egg')
                bldg.reparentTo(bldgSectionNode)
                bldg.setPos(point)

            self.buildingSectionNodes.append(bldgSectionNode)

        for data in self.tLightData:
            node = render.attachNewNode('tlight-intersection-holder')
            node.setPos(data[0])
            node.setHpr(data[1])
            light = TrafficLight.TrafficLight()
            light.reparentTo(node)
            light.startFlashing()
            light2 = TrafficLight.TrafficLight(1)
            light2.reparentTo(node)
            light2.startFlashing()
            self.trafficLightNodes.append(node)
            self.trafficLights.append(light)
            self.trafficLights.append(light2)

        self.fog = Fog('CogTropolis-fog')
        self.fog.setColor(0.3, 0.3, 0.3)
        self.fog.setExpDensity(0.0075)
        self.geom.flattenMedium()
        gsg = base.win.getGsg()
        if gsg:
            self.geom.prepareScene(gsg)

    def unload(self):
        for trafficLight in self.trafficLights:
            trafficLight.destroy()

        del self.trafficLights
        for trafficLightN in self.trafficLightNodes:
            trafficLightN.removeNode()

        for section in self.buildingSectionNodes:
            section.removeNode()

        del self.trafficLightNodes
        del self.buildingSectionNodes
        del self.fog
        SafeZoneLoader.unload(self)