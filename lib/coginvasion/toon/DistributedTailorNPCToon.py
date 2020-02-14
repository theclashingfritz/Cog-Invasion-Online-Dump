# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.toon.DistributedTailorNPCToon
from direct.directnotify.DirectNotifyGlobal import directNotify
import DistributedNPCToon

class DistributedTailorNPCToon(DistributedNPCToon.DistributedNPCToon):
    notify = directNotify.newCategory('DistributedTailorToon')

    def __init__(self, cr):
        DistributedNPCToon.DistributedNPCToon.__init__(self, cr)
        self.clothesGUI = None
        self.avatar = None
        self.oldStyle = None
        self.isBrowsing = 0
        self.button = None
        self.popupInfo = None
        return

    def cleanup(self):
        self.ignoreAll()
        taskMgr.remove(self.uniqueName('popupPurchaseGUI'))
        if self.clothesGUI:
            self.clothesGUI.exit()
            self.clothesGUI.unload()
            self.clothesGUI = None
            if self.button:
                self.button.destroy()
                del self.button
            self.cancelButton.destroy()
            del self.cancelButton
            del self.gui
            self.counter.show()
            del self.counter
        if self.popupInfo:
            self.popupInfo.destroy()
            self.popupInfo = None
        return

    def disable(self):
        self.cleanup()
        self.avatar = None
        self.oldStyle = None
        base.localAvatar.posCamera(0, 0)
        DistributedNPCToon.DistributedNPCToon.disable(self)
        return

    def resetTailor(self):
        self.show()
        self.cleanup()
        self.startLookAround()
        self.detachAvatars()
        self.clearMat()
        if self.isLocal():
            self.freeAvatar()

    def isLocal(self):
        return self.avatar == base.localAvatar