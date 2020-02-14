# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: panda3d.core
from __future__ import absolute_import
from ._core import *
import sys
main_dir = Filename()
if sys.argv and sys.argv[0]:
    main_dir = Filename.from_os_specific(sys.argv[0])
if main_dir.empty():
    main_dir = ExecutionEnvironment.get_cwd()
else:
    main_dir.make_absolute()
    main_dir = Filename(main_dir.get_dirname())
ExecutionEnvironment.shadow_environment_variable('MAIN_DIR', main_dir.to_os_specific())
del sys
del main_dir

def Dtool_funcToMethod(func, cls, method_name=None):
    func.im_func = func
    func.im_self = None
    if not method_name:
        method_name = func.__name__
    cls.DtoolClassDict[method_name] = func
    return


def id(self):
    print 'Warning: NodePath.id() is deprecated.  Use hash(NodePath) or NodePath.get_key() instead.'
    return self.getKey()


Dtool_funcToMethod(id, NodePath)
del id

def getChildrenAsList(self):
    print 'Warning: NodePath.getChildrenAsList() is deprecated.  Use get_children() instead.'
    return list(self.getChildren())


Dtool_funcToMethod(getChildrenAsList, NodePath)
del getChildrenAsList

def printChildren(self):
    for child in self.getChildren():
        print child.getName()


Dtool_funcToMethod(printChildren, NodePath)
del printChildren

def removeChildren(self):
    self.getChildren().detach()


Dtool_funcToMethod(removeChildren, NodePath)
del removeChildren

def toggleVis(self):
    if self.isHidden():
        self.show()
        return 1
    self.hide()
    return 0


Dtool_funcToMethod(toggleVis, NodePath)
del toggleVis

def showSiblings(self):
    for sib in self.getParent().getChildren():
        if sib.node() != self.node():
            sib.show()


Dtool_funcToMethod(showSiblings, NodePath)
del showSiblings

def hideSiblings(self):
    for sib in self.getParent().getChildren():
        if sib.node() != self.node():
            sib.hide()


Dtool_funcToMethod(hideSiblings, NodePath)
del hideSiblings

def showAllDescendants(self):
    self.show()
    for child in self.getChildren():
        child.showAllDescendants()


Dtool_funcToMethod(showAllDescendants, NodePath)
del showAllDescendants

def isolate(self):
    self.showAllDescendants()
    self.hideSiblings()


Dtool_funcToMethod(isolate, NodePath)
del isolate

def remove(self):
    print 'Warning: NodePath.remove() is deprecated.  Use remove_node() instead.'
    messenger.send('preRemoveNodePath', [self])
    self.removeNode()


Dtool_funcToMethod(remove, NodePath)
del remove

def lsNames(self):
    if self.isEmpty():
        print '(empty)'
    else:
        type = self.node().getType().getName()
        name = self.getName()
        print type + '  ' + name
        self.lsNamesRecurse()


Dtool_funcToMethod(lsNames, NodePath)
del lsNames

def lsNamesRecurse(self, indentString=' '):
    for nodePath in self.getChildren():
        type = nodePath.node().getType().getName()
        name = nodePath.getName()
        print indentString + type + '  ' + name
        nodePath.lsNamesRecurse(indentString + ' ')


Dtool_funcToMethod(lsNamesRecurse, NodePath)
del lsNamesRecurse

def reverseLsNames(self):
    ancestors = list(self.getAncestors())
    ancestry = ancestors.reverse()
    indentString = ''
    for nodePath in ancestry:
        type = nodePath.node().getType().getName()
        name = nodePath.getName()
        print indentString + type + '  ' + name
        indentString = indentString + ' '


Dtool_funcToMethod(reverseLsNames, NodePath)
del reverseLsNames

def getAncestry(self):
    print 'NodePath.getAncestry() is deprecated.  Use get_ancestors() instead.'
    ancestors = list(self.getAncestors())
    ancestors.reverse()
    return ancestors


