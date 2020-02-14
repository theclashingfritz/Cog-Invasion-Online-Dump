# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.stdpy.file
__all__ = [
 'open', 'listdir', 'walk', 'join',
 'isfile', 'isdir', 'exists', 'lexists', 'getmtime', 'getsize',
 'execfile']
import panda3d._core as core, sys, os, io, encodings
from posixpath import join
_vfs = core.VirtualFileSystem.getGlobalPtr()
if sys.version_info < (3, 0):
    FileNotFoundError = IOError
    IsADirectoryError = IOError
    FileExistsError = IOError
    PermissionError = IOError

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
    if sys.version_info >= (3, 0):
        for ch in mode:
            if ch not in 'rwxabt+U':
                raise ValueError("invalid mode: '%s'" % mode)

    creating = 'x' in mode
    writing = 'w' in mode
    appending = 'a' in mode
    updating = '+' in mode
    binary = 'b' in mode
    universal = 'U' in mode
    reading = universal or 'r' in mode
    if binary and 't' in mode:
        raise ValueError("can't have text and binary mode at once")
    if creating + reading + writing + appending > 1:
        raise ValueError('must have exactly one of create/read/write/append mode')
    if binary:
        if encoding:
            raise ValueError("binary mode doesn't take an encoding argument")
        if errors:
            raise ValueError("binary mode doesn't take an errors argument")
        if newline:
            raise ValueError("binary mode doesn't take a newline argument")
    if isinstance(file, core.Istream) or isinstance(file, core.Ostream):
        raw = StreamIOWrapper(file)
        raw.mode = mode
    else:
        vfile = None
        if isinstance(file, core.VirtualFile):
            vfile = file
            filename = vfile.getFilename()
        else:
            if isinstance(file, unicode):
                filename = core.Filename.fromOsSpecificW(file)
            else:
                if isinstance(file, str):
                    filename = core.Filename.fromOsSpecific(file)
                else:
                    filename = core.Filename(file)
        if binary or sys.version_info >= (3, 0):
            filename.setBinary()
        else:
            filename.setText()
        if not vfile:
            vfile = _vfs.getFile(filename)
        if not vfile:
            if reading:
                raise FileNotFoundError("No such file or directory: '%s'" % filename)
            vfile = _vfs.createFile(filename)
            if not vfile:
                raise IOError("Failed to create file: '%s'" % filename)
        else:
            if creating:
                raise FileExistsError("File exists: '%s'" % filename)
            else:
                if vfile.isDirectory():
                    raise IsADirectoryError("Is a directory: '%s'" % filename)
                if reading:
                    if updating:
                        stream = vfile.openReadWriteFile(False)
                    else:
                        stream = vfile.openReadFile(False)
                    if not stream:
                        raise IOError('Could not open %s for reading' % filename)
                else:
                    if writing or creating:
                        if updating:
                            stream = vfile.openReadWriteFile(True)
                        else:
                            stream = vfile.openWriteFile(False, True)
                        if not stream:
                            raise IOError('Could not open %s for writing' % filename)
                    else:
                        if appending:
                            if updating:
                                stream = vfile.openReadAppendFile()
                            else:
                                stream = vfile.openAppendFile()
                            if not stream:
                                raise IOError('Could not open %s for appending' % filename)
                        else:
                            raise ValueError('Must have exactly one of create/read/write/append mode and at most one plus')
                raw = StreamIOWrapper(stream, needsVfsClose=True)
                raw.mode = mode
                raw.name = vfile.getFilename().toOsSpecific()
            if binary:
                return raw
        if not encoding and sys.version_info < (3, 0):
            return raw
    line_buffering = False
    if buffering == 1:
        line_buffering = True
    else:
        if buffering == 0:
            raise ValueError("can't have unbuffered text I/O")
    wrapper = io.TextIOWrapper(raw, encoding, errors, newline, line_buffering)
    wrapper.mode = mode
    return wrapper


if sys.version_info < (3, 0):
    __all__.append('file')
    file = open

