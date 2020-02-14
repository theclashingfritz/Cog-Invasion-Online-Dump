# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.NetMessenger
from cPickle import dumps, loads
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
from direct.showbase.Messenger import Messenger

class NetMessenger(Messenger):
    notify = DirectNotifyGlobal.directNotify.newCategory('NetMessenger')

    def __init__(self, air, baseChannel=20000, baseMsgType=20000):
        Messenger.__init__(self)
        self.air = air
        self.baseChannel = baseChannel
        self.baseMsgType = baseMsgType
        self.__message2type = {}
        self.__type2message = {}
        self.__message2channel = {}

    def clear(self):
        Messenger.clear(self)

    def register(self, code, message):
        channel = self.baseChannel + code
        msgType = self.baseMsgType + code
        if message in self.__message2type:
            self.notify.error('Tried to register message %s twice!' % message)
            return
        self.__message2type[message] = msgType
        self.__type2message[msgType] = message
        self.__message2channel[message] = channel

    def prepare(self, message, sentArgs=[]):
        if message not in self.__message2type:
            self.notify.error('Tried to send unregistered message %s!' % message)
            return
        datagram = PyDatagram()
        datagram.addUint8(1)
        datagram.addChannel(self.__message2channel[message])
        datagram.addChannel(self.air.ourChannel)
        messageType = self.__message2type[message]
        datagram.addUint16(messageType)
        datagram.addString(str(dumps(sentArgs)))
        return datagram

    def accept(self, message, *args):
        if message not in self.__message2channel:
            self.notify.error('Tried to accept unregistered message %s!' % message)
            return
        anyAccepting = bool(self.whoAccepts(message))
        if not anyAccepting:
            self.air.registerForChannel(self.__message2channel[message])
        Messenger.accept(self, message, *args)

    def send(self, message, sentArgs=[]):
        datagram = self.prepare(message, sentArgs)
        self.air.send(datagram)
        Messenger.send(self, message, sentArgs=sentArgs)

    def handle(self, msgType, di):
        if msgType not in self.__type2message:
            self.notify.warning('Received unknown message: %d' % msgType)
            return
        message = self.__type2message[msgType]
        sentArgs = loads(di.getString())
        if type(sentArgs) != list:
            self.notify.warning('Received non-list item in %s message: %r' % (
             message, sentArgs))
            return
        Messenger.send(self, message, sentArgs=sentArgs)