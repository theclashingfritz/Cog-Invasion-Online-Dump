# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cog.SuitCallInBackupBehavior
from lib.coginvasion.cog.SuitBehaviorBase import SuitBehaviorBase
from lib.coginvasion.cog.SuitFollowBossBehavior import SuitFollowBossBehavior
from lib.coginvasion.cog import Variant
from direct.task.Task import Task
from direct.interval.IntervalGlobal import Sequence, Wait, Func
import random
SPEECH_BY_BACKUP_LVL = {0: ['Gah! I need backup!', 'Get me some backup!', 'Get them!!!', 'Attack!!'], 1: [
     'Is that all you got, Toons?', "There's more where that came from!", 'Send in higher backup!',
     'I need stronger reinforcements!'], 
   2: [
     "No, no, it's not working... give me everything you got!", 'I need everything I can get!',
     'Get me the highest level of backup you have!', 'Just try and get through these reinforcements!']}

class SuitCallInBackupBehavior(SuitBehaviorBase):

    def __init__(self, suit):
        doneEvent = 'suit%s-callInBackup'
        SuitBehaviorBase.__init__(self, suit, doneEvent)
        self.backup_levels = {1: range(1, 5), 2: range(5, 9), 
           3: range(9, 13)}
        self.backup_request_size = 18
        self.backupLevel = -1
        self.backupAvailable = True
        self.backupCooldown = None
        self.calledInBackup = 0
        self.isEntered = 0
        return

    def enter(self):
        SuitBehaviorBase.enter(self)
        if self.backupAvailable and self.backupCooldown is None:
            self.__toggleBackupAvailable()
            self.backupLevel = self.getBackupLevel()
            backupCooldown = random.randint(16, 20)
            self.backupCooldown = Sequence(Wait(backupCooldown), Func(self.__toggleBackupAvailable))
            self.backupCooldown.start()
            mgr = self.suit.getManager()
            mgr.flyAwayAllSuits()
            mgr.sendSysMessage(('The {0} is calling in backup level {1}!').format(self.suit.getName(), self.backupLevel + 1))
            mgr.suitsRequest = self.backup_request_size
            mgr.setActiveInvasion(1)
            mgr.suitsSpawnedThisInvasion = 0
            self.suit.d_setChat(random.choice(SPEECH_BY_BACKUP_LVL[self.backupLevel]))
            taskMgr.doMethodLater(random.randint(3, 8), self.__spawnBackupGroup, self.suit.uniqueName('Spawn Backup Group'))
        self.exit()
        return

    def resetCooldown(self):
        if self.backupCooldown:
            self.backupCooldown.pause()
            self.backupCooldown = None
        return

    def unload(self):
        SuitBehaviorBase.unload(self)
        self.resetCooldown()
        del self.backupLevel
        del self.backup_levels
        del self.backupAvailable

    def __toggleBackupAvailable(self):
        if self.backupAvailable is True:
            self.backupAvailable = False
        else:
            self.backupAvailable = True
            self.resetCooldown()

    def __spawnBackupGroup(self, task):
        if not hasattr(self, 'suit') or hasattr(self.suit, 'DELETED'):
            return Task.done
        mgr = self.suit.getManager()
        if mgr.isFullInvasion() or mgr.suits == None:
            return Task.done
        requestSize = random.randint(2, 7)
        for _ in range(requestSize):
            if mgr.isCogCountFull() or mgr.isFullInvasion():
                break
            newSuit = mgr.createSuit(levelRange=self.backup_levels[self.backupLevel + 1], anySuit=1, variant=Variant.SKELETON)
            newSuit.addBehavior(SuitFollowBossBehavior(newSuit, self.suit), priority=4)

        self.calledInBackup += requestSize
        task.delayTime = 4
        return Task.again

    def getBackupLevel(self):
        hpPerct = float(self.suit.getHealth()) / float(self.suit.getMaxHealth())
        if 0.7 <= hpPerct <= 0.9:
            return 0
        if 0.4 <= hpPerct <= 0.7:
            return 1
        if 0.05 <= hpPerct <= 0.4:
            return 2
        return -1

    def getCalledInBackup(self):
        return self.calledInBackup

    def shouldStart(self):
        newLvl = self.getBackupLevel()
        if newLvl != -1 and newLvl != self.backupLevel:
            return self.backupAvailable
        return False