class StreamIOWrapper(io.IOBase):

    def __init__(self, stream, needsVfsClose=False):
        self.__stream = stream
        self.__needsVfsClose = needsVfsClose
        self.__reader = None
        self.__writer = None
        self.__lastWrite = False
        if isinstance(stream, core.Istream):
            self.__reader = core.StreamReader(stream, False)
        if isinstance(stream, core.Ostream):
            self.__writer = core.StreamWriter(stream, False)
            self.__lastWrite = True
            if sys.version_info >= (3, 0):
                self.__write = self.__writer.appendData
            else:
                self.__write = self.__writer.write
        return

    def __repr__(self):
        s = '<direct.stdpy.file.StreamIOWrapper'
        if hasattr(self, 'name'):
            s += " name='%s'" % self.name
        if hasattr(self, 'mode'):
            s += " mode='%s'" % self.mode
        s += '>'
        return s

    def readable(self):
        return self.__reader is not None

    def writable(self):
        return self.__writer is not None

    def close(self):
        if self.__needsVfsClose:
            if self.__reader and self.__writer:
                _vfs.closeReadWriteFile(self.__stream)
            else:
                if self.__reader:
                    _vfs.closeReadFile(self.__stream)
                else:
                    _vfs.closeWriteFile(self.__stream)
            self.__needsVfsClose = False
        self.__stream = None
        self.__reader = None
        self.__writer = None
        return

    def flush(self):
        if self.__writer:
            self.__stream.clear()
            self.__stream.flush()

    def read(self, size=-1):
        if not self.__reader:
            if not self.__writer:
                raise ValueError('I/O operation on closed file')
            raise IOError('Attempt to read from write-only stream')
        self.__stream.clear()
        self.__lastWrite = False
        if size is not None and size >= 0:
            result = self.__reader.extractBytes(size)
        else:
            result = ''
            while not self.__stream.eof():
                result += self.__reader.extractBytes(512)

        return result

    read1 = read

    def readline(self, size=-1):
        if not self.__reader:
            if not self.__writer:
                raise ValueError('I/O operation on closed file')
            raise IOError('Attempt to read from write-only stream')
        self.__stream.clear()
        self.__lastWrite = False
        return self.__reader.readline()

    def seek(self, offset, whence=0):
        if self.__stream:
            self.__stream.clear()
        if self.__reader:
            self.__stream.seekg(offset, whence)
        if self.__writer:
            self.__stream.seekp(offset, whence)

    def tell(self):
        if self.__lastWrite:
            if self.__writer:
                return self.__stream.tellp()
        else:
            if self.__reader:
                return self.__stream.tellg()
        raise ValueError('I/O operation on closed file')

    def write(self, b):
        if not self.__writer:
            if not self.__reader:
                raise ValueError('I/O operation on closed file')
            raise IOError('Attempt to write to read-only stream')
        self.__stream.clear()
        self.__write(b)
        self.__lastWrite = True

    def writelines(self, lines):
        if not self.__writer:
            if not self.__reader:
                raise ValueError('I/O operation on closed file')
            raise IOError('Attempt to write to read-only stream')
        self.__stream.clear()
        for line in lines:
            self.__write(line)

        self.__lastWrite = True


def listdir(path):
    files = []
    dirlist = _vfs.scanDirectory(core.Filename.fromOsSpecific(path))
    if dirlist is None:
        raise OSError("No such file or directory: '%s'" % path)
    for file in dirlist:
        files.append(file.getFilename().getBasename())

    return files


def walk(top, topdown=True, onerror=None, followlinks=True):
    dirnames = []
    filenames = []
    dirlist = _vfs.scanDirectory(top)
    if dirlist:
        for file in dirlist:
            if file.isDirectory():
                dirnames.append(file.getFilename().getBasename())
            else:
                filenames.append(file.getFilename().getBasename())

    if topdown:
        yield (
         top, dirnames, filenames)
    for dir in dirnames:
        next = join(top, dir)
        for tuple in walk(next, topdown=topdown):
            yield tuple

    if not topdown:
        yield (
         top, dirnames, filenames)


def isfile(path):
    return _vfs.isRegularFile(core.Filename.fromOsSpecific(path))


def isdir(path):
    return _vfs.isDirectory(core.Filename.fromOsSpecific(path))


def exists(path):
    return _vfs.exists(core.Filename.fromOsSpecific(path))


def lexists(path):
    return _vfs.exists(core.Filename.fromOsSpecific(path))


def getmtime(path):
    file = _vfs.getFile(core.Filename.fromOsSpecific(path), True)
    if not file:
        raise os.error
    return file.getTimestamp()


def getsize(path):
    file = _vfs.getFile(core.Filename.fromOsSpecific(path), True)
    if not file:
        raise os.error
    return file.getFileSize()


def execfile(path, globals=None, locals=None):
    file = _vfs.getFile(core.Filename.fromOsSpecific(path), True)
    if not file:
        raise os.error
    data = file.readFile(False)
    exec data in globals, locals