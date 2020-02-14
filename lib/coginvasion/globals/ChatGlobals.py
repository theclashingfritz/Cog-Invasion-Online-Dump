# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.globals.ChatGlobals
from panda3d.core import *
from lib.coginvasion.globals import CIGlobals
import random
CFSpeech = 1
CFThought = 2
CFQuicktalker = 4
CFTimeout = 8
CFPageButton = 16
CFQuitButton = 32
CFNoQuitButton = 64
CFReversed = 128
WTNormal = 0
WTQuickTalker = 1
WTSystem = 2
WTBattleSOS = 3
WTEmote = 4
WTToontownBoardingGroup = 5
WhisperColors = {WTNormal: (
            (
             (0.0, 0.0, 0.0, 1.0), (0.2, 0.6, 0.8, 0.6)),
            (
             (1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),
            (
             (0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.9, 0.6)),
            (
             (0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.8, 0.6))), 
   WTQuickTalker: (
                 (
                  (0.0, 0.0, 0.0, 1.0), (0.2, 0.6, 0.8, 0.6)),
                 (
                  (1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),
                 (
                  (0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.9, 0.6)),
                 (
                  (0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.8, 0.6))), 
   WTSystem: (
            (
             (0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6)),
            (
             (1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),
            (
             (0.0, 0.0, 0.0, 1.0), (0.8, 0.4, 1.0, 0.8)),
            (
             (0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6))), 
   WTBattleSOS: (
               (
                (0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6)),
               (
                (1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),
               (
                (0.0, 0.0, 0.0, 1.0), (0.8, 0.4, 0.0, 0.8)),
               (
                (0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6))), 
   WTEmote: (
           (
            (0.0, 0.0, 0.0, 1.0), (0.1, 0.7, 0.41, 0.6)),
           (
            (1.0, 0.5, 0.5, 1.0), (0.2, 0.7, 0.41, 0.8)),
           (
            (0.0, 0.0, 0.0, 1.0), (0.1, 0.6, 0.51, 0.6)),
           (
            (0.0, 0.0, 0.0, 1.0), (0.1, 0.6, 0.41, 0.6))), 
   WTToontownBoardingGroup: (
                           (
                            (0.0, 0.0, 0.0, 1.0), (0.9, 0.5, 0.1, 0.6)),
                           (
                            (1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),
                           (
                            (0.0, 0.0, 0.0, 1.0), (0.9, 0.6, 0.2, 0.6)),
                           (
                            (0.0, 0.0, 0.0, 1.0), (0.9, 0.6, 0.1, 0.6)))}
WhiteListData = None

def loadWhiteListData():
    global WhiteListData
    if WhiteListData is None:
        vfs = VirtualFileSystem.getGlobalPtr()
        whitelistFile = vfs.readFile('phase_3/etc/ciwhitelist.dat', False)
        WhiteListData = set()
        for word in whitelistFile.split():
            WhiteListData.add(word)

        del whitelistFile
    return


def getWhiteListData():
    return WhiteListData


garbleData = None

def getGarble(animal):
    global garbleData
    if garbleData is None:
        garbleData = {'dog': CIGlobals.ChatGarblerDog, 'rabbit': CIGlobals.ChatGarblerRabbit, 
           'cat': CIGlobals.ChatGarblerCat, 
           'mouse': CIGlobals.ChatGarblerMouse, 
           'monkey': CIGlobals.ChatGarblerMonkey, 
           'duck': CIGlobals.ChatGarblerDuck, 
           'bear': CIGlobals.ChatGarblerBear, 
           'horse': CIGlobals.ChatGarblerHorse, 
           'pig': CIGlobals.ChatGarblerPig}
    garble = garbleData[animal]
    if garble:
        return garble
    return CIGlobals.ChatGarblerDefault


def filterChat(chat, animal):
    return chat