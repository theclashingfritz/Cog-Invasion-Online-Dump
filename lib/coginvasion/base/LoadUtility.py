# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.base.LoadUtility


class LoadUtility:

    def __init__(self, callback):
        self.callback = callback
        self.models = []

    def load(self):
        for modelFile in self.models:
            loader.loadModel(modelFile)
            loader.progressScreen.tick()

        self.done()

    def done(self):
        self.callback()
        self.destroy()

    def destroy(self):
        self.models = None
        self.callback = None
        return