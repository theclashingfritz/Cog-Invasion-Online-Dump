# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.toon.ToonTalker
from lib.coginvasion.globals import CIGlobals
from panda3d.core import BillboardEffect, Vec3, Point3
from lib.coginvasion.toon.LabelScaler import LabelScaler
from direct.directnotify.DirectNotify import DirectNotify
from lib.coginvasion.toon.ChatBalloon import ChatBalloon
import random, math
notify = DirectNotify().newCategory('ToonTalker')

class ToonTalker:
    THOUGHT_PREFIX = '.'
    LENGTH_FACTOR = 0.6
    MIN_LENGTH = 5
    MAX_LENGTH = 20

    def __init__(self):
        self.avatar = None
        self.nametag = None
        self.autoClearChat = True
        return

    def setAutoClearChat(self, flag):
        self.autoClearChat = flag

    def setAvatar(self, avatar, nametag):
        self.avatar = avatar
        self.nametag = nametag

    def setChatAbsolute(self, chatString=None):
        if not chatString or chatString.isspace() or len(chatString) == 0:
            return
        self.clearChat()
        self.taskId = random.randint(0, 1000000000000000000000000000000L)
        if self.nameTag:
            self.getNameTag().hide()
        if self.isThought(chatString):
            chatString = self.removeThoughtPrefix(chatString)
            bubble = loader.loadModel(CIGlobals.ThoughtBubble)
        else:
            length = math.sqrt(len(chatString)) / self.LENGTH_FACTOR
            if length < self.MIN_LENGTH:
                length = self.MIN_LENGTH
            if length > self.MAX_LENGTH:
                length = self.MAX_LENGTH
            bubble = loader.loadModel(CIGlobals.ChatBubble)
            if self.autoClearChat:
                taskMgr.doMethodLater(length, self.clearChatTask, 'clearAvatarChat-%s' % str(self.taskId))
        if self.avatarType == CIGlobals.Suit:
            font = CIGlobals.getSuitFont()
        else:
            font = CIGlobals.getToonFont()
        self.chatBubble = ChatBalloon(bubble).generate(chatString, font)
        self.chatBubble.setEffect(BillboardEffect.make(Vec3(0, 0, 1), True, False, 3.0, camera, Point3(0, 0, 0)))
        if self.nameTag:
            self.chatBubble.setZ(self.getNameTag().getZ())
        else:
            if self.avatarType == CIGlobals.Suit:
                self.chatBubble.setZ(CIGlobals.SuitNameTagPos[self.head])
        if hasattr(self.avatar, 'getGhost'):
            if not self.avatar.getGhost() or self.avatar.doId == base.localAvatar.doId:
                self.chatBubble.reparentTo(self)
        else:
            self.chatBubble.reparentTo(self)
        LabelScaler().resize(self.chatBubble)

    def isThought(self, message):
        if message.isspace():
            return False
        if message[0] == self.THOUGHT_PREFIX:
            return True
        return False

    def removeThoughtPrefix(self, message):
        if self.isThought(message):
            return message[len(self.THOUGHT_PREFIX):]
        notify.warning('attempted to remove a thought prefix on a non-thought message')
        return message

    def clearChatTask(self, task):
        self.clearChat()
        return task.done

    def clearChat(self):
        try:
            self.chatBubble.removeNode()
            del self.chatBubble
        except:
            return

        if hasattr(self.avatar, 'getGhost'):
            if self.nameTag and not self.avatar.getGhost() or self.nameTag and self.avatar.doId == base.localAvatar.doId:
                self.getNameTag().show()
        else:
            if self.nameTag:
                self.getNameTag().show()
        taskMgr.remove('clearAvatarChat-' + str(self.taskId))