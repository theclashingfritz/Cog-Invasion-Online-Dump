# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.directnotify.RotatingLog
import os, time

class RotatingLog:

    def __init__(self, path='./log_file', hourInterval=24, megabyteLimit=1024):
        self.path = path
        self.timeInterval = None
        self.timeLimit = None
        self.sizeLimit = None
        if hourInterval is not None:
            self.timeInterval = hourInterval * 60 * 60
            self.timeLimit = time.time() + self.timeInterval
        if megabyteLimit is not None:
            self.sizeLimit = megabyteLimit * 1024 * 1024
        return

    def __del__(self):
        self.close()

    def close(self):
        if hasattr(self, 'file'):
            self.file.flush()
            self.file.close()
            self.closed = self.file.closed
            del self.file
        else:
            self.closed = 1

    def shouldRotate(self):
        if not hasattr(self, 'file'):
            return 1
        if self.timeLimit is not None and time.time() > self.timeLimit:
            return 1
        if self.sizeLimit is not None and self.file.tell() > self.sizeLimit:
            return 1
        return 0

    def filePath(self):
        dateString = time.strftime('%Y_%m_%d_%H', time.localtime())
        for i in range(26):
            path = '%s_%s_%s.log' % (self.path, dateString, chr(i + 97))
            if not os.path.exists(path) or os.stat(path)[6] < self.sizeLimit:
                return path

        return path

    def rotate(self):
        path = self.filePath()
        file = open(path, 'a')
        if file:
            self.close()
            file.seek(0, 2)
            self.file = file
            self.closed = self.file.closed
            self.mode = self.file.mode
            self.name = self.file.name
            self.softspace = self.file.softspace
            if self.timeLimit is not None and time.time() > self.timeLimit:
                self.timeLimit = time.time() + self.timeInterval
        else:
            print 'RotatingLog error: Unable to open new log file "%s".' % (path,)
        return

    def write(self, data):
        if self.shouldRotate():
            self.rotate()
        if hasattr(self, 'file'):
            r = self.file.write(data)
            self.file.flush()
            return r

    def flush(self):
        return self.file.flush()

    def fileno(self):
        return self.file.fileno()

    def isatty(self):
        return self.file.isatty()

    def next(self):
        return self.file.next()

    def read(self, size):
        return self.file.read(size)

    def readline(self, size):
        return self.file.readline(size)

    def readlines(self, sizehint):
        return self.file.readlines(sizehint)

    def xreadlines(self):
        return self.file.xreadlines()

    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def truncate(self, size):
        return self.file.truncate(size)

    def writelines(self, sequence):
        return self.file.writelines(sequence)