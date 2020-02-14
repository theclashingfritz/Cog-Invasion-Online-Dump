# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.book.OptionPage
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.manager.SettingsManager import SettingsManager
from direct.fsm.StateData import StateData
from direct.fsm.State import State
from direct.fsm.ClassicFSM import ClassicFSM
from direct.gui.DirectGui import DirectLabel, DirectButton, DirectRadioButton
from direct.gui.DirectGui import DirectSlider, DGG
from panda3d.core import loadPrcFileData, AntialiasAttrib, TextNode
qt_btn = loader.loadModel('phase_3/models/gui/quit_button.bam')

class OptionPage(StateData):

    def __init__(self, book, parentFSM):
        self.book = book
        self.parentFSM = parentFSM
        StateData.__init__(self, 'optionPageDone')
        self.fsm = ClassicFSM('OptionPage', [State('off', self.enterOff, self.exitOff),
         State('basePage', self.enterBasePage, self.exitBasePage),
         State('displayPage', self.enterDisplayPage, self.exitDisplayPage)], 'off', 'off')
        self.fsm.enterInitialState()
        self.parentFSM.getStateNamed('optionPage').addChild(self.fsm)

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def load(self):
        StateData.load(self)

    def unload(self):
        StateData.unload(self)

    def enter(self):
        StateData.enter(self)
        self.fsm.request('basePage')

    def exit(self):
        self.fsm.request('off')
        StateData.exit(self)

    def openDisplayPage(self):
        self.fsm.request('displayPage')

    def enterDisplayPage(self):
        self.book.createPageButtons(False, False)
        self.book.setTitle('Display Options')
        dialog_gui = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui.bam')
        width, height, fs, music, sfx, tex_detail, model_detail, aa, af = SettingsManager().getSettings('settings.json')
        self.width = width
        self.height = height
        self.windowType = [fs]
        self.buttons = [
         DirectRadioButton(text='Windowed', variable=self.windowType, value=[False], scale=0.1, pos=(-0.45,
                                                                                            0.15,
                                                                                            0.15)),
         DirectRadioButton(text='Fullscreen', variable=self.windowType, value=[True], scale=0.1, pos=(-0.45,
                                                                                             -0.15,
                                                                                             -0.15))]
        for button in self.buttons:
            button.setOthers(self.buttons)

        self.resoLbl = DirectLabel(text='%sx%s' % (width, height), scale=0.08, relief=None, pos=(0.25,
                                                                                                 0,
                                                                                                 0))
        self.resSlider = DirectSlider(range=(0, 200), pageSize=50, command=self.setResoText, scale=0.3, orientation=DGG.VERTICAL, pos=(0.6,
                                                                                                                                       0,
                                                                                                                                       0))
        self.okBtn = DirectButton(text='OK', geom=CIGlobals.getOkayBtnGeom(), relief=None, pos=(-0.5,
                                                                                                -0.5,
                                                                                                -0.5), text_scale=0.05, text_pos=(0,
                                                                                                                                  -0.11), command=self.applyDisplaySettings)
        self.cancelBtn = DirectButton(text='Cancel', geom=CIGlobals.getCancelBtnGeom(), relief=None, pos=(-0.3,
                                                                                                          -0.5,
                                                                                                          -0.5), text_scale=0.05, text_pos=(0,
                                                                                                                                            -0.11), command=self.cancelDisplaySettings)
        if self.resoLbl['text'] == '640x480':
            self.resSlider['value'] = 0
        else:
            if self.resoLbl['text'] == '800x600':
                self.resSlider['value'] = 50
            else:
                if self.resoLbl['text'] == '1024x768':
                    self.resSlider['value'] = 100
                else:
                    if self.resoLbl['text'] == '1280x1024':
                        self.resSlider['value'] = 150
                    else:
                        if self.resoLbl['text'] == '1600x1200':
                            self.resSlider['value'] = 200
        return

    def exitDisplayPage(self):
        for button in self.buttons:
            button.destroy()
            del button

        self.resoLbl.destroy()
        del self.resoLbl
        self.resSlider.destroy()
        del self.resSlider
        self.okBtn.destroy()
        del self.okBtn
        self.cancelBtn.destroy()
        del self.cancelBtn
        del self.width
        del self.height
        del self.windowType
        del self.buttons
        self.book.clearTitle()

    def changeSetting(self, setting, value):
        if setting == 'music':
            if value:
                value = False
            else:
                if not value:
                    value = True
            base.enableMusic(value)
            self.music_btn['extraArgs'] = ['music', value]
            if value:
                valueTxt = 'On'
            else:
                valueTxt = 'Off'
            self.music_lbl['text'] = str(valueTxt).capitalize()
        else:
            if setting == 'sfx':
                if value:
                    value = False
                else:
                    if not value:
                        value = True
                base.enableSoundEffects(value)
                self.sfx_btn['extraArgs'] = ['sfx', value]
                if value:
                    valueTxt = 'On'
                else:
                    valueTxt = 'Off'
                self.sfx_lbl['text'] = str(valueTxt).capitalize()
            else:
                if setting == 'model-detail':
                    if value == 'high':
                        value = 'low'
                    else:
                        if value == 'medium':
                            value = 'high'
                        else:
                            if value == 'low':
                                value = 'medium'
                    self.moddet_lbl['text'] = value.capitalize()
                    self.moddet_btn['extraArgs'] = ['model-detail', value]
                else:
                    if setting == 'texture-detail':
                        if value == 'normal':
                            value = 'low'
                            loadPrcFileData('', 'compressed-textures 1')
                        else:
                            if value == 'low':
                                value = 'normal'
                                loadPrcFileData('', 'compressed-textures 0')
                        self.texdet_lbl['text'] = value.capitalize()
                        self.texdet_btn['extraArgs'] = ['texture-detail', value]
                    else:
                        if setting == 'aa':
                            if value == 'on':
                                value = 'off'
                                render.clear_antialias()
                            else:
                                if value == 'off':
                                    value = 'on'
                                    render.set_antialias(AntialiasAttrib.MAuto)
                            self.aa_lbl['text'] = value.capitalize()
                            self.aa_btn['extraArgs'] = ['aa', value]
                        else:
                            if setting == 'af':
                                if value == 'on':
                                    value = 'off'
                                else:
                                    if value == 'off':
                                        value = 'on'
                                self.af_lbl['text'] = value.capitalize()
                                self.af_btn['extraArgs'] = ['af', value]
        SettingsManager().writeSettingToFile(setting, value, 'settings.json')

    def setResoText(self):
        if self.resSlider['value'] == 200:
            self.width = 1600
            self.height = 1200
        else:
            if 150 <= self.resSlider['value'] <= 199:
                self.width = 1280
                self.height = 1024
            else:
                if 100 <= self.resSlider['value'] <= 149:
                    self.width = 1024
                    self.height = 768
                else:
                    if 50 <= self.resSlider['value'] <= 99:
                        self.width = 800
                        self.height = 600
                    else:
                        if self.resSlider['value'] == 0:
                            self.width = 640
                            self.height = 480
        self.resoLbl['text'] = str(self.width) + 'x' + str(self.height)

    def applyDisplaySettings(self):
        SettingsManager().writeSettingToFile('resolution', (self.width, self.height), 'settings.json', apply=1)
        SettingsManager().writeSettingToFile('fullscreen', self.windowType, 'settings.json', apply=1)
        self.fsm.request('basePage')

    def cancelDisplaySettings(self):
        self.fsm.request('basePage')

    def enterBasePage(self):
        self.book.createPageButtons(None, 'districtPage')
        self.book.setTitle('Options')
        width, height, fs, music, sfx, tex_detail, model_detail, aa, af = SettingsManager().getSettings('settings.json')
        if music:
            musicTxt = 'On'
        else:
            musicTxt = 'Off'
        if sfx:
            sfxTxt = 'On'
        else:
            sfxTxt = 'Off'
        if fs:
            fsTxt = 'On'
        else:
            fsTxt = 'Off'
        self.music_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
         qt_btn.find('**/QuitBtn_DN'),
         qt_btn.find('**/QuitBtn_RLVR')), relief=None, text='Music', scale=1, text_scale=0.055, command=self.changeSetting, extraArgs=['music', music], pos=(-0.45,
                                                                                                                                                             0.55,
                                                                                                                                                             0.55), text_pos=(0,
                                                                                                                                                                              -0.01))
        self.music_lbl = DirectLabel(relief=None, scale=0.09, pos=(0.45, 0.55, 0.52), text_align=TextNode.ACenter)
        self.music_lbl['text'] = str(musicTxt).capitalize()
        self.sfx_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
         qt_btn.find('**/QuitBtn_DN'),
         qt_btn.find('**/QuitBtn_RLVR')), relief=None, text='SFX', scale=1, text_scale=0.055, command=self.changeSetting, extraArgs=['sfx', sfx], pos=(-0.45,
                                                                                                                                                       0.45,
                                                                                                                                                       0.45), text_pos=(0,
                                                                                                                                                                        -0.01))
        self.sfx_lbl = DirectLabel(relief=None, scale=0.09, pos=(0.45, 0.45, 0.42), text_align=TextNode.ACenter)
        self.sfx_lbl['text'] = str(sfxTxt).capitalize()
        self.moddet_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
         qt_btn.find('**/QuitBtn_DN'),
         qt_btn.find('**/QuitBtn_RLVR')), relief=None, text='Model Detail', scale=1, text_scale=0.055, command=self.changeSetting, extraArgs=['model-detail', model_detail], pos=(-0.45,
                                                                                                                                                                                  0.35,
                                                                                                                                                                                  0.35), text_pos=(0,
                                                                                                                                                                                                   -0.01))
        self.moddet_lbl = DirectLabel(relief=None, scale=0.09, pos=(0.45, 0.35, 0.32), text_align=TextNode.ACenter)
        self.moddet_lbl['text'] = model_detail.capitalize()
        self.moddet_btn.bind(DGG.ENTER, self.createMustRestartGui)
        self.moddet_btn.bind(DGG.EXIT, self.removeMustRestartGui)
        self.texdet_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
         qt_btn.find('**/QuitBtn_DN'),
         qt_btn.find('**/QuitBtn_RLVR')), relief=None, text='Texture Detail', scale=1, text_scale=0.0535, command=self.changeSetting, extraArgs=['texture-detail', tex_detail], pos=(-0.45,
                                                                                                                                                                                     0.25,
                                                                                                                                                                                     0.25), text_pos=(0,
                                                                                                                                                                                                      -0.01))
        self.texdet_lbl = DirectLabel(relief=None, scale=0.09, pos=(0.45, 0.25, 0.22), text_align=TextNode.ACenter)
        self.texdet_lbl['text'] = tex_detail.capitalize()
        self.texdet_btn.bind(DGG.ENTER, self.createMustRestartGui)
        self.texdet_btn.bind(DGG.EXIT, self.removeMustRestartGui)
        self.display_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
         qt_btn.find('**/QuitBtn_DN'),
         qt_btn.find('**/QuitBtn_RLVR')), relief=None, text='Display', command=self.openDisplayPage, scale=1, text_scale=0.0535, pos=(-0.45,
                                                                                                                                      -0.25,
                                                                                                                                      0.02), text_pos=(0,
                                                                                                                                                       -0.01))
        self.display_lbl = DirectLabel(relief=None, scale=0.06, pos=(0.45, -0.25, 0.02), text_align=TextNode.ACenter)
        self.display_lbl['text'] = 'Fullscreen: %s\nResolution: %s' % (str(fsTxt).capitalize(), (width, height))
        self.aa_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
         qt_btn.find('**/QuitBtn_DN'),
         qt_btn.find('**/QuitBtn_RLVR')), relief=None, text='Anti-Aliasing', command=self.changeSetting, extraArgs=['aa', aa], scale=1, text_scale=0.0535, pos=(-0.45,
                                                                                                                                                                -0.35,
                                                                                                                                                                -0.18), text_pos=(0,
                                                                                                                                                                                  -0.01))
        self.aa_lbl = DirectLabel(relief=None, scale=0.09, pos=(0.45, -0.35, -0.21), text_align=TextNode.ACenter)
        self.aa_lbl['text'] = aa.capitalize()
        self.af_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
         qt_btn.find('**/QuitBtn_DN'),
         qt_btn.find('**/QuitBtn_RLVR')), relief=None, text='Anisotropic Filtering', command=self.changeSetting, extraArgs=['af', af], scale=1, text_scale=0.0435, pos=(-0.45,
                                                                                                                                                                        -0.35,
                                                                                                                                                                        -0.28), text_pos=(0,
                                                                                                                                                                                          -0.01))
        self.af_lbl = DirectLabel(relief=None, scale=0.09, pos=(0.45, -0.35, -0.31), text_align=TextNode.ACenter)
        self.af_lbl['text'] = af.capitalize()
        self.af_btn.bind(DGG.ENTER, self.createMustRestartGui)
        self.af_btn.bind(DGG.EXIT, self.removeMustRestartGui)
        self.exit_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
         qt_btn.find('**/QuitBtn_DN'),
         qt_btn.find('**/QuitBtn_RLVR')), relief=None, text='Exit Toontown', scale=1.2, text_scale=0.0535, command=self.book.finished, extraArgs=['exit'], pos=(-0.45,
                                                                                                                                                                -0.65,
                                                                                                                                                                -0.6), text_pos=(0,
                                                                                                                                                                                 -0.01))
        return

    def createMustRestartGui(self, foo):
        self.mustRestartLbl = DirectLabel(text='Changing this setting requires a game restart.', text_fg=(0.9,
                                                                                                          0,
                                                                                                          0,
                                                                                                          1), text_shadow=(0,
                                                                                                                           0,
                                                                                                                           0,
                                                                                                                           1), text_scale=0.06, text_align=TextNode.ACenter, pos=(0,
                                                                                                                                                                                  0,
                                                                                                                                                                                  -0.435), relief=None)
        return

    def removeMustRestartGui(self, foo):
        if hasattr(self, 'mustRestartLbl'):
            self.mustRestartLbl.destroy()
            del self.mustRestartLbl

    def exitBasePage(self):
        self.music_btn.destroy()
        del self.music_btn
        self.sfx_btn.destroy()
        del self.sfx_btn
        self.moddet_btn.destroy()
        del self.moddet_btn
        self.texdet_btn.destroy()
        del self.texdet_btn
        self.display_btn.destroy()
        del self.display_btn
        self.aa_btn.destroy()
        del self.aa_btn
        self.exit_btn.destroy()
        del self.exit_btn
        self.music_lbl.destroy()
        del self.music_lbl
        self.sfx_lbl.destroy()
        del self.sfx_lbl
        self.moddet_lbl.destroy()
        del self.moddet_lbl
        self.texdet_lbl.destroy()
        del self.texdet_lbl
        self.display_lbl.destroy()
        del self.display_lbl
        self.aa_lbl.destroy()
        del self.aa_lbl
        self.af_btn.destroy()
        del self.af_btn
        self.af_lbl.destroy()
        del self.af_lbl
        self.book.deletePageButtons(False, True)
        self.book.clearTitle()