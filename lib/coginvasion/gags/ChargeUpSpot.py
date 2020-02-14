# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.ChargeUpSpot
from lib.coginvasion.gags.LocationSeeker import LocationSeeker
from direct.showbase.InputStateGlobal import inputState
from direct.interval.IntervalGlobal import Sequence, Parallel, LerpScaleInterval, SoundInterval
from direct.interval.IntervalGlobal import Func, LerpColorScaleInterval
from direct.task.Task import Task
from panda3d.core import VBase4
from lib.coginvasion.globals import CIGlobals

class ChargeUpSpot(LocationSeeker):

    def __init__(self, gag, avatar, selectionRadius, minDistance, maxDistance, shadowScale, maxCogs=4):
        LocationSeeker.__init__(self, avatar, minDistance, maxDistance, shadowScale)
        self.gag = gag
        self.pollMouseTaskName = 'Poll Mouse Hold Downs'
        self.chargedUpName = 'Charged Up'
        self.chargedCancelName = 'Charge Canceled'
        self.mouseDownName = 'mouse1-down'
        self.chargingSfxPath = 'phase_4/audio/sfx/MG_sfx_ice_scoring_1.ogg'
        self.chargingSfx = None
        self.tickSfxPath = 'phase_13/audio/sfx/tick_counter_short.ogg'
        self.tickSfx = None
        self.lMouseDn = None
        self.isCharging = False
        self.shadowTrack = None
        self.chargeDuration = 2.5
        self.selectionRadius = selectionRadius
        self.maxCogs = maxCogs
        self.selectedCogs = []
        self.cleanedUp = False
        if game.process == 'client':
            self.chargingSfx = base.audio3d.loadSfx(self.chargingSfxPath)
            self.tickSfx = base.audio3d.loadSfx(self.tickSfxPath)
        return

    def buildShadow(self):
        self.cleanupShadow()
        if not self.dropShadowPath or not self.avatar:
            return
        self.dropShadow = loader.loadModel('phase_4/models/minigames/ice_game_score_circle.bam')
        self.dropShadow.setScale(self.shadowScale)
        self.dropShadow.setAlphaScale(0.5)
        self.dropShadow.setTransparency(1)

    def startSeeking(self):
        LocationSeeker.startSeeking(self)
        if not self.dropShadow:
            return
        self.avatar.ignore('mouse1')
        self.lMouseDn = inputState.watch(self.mouseDownName, 'mouse1', 'mouse1-up')
        base.taskMgr.add(self.__pollMouseHeldDown, self.pollMouseTaskName)

    def __selectNearbyCogs(self):
        self.selectedCogs = []
        for obj in base.cr.doId2do.values():
            if obj.__class__.__name__ in CIGlobals.SuitClasses:
                if obj.getPlace() == self.avatar.zoneId:
                    if obj.getDistance(self.dropShadow) <= self.selectionRadius:
                        if self.avatar.doId == self.avatar.doId:
                            if len(self.selectedCogs) < self.maxCogs:
                                if not obj.isDead():
                                    self.selectedCogs.append(obj)

    def __tickNearbyCogs(self):
        self.__selectNearbyCogs()
        tickTrack = Parallel()
        tickDuration = 0.4
        for cog in self.selectedCogs:
            if not cog.isDead():
                base.audio3d.attachSoundToObject(self.tickSfx, cog)
                tickTrack.append(Parallel(Sequence(LerpColorScaleInterval(cog, tickDuration, VBase4(1, 0, 0, 1)), Func(cog.clearColorScale), Func(cog.d_disableMovement)), SoundInterval(self.tickSfx, duration=tickDuration, node=cog)))
            else:
                self.selectedCogs.remove(cog)

        return tickTrack

    def startCharging(self):
        LocationSeeker.stopSeeking(self)
        self.dropShadow.setZ(self.dropShadow.getZ() - 0.45)
        finalScale = 6
        self.shadowTrack = Sequence()
        chargeTrack = Parallel(LerpScaleInterval(self.dropShadow, self.chargeDuration, finalScale, startScale=self.dropShadow.getScale(), blendType='easeInOut'), Func(base.audio3d.attachSoundToObject, self.chargingSfx, self.dropShadow), SoundInterval(self.chargingSfx, duration=self.chargeDuration, node=self.dropShadow))
        self.shadowTrack.append(chargeTrack)
        self.shadowTrack.append(self.__tickNearbyCogs())
        self.shadowTrack.append(Func(self.onFullCharge))
        self.shadowTrack.start()
        self.isCharging = True

    def onFullCharge(self):
        if self.gag.isLocal():
            self.gag.startTimeout()
        if self.shadowTrack:
            self.shadowTrack.finish()
            self.shadowTrack = None
        if len(self.selectedCogs) > 0:
            messenger.send(self.chargedUpName)
        else:
            messenger.send(self.chargedCancelName)
        return

    def stopCharging(self):
        if self.gag.isLocal():
            self.gag.startTimeout()
        self.isCharging = False
        if self.shadowTrack:
            self.shadowTrack.pause()
        for cog in self.selectedCogs:
            cog.clearColorScale()

        base.taskMgr.remove(self.pollMouseTaskName)
        messenger.send(self.chargedCancelName)
        if hasattr(self, 'lMouseDn'):
            if self.lMouseDn:
                self.lMouseDn.release()

    def cleanup(self):
        if hasattr(self, 'maxCogs') and not self.cleanedUp:
            self.cleanedUp = True
            LocationSeeker.cleanup(self)
            if self.chargingSfx and self.tickSfx:
                base.audio3d.detachSound(self.chargingSfx)
                base.audio3d.detachSound(self.tickSfx)
                self.chargingSfx.stop()
                self.tickSfx.stop()
            if self.shadowTrack:
                self.shadowTrack.pause()
                self.shadowTrack = None
            if self.isCharging:
                self.stopCharging()
            del self.mouseDownName
            del self.pollMouseTaskName
            del self.chargedUpName
            del self.chargedCancelName
            del self.lMouseDn
            del self.chargingSfx
            del self.chargingSfxPath
            del self.tickSfx
            del self.tickSfxPath
            del self.selectionRadius
            del self.selectedCogs
            del self.maxCogs
            del self.gag
        return

    def __pollMouseHeldDown(self, task):
        if not hasattr(self, 'mouseDownName'):
            return Task.done
        if inputState.isSet(self.mouseDownName) and not self.isCharging:
            self.startCharging()
        else:
            if not inputState.isSet(self.mouseDownName) and self.isCharging:
                self.stopCharging()
        return Task.cont

    def getSelectedCogs(self):
        return self.selectedCogs

    def getChargedUpName(self):
        return self.chargedUpName

    def getChargedCanceledName(self):
        return self.chargedCancelName