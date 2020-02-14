# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.GarbageReportScheduler
from direct.showbase.GarbageReport import GarbageReport

class GarbageReportScheduler:

    def __init__(self, waitBetween=None, waitScale=None):
        if waitBetween is None:
            waitBetween = 1800
        if waitScale is None:
            waitScale = 1.5
        self._waitBetween = waitBetween
        self._waitScale = waitScale
        self._taskName = 'startScheduledGarbageReport-%s' % serialNum()
        self._garbageReport = None
        self._scheduleNextGarbageReport()
        return

    def getTaskName(self):
        return self._taskName

    def _scheduleNextGarbageReport(self, garbageReport=None):
        if garbageReport:
            self._garbageReport = None
        taskMgr.doMethodLater(self._waitBetween, self._runGarbageReport, self._taskName)
        self._waitBetween = self._waitBetween * self._waitScale
        return

    def _runGarbageReport(self, task):
        self._garbageReport = GarbageReport('ScheduledGarbageReport', threaded=True, doneCallback=self._scheduleNextGarbageReport, autoDestroy=True, priority=GarbageReport.Priorities.Normal * 3)
        return task.done