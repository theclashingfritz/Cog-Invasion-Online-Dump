# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.TaskThreaded
__all__ = [
 'TaskThreaded', 'TaskThread']
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task import Task

class TaskThreaded:
    notify = directNotify.newCategory('TaskThreaded')
    _Serial = SerialNumGen()

    def __init__(self, name, threaded=True, timeslice=None, callback=None):
        self.__name = name
        self.__threaded = threaded
        if timeslice is None:
            timeslice = 0.01
        self.__timeslice = timeslice
        self.__taskNames = set()
        self._taskStartTime = None
        self.__threads = set()
        self._callback = callback
        return

    def finished(self):
        if self._callback:
            self._callback()

    def destroy(self):
        for taskName in self.__taskNames:
            taskMgr.remove(taskName)

        del self.__taskNames
        for thread in self.__threads:
            thread.tearDown()
            thread._destroy()

        del self.__threads
        del self._callback
        self.ignoreAll()

    def getTimeslice(self):
        return self.___timeslice

    def setTimeslice(self, timeslice):
        self.__timeslice = timeslice

    def scheduleCallback(self, callback):
        if not self.__threaded:
            callback()
        else:
            taskName = '%s-ThreadedTask-%s' % (
             self.__name, TaskThreaded._Serial.next())
            self.__taskNames.add(taskName)
            taskMgr.add(Functor(self.__doCallback, callback, taskName), taskName)

    def scheduleThread(self, thread):
        thread._init(self)
        thread.setUp()
        if thread.isFinished():
            thread._destroy()
        else:
            if not self.__threaded:
                while not thread.isFinished():
                    thread.run()

                thread._destroy()
            else:
                self.__threads.add(thread)
                taskName = '%s-ThreadedTask-%s-%s' % (
                 self.__name, thread.__class__.__name__,
                 TaskThreaded._Serial.next())
                self.__taskNames.add(taskName)
                self.__threads.add(thread)
                taskMgr.add(Functor(self._doThreadCallback, thread, taskName), taskName)

    def _doCallback(self, callback, taskName, task):
        self.__taskNames.remove(taskName)
        self._taskStartTime = globalClock.getRealTime()
        callback()
        self._taskStartTime = None
        return Task.done

    def _doThreadCallback(self, thread, taskName, task):
        self._taskStartTime = globalClock.getRealTime()
        thread.run()
        self._taskStartTime = None
        if thread.isFinished():
            thread._destroy()
            self.__taskNames.remove(taskName)
            self.__threads.remove(thread)
            return Task.done
        return Task.cont
        return

    def taskTimeLeft(self):
        if self._taskStartTime is None:
            return True
        return globalClock.getRealTime() - self._taskStartTime < self.__timeslice


class TaskThread:

    def setUp(self):
        pass

    def run(self):
        pass

    def tearDown(self):
        pass

    def done(self):
        pass

    def finished(self):
        self.tearDown()
        self._finished = True
        self.done()

    def isFinished(self):
        return self._finished

    def timeLeft(self):
        return self.parent.taskTimeLeft()

    def _init(self, parent):
        self.parent = parent
        self._finished = False

    def _destroy(self):
        del self.parent
        del self._finished