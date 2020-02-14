# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.nametag.NametagGlobals
from panda3d.core import VBase4, PGButton
CCLocal = 0
CCNoChat = 1
CCNPC = 2
CCSuit = 3
CCToonBuilding = 4
CCSuitBuilding = 5
CCHouseBuilding = 6
CCOtherPlayer = 7
CCFreeChat = 8
CHAT = 0
SPEEDCHAT = 1
CHAT_BALLOON = 0
THOUGHT_BALLOON = 1
cardModel = None
arrowModel = None
chatBalloon3dModel = None
chatBalloon3dWidth = 0
chatBalloon3dHeight = 0
chatBalloon2dModel = None
chatBalloon2dWidth = 0
chatBalloon2dHeight = 0
thoughtBalloonModel = None
thoughtBalloonWidth = 0
thoughtBalloonHeight = 0
noButton = (None, None, None, None)
pageButton = (None, None, None, None)
quitButton = (None, None, None, None)
quitButtonWidth = 0
quitButtonHeight = 0
rolloverSound = None
clickSound = None
me = None
want2dNametags = True
forceOnscreenChat = False
force2dNametags = False
wantActiveNametags = True
nametags = []

def appendNametag(tag):
    global nametags
    nametags.append(tag)


def removeNametag(tag):
    nametags.remove(tag)


def makeTagsReady():
    for tag in nametags:
        if tag.isClickable():
            tag.setClickState(PGButton.SReady)


def makeTagsInactive():
    for tag in nametags:
        tag.setClickState(PGButton.SInactive)


def setCardModel(model):
    global cardModel
    cardModel = loader.loadModel(model)


def setArrowModel(model):
    global arrowModel
    arrowModel = loader.loadModel(model)


def setChatBalloon3dModel(model):
    global chatBalloon3dHeight
    global chatBalloon3dModel
    global chatBalloon3dWidth
    chatBalloon3dModel = loader.loadModel(model)
    chatBalloon3dWidth, chatBalloon3dHeight = getModelWidthHeight(chatBalloon3dModel)


def setChatBalloon2dModel(model):
    global chatBalloon2dHeight
    global chatBalloon2dModel
    global chatBalloon2dWidth
    chatBalloon2dModel = loader.loadModel(model)
    chatBalloon2dWidth, chatBalloon2dHeight = getModelWidthHeight(chatBalloon2dModel)


def setThoughtBalloonModel(model):
    global thoughtBalloonHeight
    global thoughtBalloonModel
    global thoughtBalloonWidth
    thoughtBalloonModel = loader.loadModel(model)
    thoughtBalloonWidth, thoughtBalloonHeight = getModelWidthHeight(thoughtBalloonModel)


def setPageButton(normal, down, rollover, disabled):
    global pageButton
    pageButton = (
     normal, down, rollover, disabled)


def setQuitButton(normal, down, rollover, disabled):
    global quitButton
    global quitButtonHeight
    global quitButtonWidth
    quitButton = (
     normal, down, rollover, disabled)
    quitButtonWidth, quitButtonHeight = getModelWidthHeight(normal)


def setRolloverSound(sound):
    global rolloverSound
    rolloverSound = sound


def setClickSound(sound):
    global clickSound
    clickSound = sound


def setMe(nodePath):
    global me
    me = nodePath


def setWant2dNametags(value):
    global want2dNametags
    want2dNametags = value


def setForceOnscreenChat(value):
    global forceOnscreenChat
    forceOnscreenChat = value


def setForce2dNametags(value):
    global force2dNametags
    force2dNametags = value


def setWantActiveNametags(value):
    global wantActiveNametags
    wantActiveNametags = value


def getModelWidthHeight(model):
    tightBounds = model.getTightBounds()
    if tightBounds is None:
        return (0, 0)
    minPoint, maxPoint = tightBounds
    width = maxPoint.getX() - minPoint.getX()
    height = maxPoint.getZ() - minPoint.getZ()
    return (
     width, height)


