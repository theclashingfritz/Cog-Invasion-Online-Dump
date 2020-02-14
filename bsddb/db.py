# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: bsddb.db
import sys
absolute_import = sys.version_info[0] >= 3
if not absolute_import:
    if __name__.startswith('bsddb3.'):
        from _pybsddb import *
        from _pybsddb import __version__
    else:
        from _bsddb import *
        from _bsddb import __version__
else:
    if __name__.startswith('bsddb3.'):
        exec 'from ._pybsddb import *'
        exec 'from ._pybsddb import __version__'
    else:
        exec 'from ._bsddb import *'
        exec 'from ._bsddb import __version__'