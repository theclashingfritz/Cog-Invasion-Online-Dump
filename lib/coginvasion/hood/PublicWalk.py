# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.PublicWalk
import Walk
from direct.directnotify.DirectNotifyGlobal import directNotify

class PublicWalk(Walk.Walk):
    notify = directNotify.newCategory('PublicWalk')

    def __init__(self, parentFSM, doneEvent):
        Walk.Walk.__init__(self, doneEvent)
        self.parentFSM = parentFSM

    def enter(self):
        Walk.Walk.enter(self)
        base.localAvatar.showBookButton()
        base.localAvatar.createLaffMeter()
        base.localAvatar.showGagButton()
        base.localAvatar.enableGags(1)
        base.localAvatar.createMoney()
        self.acceptOnce('escape-up', base.localAvatar.bookButtonClicked)

    def exit(self):
        Walk.Walk.exit(self)
        self.ignore('escape-up')
        base.localAvatar.hideBookButton()
        base.localAvatar.disableLaffMeter()
        base.localAvatar.disableGags()
        base.localAvatar.hideGagButton()
        base.localAvatar.disableMoney()