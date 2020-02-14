# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.stdpy.thread
__all__ = [
 'error', 'LockType',
 'start_new_thread',
 'interrupt_main',
 'exit', 'allocate_lock', 'get_ident',
 'stack_size',
 'forceYield', 'considerYield']
from panda3d import core
forceYield = core.Thread.forceYield
considerYield = core.Thread.considerYield

class error(StandardError):
    pass


class LockType:

    def __init__(self):
        self.__lock = core.Mutex('PythonLock')
        self.__cvar = core.ConditionVar(self.__lock)
        self.__locked = False

    def acquire(self, waitflag=1):
        self.__lock.acquire()
        try:
            if self.__locked and not waitflag:
                return False
            while self.__locked:
                self.__cvar.wait()

            self.__locked = True
            return True
        finally:
            self.__lock.release()

    def release(self):
        self.__lock.acquire()
        try:
            if not self.__locked:
                raise error, 'Releasing unheld lock.'
            self.__locked = False
            self.__cvar.notify()
        finally:
            self.__lock.release()

    def locked(self):
        return self.__locked

    __enter__ = acquire

    def __exit__(self, t, v, tb):
        self.release()


_threads = {}
_nextThreadId = 0
_threadsLock = core.Mutex('thread._threadsLock')

def start_new_thread(function, args, kwargs={}, name=None):
    global _nextThreadId

    def threadFunc(threadId, function=function, args=args, kwargs=kwargs):
        try:
            function(*args, **kwargs)
        except SystemExit:
            pass
        finally:
            _remove_thread_id(threadId)

    _threadsLock.acquire()
    try:
        threadId = _nextThreadId
        _nextThreadId += 1
        if name is None:
            name = 'PythonThread-%s' % threadId
        thread = core.PythonThread(threadFunc, [threadId], name, name)
        thread.setPythonData(threadId)
        _threads[threadId] = (thread, {}, None)
        thread.start(core.TPNormal, False)
        return threadId
    finally:
        _threadsLock.release()

    return


def _add_thread(thread, wrapper):
    global _nextThreadId
    _threadsLock.acquire()
    try:
        threadId = _nextThreadId
        _nextThreadId += 1
        thread.setPythonData(threadId)
        _threads[threadId] = (thread, {}, wrapper)
        return threadId
    finally:
        _threadsLock.release()


def _get_thread_wrapper(thread, wrapperClass):
    global _nextThreadId
    threadId = thread.getPythonData()
    if threadId is None:
        _threadsLock.acquire()
        try:
            threadId = _nextThreadId
            _nextThreadId += 1
            thread.setPythonData(threadId)
            wrapper = wrapperClass(thread, threadId)
            _threads[threadId] = (thread, {}, wrapper)
            return wrapper
        finally:
            _threadsLock.release()

    else:
        _threadsLock.acquire()
        try:
            t, locals, wrapper = _threads[threadId]
            if wrapper is None:
                wrapper = wrapperClass(thread, threadId)
                _threads[threadId] = (thread, locals, wrapper)
            return wrapper
        finally:
            _threadsLock.release()

    return


def _get_thread_locals(thread, i):
    global _nextThreadId
    threadId = thread.getPythonData()
    if threadId is None:
        _threadsLock.acquire()
        try:
            threadId = _nextThreadId
            _nextThreadId += 1
            thread.setPythonData(threadId)
            locals = {}
            _threads[threadId] = (thread, locals, None)
            return locals.setdefault(i, {})
        finally:
            _threadsLock.release()

    else:
        _threadsLock.acquire()
        try:
            t, locals, wrapper = _threads[threadId]
            return locals.setdefault(i, {})
        finally:
            _threadsLock.release()

    return


def _remove_thread_id(threadId):
    _threadsLock.acquire()
    try:
        thread, locals, wrapper = _threads[threadId]
        del _threads[threadId]
        thread.setPythonData(None)
    finally:
        _threadsLock.release()

    return


def interrupt_main():
    pass


def exit():
    raise SystemExit


def allocate_lock():
    return LockType()


def get_ident():
    return core.Thread.getCurrentThread().this


def stack_size(size=0):
    raise error


class _local(object):

    def __del__(self):
        i = id(self)
        _threadsLock.acquire()
        try:
            for thread, locals, wrapper in _threads.values():
                try:
                    del locals[i]
                except KeyError:
                    pass

        finally:
            _threadsLock.release()

    def __setattr__(self, key, value):
        d = _get_thread_locals(core.Thread.getCurrentThread(), id(self))
        d[key] = value

    def __getattribute__(self, key):
        d = _get_thread_locals(core.Thread.getCurrentThread(), id(self))
        if key == '__dict__':
            return d
        try:
            return d[key]
        except KeyError:
            return object.__getattribute__(self, key)