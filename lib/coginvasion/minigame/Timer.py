# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.Timer
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import Sequence, Wait, Func
from lib.coginvasion.globals import CIGlobals

class Timer:

    def __init__(self):
        try:
            self.Timer_initialized
            return
        except:
            self.Timer_initialized = 1

        self.timer = None
        self.timeLbl = None
        self.initTime = 0
        self.zeroCommand = None
        self.time = 0
        self.timerSeq = None
        return

    def setInitialTime(self, initTime):
        self.initTime = initTime

    def getInitialTime(self):
        return self.initTime

    def setZeroCommand(self, command):
        self.zeroCommand = command

    def getZeroCommand(self):
        return self.zeroCommand

    def startTiming(self):
        seq = Sequence()
        for second in range(self.initTime):
            seq.append(Func(self.setTime, self.initTime - second))
            seq.append(Wait(1.0))

        if self.zeroCommand != None:
            seq.append(Func(self.zeroCommand))
        seq.start()
        self.timerSeq = seq
        return

    def stopTiming(self):
        if self.timerSeq:
            self.timerSeq.pause()
            self.timerSeq = None
        return

    def load(self):
        self.unload()
        timer = loader.loadModel('phase_3.5/models/gui/clock_gui.bam')
        self.timer = OnscreenImage(image=timer.find('**/alarm_clock'), pos=(-0.15,
                                                                            0, -0.15), scale=0.4, parent=base.a2dTopRight)
        self.timeLbl = DirectLabel(text='0', parent=self.timer, text_scale=0.3, text_pos=(0,
                                                                                          -0.13), text_font=CIGlobals.getMickeyFont(), text_fg=(1,
                                                                                                                                                0,
                                                                                                                                                0,
                                                                                                                                                1), relief=None)
        timer.removeNode()
        self.timer.setBin('gui-popup', 60)
        del timer
        return

    def unload(self):
        self.stopTiming()
        if self.timer:
            self.timer.destroy()
            self.timer = None
        if self.timeLbl:
            self.timeLbl.destroy()
            self.timeLbl = None
        return

    def cleanup(self):
        self.zeroCommand = None
        self.initTime = None
        self.time = None
        return

    def setTime(self, time):
        self.time = time
        if self.timeLbl:
            self.timeLbl['text'] = str(time)
            if len(str(time)) > 2:
                self.timeLbl['text_scale'] = 0.2
                self.timeLbl['text_pos'] = (0, -0.11)
            else:
                self.timeLbl['text_scale'] = 0.3
                self.timeLbl['text_pos'] = (0, -0.13)