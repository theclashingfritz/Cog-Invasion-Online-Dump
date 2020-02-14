# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.controls.TwoDWalker
from GravityWalker import *

class TwoDWalker(GravityWalker):
    notify = directNotify.newCategory('TwoDWalker')
    wantDebugIndicator = base.config.GetBool('want-avatar-physics-indicator', 0)
    wantFloorSphere = base.config.GetBool('want-floor-sphere', 0)
    earlyEventSphere = base.config.GetBool('early-event-sphere', 0)

    def __init__(self, gravity=-32.174, standableGround=0.707, hardLandingForce=16.0):
        self.notify.debug('Constructing TwoDWalker')
        GravityWalker.__init__(self)

    def handleAvatarControls(self, task):
        jump = inputState.isSet('forward')
        if self.lifter.isOnGround():
            if self.isAirborne:
                self.isAirborne = 0
                impact = self.lifter.getImpactVelocity()
                messenger.send('jumpLand')
            self.priorParent = Vec3.zero()
        else:
            if self.isAirborne == 0:
                pass
            self.isAirborne = 1
        return Task.cont

    def jumpPressed(self):
        if self.lifter.isOnGround():
            if self.isAirborne == 0:
                if self.mayJump:
                    self.lifter.addVelocity(self.avatarControlJumpForce)
                    messenger.send('jumpStart')
                    self.isAirborne = 1