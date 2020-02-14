# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cog.Head
from lib.coginvasion.cog.SuitType import SuitType
from direct.actor.Actor import Actor

class Head:

    def __init__(self, suit, head, headTex=None, headColor=None, headAnims=None):
        self.suit = suit
        self.head = head
        self.headTex = headTex
        self.headColor = headColor
        self.headMdl = None
        self.headAnims = headAnims
        return

    def generate(self):
        if self.suit:
            phase = 4
            if self.suit == SuitType.C:
                phase = 3.5
            heads = loader.loadModel('phase_%s/models/char/suit%s-heads.bam' % (str(phase), self.suit))
            self.headMdl = heads.find('**/%s' % self.head)
            if self.head == 'flunky':
                glasses = heads.find('**/glasses')
                glasses.reparentTo(self.headMdl)
                glasses.setTwoSided(True)
            heads.removeNode()
        else:
            if not self.headAnims:
                self.headMdl = loader.loadModel(self.head)
            else:
                self.headMdl = Actor(self.head)
                self.headMdl.loadAnims(self.headAnims)
        if self.headTex:
            self.headMdl.setTexture(loader.loadTexture(self.headTex), 1)
        if self.headColor:
            self.headMdl.setColor(self.headColor)
        return self.headMdl

    def get(self):
        return self.headMdl

    def cleanup(self):
        if self.headMdl:
            self.headMdl.removeNode()
            del self.headMdl
        del self.suit
        del self.headTex
        del self.headColor
        del self.head