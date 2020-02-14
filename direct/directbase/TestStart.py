# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.directbase.TestStart
print 'TestStart: Starting up test environment.'
from panda3d.core import *
from direct.showbase.PythonUtil import *
from direct.showbase import ShowBase
base = ShowBase.ShowBase()
loader.loadModel('models/misc/xyzAxis').reparentTo(render)
camera.setPosHpr(0, -10.0, 0, 0, 0, 0)
base.camLens.setFov(52.0)
base.camLens.setNearFar(1.0, 10000.0)
globalClock.setMaxDt(0.2)
base.enableParticles()
base.graphicsEngine.renderFrame()