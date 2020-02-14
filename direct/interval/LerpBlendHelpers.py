# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.interval.LerpBlendHelpers
__all__ = [
 'getBlend']
from panda3d.direct import *
easeIn = EaseInBlendType()
easeOut = EaseOutBlendType()
easeInOut = EaseInOutBlendType()
noBlend = NoBlendType()

def getBlend(blendType):
    if blendType == 'easeIn':
        return easeIn
    if blendType == 'easeOut':
        return easeOut
    if blendType == 'easeInOut':
        return easeInOut
    if blendType == 'noBlend':
        return noBlend
    raise Exception('Error: LerpInterval.__getBlend: Unknown blend type')