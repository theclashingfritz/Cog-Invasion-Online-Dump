# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.quests.QuestGlobals
from lib.coginvasion.suit import CogBattleGlobals
from lib.coginvasion.globals.CIGlobals import *
QuestTypes = {-1: 'Do', 0: 'Defeat', 1: 'Recover', 2: 'Deliver'}
QuestSubjects = {-1: 'Nothing', 0: 'Cogs', 1: 'Cog Invasions', 2: 'Lawbots', 3: 'Bossbots', 
   4: 'Sellbots', 5: 'Cashbots', 6: 'Cog Tournaments'}
AbbrToDept = {'l': QuestSubjects[2], 'c': QuestSubjects[3], 's': QuestSubjects[4], 'm': QuestSubjects[5]}
CogSubjects = [0, 2, 3, 4, 5, 6]
DeptSubjects = [2, 3, 4, 5]
QuestSubject2SubjectId = {v:k for k, v in QuestSubjects.items()}
Areas = [ToontownCentral, TheBrrrgh, DonaldsDreamland, MinniesMelodyland, DaisyGardens, DonaldsDock]
QuestAreas = {-1: 'Nowhere', 
   0: 'Anywhere', 
   1: 'in ' + ToontownCentral, 
   2: 'in ' + TheBrrrgh, 
   3: 'in ' + DonaldsDreamland, 
   4: 'in ' + MinniesMelodyland, 
   5: 'in ' + DaisyGardens, 
   6: 'in ' + DonaldsDock}
QuestRewards = {-1: 'No reward', 0: 'For a %d point Laff boost', 1: 'For access to %s', 2: 'For %d jellybeans'}
TypeIndex = 0
SubjectIndex = 1
AreaIndex = 2
RewardIndex = 3
ProgressIndex = 4
GoalIndex = 5
RewardValueIndex = 6

def makePastTense(text):
    if text.endswith('e'):
        return text + 'd'
    return text + 'ed'


def makeSingular(text):
    if text.endswith('s'):
        return text[:-1]


def makePlural(text):
    if text.endswith('y'):
        text = text[:-1]
        return text + 'ies'
    if text.endswith('s'):
        return text
    return text + 's'