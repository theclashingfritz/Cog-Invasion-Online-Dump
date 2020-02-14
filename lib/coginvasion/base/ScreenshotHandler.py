# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.base.ScreenshotHandler
from datetime import datetime
from panda3d.core import Filename
from direct.interval.IntervalGlobal import Sequence, Wait, Func
import threading
FILEPATH = 'screenshots/'
flashSeq = Sequence()
flashSfx = None

def __doEffects():
    global flashSfx
    if not flashSfx:
        flashSfx = base.loadSfx('phase_4/audio/sfx/Photo_shutter.ogg')
    flashSeq = Sequence(Func(flashSfx.play), Func(base.transitions.setFadeColor, 1, 1, 1), Func(base.transitions.fadeOut, 0.1), Wait(0.1), Func(base.transitions.fadeIn, 0.1), Wait(0.1), Func(base.transitions.setFadeColor, 0, 0, 0))
    flashSeq.start()


def __saveScreenshot(shot):
    now = datetime.now().strftime(FILEPATH + 'screenshot-%a-%b-%d-%Y-%I-%M-%S-%f')
    shot.write(Filename(now + '.jpeg'))


def __takeScreenshot():
    shot = base.win.getScreenshot()
    thread = threading.Thread(target=__saveScreenshot, args=(shot,))
    thread.start()
    __doEffects()