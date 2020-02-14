# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.WholeCreamPie
from lib.coginvasion.gags.ThrowGag import ThrowGag
from lib.coginvasion.gags import GagGlobals
from lib.coginvasion.globals import CIGlobals

class WholeCreamPie(ThrowGag):

    def __init__(self):
        ThrowGag.__init__(self, CIGlobals.WholeCreamPie, 'phase_3.5/models/props/tart.bam', 36, GagGlobals.WHOLE_PIE_SPLAT_SFX, GagGlobals.CREAM_SPLAT_COLOR)
        self.setHealth(GagGlobals.CREAM_PIE_HEAL)
        self.setImage('phase_3.5/maps/tart.png')