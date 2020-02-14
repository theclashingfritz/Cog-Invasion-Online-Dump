# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.friends.FriendRequest
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import DirectFrame, OnscreenText, DirectButton
from lib.coginvasion.toon import ToonDNA

class FriendRequest(DirectFrame):
    notify = directNotify.newCategory('FriendRequest')

    def __init__(self, name, dnaStrand):
        DirectFrame.__init__(self)
        dna = ToonDNA.ToonDNA()
        dna.setDNAStrand(dnaStrand)