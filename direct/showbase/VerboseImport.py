# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.VerboseImport
__all__ = []
import sys
oldimport = __import__
indentLevel = 0

def newimport(*args, **kw):
    global indentLevel
    fPrint = 0
    name = args[0]
    if name not in sys.modules:
        print ' ' * indentLevel + 'import ' + args[0]
        fPrint = 1
    indentLevel += 1
    result = oldimport(*args, **kw)
    indentLevel -= 1
    if fPrint:
        print ' ' * indentLevel + 'DONE: import ' + args[0]
    return result


__builtins__['__import__'] = newimport