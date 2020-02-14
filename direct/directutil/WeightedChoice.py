# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.directutil.WeightedChoice
import random

class WeightedChoice:

    def __init__(self, listOfLists, weightIndex=0):
        t = 0
        for i in listOfLists:
            t += i[weightIndex]

        self.total = t
        self.listOfLists = listOfLists
        self.weightIndex = weightIndex

    def choose(self, rng=random):
        roll = rng.randrange(self.total)
        weight = self.weightIndex
        for i in self.listOfLists:
            roll -= i[weight]
            if roll <= 0:
                return i