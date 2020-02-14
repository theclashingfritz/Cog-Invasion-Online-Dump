# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.Cupcake
from lib.coginvasion.gags.ThrowGag import ThrowGag
from lib.coginvasion.gags import GagGlobals
from lib.coginvasion.globals import CIGlobals

class Cupcake(ThrowGag):

    def __init__(self):
        ThrowGag.__init__(self, CIGlobals.Cupcake, 'phase_3.5/models/props/tart.bam', 6, GagGlobals.TART_SPLAT_SFX, GagGlobals.TART_SPLAT_COLOR, scale=GagGlobals.CUPCAKE_SCALE)
        self.setHealth(GagGlobals.CUPCAKE_HEAL)
        self.setImage('phase_3.5/maps/cupcake.png')