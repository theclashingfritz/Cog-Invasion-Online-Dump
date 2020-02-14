# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.shop.DistributedBattleShop
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import DirectLabel
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.shop.DistributedShop import DistributedShop
from lib.coginvasion.shop.BattleShop import BattleShop
from lib.coginvasion.toon.Toon import Toon
from lib.coginvasion.npc.NPCGlobals import NPC_DNA
from lib.coginvasion.nametag import NametagGlobals

class DistributedBattleShop(DistributedShop):
    notify = directNotify.newCategory('DistributedBattleShop')

    def __init__(self, cr):
        DistributedShop.__init__(self, cr)
        self.shop = BattleShop(self, 'battleShopDone')
        self.stand = None
        self.standText = None
        return

    def setupClerk(self):
        self.clerk = Toon(self.cr)
        self.clerk.setName('Coach')
        self.clerk.setDNAStrand(NPC_DNA['Coach'])
        self.clerk.nametag.setNametagColor(NametagGlobals.NametagColors[NametagGlobals.CCNPC])
        self.clerk.nametag.setActive(0)
        self.clerk.nametag.updateAll()
        self.clerk.reparentTo(self)
        self.clerk.animFSM.request('neutral')
        self.clerk.setH(180)
        self.clerk.setPos(0, 2.2, 1)
        self.stand = loader.loadModel('phase_4/models/props/bubblestand.egg')
        self.stand.reparentTo(self)
        self.stand.setScale(1.1)
        self.standText = DirectLabel(text="Coach's Battle Shop", text_fg=(0.6, 0, 0,
                                                                          1), text_decal=True, relief=None, parent=self.stand, pos=(0,
                                                                                                                                    -0.875,
                                                                                                                                    5.2), scale=0.45, text_font=CIGlobals.getMickeyFont())
        return

    def deleteClerk(self):
        DistributedShop.deleteClerk(self)
        if hasattr(self, 'standText'):
            self.standText.destroy()
            self.stand.removeNode()
            del self.standText
            del self.stand

    def enterAccepted(self):
        if not self.inShop:
            self.shop.load()
            self.shop.enter()
            self.acceptOnce(self.shop.doneEvent, self.handleShopDone)
            self.inShop = True

    def handleShopDone(self):
        self.shop.exit()
        self.shop.unload()
        self.d_requestExit()

    def disable(self):
        DistributedShop.disable(self)
        self.ignore(self.shop.doneEvent)
        if self.inShop:
            self.handleShopDone()

    def delete(self):
        DistributedShop.delete(self)
        self.shop = None
        return