# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.Loader
__all__ = [
 'Loader']
from panda3d.core import *
from panda3d.core import Loader as PandaLoader
from direct.directnotify.DirectNotifyGlobal import *
from direct.showbase.DirectObject import DirectObject
import types
phaseChecker = None

class Loader(DirectObject):
    notify = directNotify.newCategory('Loader')
    loaderIndex = 0

    class Callback:

        def __init__(self, numObjects, gotList, callback, extraArgs):
            self.objects = [
             None] * numObjects
            self.gotList = gotList
            self.callback = callback
            self.extraArgs = extraArgs
            self.numRemaining = numObjects
            self.cancelled = False
            self.requests = {}
            return

        def gotObject(self, index, object):
            self.objects[index] = object
            self.numRemaining -= 1
            if self.numRemaining == 0:
                if self.gotList:
                    self.callback(self.objects, *self.extraArgs)
                else:
                    self.callback(*(self.objects + self.extraArgs))

    def __init__(self, base):
        self.base = base
        self.loader = PandaLoader.getGlobalPtr()
        self.hook = 'async_loader_%s' % Loader.loaderIndex
        Loader.loaderIndex += 1
        self.accept(self.hook, self.__gotAsyncObject)

    def destroy(self):
        self.ignore(self.hook)
        self.loader.stopThreads()
        del self.base
        del self.loader

    def loadModel(self, modelPath, loaderOptions=None, noCache=None, allowInstance=False, okMissing=None, callback=None, extraArgs=[], priority=None):
        if loaderOptions == None:
            loaderOptions = LoaderOptions()
        else:
            loaderOptions = LoaderOptions(loaderOptions)
        if okMissing is not None:
            if okMissing:
                loaderOptions.setFlags(loaderOptions.getFlags() & ~LoaderOptions.LFReportErrors)
            else:
                loaderOptions.setFlags(loaderOptions.getFlags() | LoaderOptions.LFReportErrors)
        else:
            okMissing = loaderOptions.getFlags() & LoaderOptions.LFReportErrors == 0
        if noCache is not None:
            if noCache:
                loaderOptions.setFlags(loaderOptions.getFlags() | LoaderOptions.LFNoCache)
            else:
                loaderOptions.setFlags(loaderOptions.getFlags() & ~LoaderOptions.LFNoCache)
        if allowInstance:
            loaderOptions.setFlags(loaderOptions.getFlags() | LoaderOptions.LFAllowInstance)
        if isinstance(modelPath, types.StringTypes) or isinstance(modelPath, Filename):
            modelList = [modelPath]
            if phaseChecker:
                phaseChecker(modelPath, loaderOptions)
            gotList = False
        else:
            modelList = modelPath
            gotList = True
        if callback is None:
            result = []
            for modelPath in modelList:
                node = self.loader.loadSync(Filename(modelPath), loaderOptions)
                if node != None:
                    nodePath = NodePath(node)
                else:
                    nodePath = None
                result.append(nodePath)

            if not okMissing and None in result:
                message = 'Could not load model file(s): %s' % (modelList,)
                raise IOError, message
            if gotList:
                return result
            return result[0]
        else:
            cb = Loader.Callback(len(modelList), gotList, callback, extraArgs)
            i = 0
            for modelPath in modelList:
                request = self.loader.makeAsyncRequest(Filename(modelPath), loaderOptions)
                if priority is not None:
                    request.setPriority(priority)
                request.setDoneEvent(self.hook)
                request.setPythonObject((cb, i))
                i += 1
                self.loader.loadAsync(request)
                cb.requests[request] = True

            return cb
        return

    def cancelRequest(self, cb):
        if not cb.cancelled:
            cb.cancelled = True
            for request in cb.requests:
                self.loader.remove(request)

            cb.requests = None
        return

    def isRequestPending(self, cb):
        return bool(cb.requests)

    def loadModelOnce(self, modelPath):
        Loader.notify.info('loader.loadModelOnce() is deprecated; use loader.loadModel() instead.')
        return self.loadModel(modelPath, noCache=False)

    def loadModelCopy(self, modelPath, loaderOptions=None):
        Loader.notify.info('loader.loadModelCopy() is deprecated; use loader.loadModel() instead.')
        return self.loadModel(modelPath, loaderOptions=loaderOptions, noCache=False)

    def loadModelNode(self, modelPath):
        Loader.notify.info('loader.loadModelNode() is deprecated; use loader.loadModel() instead.')
        model = self.loadModel(modelPath, noCache=False)
        if model is not None:
            model = model.node()
        return model

    def unloadModel(self, model):
        if isinstance(model, NodePath):
            modelNode = model.node()
        else:
            if isinstance(model, ModelNode):
                modelNode = model
            else:
                if isinstance(model, types.StringTypes) or isinstance(model, Filename):
                    options = LoaderOptions(LoaderOptions.LFSearch | LoaderOptions.LFNoDiskCache | LoaderOptions.LFCacheOnly)
                    modelNode = self.loader.loadSync(Filename(model), options)
                    if modelNode == None:
                        return
                else:
                    raise 'Invalid parameter to unloadModel: %s' % model
        ModelPool.releaseModel(modelNode)
        return

    def saveModel(self, modelPath, node, loaderOptions=None, callback=None, extraArgs=[], priority=None):
        if loaderOptions == None:
            loaderOptions = LoaderOptions()
        else:
            loaderOptions = LoaderOptions(loaderOptions)
        if isinstance(modelPath, types.StringTypes) or isinstance(modelPath, Filename):
            modelList = [modelPath]
            nodeList = [node]
            if phaseChecker:
                phaseChecker(modelPath, loaderOptions)
            gotList = False
        else:
            modelList = modelPath
            nodeList = node
            gotList = True
        for i in range(len(nodeList)):
            if isinstance(nodeList[i], NodePath):
                nodeList[i] = nodeList[i].node()

        modelList = zip(modelList, nodeList)
        if callback is None:
            result = []
            for modelPath, node in modelList:
                thisResult = self.loader.saveSync(Filename(modelPath), loaderOptions, node)
                result.append(thisResult)

            if gotList:
                return result
            return result[0]
        else:
            cb = Loader.Callback(len(modelList), gotList, callback, extraArgs)
            i = 0
            for modelPath, node in modelList:
                request = self.loader.makeAsyncSaveRequest(Filename(modelPath), loaderOptions, node)
                if priority is not None:
                    request.setPriority(priority)
                request.setDoneEvent(self.hook)
                request.setPythonObject((cb, i))
                i += 1
                self.loader.saveAsync(request)
                cb.requests[request] = True

            return cb
        return

    def loadFont(self, modelPath, spaceAdvance=None, lineHeight=None, pointSize=None, pixelsPerUnit=None, scaleFactor=None, textureMargin=None, polyMargin=None, minFilter=None, magFilter=None, anisotropicDegree=None, color=None, outlineWidth=None, outlineFeather=0.1, outlineColor=VBase4(0, 0, 0, 1), renderMode=None, okMissing=False):
        if phaseChecker:
            loaderOptions = LoaderOptions()
            if okMissing:
                loaderOptions.setFlags(loaderOptions.getFlags() & ~LoaderOptions.LFReportErrors)
            phaseChecker(modelPath, loaderOptions)
        font = FontPool.loadFont(modelPath)
        if font == None:
            if not okMissing:
                message = 'Could not load font file: %s' % modelPath
                raise IOError, message
            font = StaticTextFont(PandaNode('empty'))
        if hasattr(font, 'setPointSize'):
            if pointSize != None:
                font.setPointSize(pointSize)
            if pixelsPerUnit != None:
                font.setPixelsPerUnit(pixelsPerUnit)
            if scaleFactor != None:
                font.setScaleFactor(scaleFactor)
            if textureMargin != None:
                font.setTextureMargin(textureMargin)
            if polyMargin != None:
                font.setPolyMargin(polyMargin)
            if minFilter != None:
                font.setMinfilter(minFilter)
            if magFilter != None:
                font.setMagfilter(magFilter)
            if anisotropicDegree != None:
                font.setAnisotropicDegree(anisotropicDegree)
            if color:
                font.setFg(color)
                font.setBg(VBase4(color[0], color[1], color[2], 0.0))
            if outlineWidth:
                font.setOutline(outlineColor, outlineWidth, outlineFeather)
                font.setBg(VBase4(outlineColor[0], outlineColor[1], outlineColor[2], 0.0))
            if renderMode:
                font.setRenderMode(renderMode)
        if lineHeight is not None:
            font.setLineHeight(lineHeight)
        if spaceAdvance is not None:
            font.setSpaceAdvance(spaceAdvance)
        return font

    def loadTexture(self, texturePath, alphaPath=None, readMipmaps=False, okMissing=False, minfilter=None, magfilter=None, anisotropicDegree=None, loaderOptions=None, multiview=None):
        if loaderOptions == None:
            loaderOptions = LoaderOptions()
        else:
            loaderOptions = LoaderOptions(loaderOptions)
        if multiview is not None:
            flags = loaderOptions.getTextureFlags()
            if multiview:
                flags |= LoaderOptions.TFMultiview
            else:
                flags &= ~LoaderOptions.TFMultiview
            loaderOptions.setTextureFlags(flags)
        if alphaPath is None:
            texture = TexturePool.loadTexture(texturePath, 0, readMipmaps, loaderOptions)
        else:
            texture = TexturePool.loadTexture(texturePath, alphaPath, 0, 0, readMipmaps, loaderOptions)
        if not texture and not okMissing:
            message = 'Could not load texture: %s' % texturePath
            raise IOError, message
        if minfilter is not None:
            texture.setMinfilter(minfilter)
        if magfilter is not None:
            texture.setMagfilter(magfilter)
        if anisotropicDegree is not None:
            texture.setAnisotropicDegree(anisotropicDegree)
        return texture

    def load3DTexture(self, texturePattern, readMipmaps=False, okMissing=False, minfilter=None, magfilter=None, anisotropicDegree=None, loaderOptions=None, multiview=None, numViews=2):
        if loaderOptions == None:
            loaderOptions = LoaderOptions()
        else:
            loaderOptions = LoaderOptions(loaderOptions)
        if multiview is not None:
            flags = loaderOptions.getTextureFlags()
            if multiview:
                flags |= LoaderOptions.TFMultiview
            else:
                flags &= ~LoaderOptions.TFMultiview
            loaderOptions.setTextureFlags(flags)
            loaderOptions.setTextureNumViews(numViews)
        texture = TexturePool.load3dTexture(texturePattern, readMipmaps, loaderOptions)
        if not texture and not okMissing:
            message = 'Could not load 3-D texture: %s' % texturePattern
            raise IOError, message
        if minfilter is not None:
            texture.setMinfilter(minfilter)
        if magfilter is not None:
            texture.setMagfilter(magfilter)
        if anisotropicDegree is not None:
            texture.setAnisotropicDegree(anisotropicDegree)
        return texture

    def loadCubeMap(self, texturePattern, readMipmaps=False, okMissing=False, minfilter=None, magfilter=None, anisotropicDegree=None, loaderOptions=None, multiview=None):
        if loaderOptions == None:
            loaderOptions = LoaderOptions()
        else:
            loaderOptions = LoaderOptions(loaderOptions)
        if multiview is not None:
            flags = loaderOptions.getTextureFlags()
            if multiview:
                flags |= LoaderOptions.TFMultiview
            else:
                flags &= ~LoaderOptions.TFMultiview
            loaderOptions.setTextureFlags(flags)
        texture = TexturePool.loadCubeMap(texturePattern, readMipmaps, loaderOptions)
        if not texture and not okMissing:
            message = 'Could not load cube map: %s' % texturePattern
            raise IOError, message
        if minfilter is not None:
            texture.setMinfilter(minfilter)
        if magfilter is not None:
            texture.setMagfilter(magfilter)
        if anisotropicDegree is not None:
            texture.setAnisotropicDegree(anisotropicDegree)
        return texture

    def unloadTexture(self, texture):
        TexturePool.releaseTexture(texture)

    def loadSfx(self, *args, **kw):
        if self.base.sfxManagerList:
            return self.loadSound(self.base.sfxManagerList[0], *args, **kw)
        return

    def loadMusic(self, *args, **kw):
        if self.base.musicManager:
            return self.loadSound(self.base.musicManager, *args, **kw)
        return
        return

    def loadSound(self, manager, soundPath, positional=False, callback=None, extraArgs=[]):
        if isinstance(soundPath, types.StringTypes) or isinstance(soundPath, Filename):
            soundList = [soundPath]
            gotList = False
        else:
            if isinstance(soundPath, MovieAudio):
                soundList = [
                 soundPath]
                gotList = False
            else:
                soundList = soundPath
                gotList = True
        if callback is None:
            result = []
            for soundPath in soundList:
                sound = manager.getSound(soundPath, positional)
                result.append(sound)

            if gotList:
                return result
            return result[0]
        else:
            cb = Loader.Callback(len(soundList), gotList, callback, extraArgs)
            for i in range(len(soundList)):
                soundPath = soundList[i]
                request = AudioLoadRequest(manager, soundPath, positional)
                request.setDoneEvent(self.hook)
                request.setPythonObject((cb, i))
                self.loader.loadAsync(request)
                cb.requests[request] = True

            return cb
        return

    def unloadSfx(self, sfx):
        if sfx:
            if self.base.sfxManagerList:
                self.base.sfxManagerList[0].uncacheSound(sfx.getName())

    def loadShader(self, shaderPath, okMissing=False):
        shader = ShaderPool.loadShader(shaderPath)
        if not shader and not okMissing:
            message = 'Could not load shader file: %s' % shaderPath
            raise IOError, message
        return shader

    def unloadShader(self, shaderPath):
        if shaderPath != None:
            ShaderPool.releaseShader(shaderPath)
        return

    def asyncFlattenStrong(self, model, inPlace=True, callback=None, extraArgs=[]):
        if isinstance(model, NodePath):
            modelList = [model]
            gotList = False
        else:
            modelList = model
            gotList = True
        if inPlace:
            extraArgs = [
             gotList, callback, modelList, extraArgs]
            callback = self.__asyncFlattenDone
            gotList = True
        cb = Loader.Callback(len(modelList), gotList, callback, extraArgs)
        i = 0
        for model in modelList:
            request = ModelFlattenRequest(model.node())
            request.setDoneEvent(self.hook)
            request.setPythonObject((cb, i))
            i += 1
            self.loader.loadAsync(request)
            cb.requests[request] = True

        return cb

    def __asyncFlattenDone(self, models, gotList, callback, origModelList, extraArgs):
        self.notify.debug('asyncFlattenDone: %s' % (models,))
        for i in range(len(models)):
            origModelList[i].getChildren().detach()
            orig = origModelList[i].node()
            flat = models[i].node()
            orig.copyAllProperties(flat)
            orig.replaceNode(flat)

        if callback:
            if gotList:
                callback(origModelList, *extraArgs)
            else:
                callback(*(origModelList + extraArgs))

    def __gotAsyncObject(self, request):
        cb, i = request.getPythonObject()
        if cb.cancelled:
            return
        del cb.requests[request]
        object = None
        if hasattr(request, 'getModel'):
            node = request.getModel()
            if node != None:
                object = NodePath(node)
        else:
            if hasattr(request, 'getSound'):
                object = request.getSound()
            else:
                if hasattr(request, 'getSuccess'):
                    object = request.getSuccess()
        cb.gotObject(i, object)
        return