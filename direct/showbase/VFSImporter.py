# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.VFSImporter
__all__ = [
 'register', 'sharedPackages',
 'reloadSharedPackage', 'reloadSharedPackages']
from panda3d._core import Filename, VirtualFileSystem, VirtualFileMountSystem, OFileStream, copyStream
import sys, marshal, imp, types, __builtin__
sharedPackages = {}
vfs = VirtualFileSystem.getGlobalPtr()
compiledExtensions = [
 'pyc', 'pyo']
if not __debug__:
    compiledExtensions = [
     'pyo', 'pyc']

class VFSImporter:

    def __init__(self, path):
        if isinstance(path, Filename):
            self.dir_path = Filename(path)
        else:
            self.dir_path = Filename.fromOsSpecific(path)

    def find_module(self, fullname, path=None):
        if path is None:
            dir_path = self.dir_path
        else:
            dir_path = path
        basename = fullname.split('.')[-1]
        path = Filename(dir_path, basename)
        filename = Filename(path)
        filename.setExtension('py')
        vfile = vfs.getFile(filename, True)
        if vfile:
            return VFSLoader(dir_path, vfile, filename, desc=(
             '.py', 'U', imp.PY_SOURCE))
        for ext in compiledExtensions:
            filename = Filename(path)
            filename.setExtension(ext)
            vfile = vfs.getFile(filename, True)
            if vfile:
                return VFSLoader(dir_path, vfile, filename, desc=(
                 '.' + ext, 'rb', imp.PY_COMPILED))

        for desc in imp.get_suffixes():
            if desc[2] != imp.C_EXTENSION:
                continue
            filename = Filename(path + desc[0])
            vfile = vfs.getFile(filename, True)
            if vfile:
                return VFSLoader(dir_path, vfile, filename, desc=desc)

        filename = Filename(path, '__init__.py')
        vfile = vfs.getFile(filename, True)
        if vfile:
            return VFSLoader(dir_path, vfile, filename, packagePath=path, desc=(
             '.py', 'U', imp.PY_SOURCE))
        for ext in compiledExtensions:
            filename = Filename(path, '__init__.' + ext)
            vfile = vfs.getFile(filename, True)
            if vfile:
                return VFSLoader(dir_path, vfile, filename, packagePath=path, desc=(
                 '.' + ext, 'rb', imp.PY_COMPILED))

        return


