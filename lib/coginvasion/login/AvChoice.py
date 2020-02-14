# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.login.AvChoice


class AvChoice:

    def __init__(self, dna, name, slot, avId):
        self.setDNA(dna)
        self.setName(name)
        self.setSlot(slot)
        self.setAvId(avId)

    def setDNA(self, dna):
        self.dna = dna

    def getDNA(self):
        return self.dna

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSlot(self, slot):
        self.slot = slot

    def getSlot(self):
        return self.slot

    def setAvId(self, avId):
        self.avId = avId

    def getAvId(self):
        return self.avId

    def cleanup(self):
        del self.dna
        del self.slot
        del self.name
        del self.avId