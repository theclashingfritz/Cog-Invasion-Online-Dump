# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.DDSafeZoneLoader
from lib.coginvasion.holiday.HolidayManager import HolidayType
import SafeZoneLoader, DDPlayground

class DDSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playground = DDPlayground.DDPlayground
        self.pgMusicFilename = 'phase_6/audio/bgm/DD_nbrhood.mid'
        self.interiorMusicFilename = 'phase_6/audio/bgm/DD_SZ_activity.mid'
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
        self.dnaFile = 'phase_6/dna/donalds_dock_sz.pdna'
        self.szStorageDNAFile = 'phase_6/dna/storage_DD_sz.pdna'
        self.szHolidayDNAFile = None
        if base.cr.holidayManager.getHoliday() == HolidayType.CHRISTMAS:
            self.szHolidayDNAFile = 'phase_6/dna/winter_storage_DD_sz.pdna'
        self.telescope = None
        self.birdNoise = 'phase_6/audio/sfx/SZ_DD_Seagull.ogg'
        return

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        hq = self.geom.find('**/*toon_landmark_hqDD*')
        hq.find('**/doorFrameHoleLeft_0').stash()
        hq.find('**/doorFrameHoleRight_0').stash()
        hq.find('**/doorFrameHoleLeft_1').stash()
        hq.find('**/doorFrameHoleRight_1').stash()

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)
        self.hood.setWhiteFog()

    def exit(self):
        self.hood.setNoFog()
        SafeZoneLoader.SafeZoneLoader.exit(self)