# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.particles.SpriteParticleRendererExt
from panda3d.physics import SpriteParticleRenderer

class SpriteParticleRendererExt(SpriteParticleRenderer):
    sourceTextureName = None
    sourceFileName = None
    sourceNodeName = None

    def getSourceTextureName(self):
        if self.sourceTextureName == None:
            SpriteParticleRendererExt.sourceTextureName = base.config.GetString('particle-sprite-texture', 'maps/lightbulb.rgb')
        return self.sourceTextureName

    def setSourceTextureName(self, name):
        self.sourceTextureName = name

    def setTextureFromFile(self, fileName=None):
        if fileName == None:
            fileName = self.getSourceTextureName()
        t = loader.loadTexture(fileName)
        if t != None:
            self.setTexture(t, t.getYSize())
            self.setSourceTextureName(fileName)
            return True
        print "Couldn't find rendererSpriteTexture file: %s" % fileName
        return False
        return

    def addTextureFromFile(self, fileName=None):
        if self.getNumAnims() == 0:
            return self.setTextureFromFile(fileName)
        if fileName == None:
            fileName = self.getSourceTextureName()
        t = loader.loadTexture(fileName)
        if t != None:
            self.addTexture(t, t.getYSize())
            return True
        print "Couldn't find rendererSpriteTexture file: %s" % fileName
        return False
        return

    def getSourceFileName(self):
        if self.sourceFileName == None:
            SpriteParticleRendererExt.sourceFileName = base.config.GetString('particle-sprite-model', 'models/misc/smiley')
        return self.sourceFileName

    def setSourceFileName(self, name):
        self.sourceFileName = name

    def getSourceNodeName(self):
        if self.sourceNodeName == None:
            SpriteParticleRendererExt.sourceNodeName = base.config.GetString('particle-sprite-node', '**/*')
        return self.sourceNodeName

    def setSourceNodeName(self, name):
        self.sourceNodeName = name

    def setTextureFromNode(self, modelName=None, nodeName=None, sizeFromTexels=False):
        if modelName == None:
            modelName = self.getSourceFileName()
            if nodeName == None:
                nodeName = self.getSourceNodeName()
        m = loader.loadModel(modelName)
        if m == None:
            print "SpriteParticleRendererExt: Couldn't find model: %s!" % modelName
            return False
        np = m.find(nodeName)
        if np.isEmpty():
            print "SpriteParticleRendererExt: Couldn't find node: %s!" % nodeName
            m.removeNode()
            return False
        self.setFromNode(np, modelName, nodeName, sizeFromTexels)
        self.setSourceFileName(modelName)
        self.setSourceNodeName(nodeName)
        m.removeNode()
        return True

    def addTextureFromNode(self, modelName=None, nodeName=None, sizeFromTexels=False):
        if self.getNumAnims() == 0:
            return self.setTextureFromNode(modelName, nodeName, sizeFromTexels)
        if modelName == None:
            modelName = self.getSourceFileName()
            if nodeName == None:
                nodeName = self.getSourceNodeName()
        m = loader.loadModel(modelName)
        if m == None:
            print "SpriteParticleRendererExt: Couldn't find model: %s!" % modelName
            return False
        np = m.find(nodeName)
        if np.isEmpty():
            print "SpriteParticleRendererExt: Couldn't find node: %s!" % nodeName
            m.removeNode()
            return False
        self.addFromNode(np, modelName, nodeName, sizeFromTexels)
        m.removeNode()
        return True