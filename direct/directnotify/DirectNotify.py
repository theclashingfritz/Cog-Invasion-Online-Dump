# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.directnotify.DirectNotify
import Notifier, Logger

class DirectNotify:

    def __init__(self):
        self.__categories = {}
        self.logger = Logger.Logger()
        self.streamWriter = None
        return

    def __str__(self):
        return 'DirectNotify categories: %s' % self.__categories

    def getCategories(self):
        return self.__categories.keys()

    def getCategory(self, categoryName):
        return self.__categories.get(categoryName, None)

    def newCategory(self, categoryName, logger=None):
        if categoryName not in self.__categories:
            self.__categories[categoryName] = Notifier.Notifier(categoryName, logger)
            self.setDconfigLevel(categoryName)
        return self.getCategory(categoryName)

    def setDconfigLevel(self, categoryName):
        from panda3d.core import ConfigVariableString
        dconfigParam = 'notify-level-' + categoryName
        cvar = ConfigVariableString(dconfigParam, '')
        level = cvar.getValue()
        if not level:
            cvar2 = ConfigVariableString('default-directnotify-level', 'info')
            level = cvar2.getValue()
        if not level:
            level = 'error'
        category = self.getCategory(categoryName)
        if level == 'error':
            category.setWarning(0)
            category.setInfo(0)
            category.setDebug(0)
        else:
            if level == 'warning':
                category.setWarning(1)
                category.setInfo(0)
                category.setDebug(0)
            else:
                if level == 'info':
                    category.setWarning(1)
                    category.setInfo(1)
                    category.setDebug(0)
                else:
                    if level == 'debug':
                        category.setWarning(1)
                        category.setInfo(1)
                        category.setDebug(1)
                    else:
                        print 'DirectNotify: unknown notify level: ' + str(level) + ' for category: ' + str(categoryName)

    def setDconfigLevels(self):
        for categoryName in self.getCategories():
            self.setDconfigLevel(categoryName)

    def setVerbose(self):
        for categoryName in self.getCategories():
            category = self.getCategory(categoryName)
            category.setWarning(1)
            category.setInfo(1)
            category.setDebug(1)

    def popupControls(self, tl=None):
        from direct.tkpanels import NotifyPanel
        NotifyPanel.NotifyPanel(self, tl)

    def giveNotify(self, cls):
        cls.notify = self.newCategory(cls.__name__)