# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.MinigameUtils
from direct.gui.DirectGui import OnscreenImage

def getCrosshair(scale=0.04, color=(1, 1, 1, 1), hidden=True):
    crosshair = OnscreenImage(image='phase_4/maps/crosshair.png', scale=scale, color=color)
    crosshair.setTransparency(True)
    if hidden:
        crosshair.hide()
    return crosshair