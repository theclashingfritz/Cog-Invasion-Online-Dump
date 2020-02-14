# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.Inventory
from direct.directNotify.DirectNotifyGlobal import directNotify
from direct.showbase.DirectObject import DirectObject

class Inventory(DirectObject):
    notify = directNotify.newCategory('Inventory')

    def __init__(self):
        DirectObject.__init__(self)
        self.gags = None
        return

    def setGags(self, gagArray, ammo):
        self.gags = {}
        for gag in gagArray:
            self.gags[gag] = ammo

        self.gags = gagArray
        self.gagAmmo = ammo

    def getGags(self):
        return self.gags

    def getGagAmmo(self):
        return self.gagAmmo

    def getAmmoOfGag(self, index):
        return self.getGagAmmo()[index]

    def cleanup(self):
        del self.gags
        del self.gagAmmo