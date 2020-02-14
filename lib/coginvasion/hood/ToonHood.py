# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.ToonHood
from panda3d.core import Vec4
import Hood
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State

class ToonHood(Hood.Hood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.safeZoneLoader = None
        self.townLoader = None
        self.fsm = ClassicFSM('Hood', [State('off', self.enterOff, self.exitOff),
         State('safeZoneLoader', self.enterSafeZoneLoader, self.exitSafeZoneLoader, ['quietZone', 'townLoader']),
         State('townLoader', self.enterTownLoader, self.exitTownLoader, ['quietZone', 'safeZoneLoader']),
         State('quietZone', self.enterQuietZone, self.exitQuietZone, [
          'safeZoneLoader', 'townLoader'])], 'off', 'off')
        self.fsm.enterInitialState()
        return

    def loadLoader(self, requestStatus):
        loader = requestStatus['loader']
        if loader == 'safeZoneLoader':
            if self.safeZoneLoader:
                self.loader = self.safeZoneLoader(self, self.fsm.getStateNamed('safeZoneLoader'), self.loaderDoneEvent)
                self.loader.load()
            else:
                self.notify.error('ToonHood.ToonHood.safeZoneLoader cannot be None!' % loader)
        else:
            if loader == 'townLoader':
                if self.townLoader:
                    self.loader = self.townLoader(self, self.fsm.getStateNamed('townLoader'), self.loaderDoneEvent)
                    self.loader.load(requestStatus['zoneId'])
            else:
                self.notify.error('Unknown loader %s!' % loader)

    def enterTownLoader(self, requestStatus):
        self.acceptOnce(self.loaderDoneEvent, self.handleTownLoaderDone)
        self.loader.enter(requestStatus)
        self.spawnTitleText(requestStatus['zoneId'])

    def exitTownLoader(self):
        taskMgr.remove('titleText')
        self.hideTitleText()
        self.ignore(self.loaderDoneEvent)
        self.loader.exit()
        self.loader.unload()
        del self.loader

    def handleTownLoaderDone(self):
        doneStatus = self.loader.getDoneStatus()
        if self.isSameHood(doneStatus):
            self.fsm.request('quietZone', [doneStatus])
        else:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)

    def load(self):
        Hood.Hood.load(self)
        self.whiteFogColor = Vec4(0.8, 0.8, 0.8, 1)
        self.underwaterFogColor = Vec4(0.0, 0.0, 0.6, 1.0)

    def unload(self):
        del self.safeZoneLoader
        Hood.Hood.unload(self)

    def enter(self, requestStatus):
        self.loadLoader(requestStatus)
        Hood.Hood.enter(self, requestStatus)

    def exit(self):
        Hood.Hood.exit(self)

    def setUnderwaterFog(self):
        if base.wantFog:
            self.fog.setColor(self.underwaterColor)
            self.fog.setLinearRange(0.1, 100.0)
            render.setFog(self.fog)
            self.sky.setFog(self.fog)

    def setWhiteFog(self):
        if base.wantFog:
            self.fog.setColor(self.whiteFogColor)
            self.fog.setLinearRange(0.0, 400.0)
            render.clearFog()
            render.setFog(self.fog)
            self.sky.clearFog()
            self.sky.setFog(self.fog)

    def setNoFog(self):
        if base.wantFog:
            render.clearFog()
            self.sky.clearFog()