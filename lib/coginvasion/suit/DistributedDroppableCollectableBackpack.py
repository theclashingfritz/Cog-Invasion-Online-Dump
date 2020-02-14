# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.suit.DistributedDroppableCollectableBackpack
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.IntervalGlobal import SoundInterval
from direct.task import Task
from DistributedDroppableCollectableObject import DistributedDroppableCollectableObject
from lib.coginvasion.gui.Dialog import GlobalDialog
from lib.coginvasion.gags import GagGlobals
import random

class DistributedDroppableCollectableBackpack(DistributedDroppableCollectableObject):
    notify = directNotify.newCategory('DistributedDroppableCollectableBackpack')
    MSG_CONFIRM = 'This backpack contains:\n\n%s\n\nAre you sure you want to use this backpack?'
    MSG_UNZIPPING = 'Unzipping...'
    UNZIP_TIME = 6.0

    def __init__(self, cr):
        try:
            self.DistributedDroppableCollectableBackpack_initialized
            return
        except:
            self.DistributedDroppableCollectableBackpack_initialized = 1

        DistributedDroppableCollectableObject.__init__(self, cr)
        self.backpack = None
        self.dropShadow = None
        self.bp = None
        self.pickUpDialog = None
        self.unzippingDialog = None
        self.soundUnzipping = None
        self.rotateTaskName = 'Rotate Pack'
        self.rotateSpeed = 30
        self.backpackScale = 0.35
        return

    def setBP(self, bp):
        self.bp = bp

    def getBP(self):
        return self.bp

    def removePickUpGui(self):
        if self.pickUpDialog:
            self.pickUpDialog.cleanup()
            self.pickUpDialog = None
        return

    def removeUnzipGui(self):
        if self.unzippingDialog:
            self.unzippingDialog.cleanup()
            self.unzippingDialog = None
        return

    def __showPickUpGui(self):
        gagNameArray = []
        gagString = '%s, %s, %s, %s'
        for gagId in self.getBP():
            gagNameArray.append(GagGlobals.gagIds.get(gagId))

        self.pickUpDialog = GlobalDialog(message=self.MSG_CONFIRM % (gagString % (gagNameArray[0], gagNameArray[1], gagNameArray[2], gagNameArray[3])), doneEvent='pickUpGui-Done', style=1)
        self.pickUpDialog.show()
        self.acceptOnce('pickUpGui-Done', self.__handleBackpackChoice)

    def __handleBackpackChoice(self):
        value = self.pickUpDialog.getValue()
        self.removePickUpGui()
        if value:
            self.__showUnzippingGui()
        else:
            self.cr.playGame.getPlace().fsm.request('walk')
            self.acceptCollisions()

    def __showUnzippingGui(self):
        self.unzippingDialog = GlobalDialog(message=self.MSG_UNZIPPING, style=0)
        self.unzippingDialog.show()
        self.soundUnzipping = base.loadSfx('phase_3.5/audio/sfx/ci_s_bpunzip.ogg')
        SoundInterval(self.soundUnzipping).start()
        base.taskMgr.doMethodLater(self.UNZIP_TIME, self.__unzipWaitDone, 'DDCBackpack-unzipWaitDone')

    def __unzipWaitDone(self, task):
        self.sendUpdate('collectedObject', [])
        self.removeUnzipGui()
        self.cr.playGame.getPlace().fsm.request('walk')
        return Task.done

    def __rotateBackpack(self, task):
        if self.backpack:
            self.backpack.setH(task.time * self.rotateSpeed)
            return Task.cont
        return Task.done

    def loadObject(self):
        self.removeObject()
        self.backpack = loader.loadModel('phase_4/models/accessories/tt_m_chr_avt_acc_pac_gags.bam')
        self.backpack.setScale(self.backpackScale)
        self.backpack.setZ(1.4)
        self.backpack.setH(random.uniform(0.0, 360.0))
        self.backpack.reparentTo(self)
        self.dropShadow = loader.loadModel('phase_3/models/props/drop_shadow.bam')
        self.dropShadow.setColor(0, 0, 0, 0.5)
        self.dropShadow.setScale(0.25)
        self.dropShadow.setZ(0.025)
        self.dropShadow.flattenLight()
        self.dropShadow.reparentTo(self)
        base.taskMgr.add(self.__rotateBackpack, self.rotateTaskName)

    def removeObject(self):
        if self.backpack:
            base.taskMgr.remove(self.rotateTaskName)
            self.dropShadow.removeNode()
            self.backpack.removeNode()
            self.dropShadow = None
            self.backpack = None
        return

    def handleCollisions(self, entry):
        self.cr.playGame.getPlace().fsm.request('stop')
        self.__showPickUpGui()

    def disable(self):
        base.taskMgr.remove('DDCBackpack-unzipWaitDone')
        self.removeUnzipGui()
        self.removePickUpGui()
        if self.cr.playGame.getPlace():
            if self.cr.playGame.getPlace().fsm:
                if self.cr.playGame.getPlace().fsm.getCurrentState():
                    if self.cr.playGame.getPlace().fsm.getCurrentState().getName() == 'stop':
                        self.cr.playGame.getPlace().fsm.request('walk')
        self.soundUnzipping = None
        DistributedDroppableCollectableObject.disable(self)
        return