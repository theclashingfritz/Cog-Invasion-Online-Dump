# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.Factory
__all__ = [
 'Factory']
from direct.directnotify.DirectNotifyGlobal import directNotify

class Factory:
    notify = directNotify.newCategory('Factory')

    def __init__(self):
        self._type2ctor = {}

    def create(self, type, *args, **kwArgs):
        return self._type2ctor[type](*args, **kwArgs)

    def _registerType(self, type, ctor):
        if type in self._type2ctor:
            self.notify.debug('replacing %s ctor %s with %s' % (
             type, self._type2ctor[type], ctor))
        self._type2ctor[type] = ctor

    def _registerTypes(self, type2ctor):
        for type, ctor in type2ctor.items():
            self._registerType(type, ctor)

    def nullCtor(self, *args, **kwArgs):
        return