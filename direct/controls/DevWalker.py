# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.controls.DevWalker
from direct.showbase.InputStateGlobal import inputState
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject
from direct.task.Task import Task
from pandac.PandaModules import *

class DevWalker(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DevWalker')
    wantDebugIndicator = base.config.GetBool('want-avatar-physics-indicator', 0)
    runMultiplier = base.config.GetFloat('dev-run-multiplier', 4.0)
    slideName = 'slide-is-disabled'

    def __init__(self):
        DirectObject.DirectObject.__init__(self)
        self.speed = 0.0
        self.rotationSpeed = 0.0
        self.slideSpeed = 0.0
        self.vel = Vec3(0.0, 0.0, 0.0)
        self.task = None
        return

    def setWalkSpeed(self, forward, jump, reverse, rotate):
        self.avatarControlForwardSpeed = forward
        self.avatarControlReverseSpeed = reverse
        self.avatarControlRotateSpeed = rotate

    def getSpeeds(self):
        return (
         self.speed, self.rotationSpeed, self.slideSpeed)

    def setAvatar(self, avatar):
        self.avatar = avatar
        if avatar is not None:
            pass
        return

    def setWallBitMask(self, bitMask):
        pass

    def setFloorBitMask(self, bitMask):
        pass

    def initializeCollisions(self, collisionTraverser, avatarNodePath, wallCollideMask, floorCollideMask, avatarRadius=1.4, floorOffset=1.0, reach=1.0):
        self.cTrav = collisionTraverser
        self.avatarNodePath = avatarNodePath

    def setAirborneHeightFunc(self, getAirborneHeight):
        pass

    def deleteCollisions(self):
        pass

    def setTag(self, key, value):
        pass

    def setCollisionsActive(self, active=1):
        pass

    def placeOnFloor(self):
        pass

    def oneTimeCollide(self):
        pass

    def addBlastForce(self, vector):
        pass

    def displayDebugInfo(self):
        onScreenDebug.add('w controls', 'DevWalker')

    def handleAvatarControls(self, task):
        forward = inputState.isSet('forward')
        reverse = inputState.isSet('reverse')
        turnLeft = inputState.isSet('turnLeft')
        turnRight = inputState.isSet('turnRight')
        slideLeft = inputState.isSet('slideLeft')
        slideRight = inputState.isSet('slideRight')
        levitateUp = inputState.isSet('levitateUp')
        levitateDown = inputState.isSet('levitateDown')
        run = inputState.isSet('run') and self.runMultiplier or 1.0
        if base.localAvatar.getAutoRun():
            forward = 1
            reverse = 0
        self.speed = forward and self.avatarControlForwardSpeed or reverse and -self.avatarControlReverseSpeed
        self.liftSpeed = levitateUp and self.avatarControlForwardSpeed or levitateDown and -self.avatarControlReverseSpeed
        self.slideSpeed = slideLeft and -self.avatarControlForwardSpeed or slideRight and self.avatarControlForwardSpeed
        self.rotationSpeed = turnLeft and self.avatarControlRotateSpeed or turnRight and -self.avatarControlRotateSpeed
        if self.wantDebugIndicator:
            self.displayDebugInfo()
        if self.speed or self.liftSpeed or self.slideSpeed or self.rotationSpeed:
            dt = ClockObject.getGlobalClock().getDt()
            distance = dt * self.speed * run
            lift = dt * self.liftSpeed * run
            slideDistance = dt * self.slideSpeed * run
            rotation = dt * self.rotationSpeed
            self.vel = Vec3(Vec3.forward() * distance + Vec3.up() * lift + Vec3.right() * slideDistance)
            if self.vel != Vec3.zero():
                rotMat = Mat3.rotateMatNormaxis(self.avatarNodePath.getH(), Vec3.up())
                step = rotMat.xform(self.vel)
                self.avatarNodePath.setFluidPos(Point3(self.avatarNodePath.getPos() + step))
            self.avatarNodePath.setH(self.avatarNodePath.getH() + rotation)
            messenger.send('avatarMoving')
        else:
            self.vel.set(0.0, 0.0, 0.0)
        return Task.cont

    def enableAvatarControls(self):
        if self.task:
            self.task.remove(self.task)
        self.task = taskMgr.add(self.handleAvatarControls, 'AvatarControls-dev-%s' % (id(self),))

    def disableAvatarControls(self):
        if self.task:
            self.task.remove()
            self.task = None
        return

    def flushEventHandlers(self):
        pass