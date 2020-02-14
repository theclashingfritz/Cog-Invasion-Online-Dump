# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogtropolis.TrafficLight
from panda3d.core import NodePath
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence, Wait, Func

class TrafficLight(NodePath):
    notify = directNotify.newCategory('TrafficLight')
    colors = {'light-grey': (0.141, 0.141, 0.141, 1.0), 'grey': (0.09, 0.09, 0.09, 1.0), 
       'dark-grey': (0.027, 0.027, 0.027, 1.0), 
       'black': (0, 0, 0, 1), 
       'yellow': (1, 0.711, 0, 1)}
    part2Color = {'*_holder': 'dark-grey', '*_*light': 'grey', 
       'pole*': 'light-grey', 
       'wire': 'black', 
       'light-*': 'black'}

    def __init__(self, index=0):
        NodePath.__init__(self, 'TrafficLight-' + str(id(self)))
        self.light = loader.loadModel('phase_14/models/props/cogtropolis_streetlight.egg')
        for partName, colorName in self.part2Color.items():
            for node in self.light.findAllMatches('**/' + partName):
                if '_coll' not in node.getName():
                    node.setColor(self.colors[colorName])

        self.light.reparentTo(self)
        if index == 1:
            self.setH(-90)
            self.find('**/pole1').stash()
            self.find('**/pole1_coll').stash()
        self.setTwoSided(1)
        self.soundFlicker = base.audio3d.loadSfx('phase_14/audio/sfx/cogtropolis_trafficlight_flicker.ogg')
        base.audio3d.attachSoundToObject(self.soundFlicker, self.find('**/light-base'))
        self.flashTrack = None
        return

    def flashOff(self):
        for light in self.light.findAllMatches('**/*_middlelight'):
            light.setColor(self.colors['grey'])

    def flashOn(self):
        for light in self.light.findAllMatches('**/*_middlelight'):
            light.setColor(self.colors['yellow'])

        self.soundFlicker.play()

    def startFlashing(self):
        self.stopFlashing()
        self.flashTrack = Sequence()
        self.flashTrack.append(Func(self.flashOn))
        self.flashTrack.append(Wait(1.0))
        self.flashTrack.append(Func(self.flashOff))
        self.flashTrack.append(Wait(1.0))
        self.flashTrack.loop()

    def stopFlashing(self):
        if self.flashTrack:
            self.flashTrack.finish()
            self.flashTrack = None
        self.flashOff()
        return

    def destroy(self):
        self.soundFlicker = None
        self.stopFlashing()
        self.light.removeNode()
        self.light = None
        self.removeNode()
        return