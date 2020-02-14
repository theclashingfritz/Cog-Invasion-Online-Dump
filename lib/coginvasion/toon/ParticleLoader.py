# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.toon.ParticleLoader
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import *

def loadParticleEffect(file):
    p = ParticleEffect()
    p.loadConfig(Filename(file))
    return p