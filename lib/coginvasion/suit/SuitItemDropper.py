# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.SuitItemDropper
from direct.directnotify.DirectNotifyGlobal import directNotify
from lib.coginvasion.gags import GagGlobals
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.suit.DistributedDroppableCollectableBackpackAI import DistributedDroppableCollectableBackpackAI as DBackpackAI
from lib.coginvasion.suit.DistributedDroppableCollectableJellybeanAI import DistributedDroppableCollectableJellybeanAI as DJellybeanAI
from lib.coginvasion.suit.DistributedDroppableCollectableJellybeanJarAI import DistributedDroppableCollectableJellybeanJarAI as DJellybeanJarAI
import random, SuitAttacks

class SuitItemDropper:
    notify = directNotify.newCategory('SuitItemDropper')
    possibleDrops = {DJellybeanAI: {}, DJellybeanJarAI: {}}
    jarMinSize = 10

    def __init__(self, suit):
        self.suit = suit
        self.numDrops = 1
        self.suitDrops = []
        self.isTutorialDrop = False

    def calculate(self, tutDrop=None):
        if self.suit.getMaxHealth() <= 48:
            pass
        for _ in xrange(self.numDrops):
            chance = random.randint(1, 100)
            drop = None
            for constructor, values in self.possibleDrops.iteritems():
                if 'chance' in values:
                    dropChance = values.get('chance')
                    if chance <= dropChance:
                        drop = self.generateDrop(constructor)
                        gags = list(GagGlobals.gagIds.keys())
                        maxGags = values.get('maxGags')
                        backpackGags = []
                        for _ in xrange(maxGags):
                            choice = random.choice(gags)
                            backpackGags.append(choice)
                            gags.remove(choice)

                        drop.b_setBP(backpackGags)
                else:
                    jellybeans = int(self.suit.getMaxHealth() / SuitAttacks.SuitAttackDamageFactors['glowerpower'])
                    constructor = DJellybeanAI
                    if jellybeans > self.jarMinSize:
                        constructor = DJellybeanJarAI
                    drop = self.generateDrop(constructor)
                    drop.setValue(jellybeans)

            if not drop:
                self.notify.warning('Could not find a drop.')
                return
            drop.setTutDrop(tutDrop)
            drop.setSuitManager(self.suit.getManager())
            self.suitDrops.append(drop)

        return

    def generateDrop(self, constructor):
        drop = constructor(self.suit.air)
        drop.generateWithRequired(self.suit.zoneId)
        return drop

    def drop(self):
        for i in xrange(len(self.suitDrops)):
            drop = self.suitDrops[i]
            x, y, z = self.suit.getPos(render)
            if i > 0:
                x += random.uniform(-2.5, 2.5)
                y += random.uniform(-5.0, 5.0)
            drop.d_setX(x)
            drop.d_setY(y)
            drop.d_setZ(z)
            drop.b_setParent(CIGlobals.SPRender)
            if hasattr(drop, 'startTimer'):
                drop.startTimer()
            if self.suit.getManager():
                self.suit.getManager().drops.append(drop)

    def setDropChance(self, drop, chance):
        values = self.possibleDrops.get(drop)
        values['chance'] = chance

    def getDropChance(self, drop):
        return self.possibleDrops.get(drop)['chance']

    def cleanup(self):
        self.suit = None
        self.suitDrops = []
        self.numDrops = 0
        return