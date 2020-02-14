# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.hood.SkyUtil
from direct.directnotify.DirectNotifyGlobal import directNotify
from panda3d.core import Vec3

class SkyUtil:
    notify = directNotify.newCategory('SkyUtil')

    def startSky(self, sky):
        sky.setScale(5)
        if not sky.find('**/cloud1').isEmpty() and not sky.find('**/cloud2').isEmpty():
            sky.find('**/cloud1').setScale(0.6)
            sky.find('**/cloud2').setScale(0.9)
            self.cloud1_int = sky.find('**/cloud1').hprInterval(360, Vec3(60, 0, 0))
            self.cloud2_int = sky.find('**/cloud2').hprInterval(360, Vec3(-60, 0, 0))
            self.cloud1_int.loop()
            self.cloud2_int.loop()

    def stopSky(self):
        if hasattr(self, 'cloud1_int'):
            self.cloud1_int.finish()
            self.cloud2_int.finish()

    def pauseSky(self):
        if hasattr(self, 'cloud1_int'):
            self.cloud1_int.pause()
            self.cloud2_int.pause()