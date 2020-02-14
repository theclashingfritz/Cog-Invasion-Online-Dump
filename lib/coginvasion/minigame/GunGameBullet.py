# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.GunGameBullet
import Bullet

class GunGameBullet(Bullet.Bullet):

    def __init__(self, mg, gunNozzle, local, gunName):
        Bullet.Bullet.__init__(self, mg, gunNozzle, local, gunName)

    def handleCollision(self, entry):
        Bullet.Bullet.handleCollision(self, entry)
        dmg = int(self.damageFactor / self.timeSinceShoot)
        if dmg > self.max_dmg:
            dmg = self.max_dmg
        self.mg.sendUpdate('avatarHitByBullet', [base.localAvatar.doId, dmg])
        self.deleteBullet()