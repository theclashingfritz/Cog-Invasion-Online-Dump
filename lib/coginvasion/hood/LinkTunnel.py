# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.LinkTunnel
from direct.showbase.DirectObject import DirectObject
import ZoneUtil
from lib.coginvasion.globals import CIGlobals
CollisionName = 'tunnel_trigger'
TunnelNode2LinkTunnel = {}
zonesTunnelsHaveBeenMadeIn = []

def __handleTunnelCollision(entry):
    intoNP = entry.getIntoNodePath()
    parent = intoNP.getParent()
    linkTunnel = TunnelNode2LinkTunnel.get(parent)
    if linkTunnel:
        zoneId = linkTunnel.data['zoneId']
        if base.cr.playGame.getPlace():
            base.cr.playGame.getPlace().fsm.request('tunnelIn', [linkTunnel])


def globalAcceptCollisions():
    base.acceptOnce('enter' + CollisionName, __handleTunnelCollision)


def globalIgnoreCollisions():
    base.ignore('enter' + CollisionName)


def getTunnelThatGoesToZone(zoneId):
    for linkTunnel in TunnelNode2LinkTunnel.values():
        if linkTunnel.data['zoneId'] == zoneId:
            return linkTunnel


def getZoneFromDNARootStr(string):
    for segment in string.split('_'):
        if segment.isdigit():
            return int(segment)


def maybeFixZone(zone):
    zone = str(zone)
    if zone[2] != '0':
        zone = zone[0] + zone[1]
        zone += '00'
    return int(zone)


class LinkTunnel(DirectObject):

    def __init__(self, tunnel, dnaRootStr):
        self.tunnel = tunnel
        TunnelNode2LinkTunnel[tunnel] = self
        self.dnaRootStr = dnaRootStr
        self.data = {}
        self.toZone = 0

    def cleanup(self):
        del TunnelNode2LinkTunnel[self.tunnel]
        del self.dnaRootStr
        del self.data
        del self.toZone


class SafeZoneLinkTunnel(LinkTunnel):
    ToZoneLastTwo = '00'

    def __init__(self, tunnel, dnaRootStr):
        LinkTunnel.__init__(self, tunnel, dnaRootStr)
        self.inPivotPoint = (45, 91, 6.7)
        self.outPivotPoint = (35, 91, 6.7)
        self.inPivotStartHpr = (0, 0, 0)
        self.inPivotEndHpr = (-90, 0, 0)
        self.inPivotStartX = 45
        self.inPivotEndX = 35
        self.outPivotStartHpr = (90, 0, 0)
        self.outPivotEndHpr = (180, 0, 0)
        self.outPivotStartX = 35
        self.outPivotEndX = 45
        self.toonOutPos = (-15, -5, 0)
        self.toonOutHpr = (180, 0, 0)
        self.camPos = (60, 115.0, 17.5)
        self.camHpr = (180, 345.0, 0)
        toZoneFirstTwo = None
        for segment in dnaRootStr.split('_'):
            if segment.isdigit():
                toZoneFirstTwo = segment[:2]
                toZone = toZoneFirstTwo + self.ToZoneLastTwo
                self.toZone = int(segment)

        self.data['zoneId'] = self.toZone
        return


class StreetLinkTunnel(LinkTunnel):

    def __init__(self, tunnel, dnaRootStr):
        LinkTunnel.__init__(self, tunnel, dnaRootStr)
        self.outPivotPoint = (45, 5, 0)
        self.inPivotPoint = (35, 5, 0)
        self.outPivotStartHpr = (-90, 0, 0)
        self.outPivotEndHpr = (0, 0, 0)
        self.outPivotStartX = 45
        self.outPivotEndX = 35
        self.toonOutPos = (-15, -5, 0)
        self.toonOutHpr = (180, 0, 0)
        self.inPivotStartHpr = (0, 0, 0)
        self.inPivotEndHpr = (-90, 0, 0)
        self.inPivotStartX = 35
        self.inPivotEndX = 45
        self.camPos = (19.7, -20.0, 10.0)
        self.camHpr = (0, 345.96, 0)
        for segment in dnaRootStr.split('_'):
            if segment.isdigit():
                self.toZone = int(segment)

        self.data['zoneId'] = self.toZone


class NeighborhoodLinkTunnel(LinkTunnel):
    ToZoneLastTwo = '00'

    def __init__(self, tunnel, dnaRootStr):
        LinkTunnel.__init__(self, tunnel, dnaRootStr)
        self.outPivotPoint = (25, 5, 0)
        self.inPivotPoint = (15, 5, 0)
        self.outPivotStartHpr = (-90, 0, 0)
        self.outPivotEndHpr = (0, 0, 0)
        self.outPivotStartX = 25
        self.outPivotEndX = 15
        self.toonOutPos = (-15, -5, 0)
        self.toonOutHpr = (180, 0, 0)
        self.inPivotStartHpr = (0, 0, 0)
        self.inPivotEndHpr = (-90, 0, 0)
        self.inPivotStartX = 15
        self.inPivotEndX = 25
        self.camPos = (0, -21.0, 8.0)
        self.camHpr = (0, 349.7, 0)
        for segment in dnaRootStr.split('_'):
            if segment.isdigit():
                self.toZone = int(segment)

        self.data['zoneId'] = self.toZone
        self.data['hoodId'] = ZoneUtil.getHoodId(self.toZone, 1)


def getRecommendedTunnelClassFromZone(zone):
    if ZoneUtil.getWhereName(zone) == 'playground':
        return StreetLinkTunnel
    if ZoneUtil.getWhereName(zone) == 'street':
        if ZoneUtil.getHoodId(zone, street=1) == base.cr.playGame.hood.id:
            return SafeZoneLinkTunnel
        return NeighborhoodLinkTunnel