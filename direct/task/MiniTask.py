# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.task.MiniTask
__all__ = [
 'MiniTask', 'MiniTaskManager']

class MiniTask:
    done = 0
    cont = 1

    def __init__(self, callback):
        self.__call__ = callback


class MiniTaskManager:

    def __init__(self):
        self.taskList = []
        self.running = 0

    def add(self, task, name):
        task.name = name
        self.taskList.append(task)

    def remove(self, task):
        try:
            self.taskList.remove(task)
        except ValueError:
            pass

    def __executeTask(self, task):
        return task(task)

    def step(self):
        i = 0
        while i < len(self.taskList):
            task = self.taskList[i]
            ret = task(task)
            if ret == task.cont:
                pass
            else:
                try:
                    self.taskList.remove(task)
                except ValueError:
                    pass

                continue
            i += 1

    def run(self):
        self.running = 1
        while self.running:
            self.step()

    def stop(self):
        self.running = 0