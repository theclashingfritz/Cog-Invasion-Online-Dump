# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.DistributedObjectOV
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectBase import DistributedObjectBase
ESNew = 1
ESDeleted = 2
ESDisabling = 3
ESDisabled = 4
ESGenerating = 5
ESGenerated = 6

class DistributedObjectOV(DistributedObjectBase):
    notify = directNotify.newCategory('DistributedObjectOV')

    def __init__(self, cr):
        try:
            self.DistributedObjectOV_initialized
        except:
            self.DistributedObjectOV_initialized = 1
            DistributedObjectBase.__init__(self, cr)
            self.activeState = ESNew

    def getDelayDeleteCount(self):
        return 0

    def deleteOrDelay(self):
        self.disableAnnounceAndDelete()

    def disableAnnounceAndDelete(self):
        self.disableAndAnnounce()
        self.delete()

    def disableAndAnnounce(self):
        if self.activeState != ESDisabled:
            self.activeState = ESDisabling
            messenger.send(self.uniqueName('disable'))
            self.disable()

    def announceGenerate(self):
        pass

    def disable(self):
        if self.activeState != ESDisabled:
            self.activeState = ESDisabled

    def isDisabled(self):
        return self.activeState < ESGenerating

    def isGenerated(self):
        return self.activeState == ESGenerated

    def delete(self):
        try:
            self.DistributedObjectOV_deleted
        except:
            self.DistributedObjectOV_deleted = 1
            self.cr = None
            self.dclass = None

        return

    def generate(self):
        self.activeState = ESGenerating

    def generateInit(self):
        self.activeState = ESGenerating

    def getDoId(self):
        return self.doId

    def postGenerateMessage(self):
        if self.activeState != ESGenerated:
            self.activeState = ESGenerated
            messenger.send(self.uniqueName('generate'), [self])

    def updateRequiredFields(self, dclass, di):
        dclass.receiveUpdateBroadcastRequired(self, di)
        self.announceGenerate()
        self.postGenerateMessage()

    def updateAllRequiredFields(self, dclass, di):
        dclass.receiveUpdateAllRequired(self, di)
        self.announceGenerate()
        self.postGenerateMessage()

    def updateRequiredOtherFields(self, dclass, di):
        dclass.receiveUpdateBroadcastRequiredOwner(self, di)
        self.announceGenerate()
        self.postGenerateMessage()
        dclass.receiveUpdateOther(self, di)

    def getCacheable(self):
        return False

    def sendUpdate(self, fieldName, args=[], sendToId=None):
        if self.cr:
            dg = self.dclass.clientFormatUpdate(fieldName, sendToId or self.doId, args)
            self.cr.send(dg)
        else:
            self.notify.warning('sendUpdate failed, because self.cr is not set')

    def taskName(self, taskString):
        return '%s-%s-OV' % (taskString, self.getDoId())

    def uniqueName(self, idString):
        return '%s-%s-OV' % (idString, self.getDoId())