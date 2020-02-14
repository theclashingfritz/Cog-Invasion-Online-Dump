# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.GagUtils
from direct.particles.ParticleEffect import ParticleEffect
from direct.actor.Actor import Actor

def loadParticle(phase, name):
    particle = ParticleEffect()
    particle.loadConfig('phase_%s/etc/%s.ptf' % (str(phase), name))
    return particle


def destroyProp(prop):
    if isinstance(prop, Actor):
        prop.cleanup()
    prop.removeNode()