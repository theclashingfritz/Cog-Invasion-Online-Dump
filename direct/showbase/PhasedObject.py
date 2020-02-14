# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.PhasedObject
from direct.directnotify.DirectNotifyGlobal import *

class PhasedObject:
    notify = directNotify.newCategory('PhasedObject')

    def __init__(self, aliasMap={}):
        self.phase = -1
        self.phaseAliasMap = {}
        self.aliasPhaseMap = {}
        self.__phasing = False
        for alias, phase in aliasMap.items():
            self.setAlias(phase, alias)

    def __repr__(self):
        return 'PhasedObject(%s)' % str(self.aliasPhaseMap)

    def __str__(self):
        outStr = PhasedObject.__repr__(self)
        outStr += " in phase '%s'" % self.getPhase()
        return outStr

    def setAlias(self, phase, alias):
        self.phaseAliasMap[phase] = alias
        self.aliasPhaseMap[alias] = phase

    def getPhaseAlias(self, phase):
        return self.phaseAliasMap.get(phase, phase)

    def getAliasPhase(self, alias):
        return self.aliasPhaseMap.get(alias, alias)

    def getPhase(self):
        return self.getPhaseAlias(self.phase)

    def setPhase(self, aPhase):
        self.__phasing = True
        phase = self.aliasPhaseMap.get(aPhase, aPhase)
        if phase > self.phase:
            for x in range(self.phase + 1, phase + 1):
                self.__loadPhase(x)

        else:
            if phase < self.phase:
                for x in range(self.phase, phase, -1):
                    self.__unloadPhase(x)

        self.__phasing = False

    def cleanup(self):
        if self.phase >= 0:
            self.setPhase(-1)

    def __loadPhase(self, phase):
        aPhase = self.phaseAliasMap.get(phase, phase)
        getattr(self, 'loadPhase%s' % aPhase, lambda : self.__phaseNotFound('load', aPhase))()
        self.phase = phase

    def __unloadPhase(self, phase):
        aPhase = self.phaseAliasMap.get(phase, phase)
        getattr(self, 'unloadPhase%s' % aPhase, lambda : self.__phaseNotFound('unload', aPhase))()
        self.phase = phase - 1

    def __phaseNotFound(self, mode, aPhase):
        pass