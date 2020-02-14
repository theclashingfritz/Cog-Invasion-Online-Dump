# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.base.FileUtility
from panda3d.core import VirtualFileSystem, Filename
vfs = VirtualFileSystem.getGlobalPtr()

def handleFileList(models, fileList):
    if not fileList:
        return models
        for fileName in fileList:
            if fileName.get_filename().get_fullpath().endswith(('.bam', 'egg', '.pz')):
                if fileName.get_filename().get_fullpath() not in models:
                    models.append(fileName.get_filename().get_fullpath())
            else:
                handleFileList(models, vfs.scanDirectory(Filename(fileName.get_filename().get_fullpath())))


def findAllModelFilesInVFS(phase_array):
    models = []
    for phase in phase_array:
        fileList = vfs.scanDirectory(Filename(phase))
        handleFileList(models, fileList)

    return models