# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogoffice.SuitBuildingGlobals
from ElevatorConstants import *
from lib.coginvasion.globals import CIGlobals
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8
SPAWN_TIME_RANGE = (300, 600)
GUARDS_PER_SECTION = 0
LEVEL_RANGE = 1
BOSS_LEVEL_RANGE = 2
buildingInfo = {CIGlobals.ToontownCentral: {GUARDS_PER_SECTION: (0, 2), LEVEL_RANGE: (1, 4), 
                               BOSS_LEVEL_RANGE: (2, 4)}, 
   CIGlobals.DonaldsDock: {GUARDS_PER_SECTION: (1, 3), LEVEL_RANGE: (2, 6), 
                           BOSS_LEVEL_RANGE: (3, 6)}, 
   CIGlobals.DaisyGardens: {GUARDS_PER_SECTION: (2, 3), LEVEL_RANGE: (2, 6), 
                            BOSS_LEVEL_RANGE: (4, 6)}, 
   CIGlobals.MinniesMelodyland: {GUARDS_PER_SECTION: (2, 4), LEVEL_RANGE: (3, 6), 
                                 BOSS_LEVEL_RANGE: (4, 6)}, 
   CIGlobals.TheBrrrgh: {GUARDS_PER_SECTION: (3, 4), LEVEL_RANGE: (6, 11), 
                         BOSS_LEVEL_RANGE: (8, 11)}, 
   CIGlobals.DonaldsDreamland: {GUARDS_PER_SECTION: (3, 4), LEVEL_RANGE: (8, 11), 
                                BOSS_LEVEL_RANGE: (8, 12)}}
buildingMinMax = {CIGlobals.SillyStreet: (0, 3), 
   CIGlobals.PunchlinePlace: (0, 3), 
   CIGlobals.LoopyLane: (0, 3), 
   CIGlobals.BarnacleBoulevard: (1, 5), 
   CIGlobals.SeaweedStreet: (1, 5), 
   CIGlobals.LighthouseLane: (1, 5), 
   CIGlobals.ElmStreet: (2, 6), 
   CIGlobals.MapleStreet: (2, 6), 
   CIGlobals.OakStreet: (2, 6), 
   CIGlobals.AltoAvenue: (3, 7), 
   CIGlobals.BaritoneBoulevard: (3, 7), 
   CIGlobals.TenorTerrace: (3, 7), 
   CIGlobals.WalrusWay: (5, 10), 
   CIGlobals.SleetStreet: (5, 10), 
   CIGlobals.PolarPlace: (5, 10), 
   CIGlobals.LullabyLane: (6, 12), 
   CIGlobals.PajamaPlace: (6, 12)}
buildingChances = {CIGlobals.SillyStreet: 2.0, 
   CIGlobals.LoopyLane: 2.0, 
   CIGlobals.PunchlinePlace: 2.0, 
   CIGlobals.BarnacleBoulevard: 75.0, 
   CIGlobals.SeaweedStreet: 75.0, 
   CIGlobals.LighthouseLane: 75.0, 
   CIGlobals.ElmStreet: 90.0, 
   CIGlobals.MapleStreet: 90.0, 
   CIGlobals.OakStreet: 90.0, 
   CIGlobals.AltoAvenue: 95.0, 
   CIGlobals.BaritoneBoulevard: 95.0, 
   CIGlobals.TenorTerrace: 95.0, 
   CIGlobals.WalrusWay: 100.0, 
   CIGlobals.SleetStreet: 100.0, 
   CIGlobals.PolarPlace: 100.0, 
   CIGlobals.LullabyLane: 100.0, 
   CIGlobals.PajamaPlace: 100.0}
floorNumberChances = {1: [
     range(1, 101), [], [], [], []], 
   2: [
     range(26, 101), range(1, 26), [], [], []], 
   3: [
     range(1, 51), range(51, 101), [], [], []], 
   4: [
     range(51, 76), range(1, 51), range(75, 101), [], []], 
   5: [
     range(91, 96), range(76, 91), range(1, 76), range(96, 101), []], 
   6: [[], range(96, 101), range(1, 51), range(51, 96), []], 7: [[], [], range(1, 26), range(26, 76), range(76, 101)], 8: [[], [], range(66, 101), range(1, 51), range(51, 66)], 9: [[], [], range(96, 101), range(1, 31), range(31, 96)], 10: [[], [], range(86, 101), range(56, 86), range(1, 56)], 11: [[], [], range(91, 101), range(61, 91), range(1, 61)], 12: [[], [], [], range(81, 101), range(1, 81)]}