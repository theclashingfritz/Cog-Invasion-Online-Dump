# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.AstronClientRepository
from direct.directnotify import DirectNotifyGlobal
from ClientRepositoryBase import ClientRepositoryBase
from MsgTypes import *
from direct.distributed.PyDatagram import PyDatagram
from panda3d.direct import STUint16, STUint32

class AstronClientRepository(ClientRepositoryBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('ClientRepository')
    GameGlobalsId = 0

    def __init__(self, *args, **kwargs):
        ClientRepositoryBase.__init__(self, *args, **kwargs)
        base.finalExitCallbacks.append(self.shutdown)
        self.message_handlers = {CLIENT_HELLO_RESP: self.handleHelloResp, CLIENT_EJECT: self.handleEject, 
           CLIENT_ENTER_OBJECT_REQUIRED: self.handleEnterObjectRequired, 
           CLIENT_ENTER_OBJECT_REQUIRED_OTHER: self.handleEnterObjectRequiredOther, 
           CLIENT_ENTER_OBJECT_REQUIRED_OTHER_OWNER: self.handleEnterObjectRequiredOtherOwner, 
           CLIENT_ENTER_OBJECT_REQUIRED_OWNER: self.handleEnterObjectRequiredOwner, 
           CLIENT_OBJECT_SET_FIELD: self.handleUpdateField, 
           CLIENT_OBJECT_SET_FIELDS: self.handleUpdateFields, 
           CLIENT_OBJECT_LEAVING: self.handleObjectLeaving, 
           CLIENT_OBJECT_LEAVING_OWNER: self.handleObjectLeaving, 
           CLIENT_OBJECT_LOCATION: self.handleObjectLocation, 
           CLIENT_ADD_INTEREST: self.handleAddInterest, 
           CLIENT_ADD_INTEREST_MULTIPLE: self.handleAddInterestMultiple, 
           CLIENT_REMOVE_INTEREST: self.handleRemoveInterest, 
           CLIENT_DONE_INTEREST_RESP: self.handleInterestDoneMessage}

    def handleDatagram(self, di):
        msgType = self.getMsgType()
        if msgType in self.message_handlers:
            self.message_handlers[msgType](di)
        else:
            self.notify.error('Got unknown message type %d!' % (msgType,))
        self.considerHeartbeat()

    def handleHelloResp(self, di):
        messenger.send('CLIENT_HELLO_RESP', [])

    def handleEject(self, di):
        error_code = di.get_uint16()
        reason = di.get_string()
        messenger.send('CLIENT_EJECT', [error_code, reason])

    def handleEnterObjectRequired(self, di):
        do_id = di.getArg(STUint32)
        parent_id = di.getArg(STUint32)
        zone_id = di.getArg(STUint32)
        dclass_id = di.getArg(STUint16)
        dclass = self.dclassesByNumber[dclass_id]
        self.generateWithRequiredFields(dclass, do_id, di, parent_id, zone_id)

    def handleEnterObjectRequiredOther(self, di):
        do_id = di.getArg(STUint32)
        parent_id = di.getArg(STUint32)
        zone_id = di.getArg(STUint32)
        dclass_id = di.getArg(STUint16)
        dclass = self.dclassesByNumber[dclass_id]
        self.generateWithRequiredOtherFields(dclass, do_id, di, parent_id, zone_id)

    def handleEnterObjectRequiredOtherOwner(self, di):
        do_id = di.getArg(STUint32)
        parent_id = di.getArg(STUint32)
        zone_id = di.getArg(STUint32)
        dclass_id = di.getArg(STUint16)
        dclass = self.dclassesByNumber[dclass_id]
        self.generateWithRequiredOtherFieldsOwner(dclass, do_id, di)

    def handleEnterObjectRequiredOwner(self, di):
        avatar_doId = di.getArg(STUint32)
        parentId = di.getArg(STUint32)
        zoneId = di.getArg(STUint32)
        dclass_id = di.getArg(STUint16)
        dclass = self.dclassesByNumber[dclass_id]
        self.generateWithRequiredFieldsOwner(dclass, avatar_doId, di)

    def generateWithRequiredFieldsOwner(self, dclass, doId, di):
        if doId in self.doId2ownerView:
            self.notify.error('duplicate owner generate for %s (%s)' % (
             doId, dclass.getName()))
            distObj = self.doId2ownerView[doId]
            distObj.generate()
            distObj.updateRequiredFields(dclass, di)
        else:
            if self.cacheOwner.contains(doId):
                distObj = self.cacheOwner.retrieve(doId)
                self.doId2ownerView[doId] = distObj
                distObj.generate()
                distObj.updateRequiredFields(dclass, di)
            else:
                classDef = dclass.getOwnerClassDef()
                if classDef == None:
                    self.notify.error('Could not create an undefined %s object. Have you created an owner view?' % dclass.getName())
                distObj = classDef(self)
                distObj.dclass = dclass
                distObj.doId = doId
                self.doId2ownerView[doId] = distObj
                distObj.generateInit()
                distObj.generate()
                distObj.updateRequiredFields(dclass, di)
        return distObj

    def handleUpdateFields(self, di):
        self.notify.error('CLIENT_OBJECT_SET_FIELDS not implemented!')

    def handleObjectLeaving(self, di):
        do_id = di.get_uint32()
        self.deleteObject(do_id)
        messenger.send('CLIENT_OBJECT_LEAVING', [do_id])

    def handleAddInterest(self, di):
        context = di.get_uint32()
        interest_id = di.get_uint16()
        parent_id = di.get_uint32()
        zone_id = di.get_uint32()
        messenger.send('CLIENT_ADD_INTEREST', [context, interest_id, parent_id, zone_id])

    def handleAddInterestMultiple(self, di):
        context = di.get_uint32()
        interest_id = di.get_uint16()
        parent_id = di.get_uint32()
        zone_ids = [ di.get_uint32() for i in range(0, di.get_uint16()) ]
        messenger.send('CLIENT_ADD_INTEREST_MULTIPLE', [context, interest_id, parent_id, zone_ids])

    def handleRemoveInterest(self, di):
        context = di.get_uint32()
        interest_id = di.get_uint16()
        messenger.send('CLIENT_REMOVE_INTEREST', [context, interest_id])

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

    def sendUpdate(self, distObj, fieldName, args):
        dg = distObj.dclass.clientFormatUpdate(fieldName, distObj.doId, args)
        self.send(dg)

    def sendHello(self, version_string):
        dg = PyDatagram()
        dg.add_uint16(CLIENT_HELLO)
        dg.add_uint32(self.get_dc_file().get_hash())
        dg.add_string(version_string)
        self.send(dg)

    def sendHeartbeat(self):
        datagram = PyDatagram()
        datagram.addUint16(CLIENT_HEARTBEAT)
        self.send(datagram)

    def sendAddInterest(self, context, interest_id, parent_id, zone_id):
        dg = PyDatagram()
        dg.add_uint16(CLIENT_ADD_INTEREST)
        dg.add_uint32(context)
        dg.add_uint16(interest_id)
        dg.add_uint32(parent_id)
        dg.add_uint32(zone_id)
        self.send(dg)

    def sendAddInterestMultiple(self, context, interest_id, parent_id, zone_ids):
        dg = PyDatagram()
        dg.add_uint16(CLIENT_ADD_INTEREST_MULTIPLE)
        dg.add_uint32(context)
        dg.add_uint16(interest_id)
        dg.add_uint32(parent_id)
        dg.add_uint16(len(zone_ids))
        for zone_id in zone_ids:
            dg.add_uint32(zone_id)

        self.send(dg)

    def sendRemoveInterest(self, context, interest_id):
        dg = PyDatagram()
        dg.add_uint16(CLIENT_REMOVE_INTEREST)
        dg.add_uint32(context)
        dg.add_uint16(interest_id)
        self.send(dg)

    def lostConnection(self):
        messenger.send('LOST_CONNECTION')

    def disconnect(self):
        for do_id in self.doId2do.keys():
            self.deleteObject(do_id)

        ClientRepositoryBase.disconnect(self)