# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.CogBattleGlobals
from lib.coginvasion.globals.CIGlobals import *
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.hood import ZoneUtil
MAX_TURRETS = 3
HoodId2HoodIndex = {BattleTTC: 0, 
   TheBrrrgh: 1, 
   DonaldsDreamland: 2, 
   MinniesMelodyland: 3, 
   DaisyGardens: 4, 
   DonaldsDock: 5}
HoodIndex2HoodName = {v:k for k, v in HoodId2HoodIndex.items()}
HoodIndex2HoodId = None
if HoodIndex2HoodId == None:
    HoodIndex2HoodId = {}
    for hoodName in HoodId2HoodIndex.keys():
        index = HoodId2HoodIndex[hoodName]
        zone = ZoneUtil.getZoneId(hoodName)
        HoodIndex2HoodId[index] = zone

hi2hi = HoodId2HoodIndex
HoodIndex2LevelRange = {hi2hi[BattleTTC]: list(range(1, 4)), 
   hi2hi[TheBrrrgh]: list(range(5, 10)), 
   hi2hi[DonaldsDreamland]: list(range(6, 10)), 
   hi2hi[MinniesMelodyland]: range(2, 7), 
   hi2hi[DaisyGardens]: range(2, 7), 
   hi2hi[DonaldsDock]: range(2, 7)}
HoodId2WantBattles = {BattleTTC: True, 
   TheBrrrgh: True, 
   DonaldsDreamland: False, 
   MinniesMelodyland: False, 
   DaisyGardens: False, 
   DonaldsDock: False}
HoodIndex2TotalCogs = {hi2hi[BattleTTC]: 45, 
   hi2hi[TheBrrrgh]: 45, 
   hi2hi[DonaldsDreamland]: 50, 
   hi2hi[MinniesMelodyland]: 45, 
   hi2hi[DaisyGardens]: 45, 
   hi2hi[DonaldsDock]: 45}
WaiterHoodIndex = hi2hi[TheBrrrgh]
SkeletonHoodIndex = 10