Dtool_funcToMethod(getAncestry, NodePath)
del getAncestry

def pPrintString(self, other=None):
    pass


Dtool_funcToMethod(pPrintString, NodePath)
del pPrintString

def printPos(self, other=None, sd=2):
    formatString = '%0.' + '%d' % sd + 'f'
    if other:
        pos = self.getPos(other)
        otherString = other.getName() + ', '
    else:
        pos = self.getPos()
        otherString = ''
    print self.getName() + '.setPos(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ')\n'


Dtool_funcToMethod(printPos, NodePath)
del printPos

def printHpr(self, other=None, sd=2):
    formatString = '%0.' + '%d' % sd + 'f'
    if other:
        hpr = self.getHpr(other)
        otherString = other.getName() + ', '
    else:
        hpr = self.getHpr()
        otherString = ''
    print self.getName() + '.setHpr(' + otherString + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ')\n'


Dtool_funcToMethod(printHpr, NodePath)
del printHpr

def printScale(self, other=None, sd=2):
    formatString = '%0.' + '%d' % sd + 'f'
    if other:
        scale = self.getScale(other)
        otherString = other.getName() + ', '
    else:
        scale = self.getScale()
        otherString = ''
    print self.getName() + '.setScale(' + otherString + formatString % scale[0] + ', ' + formatString % scale[1] + ', ' + formatString % scale[2] + ')\n'


Dtool_funcToMethod(printScale, NodePath)
del printScale

def printPosHpr(self, other=None, sd=2):
    formatString = '%0.' + '%d' % sd + 'f'
    if other:
        pos = self.getPos(other)
        hpr = self.getHpr(other)
        otherString = other.getName() + ', '
    else:
        pos = self.getPos()
        hpr = self.getHpr()
        otherString = ''
    print self.getName() + '.setPosHpr(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ', ' + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ')\n'


Dtool_funcToMethod(printPosHpr, NodePath)
del printPosHpr

def printPosHprScale(self, other=None, sd=2):
    formatString = '%0.' + '%d' % sd + 'f'
    if other:
        pos = self.getPos(other)
        hpr = self.getHpr(other)
        scale = self.getScale(other)
        otherString = other.getName() + ', '
    else:
        pos = self.getPos()
        hpr = self.getHpr()
        scale = self.getScale()
        otherString = ''
    print self.getName() + '.setPosHprScale(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ', ' + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ', ' + formatString % scale[0] + ', ' + formatString % scale[1] + ', ' + formatString % scale[2] + ')\n'


Dtool_funcToMethod(printPosHprScale, NodePath)
del printPosHprScale

def printTransform(self, other=None, sd=2, fRecursive=0):
    from panda3d.core import Vec3
    fmtStr = '%%0.%df' % sd
    name = self.getName()
    if other == None:
        transform = self.getTransform()
    else:
        transform = self.getTransform(other)
    if transform.hasPos():
        pos = transform.getPos()
        if not pos.almostEqual(Vec3(0)):
            outputString = '%s.setPos(%s, %s, %s)' % (name, fmtStr, fmtStr, fmtStr)
            print outputString % (pos[0], pos[1], pos[2])
    if transform.hasHpr():
        hpr = transform.getHpr()
        if not hpr.almostEqual(Vec3(0)):
            outputString = '%s.setHpr(%s, %s, %s)' % (name, fmtStr, fmtStr, fmtStr)
            print outputString % (hpr[0], hpr[1], hpr[2])
    if transform.hasScale():
        if transform.hasUniformScale():
            scale = transform.getUniformScale()
            if scale != 1.0:
                outputString = '%s.setScale(%s)' % (name, fmtStr)
                print outputString % scale
        else:
            scale = transform.getScale()
            if not scale.almostEqual(Vec3(1)):
                outputString = '%s.setScale(%s, %s, %s)' % (name, fmtStr, fmtStr, fmtStr)
                print outputString % (scale[0], scale[1], scale[2])
    if fRecursive:
        for child in self.getChildren():
            child.printTransform(other, sd, fRecursive)

    return


