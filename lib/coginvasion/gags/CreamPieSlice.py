# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.CreamPieSlice
from lib.coginvasion.gags.ThrowGag import ThrowGag
from lib.coginvasion.gags import GagGlobals
from lib.coginvasion.globals import CIGlobals

class CreamPieSlice(ThrowGag):

    def __init__(self):
        ThrowGag.__init__(self, CIGlobals.CreamPieSlice, 'phase_5/models/props/cream-pie-slice.bam', 17, GagGlobals.SLICE_SPLAT_SFX, GagGlobals.CREAM_SPLAT_COLOR)
        self.setHealth(GagGlobals.CREAM_PIE_SLICE_HEAL)
        self.setImage('phase_3.5/maps/cream_pie_slice.png')