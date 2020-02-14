# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.TimeManager
from direct.showbase.DirectObject import *
from pandac.PandaModules import *
from direct.task import Task
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta

class TimeManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TimeManager')
    updateFreq = base.config.GetFloat('time-manager-freq', 10)
    minWait = base.config.GetFloat('time-manager-min-wait', 1)
    maxUncertainty = base.config.GetFloat('time-manager-max-uncertainty', 1)
    maxAttempts = base.config.GetInt('time-manager-max-attempts', 5)
    extraSkew = base.config.GetInt('time-manager-extra-skew', 0)
    if extraSkew != 0:
        notify.info('Simulating clock skew of %0.3f s' % extraSkew)
    reportFrameRateInterval = base.config.GetDouble('report-frame-rate-interval', 300.0)

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.thisContext = -1
        self.nextContext = 0
        self.attemptCount = 0
        self.start = 0
        self.lastAttempt = -self.minWait * 2

    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        self.accept('clock_error', self.handleClockError)
        if self.updateFreq > 0:
            self.startTask()

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.cr.timeManager = self
        self.synchronize('TimeManager.announceGenerate')

    def disable(self):
        self.ignore('clock_error')
        self.stopTask()
        taskMgr.remove('frameRateMonitor')
        if self.cr.timeManager is self:
            self.cr.timeManager = None
        DistributedObject.DistributedObject.disable(self)
        return

    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    def startTask(self):
        self.stopTask()
        taskMgr.doMethodLater(self.updateFreq, self.doUpdate, 'timeMgrTask')

    def stopTask(self):
        taskMgr.remove('timeMgrTask')

    def doUpdate(self, task):
        self.synchronize('timer')
        taskMgr.doMethodLater(self.updateFreq, self.doUpdate, 'timeMgrTask')
        return Task.done

    def handleClockError(self):
        self.synchronize('clock error')

    def synchronize(self, description):
        now = globalClock.getRealTime()
        if now - self.lastAttempt < self.minWait:
            self.notify.debug('Not resyncing (too soon): %s' % description)
            return 0
        self.talkResult = 0
        self.thisContext = self.nextContext
        self.attemptCount = 0
        self.nextContext = self.nextContext + 1 & 255
        self.notify.info('Clock sync: %s' % description)
        self.start = now
        self.lastAttempt = now
        self.sendUpdate('requestServerTime', [self.thisContext])
        return 1

    def serverTime(self, context, timestamp):
        end = globalClock.getRealTime()
        if context != self.thisContext:
            self.notify.info('Ignoring TimeManager response for old context %d' % context)
            return
        elapsed = end - self.start
        self.attemptCount += 1
        self.notify.info('Clock sync roundtrip took %0.3f ms' % (elapsed * 1000.0))
        average = (self.start + end) / 2.0 - self.extraSkew
        uncertainty = (end - self.start) / 2.0 + abs(self.extraSkew)
        globalClockDelta.resynchronize(average, timestamp, uncertainty)
        self.notify.info('Local clock uncertainty +/- %.3f s' % globalClockDelta.getUncertainty())
        if globalClockDelta.getUncertainty() > self.maxUncertainty:
            if self.attemptCount < self.maxAttempts:
                self.notify.info('Uncertainty is too high, trying again.')
                self.start = globalClock.getRealTime()
                self.sendUpdate('requestServerTime', [self.thisContext])
                return
            self.notify.info('Giving up on uncertainty requirement.')
        messenger.send('gotTimeSync', taskChain='default')
        messenger.send(self.cr.uniqueName('gotTimeSync'), taskChain='default')