class VFSLoader:

    def __init__(self, dir_path, vfile, filename, desc, packagePath=None):
        self.dir_path = dir_path
        self.timestamp = None
        if vfile:
            self.timestamp = vfile.getTimestamp()
        self.filename = filename
        self.desc = desc
        self.packagePath = packagePath
        return

    def load_module(self, fullname, loadingShared=False):
        if self.desc[2] == imp.PY_FROZEN:
            return self._import_frozen_module(fullname)
        if self.desc[2] == imp.C_EXTENSION:
            return self._import_extension_module(fullname)
        if not loadingShared and self.packagePath and '.' in fullname:
            parentname = fullname.rsplit('.', 1)[0]
            if parentname in sharedPackages:
                parent = sys.modules[parentname]
                path = getattr(parent, '__path__', None)
                importer = VFSSharedImporter()
                sharedPackages[fullname] = True
                loader = importer.find_module(fullname, path=path)
                return loader.load_module(fullname)
        code = self._read_code()
        if not code:
            raise ImportError('No Python code in %s' % fullname)
        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = self.filename.toOsSpecific()
        mod.__loader__ = self
        if self.packagePath:
            mod.__path__ = [
             self.packagePath.toOsSpecific()]
        exec code in mod.__dict__
        return sys.modules[fullname]

    def getdata(self, path):
        path = Filename(self.dir_path, Filename.fromOsSpecific(path))
        vfile = vfs.getFile(path)
        if not vfile:
            raise IOError("Could not find '%s'" % path)
        return vfile.readFile(True)

    def is_package(self, fullname):
        return bool(self.packagePath)

    def get_code(self, fullname):
        return self._read_code()

    def get_source(self, fullname):
        return self._read_source()

    def get_filename(self, fullname):
        return self.filename.toOsSpecific()

    def _read_source(self):
        if self.desc[2] == imp.PY_COMPILED or self.desc[2] == imp.C_EXTENSION:
            return None
        filename = Filename(self.filename)
        filename.setExtension('py')
        filename.setText()
        vfile = vfs.getFile(filename)
        if not vfile:
            raise IOError("Could not find '%s'" % filename)
        return vfile.readFile(True)

    def _import_extension_module(self, fullname):
        vfile = vfs.getFile(self.filename, False)
        if hasattr(vfile, 'getMount') and isinstance(vfile.getMount(), VirtualFileMountSystem):
            filename = self.filename
        else:
            if self.filename.exists():
                filename = self.filename
            else:
                filename = Filename.temporary('', self.filename.getBasenameWoExtension(), '.' + self.filename.getExtension(), type=Filename.TDso)
                filename.setExtension(self.filename.getExtension())
                filename.setBinary()
                sin = vfile.openReadFile(True)
                sout = OFileStream()
                if not filename.openWrite(sout):
                    raise IOError
                if not copyStream(sin, sout):
                    raise IOError
                vfile.closeReadFile(sin)
                del sout
        module = imp.load_module(fullname, None, filename.toOsSpecific(), self.desc)
        module.__file__ = self.filename.toOsSpecific()
        return module

    def _import_frozen_module(self, fullname):
        module = imp.load_module(fullname, None, fullname, (
         '', '', imp.PY_FROZEN))
        if getattr(module, '__path__', None) == fullname:
            module.__path__ = []
        return module

    def _read_code(self):
        if self.desc[2] == imp.PY_COMPILED:
            pycVfile = vfs.getFile(self.filename, False)
            if pycVfile:
                return self._loadPyc(pycVfile, None)
            raise IOError('Could not read %s' % self.filename)
        else:
            if self.desc[2] == imp.C_EXTENSION:
                return
        t_pyc = None
        for ext in compiledExtensions:
            pycFilename = Filename(self.filename)
            pycFilename.setExtension(ext)
            pycVfile = vfs.getFile(pycFilename, False)
            if pycVfile:
                t_pyc = pycVfile.getTimestamp()
                break

        code = None
        if t_pyc and t_pyc >= self.timestamp:
            try:
                code = self._loadPyc(pycVfile, self.timestamp)
            except ValueError:
                code = None

        if not code:
            source = self._read_source()
            filename = Filename(self.filename)
            filename.setExtension('py')
            code = self._compile(filename, source)
        return code

    def _loadPyc(self, vfile, timestamp):
        code = None
        data = vfile.readFile(True)
        if data[:4] != imp.get_magic():
            raise ValueError('Bad magic number in %s' % vfile)
        if sys.version_info >= (3, 0):
            t = int.from_bytes(data[4:8], 'little')
            data = data[12:]
        else:
            t = ord(data[4]) + (ord(data[5]) << 8) + (ord(data[6]) << 16) + (ord(data[7]) << 24)
            data = data[8:]
        if not timestamp or t == timestamp:
            return marshal.loads(data)
        raise ValueError('Timestamp wrong on %s' % vfile)
        return

    def _compile(self, filename, source):
        if source and source[-1] != '\n':
            source = source + '\n'
        code = __builtin__.compile(source, filename.toOsSpecific(), 'exec')
        pycFilename = Filename(filename)
        pycFilename.setExtension(compiledExtensions[0])
        try:
            f = open(pycFilename.toOsSpecific(), 'wb')
        except IOError:
            pass
        else:
            f.write(imp.get_magic())
            if sys.version_info >= (3, 0):
                f.write((self.timestamp & 4294967295L).to_bytes(4, 'little'))
                f.write('\x00\x00\x00\x00')
            else:
                f.write(chr(self.timestamp & 255) + chr(self.timestamp >> 8 & 255) + chr(self.timestamp >> 16 & 255) + chr(self.timestamp >> 24 & 255))
            f.write(marshal.dumps(code))
            f.close()

        return code


