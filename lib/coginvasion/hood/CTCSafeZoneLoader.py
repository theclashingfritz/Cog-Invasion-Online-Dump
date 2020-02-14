# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.CTCSafeZoneLoader
from panda3d.core import TransparencyAttrib
from lib.coginvasion.holiday.HolidayManager import HolidayType
import SafeZoneLoader, CTCPlayground

class CTCSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playground = CTCPlayground.CTCPlayground
        self.pgMusicFilename = 'phase_4/audio/bgm/TC_nbrhood.mid'
        self.interiorMusicFilename = 'phase_3.5/audio/bgm/TC_SZ_activity.mid'
        self.battleMusicFile = 'phase_3.5/audio/bgm/encntr_general_bg.mid'
        self.invasionMusicFiles = [
         'phase_12/audio/bgm/BossBot_CEO_v1.mid',
         'phase_9/audio/bgm/encntr_suit_winning.mid']
        self.tournamentMusicFiles = [
         'phase_3.5/audio/bgm/encntr_nfsmw_bg_1.ogg',
         'phase_3.5/audio/bgm/encntr_nfsmw_bg_2.ogg',
         'phase_3.5/audio/bgm/encntr_nfsmw_bg_3.ogg',
         'phase_3.5/audio/bgm/encntr_nfsmw_bg_4.ogg']
        self.bossBattleMusicFile = 'phase_7/audio/bgm/encntr_suit_winning_indoor.mid'
        self.dnaFile = 'phase_4/dna/cog_toontown_central_sz.pdna'
        self.szStorageDNAFile = 'phase_4/dna/storage_TT_sz.pdna'
        self.szHolidayDNAFile = None
        if base.cr.holidayManager.getHoliday() == HolidayType.CHRISTMAS:
            self.szHolidayDNAFile = 'phase_4/dna/winter_storage_TT_sz.pdna'
        self.telescope = None
        self.birdNoises = [
         'phase_4/audio/sfx/SZ_TC_bird1.ogg',
         'phase_4/audio/sfx/SZ_TC_bird2.ogg',
         'phase_4/audio/sfx/SZ_TC_bird3.ogg']
        return

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.geom.find('**/hill').setTransparency(TransparencyAttrib.MBinary, 1)
        if base.cr.holidayManager.getHoliday() == HolidayType.CHRISTMAS:
            self.geom.find('**/mainFloor').setTexture(loader.loadTexture('winter/maps/winter_ground.jpg'), 1)

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)

    def createSafeZone(self, dnaFile):
        loader.loadDNAFile(self.hood.dnaStore, 'phase_5/dna/storage_town.pdna')
        SafeZoneLoader.SafeZoneLoader.createSafeZone(self, dnaFile)

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)
        taskMgr.add(self.telescopeTask, 'CTCSafeZoneLoader-telescopeTask')

    def telescopeTask(self, task):
        if self.telescope:
            self.telescope.play('chan')
            task.delayTime = 12.0
            return task.again
        return task.done

    def exit(self):
        taskMgr.remove('CTCSafeZoneLoader-telescopeTask')
        SafeZoneLoader.SafeZoneLoader.exit(self)