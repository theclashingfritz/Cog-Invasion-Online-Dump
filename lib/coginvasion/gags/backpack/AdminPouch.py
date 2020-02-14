# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.backpack.AdminPouch
from lib.coginvasion.gags.backpack.Backpack import Backpack
from lib.coginvasion.gags.GagManager import GagManager

class AdminPouch(Backpack):

    def __init__(self):
        Backpack.__init__(self)
        gagMgr = GagManager()
        for gag in gagMgr.getGags().values():
            gag = gag()
            self.setMaxSupply(255, gag.getName())