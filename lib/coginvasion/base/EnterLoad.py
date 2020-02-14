# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.base.EnterLoad
import FileUtility
from LoadUtility import LoadUtility

class EnterLoad(LoadUtility):

    def __init__(self, callback):
        LoadUtility.__init__(self, callback)
        phasesToScan = ['phase_3.5/models']
        self.models = FileUtility.findAllModelFilesInVFS(phasesToScan)

    def load(self):
        loader.beginBulkLoad('localAvatarEnterGame', 'localAvatarEnterGame', len(self.models), 0, False)
        LoadUtility.load(self)

    def done(self):
        LoadUtility.done(self)
        loader.endBulkLoad('localAvatarEnterGame')