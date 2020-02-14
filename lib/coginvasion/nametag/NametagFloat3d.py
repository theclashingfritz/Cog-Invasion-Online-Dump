# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.nametag.NametagFloat3d
from direct.task.Task import Task
from Nametag3d import Nametag3d

class NametagFloat3d(Nametag3d):

    def tick(self, task):
        return Task.done