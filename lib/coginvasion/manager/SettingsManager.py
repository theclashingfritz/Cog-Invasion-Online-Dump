# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.manager.SettingsManager
from panda3d.core import AntialiasAttrib, TextureStage
from panda3d.core import loadPrcFileData, WindowProperties
from direct.directnotify.DirectNotify import DirectNotify
import json, os
notify = DirectNotify().newCategory('SettingsManager')

class SettingsManager:

    def applySettings(self, jsonfile):
        if not jsonfile:
            raise IOError('no file specified!')
        info = open(jsonfile, 'r')
        jsonInfo = json.load(info)
        settings = jsonInfo['settings']
        width, height = settings['resolution']
        fs = settings['fullscreen']
        music = settings['music']
        sfx = settings['sfx']
        tex_detail = settings['texture-detail']
        model_detail = settings['model-detail']
        aa = settings['aa']
        af = settings.get('af', None)
        if af == None:
            self.writeSettingToFile('af', 'off', 'settings.json')
        base.enableMusic(music)
        base.enableSoundEffects(sfx)
        if aa == 'on':
            render.set_antialias(AntialiasAttrib.MMultisample)
            aspect2d.set_antialias(AntialiasAttrib.MMultisample)
        else:
            render.clear_antialias()
        ts = TextureStage('ts')
        if tex_detail == 'high':
            pass
        else:
            if tex_detail == 'low':
                loadPrcFileData('', 'compressed-textures 1')
        wp = WindowProperties()
        wp.setSize(width, height)
        wp.setFullscreen(fs)
        base.win.requestProperties(wp)
        info.close()
        return

    def maybeFixAA(self):
        if self.getSettings('settings.json')[7] != 'on':
            print 'Fixing anti-aliasing...'
            loadPrcFileData('', 'framebuffer-multisample 0')
            loadPrcFileData('', 'multisamples 0')

    def getSettings(self, jsonfile):
        if jsonfile:
            if not os.path.exists(jsonfile):
                jsonInfo = {'settings': {'aa': 'off', 'fullscreen': False, 'sfx': True, 'af': 'off', 'music': True, 'model-detail': 'high', 'resolution': [640, 480], 'texture-detail': 'normal'}}
                json.dump(jsonInfo, open(jsonfile, 'w'))
            else:
                info = open(jsonfile, 'r')
                jsonInfo = json.load(info)
            settings = jsonInfo['settings']
            width, height = settings['resolution']
            fs = settings['fullscreen']
            music = settings['music']
            sfx = settings['sfx']
            tex_detail = settings['texture-detail']
            model_detail = settings['model-detail']
            aa = settings['aa']
            af = settings['af']
            return tuple((width, height, fs, music, sfx, tex_detail, model_detail, aa, af))
        raise StandardError('no file specified!')

    def writeSettingToFile(self, setting, value, jsonfile, apply=0):
        info = open(jsonfile)
        jsonInfo = json.load(info)
        if setting == 'fullscreen':
            jsonInfo['settings'][setting] = value[0]
        else:
            jsonInfo['settings'][setting] = value
        jsonFile = open(jsonfile, 'w+')
        jsonFile.write(json.dumps(jsonInfo))
        jsonFile.close()
        if apply:
            if setting == 'resolution':
                width, height = value
                wp = WindowProperties()
                wp.setSize(width, height)
                base.win.requestProperties(wp)
            elif setting == 'fullscreen':
                wp = WindowProperties()
                wp.setFullscreen(value[0])
                base.win.requestProperties(wp)
        info.close()