# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.nametag.Nametag2d
from direct.task.Task import Task
import math
from panda3d.core import PGButton, VBase4, DepthWriteAttrib, Point3
from lib.coginvasion.toon.ChatBalloon import ChatBalloon
from lib.coginvasion.margins import MarginGlobals
from lib.coginvasion.margins.MarginVisible import MarginVisible
import NametagGlobals
from Nametag import Nametag
from lib.coginvasion.gui.Clickable2d import Clickable2d
from lib.coginvasion.globals import CIGlobals

class Nametag2d(Nametag, Clickable2d, MarginVisible):
    CONTENTS_SCALE = 0.25
    CHAT_TEXT_MAX_ROWS = 6
    CHAT_TEXT_WORD_WRAP = 8
    CHAT_BALLOON_ALPHA = 0.5
    ARROW_OFFSET = -1.0
    ARROW_SCALE = 1.5

    def __init__(self):
        Nametag.__init__(self)
        Clickable2d.__init__(self, 'Nametag2d')
        MarginVisible.__init__(self)
        self.actualChatText = ''
        self.arrow = None
        self.textNodePath = None
        self.contents.setScale(self.CONTENTS_SCALE)
        self.hideThought()
        self.accept('MarginVisible-update', self.update)
        return

    def destroy(self):
        self.ignoreAll()
        Nametag.destroy(self)
        if self.textNodePath is not None:
            self.textNodePath.removeNode()
            self.textNodePath = None
        if self.arrow is not None:
            self.arrow.removeNode()
            self.arrow = None
        Clickable2d.destroy(self)
        return

    def getUniqueName(self):
        return 'Nametag2d-' + str(id(self))

    def getChatBalloonModel(self):
        return NametagGlobals.chatBalloon2dModel

    def getChatBalloonWidth(self):
        return NametagGlobals.chatBalloon2dWidth

    def getChatBalloonHeight(self):
        return NametagGlobals.chatBalloon2dHeight

    def setChatText(self, chatText):
        self.actualChatText = chatText
        Nametag.setChatText(self, chatText)

    def updateClickRegion(self):
        if self.chatBalloon is not None:
            right = self.chatBalloon.width / 2.0
            left = -right
            top = self.chatBalloon.height / 2.0
            bottom = -top
            self.setClickRegionFrame(left, right, bottom, top)
            self.region.setActive(True)
        else:
            if self.panel is not None:
                centerX = (self.textNode.getLeft() + self.textNode.getRight()) / 2.0
                centerY = (self.textNode.getBottom() + self.textNode.getTop()) / 2.0
                left = centerX - self.panelWidth / 2.0
                right = centerX + self.panelWidth / 2.0
                bottom = centerY - self.panelHeight / 2.0
                top = centerY + self.panelHeight / 2.0
                self.setClickRegionFrame(left, right, bottom, top)
                self.region.setActive(True)
            else:
                if self.region is not None:
                    self.region.setActive(False)
        return

    def isClickable(self):
        if self.getChatText() and self.hasChatButton():
            return True
        return NametagGlobals.wantActiveNametags and Clickable2d.isClickable(self)

    def setClickState(self, clickState):
        if self.isClickable():
            self.applyClickState(clickState)
        else:
            self.applyClickState(PGButton.SInactive)
        Clickable2d.setClickState(self, clickState)

    def enterDepressed(self):
        if self.isClickable():
            base.playSfx(NametagGlobals.clickSound)

    def enterRollover(self):
        if self.isClickable() and self.lastClickState != PGButton.SDepressed:
            base.playSfx(NametagGlobals.rolloverSound)

    def update(self):
        self.contents.node().removeAllChildren()
        Nametag.update(self)
        if self.cell is not None:
            self.reposition()
            self.updateClickRegion()
        else:
            if self.region is not None:
                self.region.setActive(False)
        return

    def tick(self, task):
        if self.avatar is None or self.avatar.isEmpty():
            return Task.cont
        if self.cell is None or self.arrow is None:
            return Task.cont
        location = self.avatar.getPos(NametagGlobals.me)
        rotation = NametagGlobals.me.getQuat(base.cam)
        camSpacePos = rotation.xform(location)
        arrowRadians = math.atan2(camSpacePos[0], camSpacePos[1])
        arrowDegrees = arrowRadians / math.pi * 180
        self.arrow.setR(arrowDegrees - 90)
        return Task.cont

    def drawChatBalloon(self, model, modelWidth, modelHeight):
        if self.chatFont is None:
            return
        if self.avatar.avatarType == CIGlobals.Suit and len(self.getText().split('\n')) == 3:
            name, dept, level = self.getText().split('\n')
        else:
            name = self.getText()
        self.chatTextNode.setText(name + ': ' + self.actualChatText)
        self.setPriority(MarginGlobals.MP_normal)
        if self.textNodePath is not None:
            self.textNodePath.removeNode()
            self.textNodePath = None
        if self.arrow is not None:
            self.arrow.removeNode()
            self.arrow = None
        if self.isClickable():
            foreground, background = self.chatColor[self.clickState]
        else:
            foreground, background = self.chatColor[PGButton.SInactive]
        if self.chatType == NametagGlobals.SPEEDCHAT:
            background = self.speedChatColor
        if background[3] > self.CHAT_BALLOON_ALPHA:
            background = VBase4(background[0], background[1], background[2], self.CHAT_BALLOON_ALPHA)
        self.chatBalloon = ChatBalloon(model, modelWidth, modelHeight, self.chatTextNode, foreground=foreground, background=background, reversed=self.chatReversed, button=self.chatButton[self.clickState])
        self.chatBalloon.reparentTo(self.contents)
        left, right, bottom, top = self.chatTextNode.getFrameActual()
        center = self.contents.getRelativePoint(self.chatBalloon.textNodePath, (
         (left + right) / 2.0, 0, (bottom + top) / 2.0))
        self.chatBalloon.setPos(self.chatBalloon, -center)
        return

    def drawNametag(self):
        self.setPriority(MarginGlobals.MP_low)
        if self.textNodePath is not None:
            self.textNodePath.removeNode()
            self.textNodePath = None
        if self.arrow is not None:
            self.arrow.removeNode()
            self.arrow = None
        if self.font is None:
            return
        if self.icon is not None:
            self.contents.attachNewNode(self.icon)
        if self.isClickable():
            foreground, background = self.nametagColor[self.clickState]
        else:
            foreground, background = self.nametagColor[PGButton.SInactive]
        self.textNode.setTextColor(foreground)
        self.textNodePath = self.contents.attachNewNode(self.textNode, 1)
        self.textNodePath.setTransparency(foreground[3] < 1)
        self.textNodePath.setAttrib(DepthWriteAttrib.make(0))
        self.textNodePath.setY(self.TEXT_Y_OFFSET)
        self.panel = NametagGlobals.cardModel.copyTo(self.contents, 0)
        self.panel.setColor(background)
        self.panel.setTransparency(background[3] < 1)
        x = (self.textNode.getLeft() + self.textNode.getRight()) / 2.0
        z = (self.textNode.getBottom() + self.textNode.getTop()) / 2.0
        self.panel.setPos(x, 0, z)
        self.panelWidth = self.textNode.getWidth() + self.PANEL_X_PADDING
        self.panelHeight = self.textNode.getHeight() + self.PANEL_Z_PADDING
        self.panel.setScale(self.panelWidth, 1, self.panelHeight)
        self.arrow = NametagGlobals.arrowModel.copyTo(self.contents)
        self.arrow.setZ(self.ARROW_OFFSET + self.textNode.getBottom())
        self.arrow.setScale(self.ARROW_SCALE)
        self.arrow.setColor(NametagGlobals.NametagColors[NametagGlobals.CCOtherPlayer][0][0])
        return

    def marginVisibilityChanged(self):
        if self.cell is not None:
            self.reposition()
            self.updateClickRegion()
        else:
            if self.region is not None:
                self.region.setActive(False)
        return

    def reposition(self):
        if self.contents is None:
            return
        origin = Point3()
        self.contents.setPos(origin)
        if self.chatBalloon is not None:
            self.chatBalloon.removeNode()
            self.chatBalloon = None
            self.contents.node().removeAllChildren()
            if self.cell in base.leftCells or self.cell in base.rightCells:
                text = self.getChatText().replace('\x01WLDisplay\x01', '').replace('\x02', '')
                textWidth = self.chatTextNode.calcWidth(text)
                if textWidth / self.CHAT_TEXT_WORD_WRAP > self.CHAT_TEXT_MAX_ROWS:
                    self.chatTextNode.setWordwrap(textWidth / (self.CHAT_TEXT_MAX_ROWS - 0.5))
            else:
                self.chatTextNode.setWordwrap(self.CHAT_TEXT_WORD_WRAP)
            model = self.getChatBalloonModel()
            modelWidth = self.getChatBalloonWidth()
            modelHeight = self.getChatBalloonHeight()
            self.drawChatBalloon(model, modelWidth, modelHeight)
            nodePath = self.chatBalloon.textNodePath
            left, right, bottom, top = self.chatTextNode.getFrameActual()
        else:
            if self.panel is not None:
                nodePath = self.textNodePath
                left, right, bottom, top = self.textNode.getFrameActual()
                bottom -= self.ARROW_SCALE
            else:
                return
        if self.cell in base.bottomCells:
            origin = self.contents.getRelativePoint(nodePath, ((left + right) / 2.0, 0, bottom))
        else:
            if self.cell in base.leftCells:
                origin = self.contents.getRelativePoint(nodePath, (left, 0, (bottom + top) / 2.0))
            else:
                if self.cell in base.rightCells:
                    origin = self.contents.getRelativePoint(nodePath, (right, 0, (bottom + top) / 2.0))
        self.contents.setPos(self.contents, -origin)
        return