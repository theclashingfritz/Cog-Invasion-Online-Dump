# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.interval.MetaInterval
__all__ = [
 'MetaInterval', 'Sequence', 'Parallel', 'ParallelEndTogether', 'Track']
from panda3d.core import *
from panda3d.direct import *
from direct.directnotify.DirectNotifyGlobal import *
from IntervalManager import ivalMgr
import Interval
from direct.task.Task import TaskManager
import types
PREVIOUS_END = CMetaInterval.RSPreviousEnd
PREVIOUS_START = CMetaInterval.RSPreviousBegin
TRACK_START = CMetaInterval.RSLevelBegin

class MetaInterval(CMetaInterval):
    notify = directNotify.newCategory('MetaInterval')
    SequenceNum = 1

    def __init__(self, *ivals, **kw):
        name = None
        if 'name' in kw:
            name = kw['name']
            del kw['name']
        autoPause = 0
        autoFinish = 0
        if 'autoPause' in kw:
            autoPause = kw['autoPause']
            del kw['autoPause']
        if 'autoFinish' in kw:
            autoFinish = kw['autoFinish']
            del kw['autoFinish']
        self.phonyDuration = -1
        if 'duration' in kw:
            self.phonyDuration = kw['duration']
            del kw['duration']
        if kw:
            self.notify.error('Unexpected keyword parameters: %s' % kw.keys())
        self.ivals = ivals
        self.__ivalsDirty = 1
        if name == None:
            name = self.__class__.__name__ + '-%d'
        if '%' in name:
            name = name % self.SequenceNum
            MetaInterval.SequenceNum += 1
        CMetaInterval.__init__(self, name)
        self.__manager = ivalMgr
        self.setAutoPause(autoPause)
        self.setAutoFinish(autoFinish)
        self.pstats = None
        if __debug__ and TaskManager.taskTimerVerbose:
            self.pname = name.split('-', 1)[0]
            self.pstats = PStatCollector('App:Show code:ivalLoop:%s' % self.pname)
        self.pythonIvals = []
        return

    def append(self, ival):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        self.ivals.append(ival)
        self.__ivalsDirty = 1

    def extend(self, ivals):
        self += ivals

    def count(self, ival):
        return self.ivals.count(ival)

    def index(self, ival):
        return self.ivals.index(ival)

    def insert(self, index, ival):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        self.ivals.insert(index, ival)
        self.__ivalsDirty = 1

    def pop(self, index=None):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        self.__ivalsDirty = 1
        if index == None:
            return self.ivals.pop()
        return self.ivals.pop(index)
        return

    def remove(self, ival):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        self.ivals.remove(ival)
        self.__ivalsDirty = 1

    def reverse(self):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        self.ivals.reverse()
        self.__ivalsDirty = 1

    def sort(self, cmpfunc=None):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        self.__ivalsDirty = 1
        if cmpfunc == None:
            self.ivals.sort()
        else:
            self.ivals.sort(cmpfunc)
        return

    def __len__(self):
        return len(self.ivals)

    def __getitem__(self, index):
        return self.ivals[index]

    def __setitem__(self, index, value):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        self.ivals[index] = value
        self.__ivalsDirty = 1

    def __delitem__(self, index):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        del self.ivals[index]
        self.__ivalsDirty = 1

    def __getslice__(self, i, j):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        return self.__class__(self.ivals[i:j])

    def __setslice__(self, i, j, s):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        self.ivals[i:j] = s
        self.__ivalsDirty = 1

    def __delslice__(self, i, j):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        del self.ivals[i:j]
        self.__ivalsDirty = 1

    def __iadd__(self, other):
        if isinstance(self.ivals, types.TupleType):
            self.ivals = list(self.ivals)
        if isinstance(other, MetaInterval):
            ivals = other.ivals
        else:
            ivals = list(other)
        self.ivals += ivals
        self.__ivalsDirty = 1
        return self

    def __add__(self, other):
        copy = self[:]
        copy += other
        return copy

    def addSequence(self, list, name, relTime, relTo, duration):
        self.pushLevel(name, relTime, relTo)
        for ival in list:
            self.addInterval(ival, 0.0, PREVIOUS_END)

        self.popLevel(duration)

    def addParallel(self, list, name, relTime, relTo, duration):
        self.pushLevel(name, relTime, relTo)
        for ival in list:
            self.addInterval(ival, 0.0, TRACK_START)

        self.popLevel(duration)

    def addParallelEndTogether(self, list, name, relTime, relTo, duration):
        maxDuration = 0
        for ival in list:
            maxDuration = max(maxDuration, ival.getDuration())

        self.pushLevel(name, relTime, relTo)
        for ival in list:
            self.addInterval(ival, maxDuration - ival.getDuration(), TRACK_START)

        self.popLevel(duration)

    def addTrack(self, list, name, relTime, relTo, duration):
        self.pushLevel(name, relTime, relTo)
        for tuple in list:
            if isinstance(tuple, types.TupleType) or isinstance(tuple, types.ListType):
                relTime = tuple[0]
                ival = tuple[1]
                if len(tuple) >= 3:
                    relTo = tuple[2]
                else:
                    relTo = TRACK_START
                self.addInterval(ival, relTime, relTo)
            else:
                self.notify.error('Not a tuple in Track: %s' % (tuple,))

        self.popLevel(duration)

    def addInterval(self, ival, relTime, relTo):
        if isinstance(ival, CInterval):
            if getattr(ival, 'inPython', 0):
                index = len(self.pythonIvals)
                self.pythonIvals.append(ival)
                self.addExtIndex(index, ival.getName(), ival.getDuration(), ival.getOpenEnded(), relTime, relTo)
            elif isinstance(ival, MetaInterval):
                ival.applyIvals(self, relTime, relTo)
            else:
                self.addCInterval(ival, relTime, relTo)
        else:
            if isinstance(ival, Interval.Interval):
                index = len(self.pythonIvals)
                self.pythonIvals.append(ival)
                if self.pstats:
                    ival.pstats = PStatCollector(self.pstats, ival.pname)
                self.addExtIndex(index, ival.getName(), ival.getDuration(), ival.getOpenEnded(), relTime, relTo)
            else:
                self.notify.error('Not an Interval: %s' % (ival,))

    def setManager(self, manager):
        rogerroger
        self.__manager = manager
        CMetaInterval.setManager(self, manager)

    def getManager(self):
        return self.__manager

    def setT(self, t):
        self.__updateIvals()
        CMetaInterval.setT(self, t)

    def start(self, startT=0.0, endT=-1.0, playRate=1.0):
        self.__updateIvals()
        self.setupPlay(startT, endT, playRate, 0)
        self.__manager.addInterval(self)

    def loop(self, startT=0.0, endT=-1.0, playRate=1.0):
        self.__updateIvals()
        self.setupPlay(startT, endT, playRate, 1)
        self.__manager.addInterval(self)

    def pause(self):
        if self.getState() == CInterval.SStarted:
            self.privInterrupt()
        self.__manager.removeInterval(self)
        self.privPostEvent()
        return self.getT()

    def resume(self, startT=None):
        self.__updateIvals()
        if startT != None:
            self.setT(startT)
        self.setupResume()
        self.__manager.addInterval(self)
        return

    def resumeUntil(self, endT):
        self.__updateIvals()
        self.setupResumeUntil(endT)
        self.__manager.addInterval(self)

    def finish(self):
        self.__updateIvals()
        state = self.getState()
        if state == CInterval.SInitial:
            self.privInstant()
        else:
            if state != CInterval.SFinal:
                self.privFinalize()
        self.__manager.removeInterval(self)
        self.privPostEvent()

    def clearToInitial(self):
        self.pause()
        CMetaInterval.clearToInitial(self)

    def validateComponent(self, component):
        return isinstance(component, CInterval) or isinstance(component, Interval.Interval)

    def validateComponents(self, components):
        for component in components:
            if not self.validateComponent(component):
                return 0

        return 1

    def __updateIvals(self):
        if self.__ivalsDirty:
            self.clearIntervals()
            self.applyIvals(self, 0, TRACK_START)
            self.__ivalsDirty = 0

    def clearIntervals(self):
        CMetaInterval.clearIntervals(self)
        self.inPython = 0

    def applyIvals(self, meta, relTime, relTo):
        if len(self.ivals) == 0:
            pass
        else:
            if len(self.ivals) == 1:
                meta.addInterval(self.ivals[0], relTime, relTo)
            else:
                self.notify.error('Cannot build list from MetaInterval directly.')

    def setPlayRate(self, playRate):
        if self.isPlaying():
            self.pause()
            CMetaInterval.setPlayRate(self, playRate)
            self.resume()
        else:
            CMetaInterval.setPlayRate(self, playRate)

    def __doPythonCallbacks(self):
        ival = None
        try:
            while self.isEventReady():
                index = self.getEventIndex()
                t = self.getEventT()
                eventType = self.getEventType()
                self.popEvent()
                ival = self.pythonIvals[index]
                ival.privDoEvent(t, eventType)
                ival.privPostEvent()
                ival = None

        except:
            if ival != None:
                print 'Exception occurred while processing %s of %s:' % (ival.getName(), self.getName())
            else:
                print 'Exception occurred while processing %s:' % self.getName()
            print self
            raise

        return

    def privDoEvent(self, t, event):
        if self.pstats:
            self.pstats.start()
        self.__updateIvals()
        CMetaInterval.privDoEvent(self, t, event)
        if self.pstats:
            self.pstats.stop()

    def privPostEvent(self):
        if self.pstats:
            self.pstats.start()
        self.__doPythonCallbacks()
        CMetaInterval.privPostEvent(self)
        if self.pstats:
            self.pstats.stop()

    def setIntervalStartTime(self, *args, **kw):
        self.__updateIvals()
        self.inPython = 1
        return CMetaInterval.setIntervalStartTime(self, *args, **kw)

    def getIntervalStartTime(self, *args, **kw):
        self.__updateIvals()
        return CMetaInterval.getIntervalStartTime(self, *args, **kw)

    def getDuration(self):
        self.__updateIvals()
        return CMetaInterval.getDuration(self)

    def __repr__(self, *args, **kw):
        self.__updateIvals()
        return CMetaInterval.__repr__(self, *args, **kw)

    def __str__(self, *args, **kw):
        self.__updateIvals()
        return CMetaInterval.__str__(self, *args, **kw)

    def timeline(self, out=None):
        self.__updateIvals()
        if out == None:
            out = ostream
        CMetaInterval.timeline(self, out)
        return


