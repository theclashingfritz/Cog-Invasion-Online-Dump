# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: user
from warnings import warnpy3k
warnpy3k('the user module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
import os
home = os.curdir
if 'HOME' in os.environ:
    home = os.environ['HOME']
else:
    if os.name == 'posix':
        home = os.path.expanduser('~/')
    else:
        if os.name == 'nt':
            if 'HOMEPATH' in os.environ:
                if 'HOMEDRIVE' in os.environ:
                    home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
                else:
                    home = os.environ['HOMEPATH']
    pythonrc = os.path.join(home, '.pythonrc.py')
    try:
        f = open(pythonrc)
    except IOError:
        pass

    f.close()
    execfile(pythonrc)