# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.Audio3DManager
__all__ = [
 'Audio3DManager']
from panda3d.core import Vec3, VBase3
from direct.task import Task

class Audio3DManager:

    def __init__(self, audio_manager, listener_target=None, root=None, taskPriority=51):
        self.audio_manager = audio_manager
        self.listener_target = listener_target
        if root == None:
            self.root = render
        else:
            self.root = root
        self.sound_dict = {}
        self.vel_dict = {}
        self.listener_vel = VBase3(0, 0, 0)
        taskMgr.add(self.update, 'Audio3DManager-updateTask', taskPriority)
        return

    def loadSfx(self, name):
        sound = None
        if name:
            sound = self.audio_manager.getSound(name, 1)
        return sound

    def setDistanceFactor(self, factor):
        self.audio_manager.audio3dSetDistanceFactor(factor)

    def getDistanceFactor(self):
        return self.audio_manager.audio3dGetDistanceFactor()

    def setDopplerFactor(self, factor):
        self.audio_manager.audio3dSetDopplerFactor(factor)

    def getDopplerFactor(self):
        return self.audio_manager.audio3dGetDopplerFactor()

    def setDropOffFactor(self, factor):
        self.audio_manager.audio3dSetDropOffFactor(factor)

    def getDropOffFactor(self):
        return self.audio_manager.audio3dGetDropOffFactor()

    def setSoundMinDistance(self, sound, dist):
        sound.set3dMinDistance(dist)

    def getSoundMinDistance(self, sound):
        return sound.get3dMinDistance()

    def setSoundMaxDistance(self, sound, dist):
        sound.set3dMaxDistance(dist)

    def getSoundMaxDistance(self, sound):
        return sound.get3dMaxDistance()

    def setSoundVelocity(self, sound, velocity):
        if not isinstance(velocity, VBase3):
            raise TypeError, 'Invalid argument 1, expected <VBase3>'
        self.vel_dict[sound] = velocity

    def setSoundVelocityAuto(self, sound):
        self.vel_dict[sound] = None
        return

    def getSoundVelocity(self, sound):
        if sound in self.vel_dict:
            vel = self.vel_dict[sound]
            if vel != None:
                return vel
            for known_object in self.sound_dict.keys():
                if self.sound_dict[known_object].count(sound):
                    return known_object.getPosDelta(self.root) / globalClock.getDt()

        return VBase3(0, 0, 0)

    def setListenerVelocity(self, velocity):
        if not isinstance(velocity, VBase3):
            raise TypeError, 'Invalid argument 0, expected <VBase3>'
        self.listener_vel = velocity

    def setListenerVelocityAuto(self):
        self.listener_vel = None
        return

    def getListenerVelocity(self):
        if self.listener_vel != None:
            return self.listener_vel
        if self.listener_target != None:
            return self.listener_target.getPosDelta(self.root) / globalClock.getDt()
        return VBase3(0, 0, 0)
        return

    def attachSoundToObject(self, sound, object):
        for known_object in self.sound_dict.keys():
            if self.sound_dict[known_object].count(sound):
                self.sound_dict[known_object].remove(sound)
                if len(self.sound_dict[known_object]) == 0:
                    del self.sound_dict[known_object]

        if object not in self.sound_dict:
            self.sound_dict[object] = []
        self.sound_dict[object].append(sound)
        return 1

    def detachSound(self, sound):
        for known_object in self.sound_dict.keys():
            if self.sound_dict[known_object].count(sound):
                self.sound_dict[known_object].remove(sound)
                if len(self.sound_dict[known_object]) == 0:
                    del self.sound_dict[known_object]
                return 1

        return 0

    def getSoundsOnObject(self, object):
        if object not in self.sound_dict:
            return []
        sound_list = []
        sound_list.extend(self.sound_dict[object])
        return sound_list

    def attachListener(self, object):
        self.listener_target = object
        return 1

    def detachListener(self):
        self.listener_target = None
        return 1

    def update(self, task=None):
        if hasattr(self.audio_manager, 'getActive'):
            if self.audio_manager.getActive() == 0:
                return Task.cont
        for known_object in self.sound_dict.keys():
            tracked_sound = 0
            while tracked_sound < len(self.sound_dict[known_object]):
                sound = self.sound_dict[known_object][tracked_sound]
                if known_object:
                    if known_object.isEmpty():
                        self.detachSound(sound)
                        return Task.cont
                    pos = known_object.getPos(self.root)
                else:
                    self.detachSound(sound)
                    return Task.cont
                vel = self.getSoundVelocity(sound)
                sound.set3dAttributes(pos[0], pos[1], pos[2], vel[0], vel[1], vel[2])
                tracked_sound += 1

        if self.listener_target:
            pos = self.listener_target.getPos(self.root)
            forward = self.root.getRelativeVector(self.listener_target, Vec3.forward())
            up = self.root.getRelativeVector(self.listener_target, Vec3.up())
            vel = self.getListenerVelocity()
            self.audio_manager.audio3dSetListenerAttributes(pos[0], pos[1], pos[2], vel[0], vel[1], vel[2], forward[0], forward[1], forward[2], up[0], up[1], up[2])
        else:
            self.audio_manager.audio3dSetListenerAttributes(0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1)
        return Task.cont

    def disable(self):
        taskMgr.remove('Audio3DManager-updateTask')
        self.detachListener()
        for object in self.sound_dict.keys():
            for sound in self.sound_dict[object]:
                self.detachSound(sound)