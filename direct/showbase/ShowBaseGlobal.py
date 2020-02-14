# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.ShowBaseGlobal
__all__ = []
from ShowBase import *
directNotify.setDconfigLevels()

def inspect(anObject):
    from direct.tkpanels import Inspector
    return Inspector.inspect(anObject)


import __builtin__
__builtin__.inspect = inspect
if not __debug__ and __dev__:
    notify = directNotify.newCategory('ShowBaseGlobal')
    notify.error("You must set 'want-dev' to false in non-debug mode.")