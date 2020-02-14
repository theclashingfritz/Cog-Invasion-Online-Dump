# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.stdpy.pickle
from types import *
from copy_reg import dispatch_table
from panda3d.core import BamWriter, BamReader
pickle = __import__('pickle')

class Pickler(pickle.Pickler):

    def __init__(self, *args, **kw):
        self.bamWriter = BamWriter()
        pickle.Pickler.__init__(self, *args, **kw)

    def save(self, obj):
        pid = self.persistent_id(obj)
        if pid:
            self.save_pers(pid)
            return
        x = self.memo.get(id(obj))
        if x:
            self.write(self.get(x[0]))
            return
        t = type(obj)
        f = self.dispatch.get(t)
        if f:
            f(self, obj)
            return
        try:
            issc = issubclass(t, TypeType)
        except TypeError:
            issc = 0

        if issc:
            self.save_global(obj)
            return
        reduce = dispatch_table.get(t)
        if reduce:
            rv = reduce(obj)
        else:
            reduce = getattr(obj, '__reduce_persist__', None)
            if reduce:
                rv = reduce(self)
            else:
                reduce = getattr(obj, '__reduce_ex__', None)
                if reduce:
                    rv = reduce(self.proto)
                else:
                    reduce = getattr(obj, '__reduce__', None)
                    if reduce:
                        rv = reduce()
                    else:
                        raise PicklingError("Can't pickle %r object: %r" % (
                         t.__name__, obj))
        if type(rv) is StringType:
            self.save_global(obj, rv)
            return
        if type(rv) is not TupleType:
            raise PicklingError('%s must return string or tuple' % reduce)
        l = len(rv)
        if not 2 <= l <= 5:
            raise PicklingError('Tuple returned by %s must have two to five elements' % reduce)
        self.save_reduce(obj=obj, *rv)
        return


class Unpickler(pickle.Unpickler):

    def __init__(self, *args, **kw):
        self.bamReader = BamReader()
        pickle.Unpickler.__init__(self, *args, **kw)

    def load_reduce(self):
        stack = self.stack
        args = stack.pop()
        func = stack[-1]
        if func.__name__.endswith('Persist'):
            value = func(self, *args)
        else:
            value = func(*args)
        stack[-1] = value

    pickle.Unpickler.dispatch[pickle.REDUCE] = load_reduce


try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

def dump(obj, file, protocol=None):
    Pickler(file, protocol).dump(obj)


def dumps(obj, protocol=None):
    file = StringIO()
    Pickler(file, protocol).dump(obj)
    return file.getvalue()


def load(file):
    return Unpickler(file).load()


def loads(str):
    file = StringIO(str)
    return Unpickler(file).load()