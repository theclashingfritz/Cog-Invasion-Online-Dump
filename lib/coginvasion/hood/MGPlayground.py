# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.MGPlayground
from Playground import Playground
from direct.fsm.State import State
from direct.directnotify.DirectNotifyGlobal import directNotify

class MGPlayground(Playground):
    notify = directNotify.newCategory('MGPlayground')