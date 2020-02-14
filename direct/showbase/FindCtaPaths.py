# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.FindCtaPaths
__all__ = [
 'deCygwinify', 'getPaths']
import os, sys

def deCygwinify(path):
    if os.name in ('nt', ) and path[0] == '/':
        dirs = path.split('/')
        if len(dirs) > 2 and len(dirs[1]) == 1:
            path = '%s:\\%s' % (dirs[1], ('\\').join(dirs[2:]))
        else:
            pandaRoot = os.getenv('PANDA_ROOT')
            if pandaRoot:
                path = os.path.normpath(pandaRoot + path)
    return path


def getPaths():
    ctprojs = os.getenv('CTPROJS')
    if ctprojs:
        print 'Appending to sys.path based on $CTPROJS:'
        packages = []
        for proj in ctprojs.split():
            projName = proj.split(':')[0]
            packages.append(projName)

        packages.reverse()
        parents = []
        for package in packages:
            tree = os.getenv(package)
            if not tree:
                print '  CTPROJS contains %s, but $%s is not defined.' % (package, package)
                sys.exit(1)
            tree = deCygwinify(tree)
            parent, base = os.path.split(tree)
            if base != package.lower():
                print '  Warning: $%s refers to a directory named %s (instead of %s)' % (package, base, package.lower())
            if parent not in parents:
                parents.append(parent)
            libdir = os.path.join(tree, 'built', 'lib')
            if os.path.isdir(libdir):
                if libdir not in sys.path:
                    sys.path.append(libdir)

        for parent in parents:
            print '  %s' % parent
            if parent not in sys.path:
                sys.path.append(parent)


getPaths()