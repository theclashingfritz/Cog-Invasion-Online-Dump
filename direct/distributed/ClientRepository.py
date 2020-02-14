# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.ClientRepository
from ClientRepositoryBase import ClientRepositoryBase
from direct.directnotify import DirectNotifyGlobal
from MsgTypesCMU import *
from PyDatagram import PyDatagram
from PyDatagramIterator import PyDatagramIterator
from pandac.PandaModules import UniqueIdAllocator
import types

class ClientRepository(ClientRepositoryBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('ClientRepository')
    GameGlobalsId = 0
    doNotDeallocateChannel = True

    def __init__(self, dcFileNames=None, dcSuffix='', connectMethod=None, threadedNet=None):
        ClientRepositoryBase.__init__(self, dcFileNames=dcFileNames, dcSuffix=dcSuffix, connectMethod=connectMethod, threadedNet=threadedNet)
        self.setHandleDatagramsInternally(False)
        base.finalExitCallbacks.append(self.shutdown)
        self.doIdAllocator = None
        self.doIdBase = 0
        self.doIdLast = 0
        self.currentSenderId = None
        self.interestZones = []
        return

    def handleSetDoIdrange(self, di):
        self.doIdBase = di.getUint32()
        self.doIdLast = self.doIdBase + di.getUint32()
        self.doIdAllocator = UniqueIdAllocator(self.doIdBase, self.doIdLast - 1)
        self.ourChannel = self.doIdBase
        self.createReady()

    def createReady(self):
        messenger.send('createReady', taskChain='default')
        messenger.send(self.uniqueName('createReady'), taskChain='default')

    def handleRequestGenerates(self, di):
        zone = di.getUint32()
        for obj in self.doId2do.values():
            if obj.zoneId == zone:
                if self.isLocalId(obj.doId):
                    self.resendGenerate(obj)

    def resendGenerate(self, obj):
        extraFields = []
        for i in range(obj.dclass.getNumInheritedFields()):
            field = obj.dclass.getInheritedField(i)
            if field.hasKeyword('broadcast') and field.hasKeyword('ram') and not field.hasKeyword('required'):
                if field.asMolecularField():
                    continue
                extraFields.append(field.getName())

        datagram = self.formatGenerate(obj, extraFields)
        self.send(datagram)

    def handleGenerate(self, di):
        self.currentSenderId = di.getUint32()
        zoneId = di.getUint32()
        classId = di.getUint16()
        doId = di.getUint32()
        dclass = self.dclassesByNumber[classId]
        distObj = self.doId2do.get(doId)
        if distObj and distObj.dclass == dclass:
            dclass.receiveUpdateBroadcastRequired(distObj, di)
            dclass.receiveUpdateOther(distObj, di)
            return
        dclass.startGenerate()
        distObj = self.generateWithRequiredOtherFields(dclass, doId, di, 0, zoneId)
        dclass.stopGenerate()

    def allocateDoId(self):
        return self.doIdAllocator.allocate()

    def reserveDoId(self, doId):
        self.doIdAllocator.initialReserveId(doId)
        return doId

    def freeDoId(self, doId):
        self.doIdAllocator.free(doId)

    def storeObjectLocation(self, object, parentId, zoneId):
        object.parentId = parentId
        object.zoneId = zoneId

    def createDistributedObject(self, className=None, distObj=None, zoneId=0, optionalFields=None, doId=None, reserveDoId=False):
        if not className:
            if not distObj:
                self.notify.error('Must specify either a className or a distObj.')
            className = distObj.__class__.__name__
        if doId is None:
            doId = self.allocateDoId()
        else:
            if reserveDoId:
                self.reserveDoId(doId)
        dclass = self.dclassesByName.get(className)
        if not dclass:
            self.notify.error('Unknown distributed class: %s' % distObj.__class__)
        classDef = dclass.getClassDef()
        if classDef == None:
            self.notify.error('Could not create an undefined %s object.' % dclass.getName())
        if not distObj:
            distObj = classDef(self)
        if not isinstance(distObj, classDef):
            self.notify.error('Object %s is not an instance of %s' % (distObj.__class__.__name__, classDef.__name__))
        distObj.dclass = dclass
        distObj.doId = doId
        self.doId2do[doId] = distObj
        distObj.generateInit()
        distObj._retrieveCachedData()
        distObj.generate()
        distObj.setLocation(0, zoneId)
        distObj.announceGenerate()
        datagram = self.formatGenerate(distObj, optionalFields)
        self.send(datagram)
        return distObj

    def formatGenerate(self, distObj, extraFields):
        return distObj.dclass.clientFormatGenerateCMU(distObj, distObj.doId, distObj.zoneId, extraFields)

    def sendDeleteMsg(self, doId):
        datagram = PyDatagram()
        datagram.addUint16(OBJECT_DELETE_CMU)
        datagram.addUint32(doId)
        self.send(datagram)

    def sendDisconnect(self):
        if self.isConnected():
            datagram = PyDatagram()
            datagram.addUint16(CLIENT_DISCONNECT_CMU)
            self.send(datagram)
            self.notify.info('Sent disconnect message to server')
            self.disconnect()
        self.stopHeartbeat()

    def setInterestZones(self, interestZoneIds):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_SET_INTEREST_CMU)
        for zoneId in interestZoneIds:
            datagram.addUint32(zoneId)

        self.send(datagram)
        self.interestZones = interestZoneIds[:]

    def setObjectZone(self, distObj, zoneId):
        distObj.b_setLocation(0, zoneId)
        self.resendGenerate(distObj)

    def sendSetLocation(self, doId, parentId, zoneId):
        datagram = PyDatagram()
        datagram.addUint16(OBJECT_SET_ZONE_CMU)
        datagram.addUint32(doId)
        datagram.addUint32(zoneId)
        self.send(datagram)

    def sendHeartbeat(self):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_HEARTBEAT_CMU)
        self.send(datagram)
        self.lastHeartbeat = globalClock.getRealTime()
        self.considerFlush()

    def isLocalId(self, doId):
        return doId >= self.doIdBase and doId < self.doIdLast

    def haveCreateAuthority(self):
        return self.doIdLast > self.doIdBase

    def getAvatarIdFromSender(self):
        return self.currentSenderId

    def handleDatagram(self, di):
        if self.notify.getDebug():
            print 'ClientRepository received datagram:'
            di.getDatagram().dumpHex(ostream)
        msgType = self.getMsgType()
        self.currentSenderId = None
        if msgType == SET_DOID_RANGE_CMU:
            self.handleSetDoIdrange(di)
        else:
            if msgType == OBJECT_GENERATE_CMU:
                self.handleGenerate(di)
            else:
                if msgType == OBJECT_UPDATE_FIELD_CMU:
                    self.handleUpdateField(di)
                else:
                    if msgType == OBJECT_DISABLE_CMU:
                        self.handleDisable(di)
                    else:
                        if msgType == OBJECT_DELETE_CMU:
                            self.handleDelete(di)
                        else:
                            if msgType == REQUEST_GENERATES_CMU:
                                self.handleRequestGenerates(di)
                            else:
                                self.handleMessageType(msgType, di)
        self.considerHeartbeat()
        return

    def handleMessageType(self, msgType, di):
        self.notify.error('unrecognized message type %s' % msgType)

    def handleUpdateField(self, di):
        self.currentSenderId = di.getUint32()
        ClientRepositoryBase.handleUpdateField(self, di)

    def handleDisable(self, di):
        while di.getRemainingSize() > 0:
            doId = di.getUint32()
            self.disableDoId(doId)

    def handleDelete(self, di):
        doId = di.getUint32()
        self.deleteObject(doId)

    def deleteObject(self, doId):
        if doId in self.doId2do:
            obj = self.doId2do[doId]
            del self.doId2do[doId]
            obj.deleteOrDelay()
            if self.isLocalId(doId):
                self.freeDoId(doId)
        else:
            if self.cache.contains(doId):
                self.cache.delete(doId)
                if self.isLocalId(doId):
                    self.freeDoId(doId)
            else:
                self.notify.warning('Asked to delete non-existent DistObj ' + str(doId))

    def stopTrackRequestDeletedDO(self, *args):
        pass

    def sendUpdate(self, distObj, fieldName, args):
        dg = distObj.dclass.clientFormatUpdate(fieldName, distObj.doId, args)
        self.send(dg)

    def sendUpdateToChannel(self, distObj, channelId, fieldName, args):
        datagram = distObj.dclass.clientFormatUpdate(fieldName, distObj.doId, args)
        dgi = PyDatagramIterator(datagram)
        dgi.getUint16()
        dg = PyDatagram()
        dg.addUint16(CLIENT_OBJECT_UPDATE_FIELD_TARGETED_CMU)
        dg.addUint32(channelId & 4294967295L)
        dg.appendData(dgi.getRemainingBytes())
        self.send(dg)