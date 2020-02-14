# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.ZoneUtil
from lib.coginvasion.globals.CIGlobals import *

def isInInterior(zoneId):
    return int(str(zoneId)[1:]) >= 500 and int(str(zoneId)[1:]) <= 999


def getWhereName(zoneId):
    if str(zoneId)[-3:] == '000':
        return 'playground'
    if int(str(zoneId)[-3:]) < 400:
        return 'street'
    if isInInterior(zoneId):
        return 'toonInterior'
    return 'street'


def getBranchZone(zoneId):
    branchZone = zoneId - zoneId % 100
    if zoneId % 1000 >= 500:
        branchZone -= 500
    return branchZone


def getLoaderName(zoneId):
    if str(getBranchZone(zoneId))[-3:] == '000':
        return 'safeZoneLoader'
    if int(str(getBranchZone(zoneId))[-3:]) >= 100 and int(str(getBranchZone(zoneId))[-3:]) <= 999:
        return 'townLoader'
    return
    return


def isStreetInSameHood(zoneId):
    return str(zoneId)[0] == str(base.localAvatar.zoneId)[0]


def isStreet(zoneId):
    return getWhereName(zoneId) == 'street'


def getCanonicalBranchZone(zoneId):
    return getBranchZone(getCanonicalZoneId(zoneId))


def getCanonicalZoneId(zoneId):
    zoneId = zoneId % 2000
    if zoneId < 1000:
        zoneId = zoneId + ToontownCentralId
    else:
        zoneId = zoneId - 1000 + GoofySpeedwayId
    return zoneId


def getTrueZoneId(zoneId, currentZoneId):
    hoodId = getHoodId(zoneId, street=1)
    offset = currentZoneId - currentZoneId % 2000
    if hoodId == ToontownCentral and game.process != 'client' or game.process == 'client' and hoodId == ToontownCentral:
        return zoneId - ToontownCentralId + offset
    if hoodId == GoofySpeedway:
        return zoneId - GoofySpeedwayId + offset + 1000
    return zoneId


def getHoodId(zoneId, street=0):
    if street:
        if str(zoneId)[0] == '1' and len(str(zoneId)) == 4:
            return DonaldsDock
        if str(zoneId)[:2] == '10' and len(str(zoneId)) == 5:
            return MinigameArea
        if str(zoneId)[:2] == '12' and len(str(zoneId)) == 5:
            return CogTropolis
        if str(zoneId)[0] == '2':
            return ToontownCentral
        if str(zoneId)[0] == '3':
            return TheBrrrgh
        if str(zoneId)[0] == '4':
            return MinniesMelodyland
        if str(zoneId)[0] == '5':
            return DaisyGardens
        if str(zoneId)[0] == '9':
            return DonaldsDreamland
    else:
        if zoneId < DynamicZonesBegin:
            return ZoneId2Hood.get(zoneId, None)
    return


def getZoneId(hoodId):
    if hoodId == BattleTTC:
        hoodId = ToontownCentral
    return Hood2ZoneId[hoodId]