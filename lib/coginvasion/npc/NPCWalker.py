# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.npc.NPCWalker
from panda3d.core import *
from direct.interval.LerpInterval import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.IntervalGlobal import *

class NPCWalkInterval(LerpPosInterval):
    notify = directNotify.newCategory('NPCWalkInterval')

    def __init__(self, nodePath, pos, durationFactor=0.2, startPos=None, other=None, blendType='noBlend', bakeInStart=1, fluid=0, name=None, lookAtTarget=True, duration=None):
        self.nodePath = nodePath
        self.pos = pos
        if type(pos) != type(Point3()):
            self.notify.warning('pos argument must be of type %s, not of type %s' % (
             type(Point3()), type(pos)))
            return
        if duration is None:
            _distance = (pos.getXy() - (nodePath.getX(), nodePath.getY())).length()
            duration = _distance * durationFactor
        self._duration = duration
        LerpPosInterval.__init__(self, nodePath, duration, pos, startPos, other, blendType, bakeInStart, fluid, name)
        if lookAtTarget:
            self.nodePath.headsUp(self.pos)
        return

    def setDuration(self, duration):
        self._duration = duration


class NPCLookInterval(LerpHprInterval):
    notify = directNotify.newCategory('NPCLookInterval')

    def __init__(self, nodePath, lookAtNode, durationFactor=0.01, name=None, blendType='noBlend', bakeInStart=1, fluid=0, other=None, isBackwards=False):
        _oldHpr = nodePath.getHpr()
        nodePath.headsUp(lookAtNode)
        _newHpr = nodePath.getHpr()
        nodePath.setHpr(_oldHpr)
        _distance = (_newHpr.getXy() - _oldHpr.getXy()).length()
        self.distance = _distance
        duration = _distance * durationFactor
        self._duration = duration
        LerpHprInterval.__init__(self, nodePath, duration, _newHpr, startHpr=_oldHpr, other=other, blendType=blendType, bakeInStart=bakeInStart, fluid=fluid, name=name)