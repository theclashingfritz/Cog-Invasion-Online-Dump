# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.extensions_native.VBase3_extensions
from panda3d.core import VBase3
from extension_native_helpers import Dtool_funcToMethod

def pPrintValues(self):
    return '% 10.4f, % 10.4f, % 10.4f' % (self[0], self[1], self[2])


Dtool_funcToMethod(pPrintValues, VBase3)
del pPrintValues

def asTuple(self):
    print 'Warning: VBase3.asTuple() is no longer needed and deprecated.  Use the vector directly instead.'
    return tuple(self)


Dtool_funcToMethod(asTuple, VBase3)
del asTuple