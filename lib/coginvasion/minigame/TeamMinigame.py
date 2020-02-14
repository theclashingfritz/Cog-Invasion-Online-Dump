# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.minigame.TeamMinigame
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import DirectButton, OnscreenImage, DirectFrame, OnscreenText, DGG
from lib.coginvasion.globals import CIGlobals, ChatGlobals
from lib.coginvasion.gui.WhisperPopup import WhisperPopup
TEAM1 = 0
TEAM2 = 1
MSG_WELCOME = 'Welcome to the {0}!'

class TeamMinigame:
    notify = directNotify.newCategory('TeamMinigame')

    def __init__(self, team1Name, team1BtnImg, team2Name, team2BtnImg):
        self.team1Name = team1Name
        self.team1BtnImg = team1BtnImg
        self.team2Name = team2Name
        self.team2BtnImg = team2BtnImg
        self.teamNameById = {TEAM1: self.team1Name, TEAM2: self.team2Name}
        self.team = None
        self.winnerTeam = None
        self.playersByTeam = {TEAM1: 0, TEAM2: 0}
        self.playerListByTeam = {TEAM1: [], TEAM2: []}
        self.scoreByTeam = {TEAM1: 0, TEAM2: 0}
        self.container = None
        self.bg = None
        self.title = None
        self.btnFrame = None
        self.team1Frame = None
        self.team1Btn = None
        self.team1Plyrs_Lbl = None
        self.team2Frame = None
        self.team2Btn = None
        self.team2Plyrs_Lbl = None
        self.teamFull_Lbl = None
        return

    def makeSelectionGUI(self):
        font = CIGlobals.getMickeyFont()
        box = loader.loadModel('phase_3/models/gui/dialog_box_gui.bam')
        imp = CIGlobals.getToonFont()
        geom = CIGlobals.getDefaultBtnGeom()
        self.container = DirectFrame()
        self.bg = OnscreenImage(image=box, color=(1, 1, 0.75, 1), scale=(1.9, 1.4,
                                                                         1.4), parent=self.container)
        self.title = OnscreenText(text='Join  a  Team', pos=(0, 0.5, 0), font=font, scale=0.12, parent=self.container, fg=(1,
                                                                                                                           0.9,
                                                                                                                           0.3,
                                                                                                                           1))
        self.btnFrame = DirectFrame(parent=self.container, pos=(0.14, 0, 0))
        self.team1BtnFrame = DirectFrame(parent=self.btnFrame, pos=(-0.5, 0, 0))
        self.team2BtnFrame = DirectFrame(parent=self.btnFrame, pos=(0.22, 0, 0))
        self.team1Btn = DirectButton(parent=self.team1BtnFrame, relief=None, pressEffect=0, image=self.team1BtnImg, image_scale=(0.9,
                                                                                                                                 1,
                                                                                                                                 1), scale=0.4, command=self.choseTeam, extraArgs=[TEAM1])
        self.team1Plyrs_Lbl = OnscreenText(parent=self.team1BtnFrame, text=str(self.playersByTeam[TEAM1]), pos=(0,
                                                                                                                -0.46,
                                                                                                                0), font=imp)
        self.team2Btn = DirectButton(parent=self.team2BtnFrame, relief=None, pressEffect=0, image=self.team2BtnImg, image_scale=(0.9,
                                                                                                                                 1,
                                                                                                                                 1), scale=0.4, command=self.choseTeam, extraArgs=[TEAM2])
        self.team2Plyrs_Lbl = OnscreenText(parent=self.team2BtnFrame, text=str(self.playersByTeam[TEAM2]), pos=(0,
                                                                                                                -0.46,
                                                                                                                0), font=imp)
        self.teamFull_Lbl = OnscreenText(parent=self.container, text='', pos=(0, -0.6,
                                                                              0), font=imp)
        return

    def destroySelectionGUI(self):
        if self.teamFull_Lbl:
            self.teamFull_Lbl.destroy()
            self.teamFull_Lbl = None
        if self.team2Plyrs_Lbl:
            self.team2Plyrs_Lbl.destroy()
            self.team2Plyrs_Lbl = None
        if self.team1Plyrs_Lbl:
            self.team1Plyrs_Lbl.destroy()
            self.team1Plyrs_Lbl = None
        if self.team2Btn:
            self.team2Btn.destroy()
            self.team2Btn = None
        if self.team1Btn:
            self.team1Btn.destroy()
            self.team1Btn = None
        if self.team2BtnFrame:
            self.team2BtnFrame.destroy()
            self.team2BtnFrame = None
        if self.team1BtnFrame:
            self.team1BtnFrame.destroy()
            self.team1BtnFrame = None
        if self.title:
            self.title.destroy()
            self.title = None
        if self.bg:
            self.bg.destroy()
            self.bg = None
        if self.container:
            self.container.destroy()
            self.container = None
        return

    def choseTeam(self, team):
        self.team = team
        self.team1Btn['state'] = DGG.DISABLED
        self.team2Btn['state'] = DGG.DISABLED
        self.sendUpdate('choseTeam', [team])

    def acceptedIntoTeam(self):
        message = MSG_WELCOME.format(self.teamNameById[self.team])
        whisper = WhisperPopup(message, CIGlobals.getToonFont(), ChatGlobals.WTSystem)
        whisper.manage(base.marginManager)

    def teamFull(self):
        self.teamFull_Lbl.setText('Sorry, that team is full.')
        self.team = None
        self.team1Btn['state'] = DGG.NORMAL
        self.team2Btn['state'] = DGG.NORMAL
        return

    def incrementTeamPlayers(self, team):
        self.playersByTeam[team] += 1
        if self.fsm.getCurrentState().getName() == 'chooseTeam':
            if team == TEAM2:
                lbl = self.team2Plyrs_Lbl
            else:
                if team == TEAM1:
                    lbl = self.team1Plyrs_Lbl
            lbl.setText(str(self.playersByTeam[team]))

    def setTeamOfPlayer(self, avId, team):
        if not hasattr(self, 'getRemoteAvatar'):
            self.notify.error('Minigame must have remote avatars!!')
        self.playerListByTeam[team].append(avId)
        remoteAvatar = self.getRemoteAvatar(avId)
        if remoteAvatar:
            print ('setting team of {0}').format(avId)
            remoteAvatar.setTeam(team)

    def incrementTeamScore(self, team):
        self.scoreByTeam[team] += 1

    def teamWon(self, team):
        self.winnerTeam = team

    def cleanup(self):
        self.destroySelectionGUI()
        del self.scoreByTeam
        del self.team1Name
        del self.teamNameById
        del self.team2Name
        del self.team1BtnImg
        del self.team2BtnImg
        del self.team
        del self.playersByTeam
        del self.winnerTeam
        del self.playerListByTeam