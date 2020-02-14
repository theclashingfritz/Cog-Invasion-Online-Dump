# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.DistributedToonFPSGame
from panda3d.core import Vec4
from direct.interval.IntervalGlobal import Sequence, Func, LerpScaleInterval, LerpColorScaleInterval, Parallel
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.ClockDelta import globalClockDelta
from lib.coginvasion.minigame import GunGameGlobals as GGG
from DistributedMinigame import DistributedMinigame

class DistributedToonFPSGame(DistributedMinigame):
    notify = directNotify.newCategory('DistributedToonFPSGame')

    def __init__(self, cr):
        try:
            self.DistributedToonFPSGame_initialized
            return
        except:
            self.DistributedToonFPSGame_initialized = 1

        DistributedMinigame.__init__(self, cr)
        self.remoteAvatars = []
        self.myRemoteAvatar = None
        self.myKOTHPoints = 0
        self.KOTHKing = None
        return

    def setMyKOTHPoints(self, points):
        self.myKOTHPoints = points

    def setKOTHKing(self, avId):
        if avId != 0:
            self.KOTHKing = self.cr.doId2do.get(avId)
        else:
            self.KOTHKing = None
        return

    def getKOTHKing(self):
        return self.KOTHKing

    def makeSmokeEffect(self, pos):
        smoke = loader.loadModel('phase_4/models/props/test_clouds.bam')
        smoke.setBillboardAxis()
        smoke.reparentTo(render)
        smoke.setPos(pos)
        smoke.setScale(0.05, 0.05, 0.05)
        smoke.setDepthWrite(False)
        track = Sequence(Parallel(LerpScaleInterval(smoke, 0.5, (0.1, 0.15, 0.15)), LerpColorScaleInterval(smoke, 0.5, Vec4(2, 2, 2, 0))), Func(smoke.removeNode))
        track.start()

    def enterFinalScores(self):
        if self.gameMode == GGG.GameModes.KOTH:
            from lib.coginvasion.gui.KOTHKingGui import KOTHKingGui
            self.finalScoreUI = KOTHKingGui(self, self.KOTHKing, self.myKOTHPoints)
        else:
            DistributedMinigame.enterFinalScores(self)

    def finalScores(self, avIdList, scoreList):
        if self.gameMode == GGG.GameModes.KOTH:
            self.finalScoreUI.start()
        else:
            DistributedMinigame.finalScores(self, avIdList, scoreList)

    def exitFinalScores(self):
        if self.gameMode == GGG.GameModes.KOTH:
            self.finalScoreUI.destroy()
            print "I should've destroyed"
        else:
            DistributedMinigame.exitFinalScores(self)

    def avatarHitByBullet(self, avId, damage):
        pass

    def d_gunShot(self):
        timestamp = globalClockDelta.getFrameNetworkTime()
        self.sendUpdate('gunShot', [base.localAvatar.doId, timestamp])

    def jumpingAvatar(self, avId):
        av = self.getRemoteAvatar(avId)
        if av:
            av.jump()

    def getMyRemoteAvatar(self):
        return self.myRemoteAvatar

    def damage(self, amount, avId):
        self.toonFps.damageTaken(amount, avId)

    def setupRemoteAvatar(self, avId):
        pass

    def gunShot(self, avId, timestamp):
        ts = globalClockDelta.localElapsedTime(timestamp)
        av = self.getRemoteAvatar(avId)
        if av:
            av.fsm.request('shoot', [ts])

    def deadAvatar(self, avId, timestamp):
        ts = globalClockDelta.localElapsedTime(timestamp)
        av = self.getRemoteAvatar(avId)
        if av:
            av.fsm.request('die', [ts])

    def respawnAvatar(self, avId):
        av = self.getRemoteAvatar(avId)
        if av:
            av.exitDead()
            av.fsm.requestFinalState()

    def getRemoteAvatar(self, avId):
        for avatar in self.remoteAvatars:
            if avatar.avId == avId:
                return avatar

        return

    def disable(self):
        self.myRemoteAvatar.cleanup()
        self.myRemoteAvatar = None
        for av in self.remoteAvatars:
            av.cleanup()
            del av

        self.remoteAvatars = None
        DistributedMinigame.disable(self)
        return