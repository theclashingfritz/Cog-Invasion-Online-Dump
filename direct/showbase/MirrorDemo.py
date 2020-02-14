# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.MirrorDemo
__all__ = [
 'setupMirror', 'showFrustum']
from pandac.PandaModules import *
from direct.task import Task

def setupMirror(name, width, height, rootCamera=None):
    if rootCamera is None:
        rootCamera = base.camera
    root = render.attachNewNode(name)
    cm = CardMaker('mirror')
    cm.setFrame(width / 2.0, -width / 2.0, -height / 2.0, height / 2.0)
    cm.setHasUvs(1)
    card = root.attachNewNode(cm.generate())
    plane = Plane(Vec3(0, 1, 0), Point3(0, 0, 0))
    planeNode = PlaneNode('mirrorPlane')
    planeNode.setPlane(plane)
    planeNP = root.attachNewNode(planeNode)
    buffer = base.win.makeTextureBuffer(name, 256, 256)
    buffer.setClearColor(VBase4(0, 0, 1, 1))
    dr = buffer.makeDisplayRegion()
    camera = Camera('mirrorCamera')
    lens = PerspectiveLens()
    lens.setFilmSize(width, height)
    camera.setLens(lens)
    cameraNP = planeNP.attachNewNode(camera)
    dr.setCamera(cameraNP)
    dummy = NodePath('dummy')
    dummy.setAttrib(CullFaceAttrib.makeReverse())
    dummy.setClipPlane(planeNP)
    camera.setInitialState(dummy.getState())

    def moveCamera(task, cameraNP=cameraNP, plane=plane, planeNP=planeNP, card=card, lens=lens, width=width, height=height, rootCamera=rootCamera):
        cameraNP.setMat(rootCamera.getMat(planeNP) * plane.getReflectionMat())
        ul = cameraNP.getRelativePoint(card, Point3(-width / 2.0, 0, height / 2.0))
        ur = cameraNP.getRelativePoint(card, Point3(width / 2.0, 0, height / 2.0))
        ll = cameraNP.getRelativePoint(card, Point3(-width / 2.0, 0, -height / 2.0))
        lr = cameraNP.getRelativePoint(card, Point3(width / 2.0, 0, -height / 2.0))
        lens.setFrustumFromCorners(ul, ur, ll, lr, Lens.FCCameraPlane | Lens.FCOffAxis | Lens.FCAspectRatio)
        return Task.cont

    taskMgr.add(moveCamera, name, priority=40)
    card.setTexture(buffer.getTexture())
    return root


def showFrustum(np):
    cameraNP = np.find('**/+Camera')
    camera = cameraNP.node()
    lens = camera.getLens()
    geomNode = GeomNode('frustum')
    geomNode.addGeom(lens.makeGeometry())
    cameraNP.attachNewNode(geomNode)