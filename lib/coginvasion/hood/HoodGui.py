# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.HoodGui
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from lib.coginvasion.globals import CIGlobals
from panda3d.core import *

def fadeText(a, lbl):
    lbl['fg'] = (
     1, 0.3, 0.5, a)


def startFade(lbl):
    LerpFunc(fadeText, fromData=1.0, toData=0.0, duration=1.0, extraArgs=[
     lbl]).start()


def announceHood(hood):
    nameLbl = OnscreenText(text='%s\n%s' % (hood, CIGlobals.Playground), scale=0.15, font=CIGlobals.getMickeyFont(), pos=(0,
                                                                                                                          -0.65), fg=(1,
                                                                                                                                      0.3,
                                                                                                                                      0.5,
                                                                                                                                      1.0))
    Sequence(Wait(2.5), Func(startFade, nameLbl), Wait(1), Func(nameLbl.destroy)).start()