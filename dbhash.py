# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: dbhash
import sys, warnings
warnings.warnpy3k('in 3.x, the dbhash module has been removed', stacklevel=2)
try:
    import bsddb
except ImportError:
    del sys.modules[__name__]
    raise

__all__ = ['error', 'open']
error = bsddb.error

def open(file, flag='r', mode=438):
    return bsddb.hashopen(file, flag, mode)