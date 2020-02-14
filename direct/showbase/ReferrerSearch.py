# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.ReferrerSearch
import inspect, sys, gc
from direct.showbase.PythonUtil import _getSafeReprNotify
from direct.showbase.Job import Job

class ReferrerSearch(Job):

    def __init__(self, obj, maxRefs=100):
        Job.__init__(self, 'ReferrerSearch')
        self.obj = obj
        self.maxRefs = maxRefs
        self.visited = set()
        self.depth = 0
        self.found = 0
        self.shouldPrintStats = False

    def __call__(self):
        safeReprNotify = _getSafeReprNotify()
        info = safeReprNotify.getInfo()
        safeReprNotify.setInfo(0)
        self.visited = set()
        try:
            self.step(0, [self.obj])
        finally:
            self.obj = None

        safeReprNotify.setInfo(info)
        return

    def run(self):
        safeReprNotify = _getSafeReprNotify()
        self.info = safeReprNotify.getInfo()
        safeReprNotify.setInfo(0)
        print 'RefPath(%s): Beginning ReferrerSearch for %s' % (self._id, fastRepr(self.obj))
        self.visited = set()
        for x in self.stepGenerator(0, [self.obj]):
            yield

        yield Job.Done
        return

    def finished(self):
        print 'RefPath(%s): Finished ReferrerSearch for %s' % (self._id, fastRepr(self.obj))
        self.obj = None
        safeReprNotify = _getSafeReprNotify()
        safeReprNotify.setInfo(self.info)
        return

    def __del__(self):
        print 'ReferrerSearch garbage collected'

    def truncateAtNewLine(self, s):
        if s.find('\n') == -1:
            return s
        return s[:s.find('\n')]

    def printStatsWhenAble(self):
        self.shouldPrintStats = True

    def myrepr(self, referrer, refersTo):
        pre = ''
        if isinstance(referrer, dict):
            for k, v in referrer.iteritems():
                if v is refersTo:
                    pre = self.truncateAtNewLine(fastRepr(k)) + ']-> '
                    break

        else:
            if isinstance(referrer, (list, tuple)):
                for x in xrange(len(referrer)):
                    if referrer[x] is refersTo:
                        pre = '%s]-> ' % x
                        break

        if isinstance(refersTo, dict):
            post = 'dict['
        else:
            if isinstance(refersTo, list):
                post = 'list['
            else:
                if isinstance(refersTo, tuple):
                    post = 'tuple['
                else:
                    if isinstance(refersTo, set):
                        post = 'set->'
                    else:
                        post = self.truncateAtNewLine(fastRepr(refersTo)) + '-> '
        return '%s%s' % (pre, post)

    def step(self, depth, path):
        if self.shouldPrintStats:
            self.printStats(path)
            self.shouldPrintStats = False
        at = path[-1]
        if id(at) in self.visited:
            return
        if self.isAtRoot(at, path):
            self.found += 1
            return
        self.visited.add(id(at))
        referrers = [ ref for ref in gc.get_referrers(at) if not (ref is path or inspect.isframe(ref) or isinstance(ref, dict) and ref.keys() == locals().keys() or ref is self.__dict__ or id(ref) in self.visited)
                    ]
        if self.isManyRef(at, path, referrers):
            return
        while referrers:
            ref = referrers.pop()
            self.depth += 1
            for x in self.stepGenerator(depth + 1, path + [ref]):
                pass

            self.depth -= 1

    def stepGenerator(self, depth, path):
        if self.shouldPrintStats:
            self.printStats(path)
            self.shouldPrintStats = False
        at = path[-1]
        if self.isAtRoot(at, path):
            self.found += 1
            raise StopIteration
        if id(at) in self.visited:
            raise StopIteration
        self.visited.add(id(at))
        referrers = [ ref for ref in gc.get_referrers(at) if not (ref is path or inspect.isframe(ref) or isinstance(ref, dict) and ref.keys() == locals().keys() or ref is self.__dict__ or id(ref) in self.visited)
                    ]
        if self.isManyRef(at, path, referrers):
            raise StopIteration
        while referrers:
            ref = referrers.pop()
            self.depth += 1
            for x in self.stepGenerator(depth + 1, path + [ref]):
                yield

            self.depth -= 1

        yield
        return

    def printStats(self, path):
        path = list(reversed(path))
        path.insert(0, 0)
        print 'RefPath(%s) - Stats - visited(%s) | found(%s) | depth(%s) | CurrentPath(%s)' % (
         self._id, len(self.visited), self.found, self.depth, ('').join((self.myrepr(path[x], path[x + 1]) for x in xrange(len(path) - 1))))

    def isAtRoot(self, at, path):
        if at in path:
            sys.stdout.write('RefPath(%s): Circular: ' % self._id)
            path = list(reversed(path))
            path.insert(0, 0)
            for x in xrange(len(path) - 1):
                sys.stdout.write(self.myrepr(path[x], path[x + 1]))

            print
            return True
        if at is __builtins__:
            sys.stdout.write('RefPath(%s): __builtins__-> ' % self._id)
            path = list(reversed(path))
            path.insert(0, 0)
            for x in xrange(len(path) - 1):
                sys.stdout.write(self.myrepr(path[x], path[x + 1]))

            print
            return True
        if inspect.ismodule(at):
            sys.stdout.write('RefPath(%s): Module(%s)-> ' % (self._id, at.__name__))
            path = list(reversed(path))
            for x in xrange(len(path) - 1):
                sys.stdout.write(self.myrepr(path[x], path[x + 1]))

            print
            return True
        if inspect.isclass(at):
            sys.stdout.write('RefPath(%s): Class(%s)-> ' % (self._id, at.__name__))
            path = list(reversed(path))
            for x in xrange(len(path) - 1):
                sys.stdout.write(self.myrepr(path[x], path[x + 1]))

            print
            return True
        if at is simbase:
            sys.stdout.write('RefPath(%s): simbase-> ' % self._id)
            path = list(reversed(path))
            for x in xrange(len(path) - 1):
                sys.stdout.write(self.myrepr(path[x], path[x + 1]))

            print
            return True
        if at is simbase.air:
            sys.stdout.write('RefPath(%s): simbase.air-> ' % self._id)
            path = list(reversed(path))
            for x in xrange(len(path) - 1):
                sys.stdout.write(self.myrepr(path[x], path[x + 1]))

            print
            return True
        if at is messenger:
            sys.stdout.write('RefPath(%s): messenger-> ' % self._id)
            path = list(reversed(path))
            for x in xrange(len(path) - 1):
                sys.stdout.write(self.myrepr(path[x], path[x + 1]))

            print
            return True
        if at is taskMgr:
            sys.stdout.write('RefPath(%s): taskMgr-> ' % self._id)
            path = list(reversed(path))
            for x in xrange(len(path) - 1):
                sys.stdout.write(self.myrepr(path[x], path[x + 1]))

            print
            return True
        if hasattr(simbase.air, 'mainWorld') and at is simbase.air.mainWorld:
            sys.stdout.write('RefPath(%s): mainWorld-> ' % self._id)
            path = list(reversed(path))
            for x in xrange(len(path) - 1):
                sys.stdout.write(self.myrepr(path[x], path[x + 1]))

            print
            return True
        return False

    def isManyRef(self, at, path, referrers):
        if len(referrers) > self.maxRefs and at is not self.obj:
            if not isinstance(at, (list, tuple, dict, set)):
                sys.stdout.write('RefPath(%s): ManyRefs(%s)[%s]-> ' % (self._id, len(referrers), fastRepr(at)))
                path = list(reversed(path))
                path.insert(0, 0)
                for x in xrange(len(path) - 1):
                    sys.stdout.write(self.myrepr(path[x], path[x + 1]))

                print
                return True
            sys.stdout.write('RefPath(%s): ManyRefsAllowed(%s)[%s]-> ' % (self._id, len(referrers), fastRepr(at, maxLen=1, strFactor=30)))
            print
        return False