# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.controls.GhostWalker
from direct.showbase.ShowBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
import NonPhysicsWalker

class GhostWalker(NonPhysicsWalker.NonPhysicsWalker):
    notify = DirectNotifyGlobal.directNotify.newCategory('GhostWalker')
    slideName = 'jump'