NametagColors = {CCLocal: (
           (
            VBase4(0.3, 0.3, 0.7, 1.0), VBase4(0.9, 0.9, 0.9, 0.5)),
           (
            VBase4(0.3, 0.3, 0.7, 1.0), VBase4(0.2, 0.2, 0.2, 0.5)),
           (
            VBase4(0.5, 0.5, 1.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
           (
            VBase4(0.3, 0.3, 0.7, 1.0), VBase4(0.8, 0.8, 0.8, 0.5))), 
   CCNoChat: (
            (
             VBase4(0.8, 0.4, 0.0, 1.0), VBase4(0.8, 0.8, 0.8, 0.5)),
            (
             VBase4(1.0, 0.5, 0.5, 1.0), VBase4(0.2, 0.2, 0.2, 0.5)),
            (
             VBase4(1.0, 0.5, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
            (
             VBase4(0.8, 0.4, 0.0, 1.0), VBase4(0.8, 0.8, 0.8, 0.5))), 
   CCNPC: (
         (
          VBase4(0.0, 0.4, 0.0, 1.0), VBase4(0.9, 0.9, 0.9, 0.5)),
         (
          VBase4(0.0, 0.5, 0.0, 1.0), VBase4(0.2, 0.2, 0.2, 0.5)),
         (
          VBase4(0.0, 0.7, 0.2, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
         (
          VBase4(0.0, 0.4, 0.0, 1.0), VBase4(0.8, 0.8, 0.8, 0.5))), 
   CCSuit: (
          (
           VBase4(0.0, 0.0, 0.0, 1.0), VBase4(0.9, 0.9, 0.9, 0.5)),
          (
           VBase4(1.0, 1.0, 1.0, 1.0), VBase4(0.2, 0.2, 0.2, 0.5)),
          (
           VBase4(0.4, 0.4, 0.4, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
          (
           VBase4(0, 0, 0, 1.0), VBase4(0.8, 0.8, 0.8, 0.5))), 
   CCSuitBuilding: (
                  (
                   VBase4(0.5, 0.5, 0.5, 1.0), VBase4(0.8, 0.8, 0.8, 0.5)),
                  (
                   VBase4(0.5, 0.5, 0.5, 1.0), VBase4(0.8, 0.8, 0.8, 0.5)),
                  (
                   VBase4(0.5, 0.5, 0.5, 1.0), VBase4(0.8, 0.8, 0.8, 1.0)),
                  (
                   VBase4(0.5, 0.5, 0.5, 1.0), VBase4(0.8, 0.8, 0.8, 0.5))), 
   CCToonBuilding: (
                  (
                   VBase4(0.2, 0.6, 0.9, 1.0), VBase4(0.8, 0.8, 0.8, 0.5)),
                  (
                   VBase4(0.2, 0.6, 0.9, 1.0), VBase4(0.8, 0.8, 0.8, 0.5)),
                  (
                   VBase4(0.2, 0.6, 0.9, 1.0), VBase4(0.8, 0.8, 0.8, 1.0)),
                  (
                   VBase4(0.2, 0.6, 0.9, 1.0), VBase4(0.8, 0.8, 0.8, 0.5))), 
   CCHouseBuilding: (
                   (
                    VBase4(0.2, 0.6, 0.9, 1.0), VBase4(0.8, 0.8, 0.8, 0.5)),
                   (
                    VBase4(0.2, 0.2, 0.5, 1.0), VBase4(0.2, 0.2, 0.2, 0.5)),
                   (
                    VBase4(0.5, 0.5, 1.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                   (
                    VBase4(0.0, 0.6, 0.2, 1.0), VBase4(0.8, 0.8, 0.8, 0.5))), 
   CCOtherPlayer: (
                 (
                  VBase4(0.8, 0.4, 0.0, 1.0), VBase4(0.9, 0.9, 0.9, 0.5)),
                 (
                  VBase4(0.8, 0.4, 0.0, 1.0), VBase4(0.2, 0.2, 0.2, 0.5)),
                 (
                  VBase4(0.8, 0.4, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                 (
                  VBase4(0.8, 0.4, 0.0, 1.0), VBase4(0.8, 0.8, 0.8, 0.5))), 
   CCFreeChat: (
              (
               VBase4(0.3, 0.3, 0.7, 1.0), VBase4(0.8, 0.8, 0.8, 0.5)),
              (
               VBase4(0.2, 0.2, 0.5, 1.0), VBase4(0.2, 0.2, 0.2, 0.5)),
              (
               VBase4(0.5, 0.5, 1.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
              (
               VBase4(0.3, 0.3, 0.7, 1.0), VBase4(0.8, 0.8, 0.8, 0.5)))}
ChatColors = {CCLocal: (
           (
            VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
           (
            VBase4(1.0, 0.5, 0.5, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
           (
            VBase4(0.0, 0.6, 0.6, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
           (
            VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0))), 
   CCNoChat: (
            (
             VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
            (
             VBase4(1.0, 0.5, 0.5, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
            (
             VBase4(0.0, 0.6, 0.6, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
            (
             VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0))), 
   CCNPC: (
         (
          VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
         (
          VBase4(1.0, 0.5, 0.5, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
         (
          VBase4(0.0, 0.6, 0.6, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
         (
          VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0))), 
   CCSuit: (
          (
           VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
          (
           VBase4(1.0, 0.5, 0.5, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
          (
           VBase4(0.0, 0.6, 0.6, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
          (
           VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0))), 
   CCSuitBuilding: (
                  (
                   VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                  (
                   VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                  (
                   VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                  (
                   VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0))), 
   CCToonBuilding: (
                  (
                   VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                  (
                   VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                  (
                   VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                  (
                   VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0))), 
   CCHouseBuilding: (
                   (
                    VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                   (
                    VBase4(1.0, 0.5, 0.5, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                   (
                    VBase4(0.0, 0.6, 0.6, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                   (
                    VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0))), 
   CCOtherPlayer: (
                 (
                  VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                 (
                  VBase4(1.0, 0.5, 0.5, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                 (
                  VBase4(0.0, 0.6, 0.6, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
                 (
                  VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0))), 
   CCFreeChat: (
              (
               VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
              (
               VBase4(1.0, 0.5, 0.5, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
              (
               VBase4(0.0, 0.6, 0.6, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)),
              (
               VBase4(0.0, 0.0, 0.0, 1.0), VBase4(1.0, 1.0, 1.0, 1.0)))}