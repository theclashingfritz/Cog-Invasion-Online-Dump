# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: pandac.PandaModules
print 'Warning: pandac.PandaModules is deprecated, import from panda3d.core instead'
try:
    from panda3d.core import *
except ImportError as err:
    if 'No module named core' not in str(err):
        raise

try:
    from panda3d.physics import *
except ImportError as err:
    if 'No module named physics' not in str(err):
        raise

try:
    from panda3d.fx import *
except ImportError as err:
    if 'No module named fx' not in str(err):
        raise

try:
    from panda3d.direct import *
except ImportError as err:
    if 'No module named direct' not in str(err):
        raise

try:
    from panda3d.vision import *
except ImportError as err:
    if 'No module named vision' not in str(err):
        raise

try:
    from panda3d.skel import *
except ImportError as err:
    if 'No module named skel' not in str(err):
        raise

try:
    from panda3d.egg import *
except ImportError as err:
    if 'No module named egg' not in str(err):
        raise

try:
    from panda3d.ode import *
except ImportError as err:
    if 'No module named ode' not in str(err):
        raise

try:
    from panda3d.vrpn import *
except ImportError as err:
    if 'No module named vrpn' not in str(err):
        raise