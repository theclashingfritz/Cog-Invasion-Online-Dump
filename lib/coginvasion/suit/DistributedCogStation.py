# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.DistributedCogStation
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.IntervalGlobal import Sequence, Wait, Func
from lib.coginvasion.minigame.DistributedGroupStation import DistributedGroupStation
from CogStation import CogStation
from lib.coginvasion.globals import CIGlobals

class DistributedCogStation(DistributedGroupStation, CogStation):
    notify = directNotify.newCategory('DistributedCogStation')

    def __init__(self, cr):
        try:
            self.DistributedCogStation_initialized
            return
        except:
            self.DistributedCogStation_initialized = 1

        DistributedGroupStation.__init__(self, cr)
        CogStation.__init__(self)

    def headOff(self, zone, hoodIndex):
        self.deleteStationAbortGui()
        hoodId = self.cr.playGame.hood.hoodId
        requestStatus = {'zoneId': zone, 'hoodId': hoodId, 
           'where': 'playground', 
           'avId': base.localAvatar.doId, 
           'loader': 'safeZoneLoader', 
           'shardId': None, 
           'wantLaffMeter': 1, 
           'how': 'teleportIn', 
           'world': CIGlobals.CogTropolis}
        self.cr.playGame.getPlace().fsm.request('teleportOut', [requestStatus])
        Sequence(Wait(5.0), Func(self.d_leaving)).start()
        return

    def generate(self):
        DistributedGroupStation.generate(self)
        self.generateStation()

    def announceGenerate(self):
        DistributedGroupStation.announceGenerate(self)
        self.reparentTo(render)

    def disable(self):
        self.reparentTo(hidden)
        DistributedGroupStation.disable(self)

    def delete(self):
        CogStation.delete(self)
        DistributedGroupStation.delete(self)