# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.Sandbag
from lib.coginvasion.gags.LightDropGag import LightDropGag
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.gags import GagGlobals

class Sandbag(LightDropGag):

    def __init__(self):
        LightDropGag.__init__(self, CIGlobals.Sandbag, GagGlobals.getProp('5', 'sandbag-mod'), GagGlobals.getProp('5', 'sandbag-chan'), 18, GagGlobals.BAG_DROP_SFX, GagGlobals.BAG_MISS_SFX, rotate90=False, sphereSize=2)
        self.setImage('phase_3.5/maps/sandbag.png')