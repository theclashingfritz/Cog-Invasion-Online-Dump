# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.Finder
__all__ = [
 'findClass', 'rebindClass', 'copyFuncs', 'replaceMessengerFunc', 'replaceTaskMgrFunc', 'replaceStateFunc', 'replaceCRFunc', 'replaceAIRFunc', 'replaceIvalFunc']
import types, os, sys

def findClass(className):
    for moduleName, module in sys.modules.items():
        if module:
            classObj = module.__dict__.get(className)
            if classObj and (type(classObj) == types.ClassType or type(classObj) == types.TypeType) and classObj.__module__ == moduleName:
                return [classObj, module.__dict__]

    return


def rebindClass(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    for i in xrange(len(lines)):
        line = lines[i]
        if line[0:6] == 'class ':
            classHeader = line[6:].strip()
            parenLoc = classHeader.find('(')
            if parenLoc > 0:
                className = classHeader[:parenLoc]
            else:
                colonLoc = classHeader.find(':')
                if colonLoc > 0:
                    className = classHeader[:colonLoc]
                else:
                    print 'error: className not found'
                    file.close()
                    os.remove(filename)
                    return
            print 'Rebinding class name: ' + className
            break

    res = findClass(className)
    if not res:
        print 'Warning: Finder could not find class'
        file.close()
        os.remove(filename)
        return
    realClass, realNameSpace = res
    execfile(filename, realNameSpace)
    tmpClass = realNameSpace[className]
    copyFuncs(tmpClass, realClass)
    realNameSpace[className] = realClass
    file.close()
    os.remove(filename)
    print '    Finished rebind'


def copyFuncs(fromClass, toClass):
    replaceFuncList = []
    newFuncList = []
    for funcName, newFunc in fromClass.__dict__.items():
        if type(newFunc) == types.FunctionType:
            oldFunc = toClass.__dict__.get(funcName)
            if oldFunc:
                replaceFuncList.append((oldFunc, funcName, newFunc))
            else:
                newFuncList.append((funcName, newFunc))

    replaceMessengerFunc(replaceFuncList)
    replaceTaskMgrFunc(replaceFuncList)
    replaceStateFunc(replaceFuncList)
    replaceCRFunc(replaceFuncList)
    replaceAIRFunc(replaceFuncList)
    replaceIvalFunc(replaceFuncList)
    for oldFunc, funcName, newFunc in replaceFuncList:
        setattr(toClass, funcName, newFunc)

    for funcName, newFunc in newFuncList:
        setattr(toClass, funcName, newFunc)


def replaceMessengerFunc(replaceFuncList):
    try:
        messenger
    except:
        return

    for oldFunc, funcName, newFunc in replaceFuncList:
        res = messenger.replaceMethod(oldFunc, newFunc)
        if res:
            print 'replaced %s messenger function(s): %s' % (res, funcName)


def replaceTaskMgrFunc(replaceFuncList):
    try:
        taskMgr
    except:
        return

    for oldFunc, funcName, newFunc in replaceFuncList:
        if taskMgr.replaceMethod(oldFunc, newFunc):
            print 'replaced taskMgr function: %s' % funcName


def replaceStateFunc(replaceFuncList):
    if not sys.modules.get('base.direct.fsm.State'):
        return
    from direct.fsm.State import State
    for oldFunc, funcName, newFunc in replaceFuncList:
        res = State.replaceMethod(oldFunc, newFunc)
        if res:
            print 'replaced %s FSM transition function(s): %s' % (res, funcName)


def replaceCRFunc(replaceFuncList):
    try:
        base.cr
    except:
        return

    if hasattr(base.cr, 'isFake'):
        return
    for oldFunc, funcName, newFunc in replaceFuncList:
        if base.cr.replaceMethod(oldFunc, newFunc):
            print 'replaced DistributedObject function: %s' % funcName


def replaceAIRFunc(replaceFuncList):
    try:
        simbase.air
    except:
        return

    for oldFunc, funcName, newFunc in replaceFuncList:
        if simbase.air.replaceMethod(oldFunc, newFunc):
            print 'replaced DistributedObject function: %s' % funcName


def replaceIvalFunc(replaceFuncList):
    if not sys.modules.get('base.direct.interval.IntervalManager'):
        return
    from direct.interval.FunctionInterval import FunctionInterval
    for oldFunc, funcName, newFunc in replaceFuncList:
        res = FunctionInterval.replaceMethod(oldFunc, newFunc)
        if res:
            print 'replaced %s interval function(s): %s' % (res, funcName)