# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gui.Dialog
from direct.gui.DirectGui import *
from lib.coginvasion.globals import CIGlobals
from direct.directnotify.DirectNotifyGlobal import directNotify
import string
NoButtons = 0
YesNo = 1
YesCancel = 2
Ok = 3
Cancel = 4

class Dialog(DirectDialog):

    def __init__(self, parent=None, style=NoButtons, **kw):
        if parent == None:
            parent = aspect2d
        self.style = style
        if self.style == YesNo or self.style == YesCancel:
            okButtons = CIGlobals.getOkayBtnGeom()
            cancelButtons = CIGlobals.getCancelBtnGeom()
            buttonImage = [okButtons, cancelButtons]
            buttonValues = [DGG.DIALOG_OK, DGG.DIALOG_CANCEL]
            if 'buttonText' in kw:
                buttonText = kw['buttonText']
                del kw['buttonText']
            else:
                buttonText = [
                 CIGlobals.DialogYes]
                if self.style == YesNo:
                    buttonText.append(CIGlobals.DialogNo)
                elif self.style == YesCancel:
                    buttonText.append(CIGlobals.DialogCancel)
        else:
            if self.style == Ok:
                okButtons = CIGlobals.getOkayBtnGeom()
                buttonImage = [okButtons]
                buttonText = [CIGlobals.DialogOk]
                buttonValues = [DGG.DIALOG_OK]
            else:
                if self.style == Cancel:
                    cancelButtons = CIGlobals.getCancelBtnGeom()
                    buttonImage = [cancelButtons]
                    buttonText = [CIGlobals.DialogCancel]
                    buttonValues = [DGG.DIALOG_CANCEL]
                else:
                    if self.style == NoButtons:
                        buttonImage = []
                        buttonText = []
                        buttonValues = []
                    else:
                        self.notify.error('Style %s does not exist.' % self.style)
        optiondefs = (
         (
          'buttonImageList', buttonImage, DGG.INITOPT),
         (
          'buttonTextList', buttonText, DGG.INITOPT),
         (
          'buttonValueList', buttonValues, DGG.INITOPT),
         (
          'buttonPadSF', 2.2, DGG.INITOPT),
         (
          'text_font', DGG.getDefaultFont(), None),
         ('text_wordwrap', 18, None),
         ('text_scale', 0.07, None),
         (
          'buttonSize', (-0.05, 0.05, -0.05, 0.05), None),
         (
          'button_pad', (0, 0), None),
         ('button_relief', None, None),
         (
          'button_text_pos', (0, -0.1), None),
         ('fadeScreen', 0.5, None),
         (
          'image_color', CIGlobals.DialogColor, None),
         (
          'image', DGG.getDefaultDialogGeom(), None),
         ('relief', None, None))
        self.defineoptions(kw, optiondefs)
        DirectDialog.__init__(self, parent)
        self.initialiseoptions(Dialog)
        return


class GlobalDialog(Dialog):
    notify = directNotify.newCategory('GlobalDialog')

    def __init__(self, message='', doneEvent=None, style=NoButtons, okButtonText=CIGlobals.DialogOk, cancelButtonText=CIGlobals.DialogCancel, extraArgs=[], **kw):
        self.extraArgs = extraArgs
        self.doneStatus = None
        if doneEvent == None and style != NoButtons:
            self.notify.error('You must specify a doneEvent on a dialog with buttons.')
        self.__doneEvent = doneEvent
        if style == YesNo:
            okButtonText = CIGlobals.DialogYes
            cancelButtonText = CIGlobals.DialogNo
        if style == NoButtons:
            buttonText = []
        else:
            if style == Ok:
                buttonText = [
                 okButtonText]
            else:
                if style == Cancel:
                    buttonText = [
                     cancelButtonText]
                else:
                    buttonText = [
                     okButtonText, cancelButtonText]
        optiondefs = (
         (
          'dialogName', 'globalDialog', DGG.INITOPT),
         (
          'buttonTextList', buttonText, DGG.INITOPT),
         (
          'text', message, None),
         (
          'command', self.handleButton, None))
        self.defineoptions(kw, optiondefs)
        Dialog.__init__(self, style=style)
        self.initialiseoptions(GlobalDialog)
        return

    def handleButton(self, value):
        if value == DGG.DIALOG_OK:
            self.doneStatus = 'ok'
            messenger.send(self.__doneEvent, self.extraArgs)
        else:
            if value == DGG.DIALOG_CANCEL:
                self.doneStatus = 'cancel'
                messenger.send(self.__doneEvent, self.extraArgs)

    def getValue(self):
        if self.doneStatus == 'ok':
            return 1
        if self.doneStatus == 'cancel':
            return 0
        return -1