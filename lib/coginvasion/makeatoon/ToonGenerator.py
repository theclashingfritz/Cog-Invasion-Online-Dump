# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.makeatoon.ToonGenerator
from direct.directnotify.DirectNotify import DirectNotify
from lib.coginvasion.toon import Toon
import random
notify = DirectNotify().newCategory('ToonGenerator')

class ToonGenerator:

    def __init__(self, mat=None):
        self.toon = Toon.Toon(base.cr, mat=1)

    def generateToon(self, gender, matNARandomToon=0):
        genderDNA = self.toon.gender2genderDNA[gender]
        self.random_animal = random.randint(0, 8)
        shortDNA = '00'
        if self.toon.animalDNA2animal['0' + str(self.random_animal)] == 'mouse':
            self.random_head = random.randint(0, 1)
        else:
            if self.toon.animalDNA2animal['0' + str(self.random_animal)] == 'dog':
                self.random_head = random.randint(4, 7)
            else:
                self.random_head = random.randint(0, 3)
        if gender == 'girl':
            self.random_torso = random.randint(3, 5)
            shortDNA = '10'
        else:
            self.random_torso = random.randint(0, 2)
        self.random_legs = random.randint(0, 2)
        self.random_color = random.randint(0, 26)
        animalDNA = '0' + str(self.random_animal)
        headDNA = '0' + str(self.random_head)
        torsoDNA = '0' + str(self.random_torso)
        legsDNA = '0' + str(self.random_legs)
        if self.random_color < 10:
            colorDNA = '0' + str(self.random_color)
        else:
            colorDNA = str(self.random_color)
        dnaStrand = '%s/%s/%s/%s/%s/%s/%s/%s/00/00/%s/00/00/00/00' % (
         genderDNA, animalDNA, headDNA, colorDNA, torsoDNA,
         colorDNA, legsDNA, colorDNA, shortDNA)
        self.toon.setDNAStrand(dnaStrand)
        self.currentAnimFrame = 0
        if not matNARandomToon:
            self.createToon()

    def cleanupToon(self):
        self.toon.deleteCurrentToon()
        self.toon.disable()
        self.toon.delete()

    def isFinalHead(self, headDna, direction):
        if direction == 1:
            return headDna == '03' and self.toon.animal != 'mouse' and self.toon.animal != 'dog' or headDna == '01' and self.toon.animal == 'mouse' or headDna == '07' and self.toon.animal == 'dog'
        if direction == 0:
            return headDna == '00' and self.toon.animal != 'dog' or headDna == '04' and self.toon.animal == 'dog'

    def isFinalTorso(self, torsoDna, direction):
        if direction == 1:
            if self.toon.gender == 'girl':
                return torsoDna == '05'
            return torsoDna == '02'
        else:
            if direction == 0:
                if self.toon.gender == 'girl':
                    return torsoDna == '03'
                return torsoDna == '00'

    def isFinalLeg(self, legDna, direction):
        if direction == 1:
            return legDna == '02'
        if direction == 0:
            return legDna == '00'

    def isFinalAnimal(self, animalDna, direction):
        if direction == 1:
            return animalDna == '08'
        if direction == 0:
            return animalDna == '00'

    def isFinalColor(self, colorDna, direction):
        if direction == 1:
            return colorDna == '26'
        if direction == 0:
            return colorDna == '00'

    def isFinalShorts(self, shortDna, direction):
        if direction == 1:
            if self.toon.gender == 'girl':
                return shortDna == '17'
            return shortDna == '09'
        else:
            if direction == 0:
                if self.toon.gender == 'girl':
                    return shortDna == '10'
                return shortDna == '00'

    def isFinalShirt(self, shirtDna, direction):
        if direction == 1:
            return shirtDna == '22'
        if direction == 0:
            return shirtDna == '00'

    def isFinalSleeve(self, sleeveDna, direction):
        if direction == 1:
            return sleeveDna == '22'
        if direction == 0:
            return sleeveDna == '00'

    def getNextTorso(self):
        if self.isFinalTorso(self.toon.torso2torsoDNA[self.toon.torso], 1):
            if self.toon.getGender() == 'girl':
                return '03'
            return '00'
        else:
            currentTorso = int(self.toon.torso2torsoDNA[self.toon.torso])
            return '0' + str(currentTorso + 1)

    def getPrevTorso(self):
        if self.isFinalTorso(self.toon.torso2torsoDNA[self.toon.torso], 0):
            if self.toon.getGender() == 'girl':
                return '05'
            return '02'
        else:
            currentTorso = int(self.toon.torso2torsoDNA[self.toon.torso])
            return '0' + str(currentTorso - 1)

    def getNextLeg(self):
        if self.isFinalLeg(self.toon.leg2legDNA[self.toon.legs], 1):
            return '00'
        currentLeg = int(self.toon.leg2legDNA[self.toon.legs])
        return '0' + str(currentLeg + 1)

    def getPrevLeg(self):
        if self.isFinalLeg(self.toon.leg2legDNA[self.toon.legs], 0):
            return '02'
        currentLeg = int(self.toon.leg2legDNA[self.toon.legs])
        return '0' + str(currentLeg - 1)

    def getNextHead(self):
        if self.isFinalHead(self.toon.head2headDNA[self.toon.head], 1):
            if self.getNextAnimal() == '01':
                return '04'
            return '00'
        else:
            currentHead = int(self.toon.head2headDNA[self.toon.head])
            return '0' + str(currentHead + 1)

    def getNextAnimal(self):
        if self.toon.animal == 'duck' and self.isFinalHead(self.toon.head2headDNA[self.toon.head], 1):
            return '00'
        if not self.isFinalHead(self.toon.head2headDNA[self.toon.head], 1):
            return
        currentAnimal = int(self.toon.animal2animalDNA[self.toon.animal])
        return '0' + str(currentAnimal + 1)
        return

    def getPrevAnimal(self):
        if self.toon.animal == 'cat' and self.isFinalHead(self.toon.head2headDNA[self.toon.head], 0):
            return '08'
        if not self.isFinalHead(self.toon.head2headDNA[self.toon.head], 0):
            return
        currentAnimal = int(self.toon.animal2animalDNA[self.toon.animal])
        return '0' + str(currentAnimal - 1)
        return

    def getPrevHead(self):
        if self.isFinalHead(self.toon.head2headDNA[self.toon.head], 0):
            if self.getPrevAnimal() == '07':
                return '01'
            if self.getPrevAnimal() == '01':
                return '07'
            return '03'
        else:
            currentHead = int(self.toon.head2headDNA[self.toon.head])
            return '0' + str(currentHead - 1)

    def getNextColor(self, part):
        if part == 'torso':
            color = self.toon.torsocolor
        else:
            if part == 'legs':
                color = self.toon.legcolor
            else:
                if part == 'head' or part == 'all':
                    color = self.toon.headcolor
                else:
                    if part == 'shirt':
                        color = self.toon.shirtColor
                    else:
                        if part == 'shorts':
                            color = self.toon.shortColor
                        else:
                            if part == 'sleeve':
                                color = self.toon.sleeveColor
                            else:
                                if part == 'gloves':
                                    color = self.toon.gloveColor
                if self.isFinalColor(self.toon.color2colorDNA[color], 1):
                    return '00'
            currentColor = int(self.toon.color2colorDNA[color])
            if currentColor < 9:
                return '0' + str(currentColor + 1)
        return str(currentColor + 1)

    def getPrevColor(self, part):
        if part == 'torso':
            color = self.toon.torsocolor
        else:
            if part == 'legs':
                color = self.toon.legcolor
            else:
                if part == 'head' or part == 'all':
                    color = self.toon.headcolor
                else:
                    if part == 'shirt':
                        color = self.toon.shirtColor
                    else:
                        if part == 'shorts':
                            color = self.toon.shortColor
                        else:
                            if part == 'sleeve':
                                color = self.toon.sleeveColor
                            else:
                                if part == 'gloves':
                                    color = self.toon.gloveColor
                if self.isFinalColor(self.toon.color2colorDNA[color], 0):
                    return '26'
            currentColor = int(self.toon.color2colorDNA[color])
            if currentColor < 11:
                return '0' + str(currentColor - 1)
        return str(currentColor - 1)

    def getNextShirtAndSleeve(self):
        return [
         self.getNextShirt(), self.getNextSleeve()]

    def getPrevShirtAndSleeve(self):
        return [
         self.getPrevShirt(), self.getPrevSleeve()]

    def getNextShirt(self):
        if self.getNextColor('shirt') == '00':
            if self.isFinalShirt(self.toon.shirt2shirtDNA[self.toon.shirt], 1):
                return '00'
            currentShirt = int(self.toon.shirt2shirtDNA[self.toon.shirt])
            if currentShirt < 9:
                return '0' + str(currentShirt + 1)
            return str(currentShirt + 1)
        else:
            return
        return

    def getPrevShirt(self):
        if self.getPrevColor('shirt') == '26':
            if self.isFinalShirt(self.toon.shirt2shirtDNA[self.toon.shirt], 0):
                return '22'
            currentShirt = int(self.toon.shirt2shirtDNA[self.toon.shirt])
            if currentShirt < 11:
                return '0' + str(currentShirt - 1)
            return str(currentShirt - 1)
        else:
            return
        return

    def getNextSleeve(self):
        if self.getNextColor('sleeve') == '00':
            if self.isFinalSleeve(self.toon.sleeve2sleeveDNA[self.toon.sleeve], 1):
                return '00'
            currentSleeve = int(self.toon.sleeve2sleeveDNA[self.toon.sleeve])
            if currentSleeve < 9:
                return '0' + str(currentSleeve + 1)
            return str(currentSleeve + 1)
        else:
            return
        return

    def getPrevSleeve(self):
        if self.getPrevColor('sleeve') == '26':
            if self.isFinalSleeve(self.toon.sleeve2sleeveDNA[self.toon.sleeve], 0):
                return '22'
            currentSleeve = int(self.toon.sleeve2sleeveDNA[self.toon.sleeve])
            if currentSleeve < 11:
                return '0' + str(currentSleeve - 1)
            return str(currentSleeve - 1)
        else:
            return
        return

    def getNextShorts(self):
        if self.getNextColor('shorts') == '00':
            if self.isFinalShorts(self.toon.short2shortDNA[self.toon.shorts], 1):
                return '00'
            currentShorts = int(self.toon.short2shortDNA[self.toon.shorts])
            if currentShorts < 9:
                return '0' + str(currentShorts + 1)
            return str(currentShorts + 1)
        else:
            return
        return

    def getPrevShorts(self):
        if self.getPrevColor('shorts') == '26':
            if self.isFinalShorts(self.toon.short2shortDNA[self.toon.shorts], 0):
                return '16'
            currentShorts = int(self.toon.short2shortDNA[self.toon.shorts])
            if currentShorts < 11:
                return '0' + str(currentShorts - 1)
            return str(currentShorts - 1)
        else:
            return
        return

    def generateDNAStrandWithCurrentStyle(self):
        self.currentAnimFrame = self.toon.getCurrentFrame()
        self.toon.generateDNAStrandWithCurrentStyle()
        self.createToon()

    def setToonPosForNameShop(self):
        self.toon.setPos(2.29, -3, 0)
        self.toon.setHpr(138.01, 0, 0)

    def setToonPosForGeneralShop(self):
        self.toon.setPos(0, 0, 0)
        self.toon.setHpr(180, 0, 0)

    def createToon(self):
        self.toon.reparentTo(render)
        if self.currentAnimFrame == 0:
            self.toon.animFSM.request('neutral')
        else:
            self.toon.loopFromFrameToZero('neutral', fromFrame=self.currentAnimFrame)
        self.toon.startBlink()
        self.toon.startLookAround()
        self.toon.setH(180)