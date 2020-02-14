# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.TrapGag
from lib.coginvasion.gags.Gag import Gag
from lib.coginvasion.gags.GagType import GagType
import abc

class TrapGag(Gag):

    def __init__(self, name, model, damage, hitSfx, anim=None, doesAutoRelease=True):
        Gag.__init__(self, name, model, damage, GagType.TRAP, hitSfx, anim=anim, autoRelease=doesAutoRelease)
        self.hitSfx = None
        self.entity = None
        self.timeout = 3.0
        if game.process == 'client':
            self.hitSfx = base.audio3d.loadSfx(hitSfx)
        return

    def build(self):
        super(TrapGag, self).build()

    @abc.abstractmethod
    def buildCollisions(self):
        if not self.gag:
            return

    @abc.abstractmethod
    def activate(self):
        pass

    @abc.abstractmethod
    def onCollision(self, entry):
        pass

    @abc.abstractmethod
    def d_doCollision(self):
        pass

    def delete(self):
        super(TrapGag, self).delete()

    def unEquip(self):
        super(TrapGag, self).unEquip()
        if self.gag:
            self.cleanupGag()

    @abc.abstractmethod
    def startTrap(self):
        super(TrapGag, self).start()

    def throw(self):
        pass

    def release(self):
        super(TrapGag, self).release()
        if self.isLocal():
            base.localAvatar.sendUpdate('usedGag', [self.id])
        if not self.gag:
            return

    def getHandle(self):
        return self

    def getGag(self):
        if not self.gag:
            return self.entity
        return Gag.getGag(self)