class Sequence(MetaInterval):

    def applyIvals(self, meta, relTime, relTo):
        meta.addSequence(self.ivals, self.getName(), relTime, relTo, self.phonyDuration)


class Parallel(MetaInterval):

    def applyIvals(self, meta, relTime, relTo):
        meta.addParallel(self.ivals, self.getName(), relTime, relTo, self.phonyDuration)


class ParallelEndTogether(MetaInterval):

    def applyIvals(self, meta, relTime, relTo):
        meta.addParallelEndTogether(self.ivals, self.getName(), relTime, relTo, self.phonyDuration)


class Track(MetaInterval):

    def applyIvals(self, meta, relTime, relTo):
        meta.addTrack(self.ivals, self.getName(), relTime, relTo, self.phonyDuration)

    def validateComponent(self, tuple):
        if not (isinstance(tuple, types.TupleType) or isinstance(tuple, types.ListType)):
            return 0
        relTime = tuple[0]
        ival = tuple[1]
        if len(tuple) >= 3:
            relTo = tuple[2]
        else:
            relTo = TRACK_START
        if not (isinstance(relTime, types.FloatType) or isinstance(relTime, types.IntType)):
            return 0
        if not MetaInterval.validateComponent(self, ival):
            return 0
        if relTo != PREVIOUS_END and relTo != PREVIOUS_START and relTo != TRACK_START:
            return 0
        return 1