# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.holiday.HolidayManager
from panda3d.core import VirtualFileSystem, Filename
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify.DirectNotifyGlobal import directNotify

class HolidayType:
    CHRISTMAS = 1
    HALLOWEEN = 2


class HolidayGlobals:
    CHRISTMAS_TIME = 'Happy Winter Holidays! Winter has struck Toontown!'
    COACH_GREETING = 'Happy Holidays, %s! Here, take some snowballs!'


class HolidayManager(DistributedObjectGlobal):
    notify = directNotify.newCategory('HolidayManager')

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)

    def announceGenerate(self):
        DistributedObjectGlobal.announceGenerate(self)
        self.sendUpdate('requestHoliday', [])

    def setHoliday(self, holiday):
        self.holiday = holiday
        if holiday == HolidayType.CHRISTMAS:
            vfs = VirtualFileSystem.getGlobalPtr()
            vfs.mount(Filename('winter.mf'), '.', VirtualFileSystem.MFReadOnly)

    def getHoliday(self):
        return self.holiday