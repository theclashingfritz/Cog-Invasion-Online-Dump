# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.particles.GlobalForceGroup
import ForceGroup

class GlobalForceGroup(ForceGroup.ForceGroup):

    def __init__(self, name=None):
        ForceGroup.ForceGroup.__init__(self, name)

    def addForce(self, force):
        ForceGroup.ForceGroup.addForce(force)
        if force.isLinear() == 0:
            base.addAngularIntegrator()
        if force.isLinear() == 1:
            physicsMgr.addLinearForce(force)
        else:
            physicsMgr.addAngularForce(force)

    def removeForce(self, force):
        ForceGroup.ForceGroup.removeForce(force)
        if force.isLinear() == 1:
            physicsMgr.removeLinearForce(force)
        else:
            physicsMgr.removeAngularForce(force)