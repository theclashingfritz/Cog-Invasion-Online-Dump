# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.extensions_native.HTTPChannel_extensions
from panda3d.core import HTTPChannel
from extension_native_helpers import Dtool_funcToMethod

def spawnTask(self, name=None, callback=None, extraArgs=[]):
    if not name:
        name = str(self.getUrl())
    from direct.task import Task
    task = Task.Task(self.doTask)
    task.callback = callback
    task.callbackArgs = extraArgs
    return taskMgr.add(task, name)


Dtool_funcToMethod(spawnTask, HTTPChannel)
del spawnTask

def doTask(self, task):
    from direct.task import Task
    if self.run():
        return Task.cont
    if task.callback:
        task.callback(*task.callbackArgs)
    return Task.done


Dtool_funcToMethod(doTask, HTTPChannel)
del doTask