# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.toon.ToonGlobals
from lib.coginvasion.globals import CIGlobals
BASE_MODEL = 'phase_%s/models/char/tt_a_chr_%s_%s_%s_%s.bam'
ANIMATIONS = {'neutral': [
             3, 'neutral'], 
   'run': [
         3, 'run'], 
   'walk': [
          3.5, 'walk'], 
   'pie': [
         3.5, 'pie-throw'], 
   'fallb': [
           4, 'slip-backward'], 
   'fallf': [
           4, 'slip-forward'], 
   'lose': [
          5, 'lose'], 
   'win': [
         3.5, 'victory-dance'], 
   'squirt': [
            5, 'water-gun'], 
   'zend': [
          3.5, 'jump-zend'], 
   'tele': [
          3.5, 'teleport'], 
   'book': [
          3.5, 'book'], 
   'leap': [
          3.5, 'leap_zhang'], 
   'jump': [
          3.5, 'jump-zhang'], 
   'happy': [
           3.5, 'jump'], 
   'shrug': [
           3.5, 'shrug'], 
   'hdance': [
            5, 'happy-dance'], 
   'wave': [
          3.5, 'wave'], 
   'swim': [
          4, 'swim'], 
   'toss': [
          5, 'toss'], 
   'cringe': [
            3.5, 'cringe'], 
   'conked': [
            3.5, 'conked'], 
   'catchneutral': [
                  4, 'gameneutral'], 
   'catchrun': [
              4, 'gamerun'], 
   'hold-bottle': [
                 5, 'hold-bottle'], 
   'push-button': [
                 3.5, 'press-button'], 
   'happy-dance': [
                 5, 'happy-dance'], 
   'juggle': [
            5, 'juggle'], 
   'shout': [
           5, 'shout'], 
   'dneutral': [
              4, 'sad-neutral'], 
   'dwalk': [
           4, 'losewalk'], 
   'smooch': [
            5, 'smooch'], 
   'conked': [
            3.5, 'conked'], 
   'sound': [
           5, 'shout'], 
   'sprinkle-dust': [
                   5, 'sprinkle-dust'], 
   'start-sit': [
               4, 'intoSit'], 
   'sit': [
         4, 'sit'], 
   'water': [
           3.5, 'water'], 
   'spit': [
          5, 'spit'], 
   'firehose': [
              5, 'firehose'], 
   'applause': [
              4, 'applause'], 
   'left': [
          4, 'left'], 
   'strafe': [
            3, 'strafe'], 
   'pout': [
          6, 'badloop-putt']}
STAFF_TOKENS = {0: 500, 2: 300}

def generateBodyPart(toon, bodyPart, partType, partPhase, pantType):
    partAnimations = {}
    mdlPath = BASE_MODEL % (partPhase, partType, pantType, bodyPart,
     str(CIGlobals.getModelDetail(toon.avatarType)))
    if '_-' in mdlPath:
        mdlPath = mdlPath.replace('_-', '-')
    if '__' in mdlPath:
        mdlPath = mdlPath.replace('__', '_')
    toon.loadModel(mdlPath, bodyPart)
    for animName in ANIMATIONS:
        animationData = ANIMATIONS[animName]
        animPath = None
        if len(animationData) == 2:
            animPhase = animationData[0]
            animFile = animationData[1]
            animPath = BASE_MODEL % (animPhase, partType, pantType,
             bodyPart, animFile)
            if '_-' in animPath:
                animPath = animPath.replace('_-', '-')
            if '__' in animPath:
                animPath = animPath.replace('__', '_')
        partAnimations[animName] = animPath

    toon.loadAnims(partAnimations, bodyPart)
    return