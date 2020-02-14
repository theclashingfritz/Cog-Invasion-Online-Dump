# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.controls.SwimWalker
from direct.showbase.InputStateGlobal import inputState
from direct.directnotify import DirectNotifyGlobal
from direct.controls import NonPhysicsWalker

class SwimWalker(NonPhysicsWalker.NonPhysicsWalker):
    notify = DirectNotifyGlobal.directNotify.newCategory('SwimWalker')

    def _calcSpeeds(self):
        forward = inputState.isSet('forward')
        reverse = inputState.isSet('reverse')
        turnLeft = inputState.isSet('turnLeft') or inputState.isSet('slideLeft')
        turnRight = inputState.isSet('turnRight') or inputState.isSet('slideRight')
        if base.localAvatar.getAutoRun():
            forward = 1
            reverse = 0
        self.speed = forward and self.avatarControlForwardSpeed or reverse and -self.avatarControlReverseSpeed
        self.slideSpeed = 0.0
        self.rotationSpeed = turnLeft and self.avatarControlRotateSpeed or turnRight and -self.avatarControlRotateSpeed