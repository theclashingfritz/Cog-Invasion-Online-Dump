# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.extensions_native.extension_native_helpers
__all__ = ['Dtool_ObjectToDict', 'Dtool_funcToMethod']
import imp, sys, os
from panda3d.core import *

def Dtool_ObjectToDict(cls, name, obj):
    cls.DtoolClassDict[name] = obj


def Dtool_funcToMethod(func, cls, method_name=None):
    if sys.version_info < (3, 0):
        func.im_class = cls
    func.im_func = func
    func.im_self = None
    if not method_name:
        method_name = func.__name__
    cls.DtoolClassDict[method_name] = func
    return