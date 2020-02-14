# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.fsm.SampleFSM
__all__ = [
 'ClassicStyle', 'NewStyle', 'ToonEyes']
import FSM
from direct.task import Task
import string

class ClassicStyle(FSM.FSM):

    def __init__(self, name):
        FSM.FSM.__init__(self, name)
        self.defaultTransitions = {'Red': [
                 'Green'], 
           'Yellow': [
                    'Red'], 
           'Green': [
                   'Yellow']}

    def enterRed(self):
        print "enterRed(self, '%s', '%s')" % (self.oldState, self.newState)

    def exitRed(self):
        print "exitRed(self, '%s', '%s')" % (self.oldState, self.newState)

    def enterYellow(self):
        print "enterYellow(self, '%s', '%s')" % (self.oldState, self.newState)

    def exitYellow(self):
        print "exitYellow(self, '%s', '%s')" % (self.oldState, self.newState)

    def enterGreen(self):
        print "enterGreen(self, '%s', '%s')" % (self.oldState, self.newState)

    def exitGreen(self):
        print "exitGreen(self, '%s', '%s')" % (self.oldState, self.newState)


class NewStyle(FSM.FSM):

    def enterRed(self):
        print "enterRed(self, '%s', '%s')" % (self.oldState, self.newState)

    def filterRed(self, request, args):
        print "filterRed(self, '%s', %s)" % (request, args)
        if request == 'advance':
            return 'Green'
        return self.defaultFilter(request, args)

    def exitRed(self):
        print "exitRed(self, '%s', '%s')" % (self.oldState, self.newState)

    def enterYellow(self):
        print "enterYellow(self, '%s', '%s')" % (self.oldState, self.newState)

    def filterYellow(self, request, args):
        print "filterYellow(self, '%s', %s)" % (request, args)
        if request == 'advance':
            return 'Red'
        return self.defaultFilter(request, args)

    def exitYellow(self):
        print "exitYellow(self, '%s', '%s')" % (self.oldState, self.newState)

    def enterGreen(self):
        print "enterGreen(self, '%s', '%s')" % (self.oldState, self.newState)

    def filterGreen(self, request, args):
        print "filterGreen(self, '%s', %s)" % (request, args)
        if request == 'advance':
            return 'Yellow'
        return self.defaultFilter(request, args)

    def exitGreen(self):
        print "exitGreen(self, '%s', '%s')" % (self.oldState, self.newState)


class ToonEyes(FSM.FSM):

    def __init__(self):
        FSM.FSM.__init__(self, 'eyes')
        self.__unblinkName = 'unblink'
        self.request('Open')

    def defaultFilter(self, request, args):
        if request[0] in string.uppercase:
            return request
        return

    def enterOpen(self):
        print 'swap in eyes open model'

    def filterOpen(self, request, args):
        if request == 'blink':
            taskMgr.remove(self.__unblinkName)
            taskMgr.doMethodLater(0.125, self.__unblink, self.__unblinkName)
            return 'Closed'
        return self.defaultFilter(request, args)

    def __unblink(self, task):
        self.request('unblink')
        return Task.done

    def enterClosed(self):
        print 'swap in eyes closed model'

    def filterClosed(self, request, args):
        if request == 'unblink':
            return 'Open'
        return self.defaultFilter(request, args)

    def enterSurprised(self):
        print 'swap in eyes surprised model'

    def enterOff(self):
        taskMgr.remove(self.__unblinkName)