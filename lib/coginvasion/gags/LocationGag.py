# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.LocationGag
from LocationSeeker import LocationSeeker
from direct.interval.IntervalGlobal import Sequence, Func, Parallel, SoundInterval, Wait, ActorInterval
from direct.gui.DirectGui import OnscreenText
from panda3d.core import Point3
from lib.coginvasion.globals import CIGlobals

class LocationGag:

    def __init__(self, minDistance, maxDistance, shadowScale=1):
        self.buttonSoundPath = 'phase_5/audio/sfx/AA_drop_trigger_box.ogg'
        self.button = None
        self.buttonSfx = loader.loadSfx(self.buttonSoundPath)
        self.buttonAnim = 'push-button'
        self.chooseLocFrame = 34
        self.completeFrame = 77
        self.avatar = None
        self.dropLoc = None
        self.minDistance = minDistance
        self.maxDistance = maxDistance
        self.locationSeeker = None
        self.buttonHold = 0.6
        self.actorTrack = None
        self.soundTrack = None
        self.isCircle = False
        self.shadowScale = 1
        self.helpInfo = None
        return

    def setShadowData(self, isCircle, shadowScale):
        self.isCircle = isCircle
        self.shadowScale = shadowScale

    def getShadowScale(self):
        return self.shadowScale

    def start(self, avatar):
        self.avatar = avatar
        self.cleanupLocationSeeker()
        self.buildButton()
        self.button.reparentTo(self.avatar.find('**/def_joint_left_hold'))
        track = Sequence(ActorInterval(self.avatar, self.buttonAnim, startFrame=0, endFrame=self.chooseLocFrame, playRate=self.playRate))
        if self.avatar == base.localAvatar:
            self.locationSeeker = LocationSeeker(self.avatar, self.minDistance, self.maxDistance)
            self.locationSeeker.setShadowType(self.isCircle, self.shadowScale)
            self.avatar.acceptOnce(self.locationSeeker.getLocationSelectedName(), base.localAvatar.releaseGag)
            track.append(Func(self.locationSeeker.startSeeking))
            self.helpInfo = OnscreenText(text='Move the shadow with your mouse\nClick to release', pos=(0,
                                                                                                        -0.75), font=CIGlobals.getToonFont(), fg=(1,
                                                                                                                                                  1,
                                                                                                                                                  1,
                                                                                                                                                  1), shadow=(0,
                                                                                                                                                              0,
                                                                                                                                                              0,
                                                                                                                                                              1))
        track.start()

    def release(self):
        if self.avatar:
            self.cleanupLocationSeeker()
            self.buildTracks()

    def complete(self):
        if self.button:
            numFrames = base.localAvatar.getNumFrames(self.buttonAnim)
            ActorInterval(self.avatar, self.buttonAnim, startFrame=self.completeFrame, endFrame=numFrames, playRate=self.playRate).start()
        self.cleanupButton()

    def buildTracks(self, mode=0):
        if not self.avatar:
            return
        self.cleanupTracks()
        if mode == 0:
            self.actorTrack = Sequence(ActorInterval(self.avatar, self.buttonAnim, startFrame=self.chooseLocFrame, endFrame=self.completeFrame, playRate=self.playRate))
            self.soundTrack = Sequence(Wait(self.buttonHold), SoundInterval(self.buttonSfx, node=self.avatar))

    def cleanupTracks(self):
        if self.actorTrack:
            self.actorTrack.pause()
            self.actorTrack = None
        if self.soundTrack:
            self.soundTrack.pause()
            self.soundTrack = None
        return

    def getActorTrack(self):
        return self.actorTrack

    def getSoundTrack(self):
        return self.soundTrack

    def setDropLoc(self, x, y, z):
        self.dropLoc = Point3(x, y, z)

    def buildButton(self):
        self.cleanupButton()
        self.button = loader.loadModel('phase_3.5/models/props/button.bam')

    def setLocation(self, value):
        self.dropLoc = value

    def getLocation(self):
        return self.dropLoc

    def getLocationSeeker(self):
        return self.locationSeeker

    def cleanupButton(self):
        if self.button:
            self.button.removeNode()
            self.button = None
        return

    def cleanupLocationSeeker(self):
        if self.locationSeeker:
            self.dropLoc = self.locationSeeker.getLocation()
            self.locationSeeker.cleanup()
            self.locationSeeker = None
        if self.helpInfo:
            self.helpInfo.destroy()
        return

    def cleanup(self):
        LocationSeeker.cleanup(self)
        self.cleanupButton()
        self.cleanupLocationSeeker()
        self.cleanupTracks()
        self.dropLoc = None
        self.buttonSfx.stop()
        self.buttonSoundPath = None
        self.buttonAnim = None
        self.avatar = None
        return