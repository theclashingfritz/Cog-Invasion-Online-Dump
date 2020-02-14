# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.shop.BattleShop
from direct.directnotify.DirectNotifyGlobal import directNotify
from lib.coginvasion.shop.Shop import Shop
from lib.coginvasion.shop.ItemType import ItemType

class BattleShop(Shop):
    notify = directNotify.newCategory('BattleShop')

    def __init__(self, distShop, doneEvent):
        Shop.__init__(self, distShop, doneEvent, wantTurretCount=1)
        self.distShop.addItem('Whole Cream \nPie', ItemType.UPGRADE, 200, 'phase_3.5/maps/cannon-icon.png', upgradeID=0, maxUpgrades=1)
        self.distShop.addItem('Whole Fruit \nPie', ItemType.UPGRADE, 150, 'phase_3.5/maps/cannon-icon.png', upgradeID=1, maxUpgrades=1)
        self.distShop.addItem('+20 Laff', ItemType.HEAL, 100, 'phase_3.5/maps/ice-cream-cone.png', heal=20, healCooldown=5, showTitle=True)
        self.items = self.distShop.getItems()

    def confirmPurchase(self):
        self.distShop.sendUpdate('confirmPurchase', [[base.localAvatar.getPUInventory()[0], base.localAvatar.getPUInventory()[1]], base.localAvatar.getMoney()])
        if self.upgradesPurchased:
            if base.localAvatar.getPUInventory()[0] > 0:
                if base.localAvatar.getMyBattle():
                    if base.localAvatar.getMyBattle().getTurretManager():
                        if not base.localAvatar.getMyBattle().getTurretManager().myTurret:
                            base.localAvatar.getMyBattle().getTurretManager().createTurretButton()
        Shop.confirmPurchase(self)

    def cancelPurchase(self):
        if self.upgradesPurchased:
            if self.originalUpgrades[0] < base.localAvatar.getPUInventory()[0]:
                if base.localAvatar.getMyBattle():
                    if base.localAvatar.getMyBattle().getTurretManager():
                        base.localAvatar.getMyBattle().getTurretManager().destroyGui()
        base.localAvatar.setPUInventory(self.originalUpgrades)
        Shop.cancelPurchase(self)

    def enter(self):
        self.originalUpgrades = base.localAvatar.getPUInventory()
        self.upgradesPurchased = False
        Shop.enter(self)

    def exit(self):
        Shop.exit(self)
        self.originalUpgrades = None
        self.upgradesPurchased = None
        return

    def update(self, page=None):
        Shop.update(self, page)