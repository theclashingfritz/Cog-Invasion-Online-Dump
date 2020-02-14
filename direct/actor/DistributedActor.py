# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.actor.DistributedActor
__all__ = [
 'DistributedActor']
from direct.distributed import DistributedNode
import Actor

class DistributedActor(DistributedNode.DistributedNode, Actor.Actor):

    def __init__(self, cr):
        try:
            self.DistributedActor_initialized
        except:
            self.DistributedActor_initialized = 1
            Actor.Actor.__init__(self)
            DistributedNode.DistributedNode.__init__(self, cr)
            self.setCacheable(1)

    def disable(self):
        if not self.isEmpty():
            Actor.Actor.unloadAnims(self, None, None, None)
        DistributedNode.DistributedNode.disable(self)
        return

    def delete(self):
        try:
            self.DistributedActor_deleted
        except:
            self.DistributedActor_deleted = 1
            DistributedNode.DistributedNode.delete(self)
            Actor.Actor.delete(self)

    def loop(self, animName, restart=1, partName=None, fromFrame=None, toFrame=None):
        return Actor.Actor.loop(self, animName, restart, partName, fromFrame, toFrame)