Dtool_funcToMethod(printTransform, NodePath)
del printTransform

def iPos(self, other=None):
    if other:
        self.setPos(other, 0, 0, 0)
    else:
        self.setPos(0, 0, 0)


Dtool_funcToMethod(iPos, NodePath)
del iPos

def iHpr(self, other=None):
    if other:
        self.setHpr(other, 0, 0, 0)
    else:
        self.setHpr(0, 0, 0)


Dtool_funcToMethod(iHpr, NodePath)
del iHpr

def iScale(self, other=None):
    if other:
        self.setScale(other, 1, 1, 1)
    else:
        self.setScale(1, 1, 1)


Dtool_funcToMethod(iScale, NodePath)
del iScale

def iPosHpr(self, other=None):
    if other:
        self.setPosHpr(other, 0, 0, 0, 0, 0, 0)
    else:
        self.setPosHpr(0, 0, 0, 0, 0, 0)


Dtool_funcToMethod(iPosHpr, NodePath)
del iPosHpr

def iPosHprScale(self, other=None):
    if other:
        self.setPosHprScale(other, 0, 0, 0, 0, 0, 0, 1, 1, 1)
    else:
        self.setPosHprScale(0, 0, 0, 0, 0, 0, 1, 1, 1)


Dtool_funcToMethod(iPosHprScale, NodePath)
del iPosHprScale

def place(self):
    base.startDirect(fWantTk=1)
    from direct.tkpanels import Placer
    return Placer.place(self)


Dtool_funcToMethod(place, NodePath)
del place

def explore(self):
    base.startDirect(fWantTk=1)
    from direct.tkwidgets import SceneGraphExplorer
    return SceneGraphExplorer.explore(self)


Dtool_funcToMethod(explore, NodePath)
del explore

def rgbPanel(self, cb=None):
    base.startTk()
    from direct.tkwidgets import Slider
    return Slider.rgbPanel(self, cb)


Dtool_funcToMethod(rgbPanel, NodePath)
del rgbPanel

def select(self):
    base.startDirect(fWantTk=0)
    base.direct.select(self)


Dtool_funcToMethod(select, NodePath)
del select

def deselect(self):
    base.startDirect(fWantTk=0)
    base.direct.deselect(self)


Dtool_funcToMethod(deselect, NodePath)
del deselect

def showCS(self, mask=None):
    npc = self.findAllMatches('**/+CollisionNode')
    for p in range(0, npc.getNumPaths()):
        np = npc[p]
        if mask == None or (np.node().getIntoCollideMask() & mask).getWord():
            np.show()

    return


Dtool_funcToMethod(showCS, NodePath)
del showCS

def hideCS(self, mask=None):
    npc = self.findAllMatches('**/+CollisionNode')
    for p in range(0, npc.getNumPaths()):
        np = npc[p]
        if mask == None or (np.node().getIntoCollideMask() & mask).getWord():
            np.hide()

    return


Dtool_funcToMethod(hideCS, NodePath)
del hideCS

def posInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosInterval(self, *args, **kw)


Dtool_funcToMethod(posInterval, NodePath)
del posInterval

def hprInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpHprInterval(self, *args, **kw)


Dtool_funcToMethod(hprInterval, NodePath)
del hprInterval

def quatInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpQuatInterval(self, *args, **kw)


Dtool_funcToMethod(quatInterval, NodePath)
del quatInterval

def scaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpScaleInterval(self, *args, **kw)


Dtool_funcToMethod(scaleInterval, NodePath)
del scaleInterval

def shearInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpShearInterval(self, *args, **kw)


Dtool_funcToMethod(shearInterval, NodePath)
del shearInterval

def posHprInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosHprInterval(self, *args, **kw)


Dtool_funcToMethod(posHprInterval, NodePath)
del posHprInterval

def posQuatInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosQuatInterval(self, *args, **kw)


