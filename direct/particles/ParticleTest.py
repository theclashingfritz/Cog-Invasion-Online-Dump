# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.particles.ParticleTest
if __name__ == '__main__':
    from direct.directbase.TestStart import *
    from panda3d.physics import LinearVectorForce
    from panda3d.core import Vec3
    import ParticleEffect
    from direct.tkpanels import ParticlePanel
    import Particles, ForceGroup
    base.enableParticles()
    fg = ForceGroup.ForceGroup()
    gravity = LinearVectorForce(Vec3(0.0, 0.0, -10.0))
    fg.addForce(gravity)
    p = Particles.Particles()
    pe = ParticleEffect.ParticleEffect('particle-fx')
    pe.reparentTo(render)
    pe.addForceGroup(fg)
    pe.addParticles(p)
    pp = ParticlePanel.ParticlePanel(pe)
    run()