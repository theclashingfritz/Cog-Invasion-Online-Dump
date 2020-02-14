# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.dna.DNALoader
from direct.stdpy import threading
from libpandadna import *

class DNABulkLoader:

    def __init__(self, storage, files):
        self.dnaStorage = storage
        self.dnaFiles = files

    def loadDNAFiles(self):
        for file in self.dnaFiles:
            print 'Reading DNA file...', file
            loadDNABulk(self.dnaStorage, file)

        del self.dnaStorage
        del self.dnaFiles


def loadDNABulk(dnaStorage, file):
    dnaLoader = DNALoader()
    dnaLoader.loadDNAFile(dnaStorage, file)


def loadDNAFile(dnaStorage, file):
    print 'Reading DNA file...', file
    dnaLoader = DNALoader()
    node = dnaLoader.loadDNAFile(dnaStorage, file)
    if not node.isEmpty():
        if node.node().getNumChildren() > 0:
            return node.node()
    return


def loadDNAFileAI(dnaStorage, file):
    dnaLoader = DNALoader()
    data = dnaLoader.loadDNAFileAI(dnaStorage, file)
    return data