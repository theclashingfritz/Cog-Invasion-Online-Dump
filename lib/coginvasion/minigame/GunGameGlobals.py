# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.GunGameGlobals
from TeamMinigame import TEAM1, TEAM2
from panda3d.core import BitMask32

class GameModes:
    CASUAL = 0
    CTF = 1
    KOTH = 2


class Teams:
    RED = TEAM2
    BLUE = TEAM1


FFA_MODES = [
 GameModes.KOTH, GameModes.CASUAL]
CTF = 'Capture the Flag'
CASUAL = 'Casual Mode'
KOTH = 'King of the Hill'
RED = 'Red Robber Barons'
BLUE = 'Blue Bloodsuckers'
MSG_CHOSE_MODE_TIE = "It's a tie! Randomly chose: {0}"
MSG_CHOSE_MODE = '{0}, it is!'
GameModeNameById = {GameModes.CASUAL: CASUAL, GameModes.CTF: CTF, GameModes.KOTH: KOTH}
TeamColorById = {Teams.RED: (1, 0, 0, 1), Teams.BLUE: (0.2, 0.2, 1, 1)}
TeamNameById = {Teams.RED: RED, Teams.BLUE: BLUE}
CTF_SCORE_CAP = 3
HILL_BITMASK = BitMask32(4)
ToonSpeedFactor = 1.35
ToonForwardSpeed = 16.0 * ToonSpeedFactor
ToonJumpForce = 24.0
ToonReverseSpeed = 16.0 * ToonSpeedFactor
ToonRotateSpeed = 80.0 * ToonSpeedFactor