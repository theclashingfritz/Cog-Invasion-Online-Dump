# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.CountedResource


class CountedResource(object):

    @classmethod
    def incrementCounter(cls):
        try:
            cls.RESOURCE_COUNTER += 1
        except AttributeError:
            cls.RESOURCE_COUNTER = 1

        if cls.RESOURCE_COUNTER == 1:
            cls.acquire()

    @classmethod
    def decrementCounter(cls):
        try:
            cls.RESOURCE_COUNTER_INIT_FAILED
            del cls.RESOURCE_COUNTER_INIT_FAILED
        except AttributeError:
            cls.RESOURCE_COUNTER -= 1
            if cls.RESOURCE_COUNTER < 1:
                cls.release()

    @classmethod
    def getCount(cls):
        return cls.RESOURCE_COUNTER

    @classmethod
    def acquire(cls):
        pass

    @classmethod
    def release(cls):
        pass

    def __init__(self):
        cls = type(self)
        cls.RESOURCE_COUNTER_INIT_FAILED = True
        del cls.RESOURCE_COUNTER_INIT_FAILED
        self.incrementCounter()

    def __del__(self):
        self.decrementCounter()


if __debug__ and __name__ == '__main__':

    class MouseResource(CountedResource):

        @classmethod
        def acquire(cls):
            super(MouseResource, cls).acquire()
            print '-- Acquire Mouse'

        @classmethod
        def release(cls):
            print '-- Release Mouse'
            super(MouseResource, cls).release()

        def __init__(self):
            super(MouseResource, self).__init__()

        def __del__(self):
            super(MouseResource, self).__del__()


    class CursorResource(CountedResource):

        @classmethod
        def acquire(cls):
            super(CursorResource, cls).acquire()
            print '-- Acquire Cursor'

        @classmethod
        def release(cls):
            print '-- Release Cursor'
            super(CursorResource, cls).release()

        def __init__(self):
            self.__mouseResource = MouseResource()
            super(CursorResource, self).__init__()

        def __del__(self):
            super(CursorResource, self).__del__()
            del self.__mouseResource


    class InvalidResource(MouseResource):

        @classmethod
        def acquire(cls):
            super(InvalidResource, cls).acquire()
            print '-- Acquire Invalid'

        @classmethod
        def release(cls):
            print '-- Release Invalid'
            super(InvalidResource, cls).release()


    print '\nAllocate Mouse'
    m = MouseResource()
    print 'Free up Mouse'
    del m
    print '\nAllocate Cursor'
    c = CursorResource()
    print 'Free up Cursor'
    del c
    print '\nAllocate Mouse then Cursor'
    m = MouseResource()
    c = CursorResource()
    print 'Free up Cursor'
    del c
    print 'Free up Mouse'
    del m
    print '\nAllocate Mouse then Cursor'
    m = MouseResource()
    c = CursorResource()
    print 'Free up Mouse'
    del m
    print 'Free up Cursor'
    del c
    print '\nAllocate Cursor then Mouse'
    c = CursorResource()
    m = MouseResource()
    print 'Free up Mouse'
    del m
    print 'Free up Cursor'
    del c
    print '\nAllocate Cursor then Mouse'
    c = CursorResource()
    m = MouseResource()
    print 'Free up Cursor'
    del c
    try:
        print '\nAllocate Invalid'
        i = InvalidResource()
        print 'Free up Invalid'
    except AssertionError as e:
        print e

    print
    print 'Free up Mouse'
    del m

    def demoFunc():
        print '\nAllocate Cursor within function'
        c = CursorResource()
        print 'Cursor will be freed on function exit'


    demoFunc()