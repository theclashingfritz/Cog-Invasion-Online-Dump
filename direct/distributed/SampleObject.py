# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.SampleObject
from direct.directnotify.DirectNotifyGlobal import *
from direct.distributed.DistributedObject import *

class SampleObject(DistributedObject):
    notify = directNotify.newCategory('SampleObject')

    def __init__(self, cr):
        self.cr = cr

    def setColor(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue
        self.announceGenerate()

    def getColor(self):
        return (
         self.red, self.green, self.blue)