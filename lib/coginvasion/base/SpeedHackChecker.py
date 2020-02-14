# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.base.SpeedHackChecker
import sys, time
from panda3d.core import TrueClock
lastSpeedHackCheck = time.time()
lastTrueClockTime = TrueClock.getGlobalPtr().getLongTime()

def __speedHackCheckTask(task):
    global lastSpeedHackCheck
    global lastTrueClockTime
    elapsed = time.time() - lastSpeedHackCheck
    tcElapsed = TrueClock.getGlobalPtr().getLongTime() - lastTrueClockTime
    if tcElapsed > elapsed + 0.05:
        print 'Detected speed hacks, closing game.'
        sys.exit()
        return task.done
    lastSpeedHackCheck = time.time()
    lastTrueClockTime = TrueClock.getGlobalPtr().getLongTime()
    return task.cont


def startChecking():
    taskMgr.add(__speedHackCheckTask, 'speedHackCheckTask')


def stopChecking():
    taskMgr.remove('speedHackCheckTask')