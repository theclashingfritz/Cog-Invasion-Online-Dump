# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.interval.FunctionInterval
__all__ = [
 'FunctionInterval', 'EventInterval', 'AcceptInterval', 'IgnoreInterval', 'ParentInterval', 'WrtParentInterval', 'PosInterval', 'HprInterval', 'ScaleInterval', 'PosHprInterval', 'HprScaleInterval', 'PosHprScaleInterval', 'Func', 'Wait']
from panda3d.core import *
from panda3d.direct import *
from direct.showbase.MessengerGlobal import *
from direct.directnotify.DirectNotifyGlobal import directNotify
import Interval

class FunctionInterval(Interval.Interval):
    functionIntervalNum = 1
    notify = directNotify.newCategory('FunctionInterval')

    def __init__(self, function, **kw):
        name = kw.pop('name', None)
        openEnded = kw.pop('openEnded', 1)
        extraArgs = kw.pop('extraArgs', [])
        self.function = function
        if name is None:
            name = self.makeUniqueName(function)
        self.extraArgs = extraArgs
        self.kw = kw
        Interval.Interval.__init__(self, name, duration=0.0, openEnded=openEnded)
        return

    @staticmethod
    def makeUniqueName(func, suffix=''):
        name = 'Func-%s-%d' % (getattr(func, '__name__', str(func)), FunctionInterval.functionIntervalNum)
        FunctionInterval.functionIntervalNum += 1
        if suffix:
            name = '%s-%s' % (name, str(suffix))
        return name

    def privInstant(self):
        self.function(*self.extraArgs, **self.kw)
        self.notify.debug('updateFunc() - %s: executing Function' % self.name)


class EventInterval(FunctionInterval):

    def __init__(self, event, sentArgs=[]):

        def sendFunc(event=event, sentArgs=sentArgs):
            messenger.send(event, sentArgs)

        FunctionInterval.__init__(self, sendFunc, name=event)


class AcceptInterval(FunctionInterval):

    def __init__(self, dirObj, event, function, name=None):

        def acceptFunc(dirObj=dirObj, event=event, function=function):
            dirObj.accept(event, function)

        if name == None:
            name = 'Accept-' + event
        FunctionInterval.__init__(self, acceptFunc, name=name)
        return


class IgnoreInterval(FunctionInterval):

    def __init__(self, dirObj, event, name=None):

        def ignoreFunc(dirObj=dirObj, event=event):
            dirObj.ignore(event)

        if name == None:
            name = 'Ignore-' + event
        FunctionInterval.__init__(self, ignoreFunc, name=name)
        return


class ParentInterval(FunctionInterval):
    parentIntervalNum = 1

    def __init__(self, nodePath, parent, name=None):

        def reparentFunc(nodePath=nodePath, parent=parent):
            nodePath.reparentTo(parent)

        if name == None:
            name = 'ParentInterval-%d' % ParentInterval.parentIntervalNum
            ParentInterval.parentIntervalNum += 1
        FunctionInterval.__init__(self, reparentFunc, name=name)
        return


class WrtParentInterval(FunctionInterval):
    wrtParentIntervalNum = 1

    def __init__(self, nodePath, parent, name=None):

        def wrtReparentFunc(nodePath=nodePath, parent=parent):
            nodePath.wrtReparentTo(parent)

        if name == None:
            name = 'WrtParentInterval-%d' % WrtParentInterval.wrtParentIntervalNum
            WrtParentInterval.wrtParentIntervalNum += 1
        FunctionInterval.__init__(self, wrtReparentFunc, name=name)
        return


class PosInterval(FunctionInterval):
    posIntervalNum = 1

    def __init__(self, nodePath, pos, duration=0.0, name=None, other=None):

        def posFunc(np=nodePath, pos=pos, other=other):
            if other:
                np.setPos(other, pos)
            else:
                np.setPos(pos)

        if name == None:
            name = 'PosInterval-%d' % PosInterval.posIntervalNum
            PosInterval.posIntervalNum += 1
        FunctionInterval.__init__(self, posFunc, name=name)
        return


class HprInterval(FunctionInterval):
    hprIntervalNum = 1

    def __init__(self, nodePath, hpr, duration=0.0, name=None, other=None):

        def hprFunc(np=nodePath, hpr=hpr, other=other):
            if other:
                np.setHpr(other, hpr)
            else:
                np.setHpr(hpr)

        if name == None:
            name = 'HprInterval-%d' % HprInterval.hprIntervalNum
            HprInterval.hprIntervalNum += 1
        FunctionInterval.__init__(self, hprFunc, name=name)
        return


class ScaleInterval(FunctionInterval):
    scaleIntervalNum = 1

    def __init__(self, nodePath, scale, duration=0.0, name=None, other=None):

        def scaleFunc(np=nodePath, scale=scale, other=other):
            if other:
                np.setScale(other, scale)
            else:
                np.setScale(scale)

        if name == None:
            name = 'ScaleInterval-%d' % ScaleInterval.scaleIntervalNum
            ScaleInterval.scaleIntervalNum += 1
        FunctionInterval.__init__(self, scaleFunc, name=name)
        return


class PosHprInterval(FunctionInterval):
    posHprIntervalNum = 1

    def __init__(self, nodePath, pos, hpr, duration=0.0, name=None, other=None):

        def posHprFunc(np=nodePath, pos=pos, hpr=hpr, other=other):
            if other:
                np.setPosHpr(other, pos, hpr)
            else:
                np.setPosHpr(pos, hpr)

        if name == None:
            name = 'PosHprInterval-%d' % PosHprInterval.posHprIntervalNum
            PosHprInterval.posHprIntervalNum += 1
        FunctionInterval.__init__(self, posHprFunc, name=name)
        return


class HprScaleInterval(FunctionInterval):
    hprScaleIntervalNum = 1

    def __init__(self, nodePath, hpr, scale, duration=0.0, name=None, other=None):

        def hprScaleFunc(np=nodePath, hpr=hpr, scale=scale, other=other):
            if other:
                np.setHprScale(other, hpr, scale)
            else:
                np.setHprScale(hpr, scale)

        if name == None:
            name = 'HprScale-%d' % HprScaleInterval.hprScaleIntervalNum
            HprScaleInterval.hprScaleIntervalNum += 1
        FunctionInterval.__init__(self, hprScaleFunc, name=name)
        return


class PosHprScaleInterval(FunctionInterval):
    posHprScaleIntervalNum = 1

    def __init__(self, nodePath, pos, hpr, scale, duration=0.0, name=None, other=None):

        def posHprScaleFunc(np=nodePath, pos=pos, hpr=hpr, scale=scale, other=other):
            if other:
                np.setPosHprScale(other, pos, hpr, scale)
            else:
                np.setPosHprScale(pos, hpr, scale)

        if name == None:
            name = 'PosHprScale-%d' % PosHprScaleInterval.posHprScaleIntervalNum
            PosHprScaleInterval.posHprScaleIntervalNum += 1
        FunctionInterval.__init__(self, posHprScaleFunc, name=name)
        return


class Func(FunctionInterval):

    def __init__(self, *args, **kw):
        function = args[0]
        extraArgs = args[1:]
        kw['extraArgs'] = extraArgs
        FunctionInterval.__init__(self, function, **kw)


class Wait(WaitInterval):

    def __init__(self, duration):
        WaitInterval.__init__(self, duration)