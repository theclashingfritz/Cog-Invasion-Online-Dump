# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.DistributedTBTreasure
from lib.coginvasion.hood.DistributedTreasure import DistributedTreasure

class DistributedTBTreasure(DistributedTreasure):

    def __init__(self, cr):
        DistributedTreasure.__init__(self, cr)
        self.modelPath = 'phase_8/models/props/snowflake_treasure.bam'
        self.grabSoundPath = 'phase_4/audio/sfx/SZ_DD_treasure.ogg'