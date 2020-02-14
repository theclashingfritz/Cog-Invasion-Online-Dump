# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.friends.FriendRequestManager
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.DirectObject import DirectObject
from lib.coginvasion.gui.Dialog import GlobalDialog

class FriendRequestManager(DirectObject):
    notify = directNotify.newCategory('FriendRequestManager')
    MessageFriendRequest = '%s would like to be your friend. Do you want to be friends with %s?'

    def __init__(self):
        DirectObject.__init__(self)
        self.friendRequests = {}

    def cleanup(self):
        self.friendRequests = None
        return

    def iAcceptedRequest(self, requestId):
        self.cleanupRequest(requestId)
        base.cr.friendsManager.d_iAcceptedFriendRequest(requestId)

    def iRejectedRequest(self, requestId):
        self.cleanupRequest(requestId)
        base.cr.friendsManager.d_iRejectedFriendRequest(requestId)

    def watch(self):
        self.accept('newFriendRequest', self.__newFriendRequest)
        self.accept('friendRequestCancelled', self.cleanupRequest)

    def __newFriendRequest(self, requester, name, dna):
        request = GlobalDialog(message=self.MessageFriendRequest % (name, name), style=1, text_wordwrap=12, doneEvent='friendRequestDone-%d' % requester, extraArgs=[requester])
        self.friendRequests[requester] = request
        self.acceptOnce('friendRequestDone-%d' % requester, self.handleFriendRequestChoice)

    def handleFriendRequestChoice(self, requester):
        value = self.friendRequests[requester].getValue()
        if value:
            self.iAcceptedRequest(requester)
        else:
            self.iRejectedRequest(requester)

    def cleanupRequest(self, requester):
        request = self.friendRequests.get(requester)
        if request:
            request.cleanup()
            del self.friendRequests[requester]