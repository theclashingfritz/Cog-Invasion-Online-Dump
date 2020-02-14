# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.holiday.DistributedWinterCoachActivity
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedNode import DistributedNode
from panda3d.core import NodePath, CollisionSphere, CollisionNode
from lib.coginvasion.toon.Toon import Toon
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.npc.NPCGlobals import NPC_DNA
from lib.coginvasion.holiday.HolidayManager import HolidayGlobals

class DistributedWinterCoachActivity(DistributedNode):
    notify = directNotify.newCategory('DistributedWinterCoachActivity')

    def __init__(self, cr):
        DistributedNode.__init__(self, cr)
        NodePath.__init__(self, 'winter_coach')
        self.cr = cr
        self.coach = None
        self.wheelBarrow = None
        self.coachNP = None
        return

    def announceGenerate(self):
        DistributedNode.announceGenerate(self)
        self.__initInteractCollisions('coachSphere' + str(self.doId))
        self.buildCoach()
        self.setParent(CIGlobals.SPRender)

    def greetAvatar(self, avatarName):
        self.coach.setChat(HolidayGlobals.COACH_GREETING % avatarName)

    def buildCoach(self):
        self.coach = Toon(self.cr)
        self.coach.setName('Coach')
        self.coach.setDNAStrand(NPC_DNA['Coach'])
        self.coach.reparentTo(self)
        self.coach.animFSM.request('neutral')
        self.wheelBarrow = loader.loadModel('phase_5.5/models/estate/wheelbarrel.bam')
        self.wheelBarrow.find('**/dirt').setTexture(loader.loadTexture('winter/maps/sbhq_snow.png'), 1)
        self.wheelBarrow.reparentTo(self.coach)
        self.wheelBarrow.setX(-3.5)
        self.wheelBarrow.setH(90)

    def deleteCoach(self):
        if self.coach:
            self.coach.disable()
            self.coach.delete()
            self.coach = None
            self.wheelBarrow.removeNode()
            self.wheelBarrow = None
        return

    def __initInteractCollisions(self, colName):
        self.notify.debug('Setting up Coach collisions')
        collSphere = CollisionSphere(0, 0, 0, 5)
        collSphere.setTangible(0)
        collNode = CollisionNode(colName)
        collNode.addSolid(collSphere)
        collNode.setCollideMask(CIGlobals.WallBitmask)
        self.coachNP = self.attachNewNode(collNode)
        self.coachNP.setZ(3)
        self.acceptOnce('enter' + self.coachNP.node().getName(), self.__handleCollision)

    def __handleCollision(self, entry):
        self.notify.debug('Entered collision sphere.')
        self.d_requestEnter()

    def d_requestEnter(self):
        self.cr.playGame.getPlace().fsm.request('stop')
        self.sendUpdate('requestEnter', [])

    def d_requestExit(self):
        self.cr.playGame.getPlace().fsm.request('stop')
        self.sendUpdate('requestExit', [])

    def enterAccepted(self):
        self.d_requestExit()
        base.localAvatar.updateSnowballButton()

    def exitAccepted(self):
        self.cr.playGame.getPlace().fsm.request('walk')
        self.acceptOnce('enter' + self.coachNP.node().getName(), self.__handleCollision)

    def destroy(self):
        self.deleteCoach()
        self.coachNP = None
        return

    def disable(self):
        DistributedNode.disable(self)
        self.destroy()

    def delete(self):
        DistributedNode.delete(self)
        self.destroy()