Dtool_funcToMethod(posQuatInterval, NodePath)
del posQuatInterval

def hprScaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpHprScaleInterval(self, *args, **kw)


Dtool_funcToMethod(hprScaleInterval, NodePath)
del hprScaleInterval

def quatScaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpQuatScaleInterval(self, *args, **kw)


Dtool_funcToMethod(quatScaleInterval, NodePath)
del quatScaleInterval

def posHprScaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosHprScaleInterval(self, *args, **kw)


Dtool_funcToMethod(posHprScaleInterval, NodePath)
del posHprScaleInterval

def posQuatScaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosQuatScaleInterval(self, *args, **kw)


Dtool_funcToMethod(posQuatScaleInterval, NodePath)
del posQuatScaleInterval

def posHprScaleShearInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosHprScaleShearInterval(self, *args, **kw)


Dtool_funcToMethod(posHprScaleShearInterval, NodePath)
del posHprScaleShearInterval

def posQuatScaleShearInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpPosQuatScaleShearInterval(self, *args, **kw)


Dtool_funcToMethod(posQuatScaleShearInterval, NodePath)
del posQuatScaleShearInterval

def colorInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpColorInterval(self, *args, **kw)


Dtool_funcToMethod(colorInterval, NodePath)
del colorInterval

def colorScaleInterval(self, *args, **kw):
    from direct.interval import LerpInterval
    return LerpInterval.LerpColorScaleInterval(self, *args, **kw)


Dtool_funcToMethod(colorScaleInterval, NodePath)
del colorScaleInterval

def attachCollisionSphere(self, name, cx, cy, cz, r, fromCollide, intoCollide):
    from panda3d.core import CollisionSphere
    from panda3d.core import CollisionNode
    coll = CollisionSphere(cx, cy, cz, r)
    collNode = CollisionNode(name)
    collNode.addSolid(coll)
    collNode.setFromCollideMask(fromCollide)
    collNode.setIntoCollideMask(intoCollide)
    collNodePath = self.attachNewNode(collNode)
    return collNodePath


Dtool_funcToMethod(attachCollisionSphere, NodePath)
del attachCollisionSphere

def attachCollisionSegment(self, name, ax, ay, az, bx, by, bz, fromCollide, intoCollide):
    from panda3d.core import CollisionSegment
    from panda3d.core import CollisionNode
    coll = CollisionSegment(ax, ay, az, bx, by, bz)
    collNode = CollisionNode(name)
    collNode.addSolid(coll)
    collNode.setFromCollideMask(fromCollide)
    collNode.setIntoCollideMask(intoCollide)
    collNodePath = self.attachNewNode(collNode)
    return collNodePath


Dtool_funcToMethod(attachCollisionSegment, NodePath)
del attachCollisionSegment

def attachCollisionRay(self, name, ox, oy, oz, dx, dy, dz, fromCollide, intoCollide):
    from panda3d.core import CollisionRay
    from panda3d.core import CollisionNode
    coll = CollisionRay(ox, oy, oz, dx, dy, dz)
    collNode = CollisionNode(name)
    collNode.addSolid(coll)
    collNode.setFromCollideMask(fromCollide)
    collNode.setIntoCollideMask(intoCollide)
    collNodePath = self.attachNewNode(collNode)
    return collNodePath


Dtool_funcToMethod(attachCollisionRay, NodePath)
del attachCollisionRay

def flattenMultitex(self, stateFrom=None, target=None, useGeom=0, allowTexMat=0, win=None):
    from panda3d.core import MultitexReducer
    mr = MultitexReducer()
    if target != None:
        mr.setTarget(target)
    mr.setUseGeom(useGeom)
    mr.setAllowTexMat(allowTexMat)
    if win == None:
        win = base.win
    if stateFrom == None:
        mr.scan(self)
    else:
        mr.scan(self, stateFrom)
    mr.flatten(win)
    return


Dtool_funcToMethod(flattenMultitex, NodePath)
del flattenMultitex

