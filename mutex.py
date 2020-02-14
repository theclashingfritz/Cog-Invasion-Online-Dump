# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: mutex
from warnings import warnpy3k
warnpy3k('the mutex module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
from collections import deque

class mutex:

    def __init__(self):
        self.locked = False
        self.queue = deque()

    def test(self):
        return self.locked

    def testandset(self):
        if not self.locked:
            self.locked = True
            return True
        return False

    def lock(self, function, argument):
        if self.testandset():
            function(argument)
        else:
            self.queue.append((function, argument))

    def unlock(self):
        if self.queue:
            function, argument = self.queue.popleft()
            function(argument)
        else:
            self.locked = False