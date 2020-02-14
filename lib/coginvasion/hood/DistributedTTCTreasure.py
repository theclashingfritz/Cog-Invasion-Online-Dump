# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.DistributedTTCTreasure
from lib.coginvasion.hood.DistributedTreasure import DistributedTreasure
from lib.coginvasion.holiday.HolidayManager import HolidayType

class DistributedTTCTreasure(DistributedTreasure):
    __module__ = __name__

    def __init__(self, cr):
        DistributedTreasure.__init__(self, cr)
        self.modelPath = 'phase_4/models/props/icecream.bam'
        self.grabSoundPath = 'phase_4/audio/sfx/SZ_DD_treasure.ogg'
        if self.cr.holidayManager.getHoliday() == HolidayType.CHRISTMAS:
            self.modelPath = 'phase_6/models/karting/qbox.bam'