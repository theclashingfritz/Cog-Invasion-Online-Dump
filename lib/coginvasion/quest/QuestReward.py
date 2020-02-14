# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.quest.QuestReward
from direct.directnotify.DirectNotifyGlobal import directNotify
import RewardType

class QuestReward:
    notify = directNotify.newCategory('QuestReward')

    def __init__(self, rewardType, rewardModifier):
        self.rewardType = rewardType
        self.rewardModifier = rewardModifier

    def award(self):
        if self.rewardType == RewardType.JELLYBEANS:
            base.localAvatar.b_setMoney(base.localAvatar.getMoney() + self.rewardModifier)
        else:
            if self.rewardType == RewardType.TELEPORT_ACCESS:
                teleportAccess = base.localAvatar.getTeleportAccess()
                teleportAccess.append(self.rewardModifier)
                base.localAvatar.b_setTeleportAccess(teleportAccess)
            else:
                if self.rewardType == RewardType.LAFF_POINTS:
                    base.localAvatar.b_setMaxHealth(base.localAvatar.getMaxHealth() + self.rewardModifier)
                    base.localAvatar.b_setHealth(base.localAvatar.getMaxHealth())