class VFSSharedImporter:

    def __init__(self):
        pass

    def find_module(self, fullname, path=None, reload=False):
        if fullname not in sharedPackages:
            return
        if path is None:
            path = sys.path
        excludePaths = []
        if reload:
            mod = sys.modules[fullname]
            excludePaths = getattr(mod, '_vfs_shared_path', None)
            if excludePaths is None:
                d = self.getLoadedDirname(mod)
                excludePaths = [d]
        loaders = []
        for dir in path:
            if dir in excludePaths:
                continue
            importer = sys.path_importer_cache.get(dir, None)
            if importer is None:
                try:
                    importer = VFSImporter(dir)
                except ImportError:
                    continue

                sys.path_importer_cache[dir] = importer
            try:
                loader = importer.find_module(fullname)
                if not loader:
                    continue
            except ImportError:
                continue

            loaders.append(loader)

        if not loaders:
            return
        return VFSSharedLoader(loaders, reload=reload)

    def getLoadedDirname(self, mod):
        if not getattr(mod, '__file__', None):
            return
        fullname = mod.__name__
        dirname = Filename.fromOsSpecific(mod.__file__).getDirname()
        parentname = None
        basename = fullname
        if '.' in fullname:
            parentname, basename = fullname.rsplit('.', 1)
        path = None
        if parentname:
            parent = sys.modules[parentname]
            path = parent.__path__
        if path is None:
            path = sys.path
        for dir in path:
            pdir = str(Filename.fromOsSpecific(dir))
            if pdir + '/' + basename == dirname:
                return dir

        return


class VFSSharedLoader:

    def __init__(self, loaders, reload):
        self.loaders = loaders
        self.reload = reload

    def load_module(self, fullname):
        mod = None
        message = None
        path = []
        vfs_shared_path = []
        if self.reload:
            mod = sys.modules[fullname]
            path = mod.__path__ or []
            if path == fullname:
                path = []
            vfs_shared_path = getattr(mod, '_vfs_shared_path', [])
        for loader in self.loaders:
            try:
                mod = loader.load_module(fullname, loadingShared=True)
            except ImportError:
                etype, evalue, etraceback = sys.exc_info()
                print '%s on %s: %s' % (etype.__name__, fullname, evalue)
                if not message:
                    message = '%s: %s' % (fullname, evalue)
                continue

            for dir in getattr(mod, '__path__', []):
                if dir not in path:
                    path.append(dir)

        if mod is None:
            raise ImportError(message)
        mod.__path__ = path
        mod.__package__ = fullname
        mod._vfs_shared_path = vfs_shared_path + [ l.dir_path for l in self.loaders ]
        return mod


_registered = False

def register():
    global _registered
    if not _registered:
        _registered = True
        sys.path_hooks.insert(0, VFSImporter)
        sys.meta_path.insert(0, VFSSharedImporter())
        sys.path_importer_cache = {}


def reloadSharedPackage(mod):
    fullname = mod.__name__
    path = None
    if '.' in fullname:
        parentname = fullname.rsplit('.', 1)[0]
        parent = sys.modules[parentname]
        path = parent.__path__
    importer = VFSSharedImporter()
    loader = importer.find_module(fullname, path=path, reload=True)
    if loader:
        loader.load_module(fullname)
    for basename, child in mod.__dict__.items():
        if isinstance(child, types.ModuleType):
            childname = child.__name__
            if childname == fullname + '.' + basename and hasattr(child, '__path__') and childname not in sharedPackages:
                sharedPackages[childname] = True
                reloadSharedPackage(child)

    return


def reloadSharedPackages():
    for fullname in sorted(sharedPackages.keys()):
        mod = sys.modules.get(fullname, None)
        if not mod:
            continue
        reloadSharedPackage(mod)

    return