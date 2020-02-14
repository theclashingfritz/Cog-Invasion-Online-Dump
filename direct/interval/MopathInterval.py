# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.interval.MopathInterval
__all__ = [
 'MopathInterval']
import LerpInterval
from panda3d.core import *
from panda3d.direct import *
from direct.directnotify.DirectNotifyGlobal import *

class MopathInterval(LerpInterval.LerpFunctionInterval):
    mopathNum = 1
    notify = directNotify.newCategory('MopathInterval')

    def __init__(self, mopath, node, fromT=0, toT=None, duration=None, blendType='noBlend', name=None):
        if toT == None:
            toT = mopath.getMaxT()
        if duration == None:
            duration = abs(toT - fromT)
        if name == None:
            name = 'Mopath-%d' % MopathInterval.mopathNum
            MopathInterval.mopathNum += 1
        LerpInterval.LerpFunctionInterval.__init__(self, self.__doMopath, fromData=fromT, toData=toT, duration=duration, blendType=blendType, name=name)
        self.mopath = mopath
        self.node = node
        return

    def destroy(self):
        self.function = None
        return

    def __doMopath(self, t):
        self.mopath.goTo(self.node, t)