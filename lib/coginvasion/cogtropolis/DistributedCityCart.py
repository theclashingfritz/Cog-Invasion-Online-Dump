# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogtropolis.DistributedCityCart
from panda3d.core import CollisionSphere, CollisionNode
from direct.distributed.DistributedNode import DistributedNode
from direct.distributed import ClockDelta
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.interval.IntervalGlobal import Parallel, LerpHprInterval
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.cog.Suit import Suit
import NURBSMopath, CityCartGlobals, random

class DistributedCityCart(DistributedNode):
    notify = directNotify.newCategory('DistributedCityCart')

    def __init__(self, cr):
        DistributedNode.__init__(self, cr)
        self.fsm = ClassicFSM('DistributedCityCart', [State('off', self.enterOff, self.exitOff),
         State('pathFollow', self.enterPathFollow, self.exitPathFollow),
         State('collision', self.enterCollision, self.exitCollision)], 'off', 'off')
        self.fsm.enterInitialState()
        self.suitInCar = None
        self.cart = None
        self.honkSfxPath = 'phase_14/audio/sfx/cogtropolis_citycar_driveby_horn.ogg'
        self.cartModelPath = 'phase_12/models/bossbotHQ/Coggolf_cart3.bam'
        self.moPaths = ['phase_14/models/paths/ct-citycar-drivepath-1.egg',
         'phase_14/models/paths/ct-citycar-drivepath-2.egg',
         'phase_14/models/paths/ct-citycar-drivepath-3.egg',
         'phase_14/models/paths/ct-citycar-drivepath-4.egg',
         'phase_14/models/paths/ct-citycar-drivepath-5.egg',
         'phase_14/models/paths/ct-citycar-drivepath-6.egg']
        self.moPath = None
        self.soundEngineLoop = None
        self.soundDriveByHorn = None
        self.ivalTDisplace = None
        self.pathIndex = None
        self.wheelSpinTrack = None
        self.collNodePath = None
        self.soundDriveBy = None
        return

    def setIvalTDisplace(self, displace):
        self.ivalTDisplace = displace

    def setPathIndex(self, index):
        self.pathIndex = index

    def setState(self, state, timestamp):
        ts = ClockDelta.globalClockDelta.localElapsedTime(timestamp)
        self.fsm.request(state, [ts])

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterPathFollow(self, ts):
        duration = CityCartGlobals.index2Duration[self.pathIndex]
        self.moPath = NURBSMopath.NURBSMopath(self.moPaths[self.pathIndex], name=self.uniqueName('DCityCart_moPath'))
        startT = 0.0
        if ts > 0.0:
            startT = ts % duration * (1.0 / duration)
        self.moPath.play(self, loop=True, duration=duration, startT=startT)
        base.taskMgr.add(self.__drive, self.uniqueName('DCityCart.drive'))
        self.wheelSpinTrack = Parallel()
        for name in ['leftFrontWheel', 'rightBackWheel', 'rightFrontWheel', 'leftBackWheel']:
            wheel = self.find('**/' + name)
            self.wheelSpinTrack.append(LerpHprInterval(wheel, duration=0.1, hpr=(0,
                                                                                 360,
                                                                                 0), startHpr=(0,
                                                                                               0,
                                                                                               0)))

        self.wheelSpinTrack.loop()
        self.accept('enter' + self.collNodePath.node().getName(), self.__handleRanOver)

    def __handleRanOver(self, entry):
        self.suitInCar.setChat(CityCartGlobals.SuitRanOverTaunt)
        self.sendUpdate('hitByCar')
        self.cr.playGame.getPlace().fsm.request('stop')
        base.localAvatar.b_setAnimState('squish', callback=self.cr.playGame.getPlace().fsm.request, extraArgs=['walk'])

    def __drive(self, task):
        if base.localAvatar.getDistance(self) < 10.0:
            if self.soundDriveByHorn.status() == self.soundDriveByHorn.READY:
                wantsToHonk = random.randint(0, 3)
                if wantsToHonk == 3:
                    base.playSfx(self.soundDriveByHorn)
                return task.cont
        else:
            if base.localAvatar.getDistance(self) < 20.0:
                if self.soundDriveBy.status() == self.soundDriveBy.READY:
                    base.playSfx(self.soundDriveBy)
                    return task.cont
        return task.cont

    def exitPathFollow(self):
        self.ignore('enter' + self.collNodePath.node().getName())
        if self.wheelSpinTrack:
            self.wheelSpinTrack.finish()
            self.wheelSpinTrack = None
        if self.moPath:
            self.moPath.stop()
            self.moPath = None
        return

    def enterCollision(self, ts):
        pass

    def exitCollision(self):
        pass

    def generate(self):
        DistributedNode.generate(self)
        self.cart = loader.loadModel(self.cartModelPath)
        self.cart.reparentTo(self)
        self.cart.setH(180)
        heads = []
        for head in CIGlobals.SuitBodyData.keys():
            if CIGlobals.SuitBodyData[head][0] != 'B':
                heads.append(head)

        head = random.choice(heads)
        suitType = CIGlobals.SuitBodyData[head][0]
        suitDept = CIGlobals.SuitBodyData[head][1]
        self.suitInCar = Suit()
        self.suitInCar.generateSuit(suitType, head, suitDept, 137, 0, False)
        self.suitInCar.loop('sit')
        self.suitInCar.disableRay()
        self.suitInCar.setScale(0.7)
        self.suitInCar.setH(180)
        self.suitInCar.setPos(0, -1, -1.5)
        self.suitInCar.reparentTo(self.cart.find('**/seat1'))
        self.soundEngineLoop = base.audio3d.loadSfx('phase_6/audio/sfx/KART_Engine_loop_0.ogg')
        base.audio3d.attachSoundToObject(self.soundEngineLoop, self)
        base.playSfx(self.soundEngineLoop, looping=1)
        self.soundDriveByHorn = base.audio3d.loadSfx(self.honkSfxPath)
        base.audio3d.attachSoundToObject(self.soundDriveByHorn, self)
        self.soundDriveBy = base.audio3d.loadSfx('phase_14/audio/sfx/cogtropolis_citycar_driveby.ogg')
        base.audio3d.attachSoundToObject(self.soundDriveBy, self)
        sphere = CollisionSphere(0, 0, 0, 2.5)
        sphere.setTangible(0)
        node = CollisionNode(self.uniqueName('cartSphere'))
        node.setCollideMask(CIGlobals.WallBitmask)
        node.addSolid(sphere)
        self.collNodePath = self.attachNewNode(node)
        self.collNodePath.setZ(1.5)
        self.collNodePath.setSy(2.0)
        self.collNodePath.setSx(1.75)

    def disable(self):
        self.fsm.requestFinalState()
        if self.moPath:
            self.moPath.stop()
            self.moPath = None
        self.moPaths = None
        self.honkSfxPath = None
        self.cartModelPath = None
        self.soundEngineLoop = None
        self.soundDriveBy = None
        if self.suitInCar:
            self.suitInCar.disable()
            self.suitInCar.delete()
            self.suitInCar = None
        if self.cart:
            self.cart.removeNode()
            self.cart = None
        del self.fsm
        DistributedNode.disable(self)
        return