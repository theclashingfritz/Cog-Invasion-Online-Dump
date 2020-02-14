# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.TownLoader
from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.fsm.StateData import StateData
from direct.fsm.State import State
from direct.fsm.ClassicFSM import ClassicFSM
from direct.interval.IntervalGlobal import *
from QuietZoneState import QuietZoneState
import LinkTunnel, ZoneUtil, ToonInterior
from lib.coginvasion.cogoffice import CogOfficeInterior

class TownLoader(StateData):
    notify = directNotify.newCategory('TownLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        self.hood = hood
        self.parentFSMState = parentFSMState
        StateData.__init__(self, doneEvent)
        self.fsm = ClassicFSM('TownLoader', [State('start', self.enterStart, self.exitStart, ['quietZone', 'street']),
         State('street', self.enterStreet, self.exitStreet, ['quietZone']),
         State('toonInterior', self.enterToonInterior, self.exitToonInterior, ['quietZone']),
         State('suitInterior', self.enterSuitInterior, self.exitSuitInterior, ['quietZone']),
         State('quietZone', self.enterQuietZone, self.exitQuietZone, ['street', 'toonInterior', 'suitInterior']),
         State('final', self.enterFinal, self.exitFinal, ['start'])], 'start', 'final')
        self.branchZone = None
        self.canonicalBranchZone = None
        self.placeDoneEvent = 'placeDone'
        self.linkTunnels = []
        self.place = None
        return

    def findAndMakeLinkTunnels(self, requestStatus):
        for tunnel in self.geom.findAllMatches('**/*linktunnel*'):
            dnaRootStr = tunnel.getName()
            zone = LinkTunnel.getZoneFromDNARootStr(dnaRootStr)
            zone = LinkTunnel.maybeFixZone(zone)
            tunnelClass = LinkTunnel.getRecommendedTunnelClassFromZone(zone)
            link = tunnelClass(tunnel, dnaRootStr)
            self.linkTunnels.append(link)

    def load(self, zoneId):
        StateData.load(self)
        self.zoneId = zoneId
        self.branchZone = ZoneUtil.getBranchZone(zoneId)
        self.canonicalBranchZone = ZoneUtil.getCanonicalBranchZone(zoneId)
        self.music = base.loadMusic(self.musicFile)
        self.interiorMusic = base.loadMusic(self.interiorMusicFile)

    def unload(self):
        self.parentFSMState.removeChild(self.fsm)
        del self.parentFSMState
        del self.fsm
        del self.streetClass
        self.landmarkBlocks.removeNode()
        del self.landmarkBlocks
        self.hood.dnaStore.resetSuitPoints()
        self.hood.dnaStore.resetBattleCells()
        del self.hood
        del self.nodeDict
        del self.zoneDict
        del self.fadeInDict
        del self.fadeOutDict
        del self.nodeList
        self.geom.removeNode()
        del self.geom
        del self.music
        del self.interiorMusic
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        StateData.unload(self)

    def enter(self, requestStatus):
        StateData.enter(self)
        self.findAndMakeLinkTunnels(requestStatus)
        self.fsm.enterInitialState()
        self.setState(requestStatus['where'], requestStatus)

    def exit(self):
        self.fsm.requestFinalState()
        self.ignoreAll()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        StateData.exit(self)

    def setState(self, state, requestStatus):
        self.fsm.request(state, [requestStatus])

    def enterStart(self):
        pass

    def exitStart(self):
        pass

    def enterStreet(self, requestStatus):
        self.acceptOnce(self.placeDoneEvent, self.streetDone)
        self.place = self.streetClass(self, self.fsm, self.placeDoneEvent)
        self.place.load()

    def exitStreet(self):
        self.ignore(self.placeDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        base.cr.playGame.setPlace(self.place)
        return

    def streetDone(self):
        self.requestStatus = self.place.doneStatus
        status = self.place.doneStatus
        if status['loader'] == 'townLoader' and ZoneUtil.getBranchZone(status['zoneId']) == self.branchZone and status['shardId'] == None or status['how'] == 'doorOut' or status['where'] == 'suitInterior':
            self.fsm.request('quietZone', [status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)
        return

    def enterToonInterior(self, requestStatus):
        self.acceptOnce(self.placeDoneEvent, self.handleToonInteriorDone)
        self.place = ToonInterior.ToonInterior(self, self.fsm, self.placeDoneEvent)
        self.place.load()

    def exitToonInterior(self):
        self.ignore(self.placeDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        base.cr.playGame.setPlace(self.place)
        return

    def enterSuitInterior(self, requestStatus):
        self.acceptOnce(self.placeDoneEvent, self.handleSuitInteriorDone)
        self.place = CogOfficeInterior.CogOfficeInterior(self, self.fsm, self.placeDoneEvent)
        self.place.load()

    def exitSuitInterior(self):
        self.ignore(self.placeDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        base.cr.playGame.setPlace(self.place)
        return

    def enterThePlace(self, requestStatus):
        base.cr.playGame.setPlace(self.place)
        if self.place is not None:
            self.place.enter(requestStatus)
        return

    def handleToonInteriorDone(self):
        status = self.place.doneStatus
        if status['loader'] == 'townLoader' and ZoneUtil.getBranchZone(status['zoneId']) == self.branchZone and status['shardId'] == None or status['how'] == 'doorOut':
            self.fsm.request('quietZone', [status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)
        return

    def handleSuitInteriorDone(self):
        self.handleToonInteriorDone()

    def enterQuietZone(self, requestStatus):
        self.fsm.request(requestStatus['where'], [requestStatus], exitCurrent=0)
        self.quietZoneDoneEvent = uniqueName('quietZoneDone')
        self.acceptOnce(self.quietZoneDoneEvent, self.handleQuietZoneDone)
        self.quietZoneStateData = QuietZoneState(self.quietZoneDoneEvent)
        self.quietZoneStateData.load()
        self.quietZoneStateData.enter(requestStatus)

    def exitQuietZone(self):
        self.ignore(self.quietZoneDoneEvent)
        del self.quietZoneDoneEvent
        self.quietZoneStateData.exit()
        self.quietZoneStateData.unload()
        self.quietZoneStateData = None
        return

    def handleQuietZoneDone(self):
        status = self.quietZoneStateData.getRequestStatus()
        self.exitQuietZone()
        self.enterThePlace(status)

    def enterFinal(self):
        pass

    def exitFinal(self):
        pass

    def createHood(self, dnaFile, loadStorage=1):
        if loadStorage:
            loader.loadDNAFile(self.hood.dnaStore, 'phase_5/dna/storage_town.pdna')
            loader.loadDNAFile(self.hood.dnaStore, self.townStorageDNAFile)
        node = loader.loadDNAFile(self.hood.dnaStore, dnaFile)
        if node.getNumParents() == 1:
            self.geom = NodePath(node.getParent(0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.makeDictionaries(self.hood.dnaStore)
        self.reparentLandmarkBlockNodes()
        self.renameFloorPolys(self.nodeList)
        gsg = base.win.getGsg()
        if gsg:
            self.geom.prepareScene(gsg)
        self.geom.flattenLight()
        self.geom.setName('town_top_level')

    def reparentLandmarkBlockNodes(self):
        bucket = self.landmarkBlocks = hidden.attachNewNode('landmarkBlocks')
        npc = self.geom.findAllMatches('**/sb*:*_landmark_*_DNARoot')
        for i in xrange(npc.getNumPaths()):
            nodePath = npc.getPath(i)
            nodePath.wrtReparentTo(bucket)

        npc = self.geom.findAllMatches('**/sb*:*animated_building*_DNARoot')
        for i in xrange(npc.getNumPaths()):
            nodePath = npc.getPath(i)
            nodePath.wrtReparentTo(bucket)

    def makeDictionaries(self, dnaStore):
        self.nodeDict = {}
        self.zoneDict = {}
        self.zoneVisDict = {}
        self.nodeList = []
        self.fadeInDict = {}
        self.fadeOutDict = {}
        a1 = Vec4(1, 1, 1, 1)
        a0 = Vec4(1, 1, 1, 0)
        numVisGroups = dnaStore.getNumDNAVisGroupsAI()
        for i in xrange(numVisGroups):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            visGroup = dnaStore.getDNAVisGroupAI(i)
            groupName = base.cr.hoodMgr.extractGroupName(groupFullName)
            zoneId = int(groupName)
            zoneId = ZoneUtil.getTrueZoneId(zoneId, self.zoneId)
            groupNode = self.geom.find('**/' + groupFullName)
            if groupNode.isEmpty():
                continue
            else:
                if ':' in groupName:
                    groupName = '%s%s' % (zoneId, groupName[groupName.index(':'):])
                else:
                    groupName = '%s' % zoneId
                groupNode.setName(groupName)
            groupNode.flattenMedium()
            self.nodeDict[zoneId] = []
            self.nodeList.append(groupNode)
            self.zoneDict[zoneId] = groupNode
            visibles = []
            for i in xrange(visGroup.getNumVisibles()):
                visibles.append(int(visGroup.get_visible(i)))

            visibles.append(ZoneUtil.getBranchZone(zoneId))
            self.zoneVisDict[zoneId] = visibles
            fadeDuration = 0.5
            self.fadeOutDict[groupNode] = Sequence(Func(groupNode.setTransparency, 1), LerpColorScaleInterval(groupNode, fadeDuration, a0, startColorScale=a1), Func(groupNode.clearColorScale), Func(groupNode.clearTransparency), Func(groupNode.stash), name='fadeZone-' + str(zoneId), autoPause=1)
            self.fadeInDict[groupNode] = Sequence(Func(groupNode.unstash), Func(groupNode.setTransparency, 1), LerpColorScaleInterval(groupNode, fadeDuration, a1, startColorScale=a0), Func(groupNode.clearColorScale), Func(groupNode.clearTransparency), name='fadeZone-' + str(zoneId), autoPause=1)

        for i in xrange(numVisGroups):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            zoneId = int(base.cr.hoodMgr.extractGroupName(groupFullName))
            zoneId = ZoneUtil.getTrueZoneId(zoneId, self.zoneId)
            for j in xrange(dnaStore.getNumVisiblesInDNAVisGroup(i)):
                visName = dnaStore.getVisibleName(i, j)
                groupName = base.cr.hoodMgr.extractGroupName(visName)
                nextZoneId = int(groupName)
                nextZoneId = ZoneUtil.getTrueZoneId(nextZoneId, self.zoneId)
                visNode = self.zoneDict[nextZoneId]
                self.nodeDict[zoneId].append(visNode)

        self.hood.dnaStore.resetPlaceNodes()
        self.hood.dnaStore.resetDNAGroups()
        self.hood.dnaStore.resetDNAVisGroups()
        self.hood.dnaStore.resetDNAVisGroupsAI()

    def renameFloorPolys(self, nodeList):
        for i in nodeList:
            collNodePaths = i.findAllMatches('**/+CollisionNode')
            numCollNodePaths = collNodePaths.getNumPaths()
            visGroupName = i.node().getName()
            for j in xrange(numCollNodePaths):
                collNodePath = collNodePaths.getPath(j)
                bitMask = collNodePath.node().getIntoCollideMask()
                if bitMask.getBit(1):
                    collNodePath.node().setName(visGroupName)