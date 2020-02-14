# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.shop.DistributedGagShop
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.actor.Actor import Actor
from lib.coginvasion.shop.DistributedShop import DistributedShop
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.shop.GagShop import GagShop
from lib.coginvasion.npc.Char import Char

class DistributedGagShop(DistributedShop):
    notify = directNotify.newCategory('DistributedGagShop')

    def __init__(self, cr):
        DistributedShop.__init__(self, cr)
        self.shop = GagShop(self, 'gagShopDone')
        self.barrel = None
        self.barrelGags = []
        return

    def setupClerk(self):
        DistributedShop.setupClerk(self)
        self.clerk = Char()
        self.clerk.generateChar(CIGlobals.Goofy)
        self.clerk.setName(CIGlobals.Goofy)
        self.clerk.setupNameTag()
        self.clerk.reparentTo(self)
        self.clerk.animFSM.request('neutral')
        self.barrel = loader.loadModel('phase_5.5/models/estate/wheelbarrel.bam')
        self.barrel.find('**/dirt').removeNode()
        self.barrel.reparentTo(self.clerk)
        self.barrel.setX(-3.5)
        self.barrel.setH(90)
        gags = {'tart': {'pos': (0, 0.65, 1), 'hpr': (0, 30.26, 0)}, 'tart': {'pos': (0, 0, 1.14)}, 'cps': {'pos': (0, -0.56, 1.42), 'hpr': (323.97, 37.87, 0)}, 'cps': {'pos': (0, 0, 1.49)}, 'cake': {'pos': (0, 0.94, 1.4), 'playrate': 0.3}, 'cake': {'pos': (0, -0.1, 1.4), 'scale': 0.5, 'playrate': -0.3}}
        for gag, info in gags.iteritems():
            mdl = None
            if gag == 'cake':
                mdl = Actor('phase_5/models/props/birthday-cake-mod.bam', {'chan': 'phase_5/models/props/birthday-cake-chan.bam'})
                if 'playrate' in info:
                    mdl.setPlayRate(info.get('playrate'), 'chan')
                mdl.loop('chan')
            if not mdl:
                if gag == 'tart':
                    mdl = loader.loadModel('phase_3.5/models/props/tart.bam')
                elif gag == 'cps':
                    mdl = loader.loadModel('phase_5/models/props/cream-pie-slice.bam')
            if 'pos' in info:
                mdl.setPos(info.get('pos'))
            if 'hpr' in info:
                mdl.setHpr(info.get('hpr'))
            if 'scale' in info:
                mdl.setScale(info.get('scale'))
            else:
                mdl.setScale(0.6)
            mdl.reparentTo(self.barrel)

        return

    def deleteClerk(self):
        if hasattr(self, 'barrel'):
            for gag in self.barrel.getChildren():
                if isinstance(gag, Actor):
                    gag.cleanup()
                else:
                    gag.removeNode()

            self.barrel.removeNode()
            del self.barrel
        DistributedShop.deleteClerk(self)

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