# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.RemoteAvatar
from panda3d.core import TextNode, VBase4
from direct.directnotify.DirectNotifyGlobal import directNotify
from lib.coginvasion.globals import CIGlobals

class RemoteAvatar:
    notify = directNotify.newCategory('RemoteAvatar')

    def __init__(self, mg, cr, avId):
        self.mg = mg
        self.cr = cr
        self.avId = avId
        self.avatar = None
        self.teamText = None
        self.team = None
        self.ogHeadColor = None
        self.ogTorsoColor = None
        self.ogLegColor = None
        self.ogShirtColor = None
        self.ogSleeveColor = None
        self.ogShortColor = None
        self.ogShirt = None
        self.ogSleeve = None
        self.ogShort = None
        self.dnaWasChanged = False
        return

    def setTeam(self, team):
        self.team = team
        print 'setteam'
        color = self.mg.getTeamDNAColor(team)
        if color is not None:
            print 'changing shit'
            self.ogHeadColor = self.avatar.headcolor
            self.ogTorsoColor = self.avatar.torsocolor
            self.ogLegColor = self.avatar.legcolor
            self.ogShirtColor = self.avatar.shirtColor
            self.ogSleeveColor = self.avatar.sleeveColor
            self.ogShortColor = self.avatar.shortColor
            self.ogShirt = self.avatar.shirt
            self.ogSleeve = self.avatar.sleeve
            self.ogShort = self.avatar.shorts
            self.avatar.headcolor = color
            self.avatar.torsocolor = color
            self.avatar.legcolor = color
            self.avatar.shirtColor = color
            self.avatar.sleeveColor = color
            self.avatar.shortColor = color
            self.avatar.shirt = self.avatar.shirtDNA2shirt['00']
            self.avatar.sleeve = self.avatar.sleeveDNA2sleeve['00']
            if self.avatar.gender == 'girl':
                self.avatar.shorts = self.avatar.shortDNA2short['10']
            else:
                if self.avatar.gender == 'boy':
                    self.avatar.shorts = self.avatar.shortDNA2short['00']
            self.avatar.generateDNAStrandWithCurrentStyle()
            self.dnaWasChanged = True
        if self.teamText:
            self.teamText.removeNode()
            self.teamText = None
        textNode = TextNode('teamText')
        textNode.setAlign(TextNode.ACenter)
        textNode.setFont(CIGlobals.getMickeyFont())
        self.teamText = self.avatar.attachNewNode(textNode)
        self.teamText.setBillboardAxis()
        self.teamText.setZ(self.avatar.getNameTag().getZ() + 1.0)
        self.teamText.setScale(5.0)
        return

    def restoreOgDna(self):
        self.avatar.headcolor = self.ogHeadColor
        self.avatar.torsocolor = self.ogTorsoColor
        self.avatar.legcolor = self.ogLegColor
        self.avatar.shirtColor = self.ogShirtColor
        self.avatar.sleeveColor = self.ogSleeveColor
        self.avatar.shortColor = self.ogShortColor
        self.avatar.shirt = self.ogShirt
        self.avatar.sleeve = self.ogSleeve
        self.avatar.shorts = self.ogShort
        self.avatar.generateDNAStrandWithCurrentStyle()

    def getTeam(self):
        return self.team

    def retrieveAvatar(self):
        self.avatar = self.cr.doId2do.get(self.avId, None)
        self.avatar.setPythonTag('player', self.avId)
        if not self.avatar:
            self.notify.warning('Tried to create a ' + self.__class__.__name__ + " when the avatar doesn't exist!")
            self.avatar = None
        return

    def cleanup(self):
        if self.dnaWasChanged and self.avId == base.localAvatar.doId:
            self.restoreOgDna()
        self.dnaWasChanged = None
        self.ogHeadColor = None
        self.ogTorsoColor = None
        self.ogLegColor = None
        self.ogShirtColor = None
        self.ogSleeveColor = None
        self.ogShortColor = None
        self.ogShirt = None
        self.ogSleeve = None
        self.ogShort = None
        try:
            del self.avatar
            del self.avId
            del self.cr
            del self.mg
            del self.team
        except:
            pass

        if self.teamText:
            self.teamText.removeNode()
            self.teamText = None
        return