# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.toon.ChatBalloon
from panda3d.core import VBase4, NodePath, DepthWriteAttrib, AntialiasAttrib

class ChatBalloon(NodePath):
    TEXT_X_OFFSET = -0.05
    TEXT_Y_OFFSET = -0.05
    TEXT_Z_OFFSET = -(4.0 / 33.0)
    TEXT_MIN_WIDTH = 1.2
    TEXT_MIN_HEIGHT = 1.0
    TEXT_GLYPH_SCALE = 1.0
    TEXT_GLYPH_SHIFT = 0.1
    BALLOON_X_PADDING = 0.55
    BALLOON_Z_PADDING = 0.8
    BUTTON_SCALE = 6
    BUTTON_SHIFT = (0, 0, 0.6)

    def __init__(self, model, modelWidth, modelHeight, textNode, foreground=VBase4(0, 0, 0, 1), background=VBase4(1, 1, 1, 1), reversed=False, button=None):
        NodePath.__init__(self, 'chatBalloon')
        self.model = model
        self.modelWidth = modelWidth
        self.modelHeight = modelHeight
        self.textNode = textNode
        self.foreground = foreground
        self.background = background
        self.button = button
        self.textNode.setTextColor(self.foreground)
        self.balloon = self.model.copyTo(self)
        self.balloon.setColor(self.background)
        self.balloon.setTransparency(self.background[3] < 1)
        self.textNodePath = self.attachNewNode(self.textNode)
        self.textNodePath.setTransparency(self.foreground[3] < 1)
        self.textNodePath.setAttrib(DepthWriteAttrib.make(0))
        middle = self.balloon.find('**/middle')
        top = self.balloon.find('**/top')
        self.textWidth = self.textNode.getWidth()
        if self.textWidth < self.TEXT_MIN_WIDTH:
            self.textWidth = self.TEXT_MIN_WIDTH
        paddedWidth = self.textWidth + self.BALLOON_X_PADDING * 2
        self.balloon.setSx(paddedWidth / modelWidth)
        self.textHeight = textNode.getHeight()
        if self.textHeight < self.TEXT_MIN_HEIGHT:
            self.textHeight = self.TEXT_MIN_HEIGHT
        paddedHeight = self.textHeight + self.BALLOON_Z_PADDING * 2
        middle.setSz(paddedHeight - 1.5)
        top.setZ(middle, 1)
        if reversed:
            self.balloon.setSx(-self.balloon.getSx())
            self.balloon.setTwoSided(True)
        self.width = paddedWidth
        self.height = paddedHeight
        self.center = self.balloon.getBounds().getCenter()
        self.textNodePath.setPos(self.center)
        self.textNodePath.setY(self.TEXT_Y_OFFSET)
        self.textNodePath.setX(self.textNodePath, -(self.textWidth / 2))
        if self.textWidth == self.TEXT_MIN_WIDTH:
            centerX = (self.TEXT_MIN_WIDTH - self.textNode.getWidth()) / 2.0
            self.textNodePath.setX(self.textNodePath, centerX)
        self.textNodePath.setZ(top, -self.BALLOON_Z_PADDING + self.TEXT_Z_OFFSET)
        if self.textHeight == self.TEXT_MIN_HEIGHT:
            centerZ = (ChatBalloon.TEXT_MIN_HEIGHT - self.textNode.getHeight()) / 2.0
            self.textNodePath.setZ(self.textNodePath, -centerZ)
        self.textNodePath.setX(self.textNodePath, self.TEXT_X_OFFSET)
        if self.button is not None:
            self.buttonNodePath = button.copyTo(self)
            self.buttonNodePath.setPos(self.textNodePath, self.textWidth, 0, -self.textHeight)
            self.buttonNodePath.setPos(self.buttonNodePath, ChatBalloon.BUTTON_SHIFT)
            self.buttonNodePath.setScale(ChatBalloon.BUTTON_SCALE)
        else:
            self.buttonNodePath = None
        self.setAntialias(AntialiasAttrib.MMultisample)
        return

    def setForeground(self, foreground):
        self.foreground = foreground
        self.textNode.setTextColor(self.foreground)

    def getForeground(self):
        return self.foreground

    def setBackground(self, background):
        self.background = background
        self.balloon.setColor(self.background)

    def getBackground(self):
        return self.background

    def setButton(self, button):
        if self.buttonNodePath is not None:
            self.buttonNodePath.removeNode()
            self.buttonNodePath = None
        if button is not None:
            self.buttonNodePath = button.copyTo(self)
            self.buttonNodePath.setPos(self.textNodePath, self.textWidth, 0, -self.textHeight)
            self.buttonNodePath.setPos(self.buttonNodePath, ChatBalloon.BUTTON_SHIFT)
            self.buttonNodePath.setScale(ChatBalloon.BUTTON_SCALE)
        return