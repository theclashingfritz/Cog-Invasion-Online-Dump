# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.extensions_native.Mat3_extensions
from panda3d.core import Mat3
from extension_native_helpers import Dtool_funcToMethod

def pPrintValues(self):
    return '\n%s\n%s\n%s' % (
     self.getRow(0).pPrintValues(), self.getRow(1).pPrintValues(), self.getRow(2).pPrintValues())


Dtool_funcToMethod(pPrintValues, Mat3)
del pPrintValues