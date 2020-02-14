# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.task.TaskTester
__all__ = []
from direct.task.TaskManagerGlobal import *
import direct.task.Task, random
numTasks = 10000
maxDelay = 20
counter = 0

def spawnNewTask():
    global counter
    counter = (counter + 1) % 1000
    delay = random.random() * maxDelay
    taskMgr.doMethodLater(delay, taskCallback, 'taskTester-%s' % counter)


def taskCallback(task):
    randNum = int(round(random.random() * 1000))
    n = 'taskTester-%s' % randNum
    taskMgr.remove(n)
    spawnNewTask()
    spawnNewTask()
    return Task.done


taskMgr.removeTasksMatching('taskTester*')
for i in range(numTasks):
    spawnNewTask()