# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cog.Voice


class Voice:

    def __init__(self, filePath):
        self.filePath = filePath

    def getSoundFile(self, expression):
        return self.filePath % expression


NORMAL = Voice('phase_3.5/audio/dial/COG_VO_%s.ogg')
SKELETON = Voice('phase_5/audio/sfx/Skel_COG_VO_%s.ogg')
BOSS = Voice('phase_9/audio/sfx/Boss_COG_VO_%s.ogg')

def getVoiceById(self, index):
    voices = [
     NORMAL, SKELETON, BOSS]
    return voices[index]