# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.uber.NameServicesManager
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify.DirectNotifyGlobal import directNotify

class NameServicesManager(DistributedObjectGlobal):
    notify = directNotify.newCategory('NameServicesManager')

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)
        self.requestedNames = []
        self.requestCompleteEventName = 'NameServicesManager-RequestComplete'

    def d_requestName(self, name, avId):
        self.sendUpdate('requestName', [name, avId])

    def d_requestNameData(self):
        self.sendUpdate('requestNameData', [])
        print 'Requesting Data...'

    def nameDataRequest(self, names, avatarIds, accIds, dates, statuses):
        print 'Got a reply.'
        for i in xrange(len(names)):
            request = {}
            request['name'] = str(names[i])
            request['avId'] = int(avatarIds[i])
            request['accId'] = int(accIds[i])
            request['date'] = str(dates[i])
            request['status'] = int(statuses[i])
            self.requestedNames.append(request)

        messenger.send(self.requestCompleteEventName)

    def getNameRequests(self):
        return self.requestedNames

    def getRequestCompleteName(self):
        return self.requestCompleteEventName