def getNumDescendants(self):
    return len(self.findAllMatches('**')) - 1


Dtool_funcToMethod(getNumDescendants, NodePath)
del getNumDescendants

def removeNonCollisions(self):
    stack = [
     self]
    while len(stack):
        np = stack.pop()
        if np.find('**/+CollisionNode').isEmpty():
            np.detachNode()
        else:
            stack.extend(np.getChildren())


Dtool_funcToMethod(removeNonCollisions, NodePath)
del removeNonCollisions

def subdivideCollisions(self, numSolidsInLeaves):
    colNps = self.findAllMatches('**/+CollisionNode')
    for colNp in colNps:
        node = colNp.node()
        numSolids = node.getNumSolids()
        if numSolids <= numSolidsInLeaves:
            continue
        solids = []
        for i in xrange(numSolids):
            solids.append(node.getSolid(i))

        solidTree = self.r_subdivideCollisions(solids, numSolidsInLeaves)
        root = colNp.getParent().attachNewNode('%s-subDivRoot' % colNp.getName())
        self.r_constructCollisionTree(solidTree, root, colNp.getName())
        colNp.stash()


def r_subdivideCollisions(self, solids, numSolidsInLeaves):
    if len(solids) <= numSolidsInLeaves:
        return solids
    origins = []
    avgX = 0
    avgY = 0
    avgZ = 0
    minX = None
    minY = None
    minZ = None
    maxX = None
    maxY = None
    maxZ = None
    for solid in solids:
        origin = solid.getCollisionOrigin()
        origins.append(origin)
        x = origin.getX()
        y = origin.getY()
        z = origin.getZ()
        avgX += x
        avgY += y
        avgZ += z
        if minX is None:
            minX = x
            minY = y
            minZ = z
            maxX = x
            maxY = y
            maxZ = z
        else:
            minX = min(x, minX)
            minY = min(y, minY)
            minZ = min(z, minZ)
            maxX = max(x, maxX)
            maxY = max(y, maxY)
            maxZ = max(z, maxZ)

    avgX /= len(solids)
    avgY /= len(solids)
    avgZ /= len(solids)
    extentX = maxX - minX
    extentY = maxY - minY
    extentZ = maxZ - minZ
    maxExtent = max(max(extentX, extentY), extentZ)
    xyzSolids = []
    XyzSolids = []
    xYzSolids = []
    XYzSolids = []
    xyZSolids = []
    XyZSolids = []
    xYZSolids = []
    XYZSolids = []
    midX = avgX
    midY = avgY
    midZ = avgZ
    if extentX < maxExtent * 0.75 or extentX > maxExtent * 1.25:
        midX += maxExtent
    if extentY < maxExtent * 0.75 or extentY > maxExtent * 1.25:
        midY += maxExtent
    if extentZ < maxExtent * 0.75 or extentZ > maxExtent * 1.25:
        midZ += maxExtent
    for i in xrange(len(solids)):
        origin = origins[i]
        x = origin.getX()
        y = origin.getY()
        z = origin.getZ()
        if x < midX:
            if y < midY:
                if z < midZ:
                    xyzSolids.append(solids[i])
                else:
                    xyZSolids.append(solids[i])
            elif z < midZ:
                xYzSolids.append(solids[i])
            else:
                xYZSolids.append(solids[i])
        elif y < midY:
            if z < midZ:
                XyzSolids.append(solids[i])
            else:
                XyZSolids.append(solids[i])
        elif z < midZ:
            XYzSolids.append(solids[i])
        else:
            XYZSolids.append(solids[i])

    newSolids = []
    if len(xyzSolids):
        newSolids.append(self.r_subdivideCollisions(xyzSolids, numSolidsInLeaves))
    if len(XyzSolids):
        newSolids.append(self.r_subdivideCollisions(XyzSolids, numSolidsInLeaves))
    if len(xYzSolids):
        newSolids.append(self.r_subdivideCollisions(xYzSolids, numSolidsInLeaves))
    if len(XYzSolids):
        newSolids.append(self.r_subdivideCollisions(XYzSolids, numSolidsInLeaves))
    if len(xyZSolids):
        newSolids.append(self.r_subdivideCollisions(xyZSolids, numSolidsInLeaves))
    if len(XyZSolids):
        newSolids.append(self.r_subdivideCollisions(XyZSolids, numSolidsInLeaves))
    if len(xYZSolids):
        newSolids.append(self.r_subdivideCollisions(xYZSolids, numSolidsInLeaves))
    if len(XYZSolids):
        newSolids.append(self.r_subdivideCollisions(XYZSolids, numSolidsInLeaves))
    return newSolids


