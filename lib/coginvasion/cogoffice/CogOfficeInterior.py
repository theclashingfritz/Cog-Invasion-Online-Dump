# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogoffice.CogOfficeInterior
from direct.fsm import ClassicFSM, State
from lib.coginvasion.hood.Place import Place

class CogOfficeInterior(Place):

    def __init__(self, loader, parentFSM, doneEvent):
        self.parentFSM = parentFSM
        Place.__init__(self, loader, doneEvent)
        self.fsm = ClassicFSM.ClassicFSM('CogOfficeInterior', [State.State('start', self.enterStart, self.exitStart, ['stop', 'walk']),
         State.State('walk', self.enterWalk, self.exitWalk, ['stop', 'teleportOut', 'died']),
         State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, ['stop', 'final']),
         State.State('stop', self.enterStop, self.exitStop, ['final', 'walk', 'teleportOut']),
         State.State('died', self.enterDied, self.exitDied, ['final']),
         State.State('shtickerBook', self.enterShtickerBook, self.exitShtickerBook, [
          'teleportOut', 'walk']),
         State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, [
          'stop', 'final']),
         State.State('final', self.enterFinal, self.exitFinal, ['start'])], 'start', 'final')

    def enterWalk(self, teleportIn=0):
        Place.enterWalk(self, teleportIn)
        base.localAvatar.startMonitoringHP()

    def exitWalk(self):
        base.localAvatar.stopMonitoringHP()
        Place.exitWalk(self)

    def enter(self, requestStatus):
        Place.enter(self)
        self.fsm.enterInitialState()

    def load(self):
        Place.load(self)
        self.parentFSM.getStateNamed('suitInterior').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('suitInterior').removeChild(self.fsm)
        del self.fsm
        del self.parentFSM
        self.ignoreAll()
        Place.unload(self)