def r_constructCollisionTree(self, solidTree, parentNode, colName):
    for item in solidTree:
        if type(item[0]) == type([]):
            newNode = parentNode.attachNewNode('%s-branch' % colName)
            self.r_constructCollisionTree(item, newNode, colName)
        else:
            cn = CollisionNode('%s-leaf' % colName)
            for solid in item:
                cn.addSolid(solid)

            parentNode.attachNewNode(cn)


Dtool_funcToMethod(subdivideCollisions, NodePath)
Dtool_funcToMethod(r_subdivideCollisions, NodePath)
Dtool_funcToMethod(r_constructCollisionTree, NodePath)
del subdivideCollisions
del r_subdivideCollisions
del r_constructCollisionTree

def analyze(self):
    from panda3d.core import SceneGraphAnalyzer
    sga = SceneGraphAnalyzer()
    sga.addNode(self.node())
    if sga.getNumLodNodes() == 0:
        print sga
    else:
        print 'At highest LOD:'
        sga2 = SceneGraphAnalyzer()
        sga2.setLodMode(sga2.LMHighest)
        sga2.addNode(self.node())
        print sga2
        print '\nAt lowest LOD:'
        sga2.clear()
        sga2.setLodMode(sga2.LMLowest)
        sga2.addNode(self.node())
        print sga2
        print '\nAll nodes:'
        print sga


Dtool_funcToMethod(analyze, NodePath)
del analyze

def pPrintValues(self):
    return '\n%s\n%s\n%s' % (
     self.getRow(0).pPrintValues(), self.getRow(1).pPrintValues(), self.getRow(2).pPrintValues())


Dtool_funcToMethod(pPrintValues, Mat3)
del pPrintValues

def pPrintValues(self):
    return '% 10.4f, % 10.4f, % 10.4f' % (self[0], self[1], self[2])


Dtool_funcToMethod(pPrintValues, VBase3)
del pPrintValues

def asTuple(self):
    print 'Warning: VBase3.asTuple() is no longer needed and deprecated.  Use the vector directly instead.'
    return tuple(self)


Dtool_funcToMethod(asTuple, VBase3)
del asTuple

def pPrintValues(self):
    return '% 10.4f, % 10.4f, % 10.4f, % 10.4f' % (self[0], self[1], self[2], self[3])


Dtool_funcToMethod(pPrintValues, VBase4)
del pPrintValues

def asTuple(self):
    print 'Warning: VBase4.asTuple() is no longer needed and deprecated.  Use the vector directly instead.'
    return tuple(self)


Dtool_funcToMethod(asTuple, VBase4)
del asTuple

def spawnTask(self, name=None, callback=None, extraArgs=[]):
    if not name:
        name = str(self.getUrl())
    from direct.task import Task
    task = Task.Task(self.doTask)
    task.callback = callback
    task.callbackArgs = extraArgs
    return taskMgr.add(task, name)


Dtool_funcToMethod(spawnTask, HTTPChannel)
del spawnTask

def doTask(self, task):
    from direct.task import Task
    if self.run():
        return Task.cont
    if task.callback:
        task.callback(*task.callbackArgs)
    return Task.done


Dtool_funcToMethod(doTask, HTTPChannel)
del doTask