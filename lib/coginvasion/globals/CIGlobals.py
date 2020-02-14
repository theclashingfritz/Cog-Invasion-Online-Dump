# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.globals.CIGlobals
from panda3d.core import *
from lib.coginvasion.manager.SettingsManager import SettingsManager
from lib.coginvasion.cog import SuitGlobals
WalkCutOff = 0.5
RunCutOff = 8.0
STAND_INDEX = 0
WALK_INDEX = 1
RUN_INDEX = 2
REVERSE_INDEX = 3
STRAFE_RIGHT_INDEX = 4
STRAFE_LEFT_INDEX = 5
GeneralAnimPlayRate = 1.0
BackwardsAnimPlayRate = -1.0
OpenBookFromFrame = 29
OpenBookToFrame = 37
ReadBookFromFrame = 38
ReadBookToFrame = 118
CloseBookFromFrame = 119
CloseBookToFrame = 155
ChatBubble = 'phase_3/models/props/chatbox.bam'
ThoughtBubble = 'phase_3/models/props/chatbox_thought_cutout.bam'
ToonFont = None
SuitFont = None
MickeyFont = None
MinnieFont = None
FloorOffset = 0.025
NPCWalkSpeed = 0.02
NPCRunSpeed = 0.04
OriginalCameraFov = 40.0
DefaultCameraFov = 52.0
DefaultCameraFar = 2000.0
DefaultCameraNear = 1.0
PortalScale = 1.5
SPInvalid = 0
SPHidden = 1
SPRender = 2
SPDonaldsBoat = 3
SPDynamic = 5
AICollisionPriority = 10
AICollMovePriority = 8
Suit = 'Cog'
Toon = 'Toon'
CChar = 'cchar'
Goofy = 'Goofy'
Mickey = 'Mickey'
MickeyMouse = 'Mickey Mouse'
Minnie = 'Minnie'
Suits = 'Cogs'
Skelesuit = 'Skelecog'
Pluto = 'Pluto'
Donald = 'Donald'
Playground = 'Playground'
RaceGame = 'Race Game'
UnoGame = 'Uno Game'
UnoCall = 'UNO!'
GunGame = 'Toon Battle'
GunGameFOV = 70.0
FactoryGame = 'Factory Prowl'
CameraShyGame = 'Camera Shy'
EagleGame = 'Eagle Summit'
DeliveryGame = 'Delivery!'
DodgeballGame = 'Winter Dodgeball'
ChatGarblerDog = ['woof', 'arf', 'rruff']
ChatGarblerCat = ['meow', 'mew']
ChatGarblerMouse = ['squeak', 'squeaky', 'squeakity']
ChatGarblerHorse = ['neigh', 'brrr']
ChatGarblerRabbit = ['eek',
 'eepr',
 'eepy',
 'eeky']
ChatGarblerDuck = ['quack', 'quackity', 'quacky']
ChatGarblerMonkey = ['ooh', 'ooo', 'ahh']
ChatGarblerBear = ['growl', 'grrr']
ChatGarblerPig = ['oink', 'oik', 'snort']
ChatGarblerDefault = ['blah']
NoToken = -1
DevToken = 0
UndercoverToken = 1
ModToken = 2
TextColorByAdminToken = {NoToken: (0, 0, 0, 1), UndercoverToken: (
                   0, 0, 0, 1), 
   DevToken: (
            255.0 / 255, 154.0 / 255, 0.0 / 255, 1), 
   ModToken: (
            0.0 / 255, 85.0 / 255, 255.0 / 255, 1)}
ThemeSong = None
holidayTheme = None

def getThemeSong():
    global ThemeSong
    if not ThemeSong:
        themeList = []
        themeList.append('phase_3/audio/bgm/tt_theme.mid')
        vfs = VirtualFileSystem.getGlobalPtr()
        for fileName in vfs.scanDirectory('phase_3/audio/bgm/'):
            fullpath = fileName.get_filename().get_fullpath()
            if 'ci_theme' in fullpath:
                themeList.append(fullpath)

        import random
        ThemeSong = random.choice(themeList)
    return ThemeSong


def getHolidayTheme():
    global holidayTheme
    if not holidayTheme:
        holidayTheme = 'phase_3/audio/bgm/ci_holiday_christmas_bgm.ogg'
    return holidayTheme


def areFacingEachOther(obj1, obj2):
    h1 = obj1.getH(render) % 360
    h2 = obj2.getH(render) % 360
    return not -90.0 <= h1 - h2 <= 90.0


FloorBitmask = BitMask32(2)
WallBitmask = BitMask32(1)
EventBitmask = BitMask32(3)
CameraBitmask = BitMask32(4)
ShadowCameraBitmask = BitMask32.bit(5)
WeaponBitmask = BitMask32.bit(6)
DialogColor = (1, 1, 0.75, 1)
DefaultBackgroundColor = (0, 0, 0, 1)
PositiveTextColor = (0, 1, 0, 1)
NegativeTextColor = (1, 0, 0, 1)
OrangeTextColor = (1, 0.5, 0, 1)
YellowTextColor = (1, 1, 0, 1)
SuitClasses = [
 'DistributedSuit', 'DistributedTutorialSuit', 'DistributedCogOfficeSuit', 'DistributedTakeOverSuit']
OToontown = 'OToontown'
CogTropolis = 'CogTropolis'
Estate = 'The Estate'
ToontownCentral = 'Toontown Central'
BattleTTC = 'CogTropolis Central'
DonaldsDock = "Donald's Dock"
MinniesMelodyland = "Minnie's Melodyland"
TheBrrrgh = 'The Brrrgh'
DonaldsDreamland = "Donald's Dreamland"
GoofySpeedway = 'Goofy Speedway'
CashbotHQ = 'Cashbot HQ'
SellbotHQ = 'Sellbot HQ'
LawbotHQ = 'Lawbot HQ'
BossbotHQ = 'Bossbot HQ'
MinigameArea = 'Minigame Area'
OutdoorZone = 'Outdoor Area'
GolfZone = 'Minigolf Area'
DaisyGardens = 'Daisy Gardens'
Minigame = 'Minigame'
RecoverArea = 'Recover Area'
Hood2ZoneId = {ToontownCentral: 2000, DonaldsDock: 1000, TheBrrrgh: 3000, MinniesMelodyland: 4000, 
   DaisyGardens: 5000, DonaldsDreamland: 9000, MinigameArea: 10000}
ZoneId2Hood = {2000: ToontownCentral, 1000: DonaldsDock, 3000: TheBrrrgh, 4000: MinniesMelodyland, 
   5000: DaisyGardens, 9000: DonaldsDreamland, 10000: MinigameArea}
SellbotFactory = 'Sellbot Factory'
ToonBattleOriginalLevel = 'Original Level'
ToontownCentralId = 2000
MinigameAreaId = 10000
RecoverAreaId = 11000
CogTropolisId = 12000
TheBrrrghId = 3000
DonaldsDockId = 1000
MinniesMelodylandId = 4000
DonaldsDreamlandId = 9000
DaisyGardensId = 5000
GoofySpeedwayId = 8000
QuietZone = 1
UberZone = 2
DistrictZone = 3
DynamicZonesBegin = 61000
DynamicZonesEnd = 1 << 20
safeZoneLSRanges = {ToontownCentral: 6, MinigameArea: 6, 
   RecoverArea: 8}
ToonStandableGround = 0.707
ToonSpeedFactor = 1.0
ToonForwardSpeed = 16.0 * ToonSpeedFactor
ToonJumpForce = 24.0
ToonReverseSpeed = 8.0 * ToonSpeedFactor
ToonRotateSpeed = 80.0 * ToonSpeedFactor
ToonForwardSlowSpeed = 6.0
ToonJumpSlowForce = 4.0
ToonReverseSlowSpeed = 2.5
ToonRotateSlowSpeed = 33.0
ErrorCode2ErrorMsg = {}
SecretPlace = 'Secret Place'
TryAgain = 'Try again?'
NoConnectionMsg = 'Could not connect to %s.'
DisconnectionMsg = 'Your internet connection to the servers has been unexpectedly broken.'
JoinFailureMsg = 'There was a problem getting you into ' + config.GetString('game-name') + '. Please restart the game.'
SuitDefeatMsg = 'You have been defeated by the ' + Suits + '! Try again?'
ConnectingMsg = 'Connecting...'
ServerUnavailable = 'The server appears to be temporarily unavailable. Still trying...'
JoiningMsg = 'Retrieving server info...'
OutdatedFilesMsg = 'Your game files are out of date. Please run the game from the launcher.'
ServerLockedMsg = 'The server is locked.'
NoShardsMsg = 'No Cog Invasion Districts are available.'
InvalidName = 'Sorry, that name will not work.'
Submitting = 'Submitting...'
AlreadyLoggedInMsg = 'You have been disconnected because someone else has logged into this account from another computer.'
DistrictResetMsg = 'The district you were playing in has been reset. Everybody playing in that district has been logged out.'
SuitFlyingDownMsg = 'A ' + Suit + ' is flying down!'
SuitInvasionMsg = 'A ' + Suit + ' Invasion has begun!'
SuitInvasionInProgMsg = 'There is a ' + Suit + ' Invasion in progress!'
SuitTournamentInProgMsg = 'There is a ' + Suit + ' Tournament in progress!'
SuitBreakMsgArray = [
 'The ' + Suits + " are going on break now... but they'll be back!",
 "You've defeated them all, but they'll be back...",
 'The ' + Suits + " are rethinking their plans. They'll be back soon.",
 'The ' + Suits + ' are taking a break for a few minutes.',
 'The ' + Suits + " are exhausted from all the battling! They'll be back momentarily.",
 'The ' + Suits + ' are taking a break! This is a good time to refill on gags and Laff!']
SuitBackFromBreakMsgArray = [
 'The ' + Suits + ' have returned from their break!',
 'The ' + Suits + ' are back!',
 'The ' + Suits + ' are back from their break!']
DialogOk = 'OK'
DialogCancel = 'Cancel'
DialogNo = 'No'
DialogYes = 'Yes'
BootedMsg = 'You have been booted out by the server. Code: %s'
GameVersionURL = 'https://dl.dropboxusercontent.com/u/239921115/ToontownOnlineMultifiles/gameversion.txt'
MatNAMsg = 'Make-A-Toon is currently unavailable right now. Do you want to be given a random Toon?'
FirstTimeMsg = 'It looks like it is your first time playing. Do you want to watch a tutorial video?'
UpdateReg5Min = 'The Cog Invasion server will be restarting for an update in 5 minutes.'
UpdateReg1Min = 'The Cog Invasion server will be restarting for an update in 60 seconds.'
UpdateRegClosed = 'The Cog Invasion server will be restarting now.'
UpdateEmg5Min = 'The Cog Invasion server will be closing for an emergency update in 5 minutes.'
UpdateEmg1Min = 'The Cog Invasion server will be closing for an emergency update in 60 seconds.'
UpdateEmgClosed = "The Cog Invasion server is now closing for an emergency update. It shouldn't be too long until the server is back up."
TutorialCoachDialogue = {'intro': [
           "Ay, my name's Coach, and welcome to da Cog Invasion tutorial!",
           'Dis will prepare ya for da real stuff, ya know?',
           "Now since ya knew here, I'm just gon' go ovah da basics.",
           "I'll teach ya about ya gags, and dose pesky " + Suits + '.',
           "Den I'll send in some " + Suits + ' for ya to take out.',
           "Oh no, don't worry, dey ain't real.",
           "Go 'head and click dat 'OK' button when ya ready to continue."], 
   'ready': [
           "Aight, let's get dis show on da road!"], 
   'cogs': [
          'So deez ' + Suits + " are robots created by deez evil scientists somewhere. I got no idea who deez guys ah, I don't think anybody does.",
          "Anyway, we don't want deez '" + Suits + "' messin' wit us, so we found ah own way to take 'em down.",
          'We use pastries and otha weeyad stuff.',
          "I think it clogs der internals or somethin'."], 
   'gags': [
          "So here's a quick look at da gags.",
          'Da LBT' + Suits[0] + "A (Let's Bust Those " + Suits + ' Association), has approved da use of only four items at da moment.',
          'Dose ah: Cream Pie Slice, Whole Cream Pie, Birthday Cake, and TNT',
          "Da TNT can only be used by purchasin' it at Goofy's Gag Shop in Toontown Central. But, for tutorial purposes, I'm gonna give ya one later on to use.",
          'Da LBT' + Suits[0] + "A requiyez all new Toons in town to specialize in all four gags before enterin'.",
          "Go 'head and click dat 'OK' button when ya ready to continue."], 
   'tut1': [
          "Aight, so I've equipped ya wit all four gags.",
          'As you can see on da right side of ya screen, deres da gags!',
          'To select anotha gag to use, eitha press da key on ya keyboard dat matches da numba, ' + 'use da scroll wheel on ya mouse, or just simply click on da gag.',
          "Go 'head and switch ya gag to a Cream Pie Slice in any way you desiyeh."], 
   'tut1complete': [
                  "Dat was difficult, wasn't it?",
                  "Yeah, dat's what I thought.",
                  "Go 'head and click dat 'OK' button when ya ready to continue."], 
   'tut2': [
          'Ya should see a ' + Suit + ' flying down somewhere.',
          'Der it is!',
          'Now, use da arrow keys to move around.',
          'Good! Walk ovah to dat ' + Suit + " and click da 'Throw Gag' button or press delete on ya keyboard to use any gag ya want on dis guy.",
          'Awesome job!',
          'Whoa, what is dat?! It looks like dat ' + Suit + ' was a naughty one and stole some of ah jellybeans.',
          'Simply walk into da item to collect it.',
          "You can use dose jellybeans you just collected der to purchase gags at Goofy's Gag Shop."], 
   'tut2complete': [
                  "Dat was difficult, wasn't it?",
                  "Go 'head and click dat 'OK' button when ya ready to continue."], 
   'tut3': [
          'Anotha ' + Suit + ' is flying down.',
          'Dis ' + Suit + ' is a little angry and wants to attack ya!',
          "Try to avoid a few of dis guy's attacks.",
          "Wow, you're better at dis den I thought!",
          'Now, take dis ' + Suit + ' down!'], 
   'tut3complete': [
                  'Sweet!',
                  "Go 'head and click dat 'OK' button when ya ready to continue."], 
   'tut4': [
          "Here's dat TNT I promised ya!",
          "Aight, I'm sending in a group of " + Suits + ' for ya.',
          "Now, throw dat TNT in a place dat you think will take 'em all out!"], 
   'tut4complete': [
                  "Kaboom! Good job!Go 'head and click dat 'OK' button when ya ready to continue."], 
   'outro': [
           'I think ya ready for da real stuff!',
           'Oh, one last thing. If ya lose all ya Laff points, ya go sad!',
           "Once that happens, ya sent to an area similah to dis one, but it's got delicious ice cream cones everywhere.",
           'Collect dose ice cream cones in da same way you collected da stolen jellybeans, to refill ya Laff points!See ya later!']}
ModelPolys = {CChar: {'high': 1200, 'medium': 800, 
           'low': 400}, 
   Toon: {'high': 1000, 'medium': 500, 
          'low': 250}}
ModelDetail = None
OkayBtnGeom = None
CancelBtnGeom = None
DefaultBtnGeom = None

def getToonFont():
    global ToonFont
    if not ToonFont:
        ToonFont = loader.loadFont('phase_3/models/fonts/ImpressBT.ttf', lineHeight=1.0)
    return ToonFont


def getSuitFont():
    global SuitFont
    if not SuitFont:
        SuitFont = loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf', pixelsPerUnit=40, spaceAdvance=0.25, lineHeight=1.0)
    return SuitFont


def getMickeyFont():
    global MickeyFont
    if not MickeyFont:
        MickeyFont = loader.loadFont('phase_3/models/fonts/MickeyFont.bam')
    return MickeyFont


def getMinnieFont():
    global MinnieFont
    if not MinnieFont:
        MinnieFont = loader.loadFont('phase_3/models/fonts/MinnieFont.bam')
    return MinnieFont


def getModelDetail(avatar):
    global ModelDetail
    width, height, fs, music, sfx, tex_detail, model_detail, aa, af = SettingsManager().getSettings('settings.json')
    ModelDetail = ModelPolys[avatar][model_detail]
    return ModelDetail


def getOkayBtnGeom():
    global OkayBtnGeom
    if not OkayBtnGeom:
        OkayBtnGeom = (
         loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui.bam').find('**/ChtBx_OKBtn_UP'),
         loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui.bam').find('**/ChtBx_OKBtn_DN'),
         loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui.bam').find('**/ChtBx_OKBtn_Rllvr'))
    return OkayBtnGeom


def getCancelBtnGeom():
    global CancelBtnGeom
    if not CancelBtnGeom:
        CancelBtnGeom = (
         loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui.bam').find('**/CloseBtn_UP'),
         loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui.bam').find('**/CloseBtn_DN'),
         loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui.bam').find('**/CloseBtn_Rllvr'))
    return CancelBtnGeom


def getDefaultBtnGeom():
    global DefaultBtnGeom
    if not DefaultBtnGeom:
        btn = loader.loadModel('phase_3/models/gui/quit_button.bam')
        DefaultBtnGeom = (btn.find('**/QuitBtn_UP'),
         btn.find('**/QuitBtn_DN'),
         btn.find('**/QuitBtn_RLVR'))
    return DefaultBtnGeom


ShadowScales = {Suit: 0.4, Toon: 0.4, 
   CChar: 0.55}
ToonColors = [(1.0, 1.0, 1.0, 1.0),
 (
  0.96875, 0.691406, 0.699219, 1.0),
 (
  0.933594, 0.265625, 0.28125, 1.0),
 (
  0.863281, 0.40625, 0.417969, 1.0),
 (
  0.710938, 0.234375, 0.4375, 1.0),
 (
  0.570312, 0.449219, 0.164062, 1.0),
 (
  0.640625, 0.355469, 0.269531, 1.0),
 (
  0.996094, 0.695312, 0.511719, 1.0),
 (
  0.832031, 0.5, 0.296875, 1.0),
 (
  0.992188, 0.480469, 0.167969, 1.0),
 (
  0.996094, 0.898438, 0.320312, 1.0),
 (
  0.996094, 0.957031, 0.597656, 1.0),
 (
  0.855469, 0.933594, 0.492188, 1.0),
 (
  0.550781, 0.824219, 0.324219, 1.0),
 (
  0.242188, 0.742188, 0.515625, 1.0),
 (
  0.304688, 0.96875, 0.402344, 1.0),
 (
  0.433594, 0.90625, 0.835938, 1.0),
 (
  0.347656, 0.820312, 0.953125, 1.0),
 (
  0.191406, 0.5625, 0.773438, 1.0),
 (
  0.558594, 0.589844, 0.875, 1.0),
 (
  0.285156, 0.328125, 0.726562, 1.0),
 (
  0.460938, 0.378906, 0.824219, 1.0),
 (
  0.546875, 0.28125, 0.75, 1.0),
 (
  0.726562, 0.472656, 0.859375, 1.0),
 (
  0.898438, 0.617188, 0.90625, 1.0),
 (
  0.7, 0.7, 0.8, 1.0),
 (
  0.3, 0.3, 0.35, 1.0)]
ShirtColors = [(1.0, 1.0, 1.0, 1.0),
 (
  0.96875, 0.691406, 0.699219, 1.0),
 (
  0.933594, 0.265625, 0.28125, 1.0),
 (
  0.863281, 0.40625, 0.417969, 1.0),
 (
  0.710938, 0.234375, 0.4375, 1.0),
 (
  0.570312, 0.449219, 0.164062, 1.0),
 (
  0.640625, 0.355469, 0.269531, 1.0),
 (
  0.996094, 0.695312, 0.511719, 1.0),
 (
  0.832031, 0.5, 0.296875, 1.0),
 (
  0.992188, 0.480469, 0.167969, 1.0),
 (
  0.996094, 0.898438, 0.320312, 1.0),
 (
  0.996094, 0.957031, 0.597656, 1.0),
 (
  0.855469, 0.933594, 0.492188, 1.0),
 (
  0.550781, 0.824219, 0.324219, 1.0),
 (
  0.242188, 0.742188, 0.515625, 1.0),
 (
  0.304688, 0.96875, 0.402344, 1.0),
 (
  0.433594, 0.90625, 0.835938, 1.0),
 (
  0.347656, 0.820312, 0.953125, 1.0),
 (
  0.191406, 0.5625, 0.773438, 1.0),
 (
  0.558594, 0.589844, 0.875, 1.0),
 (
  0.285156, 0.328125, 0.726562, 1.0),
 (
  0.460938, 0.378906, 0.824219, 1.0),
 (
  0.546875, 0.28125, 0.75, 1.0),
 (
  0.726562, 0.472656, 0.859375, 1.0),
 (
  0.898438, 0.617188, 0.90625, 1.0),
 (
  0.7, 0.7, 0.8, 1.0),
 (
  0.3, 0.3, 0.35, 1.0),
 (
  1.0, 1.0, 1.0, 1.0),
 (
  0.96875, 0.691406, 0.699219, 1.0),
 (
  0.933594, 0.265625, 0.28125, 1.0),
 (
  0.863281, 0.40625, 0.417969, 1.0),
 (
  0.710938, 0.234375, 0.4375, 1.0),
 (
  0.570312, 0.449219, 0.164062, 1.0),
 (
  0.640625, 0.355469, 0.269531, 1.0),
 (
  0.996094, 0.695312, 0.511719, 1.0),
 (
  0.832031, 0.5, 0.296875, 1.0),
 (
  0.992188, 0.480469, 0.167969, 1.0),
 (
  0.996094, 0.898438, 0.320312, 1.0),
 (
  0.996094, 0.957031, 0.597656, 1.0),
 (
  0.855469, 0.933594, 0.492188, 1.0),
 (
  0.550781, 0.824219, 0.324219, 1.0),
 (
  0.242188, 0.742188, 0.515625, 1.0),
 (
  0.304688, 0.96875, 0.402344, 1.0),
 (
  0.433594, 0.90625, 0.835938, 1.0),
 (
  0.347656, 0.820312, 0.953125, 1.0),
 (
  0.191406, 0.5625, 0.773438, 1.0),
 (
  0.558594, 0.589844, 0.875, 1.0),
 (
  0.285156, 0.328125, 0.726562, 1.0),
 (
  0.460938, 0.378906, 0.824219, 1.0),
 (
  0.546875, 0.28125, 0.75, 1.0),
 (
  0.726562, 0.472656, 0.859375, 1.0),
 (
  0.898438, 0.617188, 0.90625, 1.0),
 (
  0.7, 0.7, 0.8, 1.0),
 (
  0.3, 0.3, 0.35, 1.0)]
SuitHealTaunt = 'Here, take this med-kit.'
SuitGeneralTaunts = ["It's my day off.",
 "I believe you're in the wrong office.",
 'Have your people call my people.',
 "You're in no position to meet with me.",
 'Talk to my assistant.',
 "I don't take meetings with Toons.",
 'I excel at Toon disposal.',
 "You'll have to go through me first.",
 "You're not going to like the way I work.",
 "Let's see how you rate my job performance.",
 "I'd like some feedback on my performance.",
 'Surprised to hear from me?',
 "You've got big trouble on the line."]
SuitFaceoffTaunts = {SuitGlobals.Bloodsucker: ['Do you have a donation for me?',
                           "I'm going to make you a sore loser.",
                           "I'm going to leave you high and dry.",
                           'I\'m "A Positive" I\'m going to win.',
                           '"O" don\'t be so "Negative".',
                           "I'm surprised you found me, I'm very mobile.",
                           "I'm going to need to do a quick count on you.",
                           "You're soon going to need a cookie and some juice.",
                           "When I'm through you'll need to lie down.",
                           'This will only hurt for a second.',
                           "I'm going to make you dizzy.",
                           "Good timing, I'm a pint low.",
                           "You'll B the opposite of A happy toon when I'm finished with you."], 
   SuitGlobals.TheMingler: [
                          "You don't know who you're mingling with.",
                          'Ever mingle with the likes of me?',
                          'Good, it takes two to mingle.',
                          "Let's mingle.",
                          'This looks like a good place to mingle.',
                          "Well,isn't this cozy?",
                          "You're mingling with defeat.",
                          "I'm going to mingle in your business.",
                          "Are you sure you're ready to mingle?"], 
   SuitGlobals.MoverShaker: [
                           'Get ready for a shake down.',
                           'You had better move out of the way.',
                           'Move it or lose it.',
                           "I believe it's my move.",
                           'This should shake you up.',
                           'Prepare to be moved.',
                           "I'm ready to make my move.",
                           "Watch out toon, you're on shaky ground.",
                           'This should be a moving moment.',
                           'I feel moved to defeat you.',
                           'Are you shaking yet?'], 
   SuitGlobals.HeadHunter: [
                          "I'm way ahead of you.",
                          "You're headed for big trouble.",
                          "You'll wish this was all in your head.",
                          "Oh good, I've been hunting for you.",
                          "I'll have your head for this.",
                          'Heads up!',
                          "Looks like you've got a head for trouble.",
                          'Headed my way?',
                          'A perfect trophy for my collection.',
                          'You are going to have such a headache.',
                          "Don't lose your head over me."], 
   SuitGlobals.TheBigCheese: [
                            "Watch out, I'm gouda getcha.",
                            'You can call me Jack.',
                            'Are you sure?  I can be such a Muenster at times.',
                            'Well finally, I was afraid you were stringing me along.',
                            "I'm going to cream you.",
                            "Don't you think I've aged well?",
                            "I'm going to make mozzarella outta ya.",
                            "I've been told I'm very strong.",
                            'Careful, I know your expiration date.',
                            "Watch out, I'm a whiz at this game.",
                            'Beating you will be a brieeze.'], 
   SuitGlobals.CorporateRaider: [
                               'RAID!',
                               "You don't fit in my corporation.",
                               'Prepare to be raided.',
                               "Looks like you're primed for a take-over.",
                               'That is not proper corporate attire.',
                               "You're looking rather vulnerable.",
                               'Time to sign over your assets.',
                               "I'm on a toon removal crusade.",
                               'You are defenseless against my ideas.',
                               "Relax, you'll find this is for the best."], 
   SuitGlobals.MrHollywood: [
                           'Are you ready for my take?',
                           'Lights, camera, action!',
                           "Let's start rolling.",
                           'Today the role of defeated toon, will be played by - YOU!',
                           'This scene will go on the cutting room floor.',
                           'I already know my motivation for this scene.',
                           'Are you ready for your final scene?',
                           "I'm ready to roll your end credits.",
                           'I told you not to call me.',
                           "Let's get on with the show.",
                           "There's no business like it!",
                           "I hope you don't forget your lines."], 
   SuitGlobals.NumberCruncher: [
                              'Looks like your number is up.',
                              'I hope you prefer extra crunchy.',
                              "Now you're really in a crunch.",
                              'Is it time for crunch already?',
                              "Let's do crunch.",
                              'Where would you like to have your crunch today?',
                              "You've given me something to crunch on.",
                              'This will not be smooth.',
                              'Go ahead, try and take a number.',
                              'I could do with a nice crunch about now.'], 
   SuitGlobals.LoanShark: [
                         "It's time to collect on your loan.",
                         "You've been on borrowed time.",
                         'Your loan is now due.',
                         'Time to pay up.',
                         'Well you asked for an advance and you got it.',
                         "You're going to pay for this.",
                         "It's pay back time.",
                         'Can you lend me an ear?',
                         "Good thing you're here,  I'm in a frenzy.",
                         'Shall we have a quick bite?',
                         'Let me take a bite at it.'], 
   SuitGlobals.MoneyBags: [
                         'Time to bring in the big bags.',
                         'I can bag this.',
                         'Paper or plastic?',
                         'Do you have your baggage claim?',
                         "Remember, money won't make you happy.",
                         'Careful, I have some serious baggage.',
                         "You're about to have money trouble.",
                         'Money will make your world go around.',
                         "I'm too rich for your blood.",
                         'You can never have too much money!'], 
   SuitGlobals.RobberBaron: [
                           "You've been robbed.",
                           "I'll rob you of this victory.",
                           "I'm a royal pain!",
                           'Hope you can grin and baron.',
                           "You'll need to report this robbery.",
                           "Stick 'em up.",
                           "I'm a noble adversary.",
                           "I'm going to take everything you have.",
                           'You could call this neighborhood robbery.',
                           'You should know not to talk to strangers.'], 
   SuitGlobals.BackStabber: [
                           'Never turn your back on me.',
                           "You won't be coming back.",
                           'Take that back or else!',
                           "I'm good at cutting costs.",
                           'I have lots of back up.',
                           "There's no backing down now.",
                           "I'm the best and I can back that up.",
                           'Whoa, back up there toon.',
                           'Let me get your back.',
                           "You're going to have a stabbing headache soon.",
                           'I have perfect puncture.',
                           "Don't worry toon, you can always trust me."], 
   SuitGlobals.BigWig: [
                      "Don't brush me aside.",
                      'You make my hair curl.',
                      'I can make this permanent if you want.',
                      "It looks like you're going to have some split ends.",
                      "You can't handle the truth.",
                      "I think it's your turn to be dyed.",
                      "I'm so glad you're on time for your cut.",
                      "You're in big trouble.",
                      "I'm going to wig out on you.",
                      "I'm a big deal little toon."], 
   SuitGlobals.LegalEagle: [
                          "Careful, my legal isn't very tender.",
                          'I soar, then I score.',
                          "I'm bringing down the law on you.",
                          'You should know, I have some killer instincts.',
                          "I'm going to give you legal nightmares.",
                          "You won't win this battle.",
                          'This is so much fun it should be illegal.',
                          "Legally, you're too small to fight me.",
                          'There is no limit to my talons.',
                          "I call this a citizen's arrest.",
                          "I've got the court under my wing."], 
   SuitGlobals.SpinDoctor: [
                          "You'll never know when I'll stop.",
                          'Let me take you for a spin.',
                          'The doctor will see you now.',
                          "I'm going to put you into a spin.",
                          'You look like you need a doctor.',
                          'The doctor is in, the Toon is out.',
                          "You won't like my spin on this.",
                          'You are going to spin out of control.',
                          'Care to take a few turns with me?',
                          'I have my own special spin on the subject.'], 
   SuitGlobals.Flunky: [
                      "I'm gonna tell the boss about you!",
                      "I may be just a flunky - But I'm real spunky.",
                      "I'm using you to step up the corporate ladder.",
                      "You're not going to like the way I work.",
                      'The boss is counting on me to stop you.',
                      "You're going to look good on my resume.",
                      "You'll have to go through me first.",
                      "Let's see how you rate my job performance.",
                      'I excel at Toon disposal.',
                      "You're never going to meet my boss.",
                      "I'm sending you back to the Playground."], 
   SuitGlobals.PencilPusher: [
                            "I'm gonna rub you out!",
                            "Hey, you can't push me around.",
                            "I'm No.2!",
                            "I'm going to scratch you out.",
                            "I'll have to make my point more clear.",
                            'Let me get right to the point.',
                            "Let's hurry, I bore easily.",
                            'I hate it when things get dull.',
                            'So you want to push your luck?',
                            'Did you pencil me in?',
                            'Careful, I may leave a mark.'], 
   SuitGlobals.Yesman: [
                      "I'm positive you're not going to like this.",
                      "I don't know the meaning of no.",
                      'Want to meet?  I say yes, anytime.',
                      'You need some positive enforcement.',
                      "I'm going to make a positive impression.",
                      "I haven't been wrong yet.",
                      "Yes, I'm ready for you.",
                      'Are you positive you want to do this?',
                      "I'll be sure to end this on a positive note.",
                      "I'm confirming our meeting time.",
                      "I won't take no for an answer."], 
   SuitGlobals.Micromanager: [
                            "I'm going to get into your business!",
                            'Sometimes big hurts come in small packages.',
                            'No job is too small for me.',
                            "I want the job done right, so I'll do it myself.",
                            'You need someone to manage your assets.',
                            'Oh good, a project.',
                            "Well, you've managed to find me.",
                            'I think you need some managing.',
                            "I'll take care of you in no time.",
                            "I'm watching every move you make.",
                            'Are you sure you want to do this?',
                            "We're going to do this my way.",
                            "I'm going to be breathing down your neck.",
                            'I can be very intimidating.',
                            "I've been searching for my growth spurt."], 
   SuitGlobals.Downsizer: [
                         "You're going down!",
                         'Your options are shrinking.',
                         'Expect diminishing returns.',
                         "You've just become expendable.",
                         "Don't ask me to lay off.",
                         'I might have to make a few cutbacks.',
                         'Things are looking down for you.',
                         'Why do you look so down?'], 
   SuitGlobals.ColdCaller: [
                          'Surprised to hear from me?',
                          'You rang?',
                          'Are you ready to accept my charges?',
                          'This caller always collects.',
                          "I'm one smooth operator.",
                          "Hold the phone -- I'm here.",
                          'Have you been waiting for my call?',
                          "I was hoping you'd answer my call.",
                          "I'm going to cause a ringing sensation.",
                          'I always make my calls direct.',
                          'Boy, did you get your wires crossed.',
                          'This call is going to cost you.',
                          "You've got big trouble on the line."], 
   SuitGlobals.Telemarketer: [
                            'I plan on making this inconvenient for you.',
                            'Can I interest you in an insurance plan?',
                            'You should have missed my call.',
                            "You won't be able to get rid of me now.",
                            'This a bad time?  Good.',
                            'I was planning on running into you.',
                            'I will be reversing the charges for this call.',
                            'I have some costly items for you today.',
                            'Too bad for you - I make house calls.',
                            "I'm prepared to close this deal quickly.",
                            "I'm going to use up a lot of your resources."], 
   SuitGlobals.NameDropper: [
                           'In my opinion, your name is mud.',
                           "I hope you don't mind if I drop your name.",
                           "Haven't we met before?",
                           "Let's hurry, I'm having lunch with 'Mr. Hollywood.'",
                           "Have I mentioned I know 'The Mingler?'",
                           "You'll never forget me.",
                           'I know all the right people to bring you down.',
                           "I think I'll just drop in.",
                           "I'm in the mood to drop some Toons.",
                           "You name it, I've dropped it."], 
   SuitGlobals.GladHander: [
                          'Put it there, Toon.',
                          "Let's shake on it.",
                          "I'm going to enjoy this.",
                          "You'll notice I have a very firm grip.",
                          "Let's seal the deal.",
                          "Let's get right to the business at hand.",
                          "Off handedly I'd say, you're in trouble.",
                          "You'll find I'm a handful.",
                          'I can be quite handy.',
                          "I'm a very hands-on kinda guy.",
                          'Would you like some hand-me-downs?',
                          'Let me show you some of my handiwork.',
                          'I think the handwriting is on the wall.',
                          "I'll gladly handle your gags for you"], 
   SuitGlobals.ShortChange: [
                           'I will make short work of you.',
                           "You're about to have money trouble.",
                           "You're about to be overcharged.",
                           'This will be a short-term assignment.',
                           "I'll be done with you in short order.",
                           "You'll soon experience a shortfall.",
                           "Let's make this a short stop.",
                           "I think you've come up short.",
                           'I have a short temper for Toons.',
                           "I'll be with you shortly.",
                           "You're about to be shorted.",
                           "Well, aren't you a little short on your changes?"], 
   SuitGlobals.PennyPincher: [
                            'This is going to sting a little.',
                            "I'm going to give you a pinch for luck.",
                            "You don't want to press your luck with me.",
                            "I'm going to put a crimp in your smile.",
                            'Perfect, I have an opening for you.',
                            'Let me add my two cents.',
                            "I've been asked to pinch-hit.",
                            "I'll prove you're not dreaming.",
                            'Heads you lose, tails I win.',
                            'A Penny for your gags.'], 
   SuitGlobals.Tightwad: [
                        'Things are about to get very tight.',
                        "That's Mr. Tightwad to you.",
                        "I'm going to cut off your funding.",
                        'Is this the best deal you can offer?',
                        "Let's get going - time is money.",
                        "You'll find I'm very tightfisted.",
                        "You're in a tight spot.",
                        'Prepare to walk a tight rope.',
                        'I hope you can afford this.',
                        "I'm going to make this a tight squeeze.",
                        "I'm going to make a big dent in your budget."], 
   SuitGlobals.BeanCounter: [
                           'I enjoy subtracting Toons.',
                           'You can count on me to make you pay.',
                           'Bean there, done that.',
                           'I can hurt you where it counts.',
                           'I make every bean count.',
                           'Your expense report is overdue.',
                           'Time for an audit.',
                           "Let's step into my office.",
                           'Where have you bean?',
                           "I've bean waiting for you.",
                           "I'm going to bean you."], 
   SuitGlobals.BottomFeeder: [
                            "Looks like you've hit rock bottom.",
                            "I'm ready to feast.",
                            "I'm a sucker for Toons.",
                            'Oh goody, lunch time.',
                            'Perfect timing, I need a quick bite.',
                            "I'd like some feedback on my performance.",
                            "Let's talk about the bottom line.",
                            "You'll find my talents are bottomless.",
                            'Good, I need a little pick-me-up.',
                            "I'd love to have you for lunch."], 
   SuitGlobals.TwoFace: [
                       "It's time to face-off!",
                       'You had better face up to defeat.',
                       'Prepare to face your worst nightmare!',
                       "Face it, I'm better than you.",
                       'Two heads are better than one.',
                       'It takes two to tango, you wanna tango?',
                       "You're in for two times the trouble.",
                       'Which face would you like to defeat you?',
                       "I'm 'two' much for you.",
                       "You don't know who you're facing.",
                       'Are you ready to face your doom?',
                       'My eyes are on you.'], 
   SuitGlobals.DoubleTalker: [
                            "I'm gonna give you double the trouble.",
                            'See if you can stop my double cross.',
                            'I serve a mean double-\x04DECKER.',
                            "It's time to do some double-dealing.",
                            'I plan to do some double DIPPING.',
                            "You're not going to like my double play.",
                            'You may want to double think this.',
                            'Get ready for a double TAKE.',
                            'You may want to double up against me.',
                            'Doubles anyone??'], 
   SuitGlobals.AmbulanceChaser: [
                               "I'm going to chase you out of town!",
                               'Do you hear a siren?',
                               "I'm going to enjoy this.",
                               'I love the thrill of the chase.',
                               'Let me give you the run down.',
                               'Do you have insurance?',
                               'I hope you brought a stretcher with you.',
                               'I doubt you can keep up with me.',
                               "It's all uphill from here.",
                               "You're going to need some urgent care soon.",
                               'This is no laughing matter.',
                               "I'm going to give you the business."]}
SuitAttackTaunts = {'canned': ['Do you like it out of the can?',
            '"Can" you handle this?',
            "This one's fresh out of the can!",
            'Ever been attacked by canned goods before?',
            "I'd like to donate this canned good to you!",
            'Get ready to "Kick the can"!',
            'You think you "can", you think you "can".',
            "I'll throw you in the can!",
            "I'm making me a can o' toon-a!",
            "You don't taste so good out of the can."], 
   'clipontie': [
               'Better dress for our meeting.',
               "You can't go OUT without your tie.",
               'The best dressed Cogs wear them.',
               'Try this on for size.',
               'You should dress for success.',
               'No tie, no service.',
               'Do you need help putting this on?',
               'Nothing says powerful like a good tie.',
               "Let's see if this fits.",
               'This is going to choke you up.',
               "You'll want to dress up before you go OUT.",
               "I think I'll tie you up."], 
   'powertie': [
              "I'll call later, you looked tied up.",
              'Are you ready to tie die?',
              "Ladies and gentlemen, it's a tie!",
              'You had better learn how to tie.',
              "I'll have you tongue-tied!",
              "This is the worst tie you'll ever get!",
              'Can you feel the power?',
              'My powers are far too great for you!',
              "I've got the power!",
              "By the powers vested in me, I'll tie you up."], 
   'halfwindsor': [
                 "This is the fanciest tie you'll ever see!",
                 'Try not to get too winded.',
                 "This isn't even half the trouble you're in.",
                 "You're lucky I don't have a whole windsor.",
                 "You can't afford this tie.",
                 "I bet you've never even SEEN a half windsor!",
                 'This tie is out of your league.',
                 "I shouldn't even waste this tie on you.",
                 "You're not even worth half of this tie!"], 
   'filibuster': [
                "Shall I fill 'er up?",
                'This is going to take awhile.',
                'I could do this all day.',
                "I don't even need to take a breath.",
                'I keep going and going and going.',
                'I never get tired of this one.',
                'I can talk a blue streak.',
                'Mind if I bend your ear?',
                "I think I'll shoot the breeze.",
                'I can always get a word in edgewise.'], 
   'evictionnotice': [
                    "It's moving time.",
                    'Pack your bags, Toon.',
                    'Time to make some new living arrangements.',
                    'Consider yourself served.',
                    "You're behind on your lease.",
                    'This will be extremely unsettling.',
                    "You're about to be uprooted.",
                    "I'm going to send you packing.",
                    "You're out of place.",
                    'Prepare to be relocated.',
                    "You're in a hostel position."], 
   'restrainingorder': [
                      'You should show a little restraint.',
                      "I'm slapping you with a restraining order!",
                      "You can't come within five feet of me.",
                      'Perhaps you better keep your distance.',
                      'You should be restrained.',
                      Suits + '!  Restrain that Toon!',
                      'Try and restrain yourself.',
                      "I hope I'm being too much of a restraint on you.",
                      'See if you can lift these restraints!',
                      "I'm ordering you to restrain!",
                      "Why don't we start with basic restraining?"], 
   'buzzword': [
              'Pardon me if I drone on.',
              'Have you heard the latest?',
              'Can you catch on to this?',
              'See if you can hum this Toon.',
              'Let me put in a good word for you.',
              'I\'ll "B" perfectly clear.',
              'You should "B" more careful.',
              'See if you can dodge this swarm.',
              "Careful, you're about to get stung.",
              'Looks like you have a bad case of hives.'], 
   'jargon': [
            'What nonsense.',
            'See if you can make sense of this.',
            'I hope you get this loud and clear.',
            "Looks like I'm going to have to raise my voice.",
            'I insist on having my say.',
            "I'm very outspoken.",
            'I must pontificate on this subject.',
            'See, words can hurt you.',
            'Did you catch my meaning?',
            'Words, words, words, words, words.'], 
   'mumbojumbo': [
                'Let me make this perfectly clear.',
                "It's as simple as this.",
                "This is how we're going to do this.",
                'Let me supersize this for you.',
                'You might call this technobabble.',
                'Here are my five-dollar words.',
                'Boy, this is a mouth full.',
                'Some call me bombastic.',
                'Let me just interject this.',
                'I believe these are the right words.'], 
   'doubletalk': [
                'Take a memo on this!'], 
   'schmooze': [
              "You'll never see this coming.",
              'This will look good on you.',
              "You've earned this.",
              "I don't mean to gush.",
              'Flattery will get me everywhere.',
              "I'm going to pile it on now.",
              'Time to lay it on thick.',
              "I'm going to get on your good side.",
              'That deserves a good slap on the back.',
              "I'm going to ring your praises.",
              'I hate to knock you off your pedestal, but...'], 
   'fingerwag': [
               'I have told you a thousand times.',
               'Now see here Toon.',
               "Don't make me laugh.",
               "Don't make me come over there.",
               "I'm tired of repeating myself.",
               "I believe we've been over this.",
               'You have no respect for us ' + Suits + '.',
               "I think it's time you pay attention.",
               'Blah, Blah, Blah, Blah, Blah.',
               "Don't make me stop this meeting.",
               'Am I going to have to separate you?',
               "We've been through this before."], 
   'razzledazzle': [
                  'Read my lips.',
                  'How about these choppers?',
                  "Aren't I charming?",
                  "I'm going to wow you.",
                  'My dentist does excellent work.',
                  "Blinding aren't they?",
                  "Hard to believe these aren't real.",
                  "Shocking, aren't they?",
                  "I'm going to cap this off.",
                  'I floss after every meal.',
                  'Say Cheese!'], 
   'chomp': [
           'Take a look at these chompers!',
           'Chomp, chomp, chomp!',
           "Here's something to chomp on.",
           'Looking for something to chomp on?',
           "Why don't you chomp on this?",
           "I'm going to have you for dinner.",
           'I love to feed on Toons!'], 
   'bite': [
          'Would you like a bite?',
          'Try a bite of this!',
          "You're biting off more than you can chew.",
          'My bite is bigger than my bark.',
          'Bite down on this!',
          'Watch out, I may bite.',
          "I don't just bite when I'm cornered.",
          "I'm just gonna grab a quick bite.",
          "I haven't had a bite all day.",
          'I just want a bite.  Is that too much to ask?'], 
   'glowerpower': [
                 'You looking at me?',
                 "I'm told I have very piercing eyes.",
                 'I like to stay on the cutting edge.',
                 "Jeepers, Creepers, don't you love my peepers?",
                 "Here's looking at you kid.",
                 "How's this for expressive eyes?",
                 'My eyes are my strongest feature.',
                 'The eyes have it.',
                 'Peeka-boo, I see you.',
                 'Look into my eyes...',
                 'Shall we take a peek at your future?'], 
   'marketcrash': [
                 "I'm going to crash your party.",
                 "You won't survive the crash.",
                 "I'm more than the market can bear.",
                 "I've got a real crash course for you!",
                 "Now I'll come crashing down.",
                 "I'm a real bull in the market.",
                 'Looks like the market is going down.',
                 'You had better get out quick!',
                 'Sell! Sell! Sell!',
                 'Shall I lead the recession?',
                 "Everybody's getting out, shouldn't you?"], 
   'playhardball': [
                  'So you wanna play hardball?',
                  "You don't wanna play hardball with me.",
                  'Batter up!',
                  'Hey batter, batter!',
                  "And here's the pitch...",
                  "You're going to need a relief pitcher.",
                  "I'm going to knock you out of the park.",
                  "Once you get hit, you'll run home.",
                  'This is your final inning!',
                  "You can't play with me!",
                  "I'll strike you out.",
                  "I'm throwing you a real curve ball!"], 
   'sacked': [
            "Looks like you're getting sacked.",
            "This one's in the bag.",
            "You've been bagged.",
            'Paper or plastic?',
            'My enemies shall be sacked!',
            'I hold the Toontown record in sacks per game.',
            "You're no longer wanted around here.",
            "Your time is up around here, you're being sacked!",
            'Let me bag that for you.',
            'No defense can match my sack attack!'], 
   'pickpocket': [
                'Let me check your valuables.',
                "Hey, what's that over there?",
                'Like taking candy from a baby.',
                'What a steal.',
                "I'll hold this for you.",
                'Watch my hands at all times.',
                'The hand is quicker than the eye.',
                "There's nothing up my sleeve.",
                'The management is not responsible for lost items.',
                "Finder's keepers.",
                "You'll never see it coming.",
                'One for me, none for you.',
                "Don't mind if I do.",
                "You won't be needing this..."], 
   'fountainpen': [
                 'This is going to leave a stain.',
                 "Let's ink this deal.",
                 'Be prepared for some permanent damage.',
                 "You're going to need a good dry cleaner.",
                 'You should change.',
                 'This fountain pen has such a nice font.',
                 "Here, I'll use my pen.",
                 'Can you read my writing?',
                 'I call this the plume of doom.',
                 "There's a blot on your performance.",
                 "Don't you hate when this happens?"], 
   'hangup': [
            "You've been disconnected.",
            'Good bye!',
            "It's time I end our connection.",
            " ...and don't call back!",
            'Click!',
            'This conversation is over.',
            "I'm severing this link.",
            'I think you have a few hang ups.',
            "It appears you've got a weak link.",
            'Your time is up.',
            'I hope you receive this loud and clear.',
            'You got the wrong number.'], 
   'redtape': [
             'This should wrap things up.',
             "I'm going to tie you up for awhile.",
             "You're on a roll.",
             'See if you can cut through this.',
             'This will get sticky.',
             "Hope you're claustrophobic.",
             "I'll make sure you stick around.",
             'Let me keep you busy.',
             'Just try to unravel this.',
             'I want this meeting to stick with you.']}
SuitTimeUntilToss = {'canned': {'A': 3, 'B': 3, 
              'C': 2.2}, 
   'playhardball': {'A': 3, 'B': 3, 
                    'C': 2.2}, 
   'clipontie': {'A': 3, 'B': 3, 
                 'C': 2.2}, 
   'marketcrash': {'A': 3, 'B': 3, 
                   'C': 2.2}, 
   'sacked': {'A': 3, 'B': 3, 
              'C': 2.2}, 
   'glowerpower': {'A': 1, 'B': 1, 
                   'C': 1}}
SuitHandColors = {'c': (0.95, 0.75, 0.75, 1.0), 's': (
       0.95, 0.75, 0.95, 1.0), 
   'l': (
       0.75, 0.75, 0.95, 1.0), 
   'm': (
       0.65, 0.95, 0.85, 1.0)}
SuitNameTagPos = {'tightwad': 5.8, 'moneybags': 7.4, 
   'micromanager': 3.5, 
   'gladhander': 6.7, 
   'flunky': 5.2, 
   'coldcaller': 4.9, 
   'ambulancechaser': 7.0, 
   'beancounter': 6.3, 
   'loanshark': 8.9, 
   'movershaker': 7.1, 
   'pencilpusher': 5.2, 
   'telemarketer': 5.6, 
   'backstabber': 7, 
   'bigcheese': 9.8, 
   'bigwig': 9.2, 
   'headhunter': 7.9, 
   'legaleagle': 8.75, 
   'numbercruncher': 7.8, 
   'pennypincher': 5.6, 
   'yesman': 5.6, 
   'twoface': 7.3, 
   'bottomfeeder': 5.1, 
   'corporateraider': 9.0, 
   'mrhollywood': 9.4, 
   'robberbaron': 9.4, 
   'shortchange': 4.9, 
   'downsizer': 6.3, 
   'bloodsucker': 6.5, 
   'spindoctor': 8.3, 
   'namedropper': 6.3, 
   'mingler': 8.0, 
   'doubletalker': 6.0, 
   'vp': 14.0}
SuitScales = {'tightwad': 4.5, 'moneybags': 5.3, 
   'micromanager': 2.5, 
   'gladhander': 4.75, 
   'flunky': 4.0, 
   'coldcaller': 3.5, 
   'ambulancechaser': 4.35, 
   'beancounter': 4.4, 
   'loanshark': 6.5, 
   'movershaker': 4.75, 
   'pencilpusher': 3.35, 
   'telemarketer': 3.75, 
   'backstabber': 4.5, 
   'bigcheese': 7.0, 
   'bigwig': 7.0, 
   'headhunter': 6.5, 
   'legaleagle': 7.125, 
   'numbercruncher': 5.25, 
   'pennypincher': 3.55, 
   'yesman': 4.125, 
   'twoface': 5.25, 
   'bottomfeeder': 4.0, 
   'corporateraider': 6.75, 
   'mrhollywood': 7.0, 
   'robberbaron': 7.0, 
   'shortchange': 3.6, 
   'downsizer': 4.5, 
   'bloodsucker': 4.375, 
   'spindoctor': 5.65, 
   'namedropper': 4.35, 
   'mingler': 5.75, 
   'doubletalker': 4.25, 
   'vp': 10}
SuitScaleFactors = {'A': 6.06, 'B': 5.29, 
   'C': 4.14}
SuitHealthAmounts = {'flunky': 20, 'bottomfeeder': 20, 
   'shortchange': 20, 
   'coldcaller': 20, 
   'pencilpusher': 30, 
   'bloodsucker': 30, 
   'pennypincher': 30, 
   'telemarketer': 30, 
   'yesman': 42, 
   'doubletalker': 42, 
   'tightwad': 42, 
   'namedropper': 42, 
   'micromanager': 56, 
   'ambulancechaser': 56, 
   'beancounter': 56, 
   'gladhander': 56, 
   'downsizer': 72, 
   'backstabber': 72, 
   'numbercruncher': 72, 
   'movershaker': 72, 
   'headhunter': 90, 
   'spindoctor': 90, 
   'moneybags': 90, 
   'twoface': 90, 
   'corporateraider': 110, 
   'legaleagle': 110, 
   'loanshark': 110, 
   'mingler': 110, 
   'bigcheese': 132, 
   'bigwig': 132, 
   'robberbaron': 132, 
   'mrhollywood': 132, 
   'vp': 5000}
SuitBodyData = {'flunky': (
            'C', 'c'), 
   'coldcaller': (
                'C', 's'), 
   'shortchange': (
                 'C', 'm'), 
   'bottomfeeder': (
                  'C', 'l'), 
   'pencilpusher': (
                  'B', 'c'), 
   'bloodsucker': (
                 'B', 'l'), 
   'pennypincher': (
                  'A', 'm'), 
   'telemarketer': (
                  'B', 's'), 
   'yesman': (
            'A', 'c'), 
   'doubletalker': (
                  'A', 'l'), 
   'tightwad': (
              'C', 'm'), 
   'namedropper': (
                 'A', 's'), 
   'micromanager': (
                  'C', 'c'), 
   'ambulancechaser': (
                     'B', 'l'), 
   'beancounter': (
                 'B', 'm'), 
   'gladhander': (
                'C', 's'), 
   'downsizer': (
               'B', 'c'), 
   'backstabber': (
                 'A', 'l'), 
   'numbercruncher': (
                    'A', 'm'), 
   'movershaker': (
                 'B', 's'), 
   'headhunter': (
                'A', 'c'), 
   'spindoctor': (
                'B', 'l'), 
   'moneybags': (
               'C', 'm'), 
   'twoface': (
             'A', 's'), 
   'corporateraider': (
                     'C', 'c'), 
   'legaleagle': (
                'A', 'l'), 
   'loanshark': (
               'B', 'm'), 
   'mingler': (
             'A', 's'), 
   'bigcheese': (
               'A', 'c'), 
   'bigwig': (
            'A', 'l'), 
   'robberbaron': (
                 'A', 'm'), 
   'mrhollywood': (
                 'A', 's'), 
   'vp': (
        'A', 's')}
SuitLevelRanges = None

def getSuitLevelRanges():
    global SuitLevelRanges
    if not SuitLevelRanges:
        SuitLevelRanges = {}
        for suit in ('flunky', 'bottomfeeder', 'shortchange', 'coldcaller'):
            SuitLevelRanges[suit] = range(1, 6)

        for suit in ('pencilpusher', 'bloodsucker', 'pennypincher', 'telemarketer'):
            SuitLevelRanges[suit] = range(2, 7)

        for suit in ('yesman', 'doubletalker', 'tightwad', 'namedropper'):
            SuitLevelRanges[suit] = range(3, 8)

        for suit in ('micromanager', 'ambulancechaser', 'beancounter', 'gladhander'):
            SuitLevelRanges[suit] = range(4, 9)

        for suit in ('downsizer', 'backstabber', 'numbercruncher', 'movershaker'):
            SuitLevelRanges[suit] = range(5, 10)

        for suit in ('headhunter', 'spindoctor', 'moneybags', 'twoface'):
            SuitLevelRanges[suit] = range(6, 11)

        for suit in ('corporateraider', 'legaleagle', 'loanshark', 'mingler'):
            SuitLevelRanges[suit] = range(7, 12)

        for suit in ('bigcheese', 'bigwig', 'robberbaron', 'mrhollywood'):
            SuitLevelRanges[suit] = range(8, 13)

        SuitLevelRanges['vp'] = [
         70]
    return SuitLevelRanges


def getSuitHP(level):
    return (level + 1) * (level + 2)


SuitHeads = {'tightwad': 'tightwad', 'moneybags': 'moneybags', 
   'micromanager': 'micromanager', 
   'gladhander': 'gladhander', 
   'flunky': 'flunky', 
   'shortchange': 'coldcaller', 
   'ambulancechaser': 'ambulancechaser', 
   'beancounter': 'beancounter', 
   'loanshark': 'loanshark', 
   'movershaker': 'movershaker', 
   'pencilpusher': 'pencilpusher', 
   'telemarketer': 'telemarketer', 
   'backstabber': 'backstabber', 
   'bigcheese': 'bigcheese', 
   'bigwig': 'bigwig', 
   'headhunter': 'headhunter', 
   'legaleagle': 'legaleagle', 
   'numbercruncher': 'numbercruncher', 
   'pennypincher': 'pennypincher', 
   'yesman': 'yesman', 
   'twoface': 'twoface', 
   'bottomfeeder': 'tightwad', 
   'corporateraider': 'flunky', 
   'mrhollywood': 'yesman', 
   'robberbaron': 'yesman', 
   'coldcaller': 'coldcaller', 
   'downsizer': 'beancounter', 
   'bloodsucker': 'movershaker', 
   'spindoctor': 'telemarketer', 
   'namedropper': 'numbercruncher', 
   'mingler': 'twoface', 
   'doubletalker': 'twoface', 
   'vp': None}
toonBodyScales = {'mouse': 0.6, 'cat': 0.73, 
   'duck': 0.66, 
   'rabbit': 0.74, 
   'horse': 0.85, 
   'dog': 0.85, 
   'monkey': 0.68, 
   'bear': 0.85, 
   'pig': 0.77}
toonHeadScales = {'mouse': Point3(1.0), 'cat': Point3(1.0), 
   'duck': Point3(1.0), 
   'rabbit': Point3(1.0), 
   'horse': Point3(1.0), 
   'dog': Point3(1.0), 
   'monkey': Point3(1.0), 
   'bear': Point3(1.0), 
   'pig': Point3(1.0)}
legHeightDict = {'dgs': 1.5, 'dgm': 2.0, 
   'dgl': 2.75}
torsoHeightDict = {'dgs_shorts': 1.5, 'dgm_shorts': 1.75, 
   'dgl_shorts': 2.25, 
   'dgs_skirt': 1.5, 
   'dgm_skirt': 1.75, 
   'dgl_skirt': 2.25}
headHeightDict = {'3': 0.75, '1': 0.5, 
   '2': 0.5, 
   '4': 0.75, 
   'dgs_shorts': 0.5, 
   'dgl_shorts': 0.75, 
   'dgm_shorts': 0.75, 
   'dgm_skirt': 0.5}
SuitPathHeights = {ToontownCentral: 0, TheBrrrgh: 6}
SuitSpawnPoints = {BattleTTC: {'1': LPoint3f(17, -17, 4.025), 
               '2': LPoint3f(17.5, 7.6, 4.025), 
               '3': LPoint3f(85, 11.5, 4.025), 
               '4': LPoint3f(85, -13, 4.025), 
               '5': LPoint3f(-27.5, -5.25, 0.0), 
               '6': LPoint3f(-106.15, -4.0, -2.5), 
               '7': LPoint3f(-89.5, 93.5, 0.5), 
               '8': LPoint3f(-139.95, 1.69, 0.5), 
               '9': LPoint3f(-110.95, -68.57, 0.5), 
               '10': LPoint3f(70.0001, -1.90735e-06, 4), 
               '11': LPoint3f(35.0001, -1.90735e-06, 4), 
               '12': LPoint3f(52.5001, 19, 4), 
               '13': LPoint3f(52.5001, -19, 4), 
               '14': LPoint3f(-9.99991, 50, 2.6226e-06), 
               '15': LPoint3f(-9.99991, -50, 2.6226e-06), 
               '16': LPoint3f(-40.8999, -87.6, 0.500003), 
               '17': LPoint3f(-40.8999, 87.6, 0.500003), 
               '18': LPoint3f(-116.86, -50, 0.500003), 
               '19': LPoint3f(-116.86, 50, 2.6226e-06), 
               '20': LPoint3f(-75.8099, 71.28, 2.6226e-06), 
               '21': LPoint3f(-75.8099, -71.28, 2.6226e-06), 
               '22': LPoint3f(-40.8999, 61.23, 2.6226e-06), 
               '23': LPoint3f(-40.8999, -61.23, 2.6226e-06), 
               '24': LPoint3f(-25.2999, 26.5, 2.6226e-06), 
               '25': LPoint3f(-25.2999, -26.5, 2.6226e-06), 
               '26': LPoint3f(-45.53, -7.62, -1.81), 
               '27': LPoint3f(-75.72, -8.71, -2.0), 
               '28': LPoint3f(-79.66, -5.78, -2.45), 
               '29': LPoint3f(-101.4, -31.23, -2.0), 
               '30': LPoint3f(-42.16, -31.23, -1.72), 
               '31': LPoint3f(-76.4, -59.59, -0.6), 
               '32': LPoint3f(6.09, -71.23, 1.52), 
               '33': LPoint3f(35.69, -89.27, 2.5), 
               '34': LPoint3f(35.69, -129.51, 2.5), 
               '35': LPoint3f(79.44, -135.14, 2.5), 
               '36': LPoint3f(62.44, -82.16, 3.0), 
               '37': LPoint3f(62.44, -68.04, 4.0), 
               '38': LPoint3f(38.02, -68.04, 4.0), 
               '39': LPoint3f(33.14, -58.11, 4.0), 
               '40': LPoint3f(32.25, -46.44, 4.0), 
               '41': LPoint3f(-68.85, -24.14, -2.05), 
               '42': LPoint3f(-68.85, 6.71, -2.0), 
               '43': LPoint3f(-45.35, 25.83, -2.39), 
               '44': LPoint3f(-112.36, 25.83, -0.4), 
               '45': LPoint3f(-82.9, 53.04, -1.81), 
               '46': LPoint3f(-53.79, 63.31, 0.0), 
               '47': LPoint3f(4.71, 72.1, 1.48), 
               '48': LPoint3f(39.0, 102.95, 2.5), 
               '49': LPoint3f(39.0, 134.81, 2.5), 
               '50': LPoint3f(90.29, 143.33, 2.5), 
               '51': LPoint3f(90.29, 106.5, 2.5)}, 
   TheBrrrgh: {'1': LPoint3f(0.0, 0.0, 6.17), 
               '2': LPoint3f(-5.1, -39.77, 6.17), 
               '3': LPoint3f(-26.19, -72.94, 6.17), 
               '4': LPoint3f(-55.71, -104.96, 6.17), 
               '5': LPoint3f(-68.23, -149.52, 6.17), 
               '6': LPoint3f(-88.0, -129.83, 6.17), 
               '7': LPoint3f(-88.0, -97.63, 5.65), 
               '8': LPoint3f(-107.42, -109.05, 6.17), 
               '9': LPoint3f(-123.97, -98.67, 6.09), 
               '10': LPoint3f(-141.66, -98.54, 6.17), 
               '11': LPoint3f(-147.29, -82.0, 6.17), 
               '12': LPoint3f(-153.66, -64.12, 6.17), 
               '13': LPoint3f(-158.09, -45.05, 6.17), 
               '14': LPoint3f(-155.12, -20.3, 6.17), 
               '15': LPoint3f(-147.86, -4.07, 6.17), 
               '16': LPoint3f(-155.18, 15.27, 6.17), 
               '17': LPoint3f(-133.65, 11.7, 6.17), 
               '18': LPoint3f(-108.84, 25.46, 6.17), 
               '19': LPoint3f(-119.91, 46.11, 6.17), 
               '20': LPoint3f(-134.68, 56.76, 6.17), 
               '21': LPoint3f(-110.99, 86.76, 6.17), 
               '22': LPoint3f(-76.26, 86.76, 6.17), 
               '23': LPoint3f(-76.26, 62.67, 6.17), 
               '24': LPoint3f(-82.1, 40.93, 6.17), 
               '25': LPoint3f(-39.3, 55.26, 6.17), 
               '26': LPoint3f(-30.34, 17.88, 6.17), 
               '27': LPoint3f(-8.67, 44.76, 6.17), 
               '28': LPoint3f(-65.33, 9.68, 2.98), 
               '29': LPoint3f(-103.9, -1.27, 2.98), 
               '30': LPoint3f(-126.96, -10.3, 2.98), 
               '31': LPoint3f(-101.37, -79.26, 2.98), 
               '32': LPoint3f(-69.53, -57.59, 2.98), 
               '33': LPoint3f(-128.29, -73.53, 2.98), 
               '34': LPoint3f(-141.63, -42.81, 2.98), 
               '35': LPoint3f(28.95, -14.11, 6.17), 
               '36': LPoint3f(45.64, -14.11, 6.17), 
               '37': LPoint3f(-17.03, 65.84, 6.17), 
               '38': LPoint3f(-5.83, 76.32, 6.17), 
               '39': LPoint3f(-14.97, -124.79, 6.17), 
               '40': LPoint3f(-24.35, -114.52, 6.17), 
               '41': LPoint3f(-39.52, -145, 6.17), 
               '42': LPoint3f(6.9, -113.53, 6.17), 
               '43': LPoint3f(41.63, -49.65, 6.17), 
               '44': LPoint3f(33.8, 47.5, 6.17), 
               '45': LPoint3f(-23.95, 95.46, 6.17), 
               '46': LPoint3f(-49.89, 101.47, 6.17)}, 
   DonaldsDreamland: {'1': LPoint3f(0.0, 0.0, -15.0), 
                      '2': LPoint3f(28.14, 34.35, -15.76), 
                      '3': LPoint3f(-28.14, -34.35, -15.76), 
                      '4': LPoint3f(28.66, -25.4, -15.33), 
                      '5': LPoint3f(66.96, 2.77, -15.0), 
                      '6': LPoint3f(73.89, 65.4, -17.25), 
                      '7': LPoint3f(73.89, 85.3, 0.0), 
                      '8': LPoint3f(73.89, 92.71, 0.0), 
                      '9': LPoint3f(55.62, 92.19, 0.0), 
                      '10': LPoint3f(25.48, 94.49, 0.0), 
                      '11': LPoint3f(-3.91, 92.38, 0.0), 
                      '12': LPoint3f(-42.91, 93.76, 0.0), 
                      '13': LPoint3f(-57.99, 89.79, 0.0), 
                      '14': LPoint3f(-70.62, 89.79, 0.0), 
                      '15': LPoint3f(-87.87, 98.06, 0.0), 
                      '16': LPoint3f(-95.59, 85.3, 0.0), 
                      '17': LPoint3f(-95.59, 66.53, -9.05), 
                      '18': LPoint3f(-49.94, 66.53, -17.3), 
                      '19': LPoint3f(2.76, 66.53, -17.3), 
                      '20': LPoint3f(-21.23, 34.46, -15.76), 
                      '21': LPoint3f(-50.9, 20.99, -15.12), 
                      '22': LPoint3f(-53.53, -1.82, -15.0), 
                      '23': LPoint3f(-50.8, -23.0, -15.21), 
                      '24': LPoint3f(-49.93, -66.14, -17.28), 
                      '25': LPoint3f(0.0, -66.14, -17.28), 
                      '26': LPoint3f(46.21, -58.74, -16.92), 
                      '27': LPoint3f(73.89, -65.4, -17.24), 
                      '28': LPoint3f(73.89, -85.25, 0.0), 
                      '29': LPoint3f(70.62, -95.8, 0.0), 
                      '30': LPoint3f(17.75, -94.11, 0.0), 
                      '31': LPoint3f(-5.43, -91.53, 0.0), 
                      '32': LPoint3f(-25.79, -93.54, 0.0), 
                      '33': LPoint3f(-49.36, -89.32, 0.0), 
                      '34': LPoint3f(-65.33, -89.32, 0.0), 
                      '35': LPoint3f(-87.65, -96.19, 0.0), 
                      '36': LPoint3f(-95.53, -85.25, 0.0), 
                      '37': LPoint3f(-95.53, -66.49, -9.05), 
                      '38': LPoint3f(77.4, -35.61, -15.82), 
                      '39': LPoint3f(35.25, -1.14, -15.0), 
                      '40': LPoint3f(128.87, 0.0, -15.02), 
                      '41': LPoint3f(151.72, -24.48, -15.02), 
                      '42': LPoint3f(175.42, -22.88, -15.02), 
                      '43': LPoint3f(187.25, -4.65, -15.02), 
                      '44': LPoint3f(184.32, 19.31, -15.02), 
                      '45': LPoint3f(154.72, 27.67, -15.02), 
                      '46': LPoint3f(95.55, 0.0, -15.0), 
                      '47': LPoint3f(44.46, 51.43, -16.58)}, 
   DonaldsDock: {'1': LPoint3f(62.06, 0.0, 5.67), 
                 '2': LPoint3f(62.06, -19.87, 5.67), 
                 '3': LPoint3f(69.73, -37.32, 5.67), 
                 '4': LPoint3f(69.44, -47.98, 3.25), 
                 '5': LPoint3f(57.8, -43.84, 3.25), 
                 '6': LPoint3f(65.39, -67.63, 3.25), 
                 '7': LPoint3f(53.27, -81.18, 3.25), 
                 '8': LPoint3f(37.89, -79.96, 3.25), 
                 '9': LPoint3f(26.79, -83.36, 3.25), 
                 '10': LPoint3f(19.22, -89.78, 3.25), 
                 '11': LPoint3f(10.86, -84.61, 3.25), 
                 '12': LPoint3f(2.27, -84.61, 5.67), 
                 '13': LPoint3f(-27.05, -79.18, 5.67), 
                 '14': LPoint3f(-62.48, -79.18, 5.67), 
                 '15': LPoint3f(-66.49, -66.8, 5.67), 
                 '16': LPoint3f(-73.74, -62.02, 5.67), 
                 '17': LPoint3f(-90.98, -57.4, 5.67), 
                 '18': LPoint3f(-107.22, -46.28, 5.67), 
                 '20': LPoint3f(-117.52, -49.41, 5.67), 
                 '21': LPoint3f(-113.89, -40.01, 5.67), 
                 '22': LPoint3f(-107.48, -18.4, 5.67), 
                 '23': LPoint3f(-109.37, -8.61, 5.67), 
                 '24': LPoint3f(-111.68, 11.51, 5.67), 
                 '25': LPoint3f(-110.39, 33.91, 5.67), 
                 '26': LPoint3f(-115.5, 43.32, 5.67), 
                 '27': LPoint3f(-112.04, 59.05, 3.26), 
                 '28': LPoint3f(-91.57, 57.64, 2.59), 
                 '29': LPoint3f(-84.91, 76.02, 3.25), 
                 '30': LPoint3f(-75.35, 99.4, 3.25), 
                 '31': LPoint3f(-59.45, 78.87, 3.25), 
                 '32': LPoint3f(-57.13, 100.83, 3.25), 
                 '33': LPoint3f(-42.82, 94.67, 3.25), 
                 '34': LPoint3f(-70.22, 124.43, 3.25), 
                 '35': LPoint3f(-45.77, 128.58, 3.25), 
                 '36': LPoint3f(-37.42, 161.01, 3.25), 
                 '37': LPoint3f(-4.24, 165.66, 3.25), 
                 '38': LPoint3f(12.71, 147.45, 3.25), 
                 '39': LPoint3f(10.82, 96.95, 3.25), 
                 '40': LPoint3f(34.11, 86.65, 3.25), 
                 '41': LPoint3f(54.13, 104.98, 3.25), 
                 '42': LPoint3f(59.58, 78.15, 3.25), 
                 '43': LPoint3f(70.15, 65.98, 3.25), 
                 '44': LPoint3f(69.67, 46.55, 5.67), 
                 '45': LPoint3f(61.38, 23.74, 5.67)}}
SuitPathData = {BattleTTC: {'28': ['42', '43', '27', '20', '21', '22', '46', '47', '45', '29', '7', '9', '17', '16', '19', '18', '31'], '48': ['30', '42', '43', '24', '26', '20', '21', '22', '47', '44', '28', '5', '6', '8', '14', '19', '31', '49', '51'], '29': ['30', '42', '32', '25', '27', '21', '23', '44', '28', '41', '1', '3', '4', '7', '6', '9', '8', '11', '10', '13', '19', '18', '31', '33'], '49': ['30', '43', '24', '25', '26', '21', '23', '47', '5', '14', '16', '50', '48'], '24': ['30', '42', '43', '32', '25', '26', '20', '21', '22', '23', '46', '47', '44', '45', '40', '1', '2', '5', '4', '8', '11', '10', '13', '14', '17', '16', '19', '49', '34', '48'], '25': ['30', '43', '32', '24', '26', '20', '21', '22', '23', '46', '47', '45', '29', '41', '1', '3', '2', '5', '4', '9', '11', '10', '13', '12', '15', '14', '17', '16', '18', '31', '49', '35', '34', '33'], '26': ['30', '43', '32', '24', '25', '27', '22', '23', '46', '47', '1', '3', '2', '5', '4', '11', '10', '13', '12', '15', '14', '17', '16', '49', '35', '34', '33'], '27': ['26', '21', '44', '45', '28', '29', '4', '7', '9', '19', '18', '31'], '20': ['42', '43', '32', '24', '25', '27', '21', '22', '46', '44', '45', '28', '40', '1', '2', '5', '4', '6', '9', '8', '11', '15', '14', '17', '19', '18', '31', '51', '34', '48'], '21': ['30', '24', '25', '27', '20', '23', '47', '44', '45', '28', '29', '41', '1', '3', '2', '5', '7', '6', '8', '11', '10', '13', '12', '15', '14', '16', '19', '18', '31', '49', '33', '48'], '22': ['30', '42', '43', '32', '24', '25', '26', '20', '23', '46', '47', '44', '45', '28', '40', '1', '2', '5', '6', '9', '8', '11', '13', '15', '14', '17', '16', '19', '18', '34', '48'], '23': ['30', '43', '32', '24', '25', '26', '21', '22', '46', '47', '29', '41', '1', '3', '2', '5', '6', '8', '11', '10', '13', '12', '15', '14', '17', '16', '18', '31', '49', '34', '33'], '46': ['30', '42', '43', '32', '24', '25', '26', '20', '22', '23', '47', '44', '45', '28', '40', '1', '2', '5', '7', '6', '9', '8', '11', '15', '14', '17', '16', '19', '18', '34'], '47': ['30', '42', '43', '32', '24', '25', '26', '21', '22', '23', '46', '44', '45', '28', '40', '1', '2', '5', '7', '6', '8', '39', '15', '14', '17', '16', '19', '31', '49', '48'], '44': ['42', '43', '24', '20', '21', '22', '46', '47', '45', '29', '1', '3', '2', '5', '4', '7', '6', '9', '8', '11', '10', '13', '14', '17', '19', '18', '31', '48'], '45': ['42', '43', '32', '24', '25', '27', '20', '21', '22', '46', '47', '44', '28', '1', '2', '5', '4', '7', '6', '9', '8', '11', '10', '13', '15', '14', '17', '19', '18', '31', '34', '33'], '42': ['43', '24', '20', '22', '46', '47', '44', '45', '28', '29', '1', '3', '2', '5', '4', '7', '8', '11', '10', '13', '14', '17', '19', '18', '48'], '43': ['30', '42', '32', '24', '25', '26', '20', '22', '23', '46', '47', '44', '45', '28', '40', '1', '2', '5', '4', '6', '8', '10', '13', '14', '17', '16', '19', '49', '34', '48'], '40': ['43', '24', '20', '22', '46', '47', '1', '2', '39', '11', '14', '17'], '41': ['30', '32', '25', '21', '23', '29', '1', '3', '2', '4', '9', '8', '11', '10', '13', '12', '15', '16', '18', '31', '35', '33'], '1': ['30', '42', '43', '24', '25', '26', '20', '21', '22', '23', '46', '47', '44', '45', '29', '40', '41', '3', '2', '5', '4', '9', '11', '10', '13', '12', '15', '14', '17', '16', '19', '18', '31'], '3': ['30', '42', '25', '26', '21', '23', '44', '29', '41', '1', '2', '5', '4', '9', '8', '10', '13', '12', '15', '18', '31'], '2': ['30', '42', '43', '32', '24', '25', '26', '20', '21', '22', '23', '46', '47', '44', '45', '40', '41', '1', '3', '5', '4', '7', '9', '8', '39', '11', '10', '13', '12', '15', '14', '17', '16', '19', '18', '31'], '5': ['30', '42', '43', '32', '24', '25', '26', '20', '21', '22', '23', '46', '47', '44', '45', '1', '3', '2', '4', '9', '11', '10', '13', '12', '15', '14', '17', '16', '19', '18', '31', '49', '34', '48'], '4': ['30', '42', '43', '24', '25', '26', '27', '20', '44', '45', '29', '41', '1', '3', '2', '5', '11', '10', '13', '12', '19', '18'], '7': ['42', '27', '21', '22', '46', '47', '44', '45', '28', '29', '2', '6', '9', '8', '11', '13', '14', '19', '18', '31'], '6': ['43', '20', '21', '22', '23', '46', '47', '44', '45', '29', '7', '9', '8', '14', '17', '19', '18', '31', '34', '48'], '9': ['30', '25', '27', '20', '22', '46', '44', '45', '28', '29', '41', '1', '3', '2', '5', '7', '6', '11', '10', '13', '12', '15', '17', '19', '18', '31'], '8': ['30', '42', '43', '32', '24', '20', '21', '22', '23', '46', '47', '44', '45', '29', '41', '2', '7', '6', '15', '14', '17', '31', '35', '33', '48'], '13': ['30', '42', '43', '24', '25', '26', '20', '21', '22', '23', '46', '44', '45', '29', '41', '1', '3', '2', '5', '4', '7', '9', '11', '10', '12', '15', '14', '19', '18', '31'], '12': ['30', '25', '26', '21', '23', '41', '1', '3', '2', '5', '4', '9', '11', '10', '13', '15', '16', '18', '31'], '11': ['30', '42', '43', '24', '25', '26', '21', '22', '23', '46', '44', '45', '29', '40', '41', '1', '3', '2', '5', '4', '7', '9', '10', '13', '12', '15', '14', '16', '19', '18', '31'], '10': ['30', '42', '43', '24', '25', '26', '21', '23', '44', '45', '29', '41', '1', '3', '2', '5', '4', '9', '11', '13', '12', '15', '19', '18', '31'], '39': ['47', '40', '2', '38'], '38': ['39', '37'], '15': ['30', '43', '32', '24', '25', '26', '20', '21', '22', '23', '46', '47', '45', '29', '41', '1', '3', '2', '5', '9', '8', '11', '10', '13', '12', '14', '17', '16', '18', '31', '34', '33'], '14': ['30', '42', '43', '32', '24', '25', '26', '20', '21', '22', '23', '46', '47', '44', '45', '40', '1', '2', '5', '7', '6', '8', '11', '13', '15', '17', '16', '19', '49', '48'], '17': ['30', '42', '43', '32', '24', '25', '26', '20', '22', '23', '46', '47', '44', '45', '28', '40', '1', '5', '6', '9', '8', '15', '14', '16', '19', '18', '34'], '16': ['30', '43', '32', '24', '25', '26', '21', '22', '23', '46', '47', '28', '41', '1', '2', '5', '11', '12', '15', '14', '17', '19', '18', '31', '49', '33'], '19': ['42', '43', '24', '27', '20', '21', '22', '46', '47', '44', '45', '28', '29', '1', '5', '4', '7', '6', '9', '11', '10', '13', '14', '17', '16', '18', '31', '48'], '32': ['30', '43', '24', '25', '26', '20', '22', '23', '46', '47', '45', '29', '41', '2', '5', '8', '15', '14', '17', '16', '18', '31', '35', '34', '33'], '31': ['30', '32', '25', '27', '20', '21', '23', '47', '44', '45', '28', '29', '41', '1', '3', '2', '5', '7', '6', '9', '8', '11', '10', '13', '12', '15', '16', '19', '18', '33', '48'], '30': ['43', '32', '24', '25', '26', '21', '22', '23', '46', '47', '29', '41', '1', '3', '2', '5', '4', '9', '8', '11', '10', '13', '12', '15', '14', '17', '16', '18', '31', '49', '35', '33', '48'], '51': ['20', '50', '48'], '36': ['35', '34', '37'], '35': ['30', '36', '32', '25', '26', '41', '8', '15', '34', '33', '37'], '34': ['43', '36', '32', '24', '25', '26', '20', '22', '23', '46', '45', '5', '6', '15', '17', '35', '33', '37'], '33': ['30', '32', '25', '26', '21', '23', '45', '29', '41', '8', '15', '16', '18', '31', '35', '34'], '37': ['36', '38', '35', '34'], '18': ['30', '42', '32', '25', '27', '20', '21', '22', '23', '46', '44', '45', '28', '29', '41', '1', '3', '2', '5', '4', '7', '6', '9', '11', '10', '13', '12', '15', '17', '16', '19', '31', '33'], '50': ['49', '51']}, TheBrrrgh: {'42': ['43', '41', '39', '36'], '29': ['24', '25', '26', '27', '20', '22', '23', '28', '40', '1', '3', '2', '39', '38', '13', '15', '14', '17', '16', '19', '18', '30', '37', '36', '35'], '24': ['25', '26', '27', '22', '23', '28', '29', '40', '1', '3', '2', '5', '4', '39', '38', '13', '15', '14', '17', '16', '19', '18', '30', '37', '35', '32'], '25': ['24', '26', '27', '21', '22', '23', '28', '29', '40', '1', '3', '2', '5', '4', '7', '6', '8', '39', '38', '13', '15', '14', '17', '16', '18', '30', '37', '35', '32'], '26': ['24', '25', '27', '21', '22', '23', '28', '29', '40', '1', '3', '2', '5', '4', '7', '6', '8', '15', '14', '17', '16', '19', '18', '31', '30', '37', '35', '32'], '27': ['24', '25', '26', '21', '22', '23', '28', '29', '40', '1', '3', '2', '5', '4', '7', '6', '8', '15', '14', '17', '16', '18', '31', '30', '37', '32'], '20': ['21', '28', '29', '40', '3', '2', '39', '11', '10', '13', '12', '15', '14', '17', '16', '19', '18', '30', '34'], '21': ['25', '26', '27', '20', '22', '23', '1', '16', '37', '35'], '22': ['24', '25', '26', '27', '21', '23', '28', '29', '40', '1', '3', '2', '5', '4', '6', '39', '35', '32'], '23': ['24', '25', '26', '27', '21', '22', '28', '29', '40', '1', '3', '2', '5', '4', '6', '39', '13', '15', '14', '17', '18', '30', '37', '35', '32'], '46': ['45'], '44': ['45', '38', '36'], '45': ['46', '44', '38'], '28': ['24', '25', '26', '27', '20', '22', '23', '29', '40', '1', '3', '2', '5', '4', '7', '6', '39', '38', '15', '14', '17', '16', '19', '18', '30', '37', '36', '35', '32'], '43': ['42', '36'], '40': ['24', '25', '26', '27', '20', '22', '23', '28', '29', '1', '3', '2', '4', '7', '6', '9', '8', '39', '11', '10', '13', '12', '19', '18', '31', '37', '35', '33', '32'], '41': ['42', '39'], '1': ['24', '25', '26', '27', '21', '22', '23', '28', '29', '40', '3', '2', '5', '4', '7', '6', '9', '8', '10', '15', '17', '16', '19', '18', '31', '30', '37', '36', '35', '32'], '3': ['24', '25', '26', '27', '20', '22', '23', '28', '29', '40', '1', '2', '5', '4', '7', '6', '9', '8', '39', '11', '10', '12', '19', '18', '31', '37', '35', '33', '32'], '2': ['24', '25', '26', '27', '20', '23', '28', '29', '40', '1', '3', '5', '4', '7', '6', '9', '8', '11', '10', '17', '16', '19', '18', '31', '37', '35', '33', '32'], '5': ['24', '25', '26', '27', '22', '23', '28', '1', '3', '2', '4', '7', '6', '9', '8', '11', '12', '14', '31', '37', '34', '33', '32'], '4': ['24', '25', '26', '27', '22', '23', '28', '40', '1', '3', '2', '5', '7', '6', '9', '8', '11', '10', '13', '12', '31', '37', '35', '33', '32'], '7': ['25', '26', '27', '28', '40', '1', '3', '2', '5', '4', '6', '9', '8', '11', '10', '13', '12', '31', '37', '35', '33', '32'], '6': ['25', '26', '27', '22', '23', '28', '40', '1', '3', '2', '5', '4', '7', '9', '8', '11', '13', '12', '14', '31', '37', '35', '34', '33', '32'], '9': ['40', '1', '3', '2', '5', '4', '7', '6', '8', '11', '10', '13', '12', '15', '14', '16', '31', '35', '34', '33', '32'], '8': ['25', '26', '27', '40', '1', '3', '2', '5', '4', '7', '6', '9', '11', '10', '13', '12', '14', '31', '37', '35', '34', '33', '32'], '13': ['24', '25', '20', '23', '29', '40', '5', '4', '7', '6', '9', '8', '39', '38', '11', '10', '12', '15', '14', '17', '16', '19', '18', '31', '30', '37', '34', '33'], '12': ['20', '40', '3', '5', '4', '7', '6', '9', '8', '11', '10', '13', '15', '14', '17', '16', '19', '18', '31', '30', '34', '33'], '11': ['20', '40', '3', '2', '5', '4', '7', '6', '9', '8', '10', '13', '12', '15', '14', '17', '16', '19', '31', '35', '34', '33', '32'], '10': ['20', '40', '1', '3', '2', '4', '7', '9', '8', '11', '13', '12', '15', '14', '17', '16', '31', '35', '34', '33', '32'], '39': ['42', '24', '25', '20', '22', '23', '28', '29', '40', '41', '3', '13', '19', '18', '31', '32'], '38': ['24', '25', '44', '45', '28', '29', '8', '13', '15', '14', '17', '16', '18', '31', '30', '37', '32'], '15': ['24', '25', '26', '27', '20', '23', '28', '29', '1', '9', '38', '11', '10', '13', '12', '14', '17', '16', '19', '18', '30', '37', '36', '35', '34', '33'], '14': ['24', '25', '26', '27', '20', '23', '28', '29', '5', '6', '9', '8', '38', '11', '10', '13', '12', '15', '17', '16', '19', '18', '30', '37', '34', '33'], '17': ['24', '25', '26', '27', '20', '23', '28', '29', '1', '2', '38', '11', '10', '13', '12', '15', '14', '16', '19', '18', '30', '37', '36', '35', '34'], '16': ['24', '25', '26', '27', '20', '21', '28', '29', '1', '2', '9', '38', '11', '10', '13', '12', '15', '14', '17', '19', '18', '30', '37', '36', '35', '34', '33'], '19': ['24', '26', '20', '28', '29', '40', '1', '3', '2', '39', '11', '13', '12', '15', '14', '17', '16', '18', '30', '36', '35', '34', '32'], '18': ['24', '25', '26', '27', '20', '23', '28', '29', '40', '1', '3', '2', '39', '38', '13', '12', '15', '14', '17', '16', '19', '30', '37', '36', '35', '34', '32'], '31': ['26', '27', '40', '1', '3', '2', '5', '4', '7', '6', '9', '8', '39', '38', '11', '10', '13', '12', '37', '35', '33', '32'], '30': ['24', '25', '26', '27', '20', '23', '28', '29', '1', '38', '13', '12', '15', '14', '17', '16', '19', '18', '37', '36', '35', '34'], '37': ['24', '25', '26', '27', '21', '22', '23', '28', '29', '40', '1', '3', '2', '5', '4', '7', '6', '8', '38', '13', '15', '14', '17', '16', '18', '31', '30', '32'], '36': ['42', '43', '44', '28', '29', '1', '15', '17', '16', '19', '18', '30', '35'], '35': ['24', '26', '21', '22', '23', '28', '29', '40', '1', '3', '2', '4', '7', '6', '9', '8', '10', '15', '17', '16', '19', '18', '31', '30', '36', '32'], '34': ['20', '5', '6', '9', '8', '11', '10', '13', '12', '15', '14', '17', '16', '19', '18', '30', '33'], '33': ['40', '3', '2', '5', '4', '7', '6', '9', '8', '11', '10', '13', '12', '15', '14', '16', '31', '34', '32'], '32': ['24', '25', '26', '27', '22', '23', '28', '40', '1', '3', '2', '5', '4', '7', '6', '9', '8', '39', '11', '10', '19', '18', '31', '37', '35', '33']}, DonaldsDreamland: {'28': ['26', '27', '23', '46', '47', '29', '3', '5', '7', '6', '38', '16'], '29': ['46', '47', '28', '5', '7', '6', '9', '8', '38', '31', '30'], '24': ['25', '26', '47', '1', '3', '2', '5', '4', '7', '6', '8', '39', '19', '37'], '25': ['24', '26', '20', '23', '47', '1', '3', '2', '4', '7', '6', '39', '12', '19', '18', '37', '36'], '26': ['24', '25', '27', '46', '28', '3', '38', '16', '37', '36'], '27': ['26', '23', '46', '47', '28', '29', '3', '2', '5', '7', '6', '9', '8', '38'], '20': ['25', '21', '46', '47', '1', '3', '2', '5', '4', '7', '6', '39', '38', '14', '16', '19', '18'], '21': ['20', '22', '46', '47', '2', '5', '4', '7', '6', '39', '38', '10', '19'], '22': ['21', '23', '32'], '23': ['25', '26', '27', '22', '46', '28', '1', '3', '2', '5', '4', '6', '39'], '46': ['26', '27', '20', '21', '22', '23', '47', '28', '29', '40', '1', '3', '2', '5', '7', '6', '8', '39', '38', '16', '19', '18'], '47': ['24', '25', '27', '20', '21', '46', '28', '29', '1', '3', '2', '5', '4', '7', '6', '39', '38', '17', '18', '36', '34'], '44': ['43', '45'], '45': ['42', '44', '40'], '42': ['43', '45', '41'], '43': ['42', '44'], '40': ['23', '46', '45', '41', '1', '5', '39'], '41': ['42', '40'], '1': ['24', '25', '27', '20', '21', '23', '46', '47', '40', '3', '2', '5', '4', '7', '6', '39', '38', '19', '18', '34', '32'], '3': ['24', '25', '26', '27', '20', '23', '46', '47', '45', '28', '1', '2', '5', '4', '7', '6', '39', '19', '36'], '2': ['24', '25', '27', '20', '21', '23', '46', '47', '1', '3', '5', '4', '7', '6', '39', '38', '16', '19', '18', '36'], '5': ['24', '27', '20', '21', '23', '46', '47', '28', '29', '40', '1', '3', '2', '4', '7', '6', '8', '39', '38', '14', '19', '18', '36', '34'], '4': ['24', '25', '20', '21', '23', '47', '1', '3', '2', '5', '7', '6', '8', '39', '12', '14', '16', '19', '18', '36'], '7': ['24', '25', '27', '20', '21', '46', '47', '28', '29', '1', '3', '2', '5', '4', '6', '8', '39', '38', '36'], '6': ['24', '25', '27', '20', '21', '23', '46', '47', '28', '29', '1', '3', '2', '5', '4', '7', '39', '38', '36', '35', '33', '32'], '9': ['8', '11', '10', '12'], '8': ['24', '25', '27', '46', '28', '29', '3', '5', '4', '7', '6', '9', '39', '38', '11', '10', '12', '14', '30', '34', '33', '32'], '13': ['10', '12', '14'], '12': ['9', '8', '10', '13', '14'], '11': ['3', '4', '9', '8', '10', '13', '12', '14'], '10': ['9', '8', '11', '13', '12', '14'], '39': ['24', '25', '20', '21', '23', '46', '47', '40', '3', '2', '5', '4', '7', '6', '8', '38', '16', '19', '18', '36', '34', '33'], '38': ['26', '27', '20', '21', '46', '47', '28', '29', '1', '2', '5', '7', '6', '39', '11', '12', '14', '19', '18'], '15': ['14', '17', '16'], '14': ['9', '8', '11', '10', '13', '12', '15'], '17': ['47', '15', '16', '19', '18'], '16': ['26', '27', '20', '46', '2', '5', '4', '39', '38', '15'], '19': ['24', '25', '20', '21', '46', '47', '1', '3', '2', '5', '4', '39', '38', '17', '18', '32'], '18': ['25', '20', '46', '47', '1', '5', '4', '39', '38', '17', '16', '19'], '31': ['29', '30', '32'], '30': ['33', '32'], '37': ['24', '25', '26', '27', '36', '35'], '36': ['47', '2', '5', '4', '7', '6', '39', '35'], '35': ['37', '36', '34'], '34': ['35', '33'], '33': ['22', '34', '32'], '32': ['14', '30', '33']}, DonaldsDock: {'42': ['43', '40', '41', '39', '38', '37'], '29': ['27', '28', '33', '31', '30', '36', '34', '32'], '24': ['25', '26', '22', '23'], '25': ['24', '26', '22', '23'], '26': ['24', '25', '27', '22', '23', '34'], '27': ['28', '29', '33', '31', '30', '36', '34', '32'], '20': ['21', '22', '18'], '21': ['20', '22', '17', '18'], '22': ['24', '25', '26', '20', '21', '23', '15', '17', '16'], '23': ['24', '25', '26', '22', '17'], '44': ['43', '45'], '45': ['43', '44', '40', '1', '2', '39', '38', '37'], '28': ['27', '29', '33', '31', '30', '36', '34', '32'], '43': ['42', '44', '45', '40', '41', '39', '38', '37'], '40': ['42', '43', '41', '39', '38', '37'], '41': ['42', '43', '40', '39'], '1': ['45', '3', '2', '4'], '3': ['1', '2', '6'], '2': ['45', '1', '3'], '5': ['4', '6'], '4': ['1', '3', '5', '6', '9', '8', '10'], '7': ['6', '9', '8'], '6': ['5', '4', '7'], '9': ['4', '7', '8', '10'], '8': ['4', '7', '9', '10'], '13': ['11', '10', '12', '14'], '12': ['11', '10', '13', '14', '17', '16'], '11': ['10', '13', '12', '14', '17', '16'], '10': ['4', '9', '8', '11', '13', '12', '16'], '39': ['42', '43', '45', '40', '41', '38'], '38': ['42', '43', '40', '39', '37', '36'], '15': ['22', '14', '17', '16', '18'], '14': ['11', '12', '15'], '17': ['21', '22', '23', '15', '16', '18'], '16': ['22', '10', '12', '15', '17', '18'], '33': ['28', '29', '31', '30', '36', '35', '34', '32'], '18': ['20', '21', '13', '15', '17', '16'], '31': ['28', '29', '33', '30', '36', '35', '34', '32'], '30': ['27', '28', '29', '33', '31', '36', '34', '32'], '37': ['42', '43', '40', '38', '36', '34'], '36': ['26', '27', '28', '29', '38', '33', '31', '30', '37', '35'], '35': ['33', '31', '36', '34', '32'], '34': ['27', '28', '29', '33', '31', '30', '37', '35', '32'], '32': ['27', '28', '29', '33', '31', '30', '35', '34']}}
SuitPaths = [
 LPoint3f(17, -17, 0.5),
 LPoint3f(17.5, 7.6, 0.5),
 LPoint3f(85, 11.5, 0.5),
 LPoint3f(85, -13, 0.5),
 LPoint3f(-27.5, -5.25, 0.5),
 LPoint3f(-106.15, -4.0, 0.5),
 LPoint3f(-89.5, 93.5, 0.5),
 LPoint3f(-139.95, 1.69, 0.5),
 LPoint3f(-110.95, -68.57, 0.5),
 LPoint3f(70.0001, -1.90735e-06, 0.5),
 LPoint3f(35.0001, -1.90735e-06, 0.5),
 LPoint3f(52.5001, 19, 0.5),
 LPoint3f(52.5001, -19, 0.5),
 LPoint3f(-9.99991, 50, 0.5),
 LPoint3f(-9.99991, -50, 0.5),
 LPoint3f(-40.8999, -87.6, 0.5),
 LPoint3f(-40.8999, 87.6, 0.5),
 LPoint3f(-116.86, -50, 0.5),
 LPoint3f(-116.86, 50, 0.5),
 LPoint3f(-75.8099, 71.28, 0.5),
 LPoint3f(-75.8099, -71.28, 0.5),
 LPoint3f(-40.8999, 61.23, 0.5),
 LPoint3f(-40.8999, -61.23, 0.5),
 LPoint3f(-25.2999, 26.5, 0.5),
 LPoint3f(-25.2999, -26.5, 0.5)]
SuitNames = {'tightwad': 'Tightwad', 'moneybags': 'Money Bags', 
   'micromanager': 'Micromanager', 
   'gladhander': 'Glad Hander', 
   'flunky': 'Flunky', 
   'coldcaller': 'Cold Caller', 
   'ambulancechaser': 'Ambulance Chaser', 
   'beancounter': 'Bean Counter', 
   'loanshark': 'Loan Shark', 
   'movershaker': 'Mover & Shaker', 
   'pencilpusher': 'Pencil Pusher', 
   'telemarketer': 'Telemarketer', 
   'backstabber': 'Back Stabber', 
   'bigcheese': 'The Big Cheese', 
   'bigwig': 'Big Wig', 
   'headhunter': 'Head Hunter', 
   'legaleagle': 'Legal Eagle', 
   'numbercruncher': 'Number Cruncher', 
   'pennypincher': 'Penny Pincher', 
   'yesman': 'Yesman', 
   'twoface': 'Two-Face', 
   'bottomfeeder': 'Bottom Feeder', 
   'corporateraider': 'Corporate Raider', 
   'mrhollywood': 'Mr. Hollywood', 
   'robberbaron': 'Robber Baron', 
   'shortchange': 'Short Change', 
   'downsizer': 'Downsizer', 
   'bloodsucker': 'Bloodsucker', 
   'spindoctor': 'Spin Doctor', 
   'namedropper': 'Name Dropper', 
   'mingler': 'The Mingler', 
   'doubletalker': 'Double Talker', 
   'vp': 'Senior V.P'}
SuitSharedHeads = ['bottomfeeder',
 'corporateraider',
 'robberbaron',
 'coldcaller',
 'bloodsucker',
 'spindoctor',
 'namedropper',
 'mingler',
 'doubletalker']
SuitAttacks = ['canned',
 'clipontie',
 'sacked',
 'glowerpower',
 'playhardball',
 'marketcrash',
 'redtape',
 'pickpocket',
 'fountainpen',
 'hangup',
 'powertie']
MickeyPaths = {'a': Point3(17, -17, 4.025), 'b': Point3(17.5, 7.6, 4.025), 
   'c': Point3(85, 11.5, 4.025), 
   'd': Point3(85, -13, 4.025), 
   'e': Point3(-27.5, -5.25, 0.0), 
   'f': Point3(-106.15, -4.0, -2.5), 
   'g': Point3(-89.5, 93.5, 0.5), 
   'h': Point3(-139.95, 1.69, 0.5), 
   'i': Point3(-110.95, -68.57, 0.5)}
ShopGoodbye = 'See you later!'
ShopNoMoney = 'Sorry, you need more jellybeans to shop! Pickup jellybeans from fallen ' + Suits + ' or play minigames to get more.'
SharedChatterGreetings = ['Hi, %s!',
 'Yoo-hoo %s, nice to see you.',
 "I'm glad you're here today!",
 'Well, hello there, %s.']
SharedChatterComments = ["That's a great name, %s.",
 'I like your name.',
 'Watch out for the Cogs.',
 'Looks like the trolley is coming!',
 'I need to go to see Goofy to get some pies!',
 'Whew, I just stopped a bunch of Cogs. I need a rest!',
 'Yikes, some of those Cogs are big guys!',
 "You look like you're having fun.",
 "Oh boy, I'm having a good day.",
 "I like what you're wearing.",
 "I think I'll go fishing this afternoon.",
 'Have fun in my neighborhood.',
 'I hope you are enjoying your stay in Toontown!',
 "I heard it's snowing at the Brrrgh.",
 'Have you ridden the trolley today?',
 'I like to meet new people.',
 'Wow, there are lots of Cogs in the Brrrgh.',
 'I love to play tag. Do you?',
 'Trolley games are fun to play.',
 'I like to make people laugh.',
 "It's fun helping my friends.",
 "A-hem, are you lost?  Don't forget your map is in your Shticker Book.",
 'I hear Daisy has planted some new flowers in her garden.',
 'If you press the Ctrl key, you can jump!']
SharedChatterGoodbyes = ['I have to go now, bye!',
 "I think I'll go play a trolley game.",
 "Well, so long. I'll be seeing you, %s!",
 "I'd better hurry and get to work stopping those Cogs.",
 "It's time for me to get going.",
 'Sorry, but I have to go.',
 'Good-bye.',
 'See you later, %s!',
 "I think I'm going to go practice tossing cupcakes.",
 "I'm going to join a group and stop some Cogs.",
 'It was nice to see you today, %s.',
 "I have a lot to do today. I'd better get busy."]
MickeyChatter = ['Welcome to Toontown Central.', "Hi, my name is Mickey. What's yours?", 'Hey, have you seen Donald?',
 "I'm going to go watch the fog roll in at Donald's Dock.",
 'If you see my pal Goofy, say hi to him for me.',
 'I hear Daisy has planted some new flowers in her garden.', "I'm going to MelodyLand to see Minnie!",
 "Gosh, I'm late for my date with Minnie!",
 "Looks like it's time for Pluto's dinner!",
 "I think I'll go swimming at Donald's Dock.",
 "It's time for a nap. I'm going to Dreamland."]
MinnieChatter = ['Welcome to Melodyland.', "Hi, my name is Minnie. What's yours?", 'The hills are alive with the sound of music!',
 'You have a cool outfit, %s.',
 'Hey, have you seen Mickey?',
 'If you see my friend Goofy, say hi to him for me.',
 "Wow, there are lots of Cogs near Donald's Dreamland.",
 "I heard it's foggy at the Donald's Dock.",
 "Be sure and try the maze in Daisy Gardens.I think I'll go catch some tunes.",
 'Hey %s, look at that over there.',
 'I love the sound of music.',
 "I bet you didn't know Melodyland is also called TuneTown!  Hee Hee!",
 'I love to play the Matching Game. Do you?',
 'I like to make people giggle.',
 'Boy, trotting around in heels all day is hard on your feet!',
 'Nice shirt, %s.',
 'Is that a Jellybean on the ground?', "Gosh, I'm late for my date with Mickey!", "Looks like it's time for Pluto's dinner.", "It's time for a nap. I'm going to Dreamland."]
GoofySpeedwayChatter = [
 'Welcome to ' + ToontownCentral + '.', 'Hi, my name is ' + Goofy + ". What's yours?", "Gawrsh, it's nice to see you %s!", 'Boy, I saw a terrific race earlier.',
 'Watch out for banana peels on the race track!',
 'Have you upgraded your kart lately?',
 'We just got in some new rims at the kart shop.',
 'Hey, have you seen ' + Donald + '?',
 'If you see my friend ' + Mickey + ', say hi to him for me.',
 "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
 'Gawrsh there sure are a lot of ' + Suits + ' near ' + DonaldsDock + '.',
 'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 Jellybean!',
 "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
 "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your Jellybeans back!", "I'm going to Melody Land to see %s!" % Mickey,
 "Gosh, I'm late for my game with %s!" % Donald,
 "I think I'll go swimming at " + DonaldsDock + '.',
 "It's time for a nap. I'm going to Dreamland."]
WholeCreamPie = 'Whole Cream Pie'
WholeFruitPie = 'Whole Fruit Pie'
CreamPieSlice = 'Cream Pie Slice'
FruitPieSlice = 'Fruit Pie Slice'
BirthdayCake = 'Birthday Cake'
WeddingCake = 'Wedding Cake'
TNT = 'TNT'
SeltzerBottle = 'Seltzer Bottle'
GrandPiano = 'Grand Piano'
Safe = 'Safe'
BambooCane = 'Bamboo Cane'
JugglingBalls = 'Juggling Balls'
Megaphone = 'Megaphone'
Cupcake = 'Cupcake'
TrapDoor = 'Trap Door'
Quicksand = 'Quicksand'
BananaPeel = 'Banana Peel'
Lipstick = 'Lipstick'
Foghorn = 'Foghorn'
Aoogah = 'Aoogah'
ElephantHorn = 'Elephant Horn'
Opera = 'Opera Singer'
BikeHorn = 'Bike Horn'
Whistle = 'Whistle'
Bugle = 'Bugle'
PixieDust = 'Pixie Dust'
FlowerPot = 'Flower Pot'
Sandbag = 'Sandbag'
Anvil = 'Anvil'
Geyser = 'Geyser'
BigWeight = 'Big Weight'
StormCloud = 'Storm Cloud'
WaterGlass = 'Glass of Water'
FireHose = 'Fire Hose'
SquirtFlower = 'Squirting Flower'
WaterGun = 'Squirt Gun'
ToonHealJokes = [
 [
  'What goes TICK-TICK-TICK-WOOF?', 'A watchdog! '],
 [
  'Why do male deer need braces?', "Because they have 'buck teeth'!"],
 [
  'Why is it hard for a ghost to tell a lie?', 'Because you can see right through him.'],
 [
  'What did the ballerina do when she hurt her foot?', 'She called the toe truck!'],
 [
  'What has one horn and gives milk?', 'A milk truck!'],
 [
  "Why don't witches ride their brooms when they're angry?", "They don't want to fly off the handle!"],
 [
  'Why did the dolphin cross the ocean?', 'To get to the other tide.'],
 [
  'What kind of mistakes do spooks make?', 'Boo boos.'],
 [
  'Why did the chicken cross the playground?', 'To get to the other slide!'],
 [
  'Where does a peacock go when he loses his tail?', 'A retail store.'],
 [
  "Why didn't the skeleton cross the road?", "He didn't have the guts."],
 [
  "Why wouldn't they let the butterfly into the dance?", 'Because it was a moth ball.'],
 [
  "What's gray and squirts jam at you?", 'A mouse eating a doughnut.'],
 [
  'What happened when 500 hares got loose on the main street?', 'The police had to comb the area.'],
 [
  "What's the difference between a fish and a piano?", "You can tune a piano, but you can't tuna fish!"],
 [
  'What do people do in clock factories?', 'They make faces all day.'],
 [
  'What do you call a blind dinosaur?', "An I-don't-think-he-saurus."],
 [
  'If you drop a white hat into the Red Sea, what does it become?', 'Wet.'],
 [
  'Why was Cinderella thrown off the basketball team?', 'She ran away from the ball.'],
 [
  'Why was Cinderella such a bad player?', 'She had a pumpkin for a coach.'],
 [
  "What two things can't you have for breakfast?", 'Lunch and dinner.'],
 [
  'What do you give an elephant with big feet?', 'Big shoes.'],
 [
  'Where do baby ghosts go during the day?', 'Day-scare centers.'],
 [
  'What did Snow White say to the photographer?', 'Some day my prints will come.'],
 [
  "What's Tarzan's favorite song?", 'Jungle bells.'],
 [
  "What's green and loud?", 'A froghorn.'],
 [
  "What's worse than raining cats and dogs?", 'Hailing taxis.'],
 [
  'When is the vet busiest?', "When it's raining cats and dogs."],
 [
  'What do you call a gorilla wearing ear-muffs?', "Anything you want, he can't hear you."],
 [
  'Where would you weigh a whale?', 'At a whale-weigh station.'],
 [
  'What travels around the world but stays in the corner?', 'A stamp.'],
 [
  'What do you give a pig with a sore throat?', 'Oinkment.'],
 [
  'What did the hat say to the scarf?', 'You hang around while I go on a head.'],
 [
  "What's the best parting gift?", 'A comb.'],
 [
  'What kind of cats like to go bowling?', 'Alley cats.'],
 [
  "What's wrong if you keep seeing talking animals?", "You're having Disney spells."],
 [
  'What did one eye say to the other?', 'Between you and me, something smells.'],
 [
  "What's round, white and giggles?", 'A tickled onion.'],
 [
  'What do you get when you cross Bambi with a ghost?', 'Bamboo.'],
 [
  'Why do golfers take an extra pair of socks?', 'In case they get a hole in one.'],
 [
  'What do you call a fly with no wings?', 'A walk.'],
 [
  'Who did Frankenstein take to the prom?', 'His ghoul friend.'],
 [
  'What lies on its back, one hundred feet in the air?', 'A sleeping centipede.'],
 [
  'How do you keep a bull from charging?', 'Take away his credit card.'],
 [
  'What do you call a chicken at the North Pole?', 'Lost.'],
 [
  'What do you get if you cross a cat with a dog?', 'An animal that chases itself.'],
 [
  'What did the digital watch say to the grandfather clock?', 'Look dad, no hands.'],
 [
  'Where does Ariel the mermaid go to see movies?', 'The dive-in.'],
 [
  'What do you call a mosquito with a tin suit?', 'A bite in shining armor.'],
 [
  'What do giraffes have that no other animal has?', 'Baby giraffes.'],
 [
  'Why did the man hit the clock?', 'Because the clock struck first.'],
 [
  'Why did the apple go out with a fig?', "Because it couldn't find a date."],
 [
  'What do you get when you cross a parrot with a monster?', 'A creature that gets a cracker whenever it asks for one.'],
 [
  "Why didn't the monster make the football team?", 'Because he threw like a ghoul!'],
 [
  'What do you get if you cross a Cocker Spaniel with a Poodle and a rooster?', 'A cockapoodledoo!'],
 [
  'What goes dot-dot-dash-dash-squeak?', 'Mouse code.'],
 [
  "Why aren't elephants allowed on beaches?", "They can't keep their trunks up."],
 [
  'What is at the end of everything?', 'The letter G.'],
 [
  'How do trains hear?', 'Through the engineers.'],
 [
  'What does the winner of a marathon lose?', 'His breath.'],
 [
  'Why did the pelican refuse to pay for his meal?', 'His bill was too big.'],
 [
  'What has six eyes but cannot see?', 'Three blind mice.'],
 [
  "What works only when it's fired?", 'A rocket.'],
 [
  "Why wasn't there any food left after the monster party?", 'Because everyone was a goblin!'],
 [
  'What bird can be heard at mealtimes?', 'A swallow.'],
 [
  'What goes Oh, Oh, Oh?', 'Santa walking backwards.'],
 [
  'What has green hair and runs through the forest?', 'Moldy locks.'],
 [
  'Where do ghosts pick up their mail?', 'At the ghost office.'],
 [
  'Why do dinosaurs have long necks?', 'Because their feet smell.'],
 [
  'What do mermaids have on toast?', 'Mermarlade.'],
 [
  'Why do elephants never forget?', 'Because nobody ever tells them anything.'],
 [
  "What's in the middle of a jellyfish?", 'A jellybutton.'],
 [
  'What do you call a very popular perfume?', 'A best-smeller.'],
 [
  "Why can't you play jokes on snakes?", 'Because you can never pull their legs.'],
 [
  'Why did the baker stop making donuts?', 'He got sick of the hole business.'],
 [
  'Why do mummies make excellent spies?', "They're good at keeping things under wraps."],
 [
  'How do you stop an elephant from going through the eye of a needle?', 'Tie a knot in its tail.'],
 [
  "What goes 'Ha Ha Ha Thud'?", 'Someone laughing his head off.'],
 [
  "My friend thinks he's a rubber band.", 'I told him to snap out of it.'],
 [
  "My sister thinks she's a pair of curtains.", 'I told her to pull herself together!'],
 [
  'Did you hear about the dentist that married the manicurist?', 'Within a month they were fighting tooth and nail.'],
 [
  'Why do hummingbirds hum?', "Because they don't know the words."],
 [
  'Why did the baby turkey bolt down his food?', 'Because he was a little gobbler.'],
 [
  'Where did the whale go when it was bankrupt?', 'To the loan shark.'],
 [
  'How does a sick sheep feel?', 'Baah-aahd.'],
 [
  "What's gray, weighs 10 pounds and squeaks?", 'A mouse that needs to go on a diet.'],
 [
  'Why did the dog chase his tail?', 'To make ends meet.'],
 [
  'Why do elephants wear running shoes?', 'For jogging of course.'],
 [
  'Why are elephants big and gray?', "Because if they were small and yellow they'd be canaries."],
 [
  'If athletes get tennis elbow what do astronauts get?', 'Missile toe.'],
 [
  'Did you hear about the man who hated Santa?', 'He suffered from Claustrophobia.'],
 [
  'Why did ' + Donald + ' sprinkle sugar on his pillow?', 'Because he wanted to have sweet dreams.'],
 [
  'Why did ' + Goofy + ' take his comb to the dentist?', 'Because it had lost all its teeth.'],
 [
  'Why did ' + Goofy + ' wear his shirt in the bath?', 'Because the label said wash and wear.'],
 [
  'Why did the dirty chicken cross the road?', 'For some fowl purpose.'],
 [
  "Why didn't the skeleton go to the party?", 'He had no body to go with.'],
 [
  'Why did the burglar take a shower?', 'To make a clean getaway.'],
 [
  'Why does a sheep have a woolly coat?', "Because he'd look silly in a plastic one."],
 [
  'Why do potatoes argue all the time?', "They can't see eye to eye."],
 [
  'Why did ' + Pluto + ' sleep with a banana peel?', 'So he could slip out of bed in the morning.'],
 [
  'Why did the mouse wear brown sneakers?', 'His white ones were in the wash.'],
 [
  'Why are false teeth like stars?', 'They come out at night.'],
 [
  'Why are Saturday and Sunday so strong?', 'Because the others are weekdays.'],
 [
  'Why did the archaeologist go bankrupt?', 'Because his career was in ruins.'],
 [
  'What do you get if you cross the Atlantic on the Titanic?', 'Very wet.'],
 [
  'What do you get if you cross a chicken with cement?', 'A brick-layer.'],
 [
  'What do you get if you cross a dog with a phone?', 'A golden receiver.'],
 [
  'What do you get if you cross an elephant with a shark?', 'Swimming trunks with sharp teeth.'],
 [
  'What did the tablecloth say to the table?', "Don't move, I've got you covered."],
 [
  'Did you hear about the time ' + Goofy + ' ate a candle?', 'He wanted a light snack.'],
 [
  'What did the balloon say to the pin?', 'Hi Buster.'],
 [
  'What did the big chimney say to the little chimney?', "You're too young to smoke."],
 [
  'What did the carpet say to the floor?', 'I got you covered.'],
 [
  'What did the necklace say to the hat?', "You go ahead, I'll hang around."],
 [
  'What goes zzub-zzub?', 'A bee flying backwards.'],
 [
  'How do you communicate with a fish?', 'Drop him a line.'],
 [
  "What do you call a dinosaur that's never late?", 'A prontosaurus.'],
 [
  'What do you get if you cross a bear and a skunk?', 'Winnie-the-phew.'],
 [
  'How do you clean a tuba?', 'With a tuba toothpaste.'],
 [
  'What do frogs like to sit on?', 'Toadstools.'],
 [
  'Why was the math book unhappy?', 'It had too many problems.'],
 [
  'Why was the school clock punished?', 'It tocked too much.'],
 [
  "What's a polygon?", 'A dead parrot.'],
 [
  'What needs a bath and keeps crossing the street?', 'A dirty double crosser.'],
 [
  'What do you get if you cross a camera with a crocodile?', 'A snap shot.'],
 [
  'What do you get if you cross an elephant with a canary?', 'A very messy cage.'],
 [
  'What do you get if you cross a jeweler with a plumber?', 'A ring around the bathtub.'],
 [
  'What do you get if you cross an elephant with a crow?', 'Lots of broken telephone poles.'],
 [
  'What do you get if you cross a plum with a tiger?', 'A purple people eater.'],
 [
  "What's the best way to save water?", 'Dilute it.'],
 [
  "What's a lazy shoe called?", 'A loafer.'],
 [
  "What's green, noisy and dangerous?", 'A thundering herd of cucumbers.'],
 [
  'What color is a shout?', 'Yellow!'],
 [
  'What do you call a sick duck?', 'A mallardy.'],
 [
  "What's worse then a giraffe with a sore throat?", "A centipede with athlete's foot."],
 [
  'What goes ABC...slurp...DEF...slurp?', 'Someone eating alphabet soup.'],
 [
  "What's green and jumps up and down?", 'Lettuce at a dance.'],
 [
  "What's a cow after she gives birth?", 'De-calf-inated.'],
 [
  'What do you get if you cross a cow and a camel?', 'Lumpy milk shakes.'],
 [
  "What's white with black and red spots?", 'A Dalmatian with measles.'],
 [
  "What's brown has four legs and a trunk?", 'A mouse coming back from vacation.'],
 [
  "What does a skunk do when it's angry?", 'It raises a stink.'],
 [
  "What's gray, weighs 200 pounds and says, Here Kitty, kitty?", 'A 200 pound mouse.'],
 [
  "What's the best way to catch a squirrel?", 'Climb a tree and act like a nut.'],
 [
  "What's the best way to catch a rabbit?", 'Hide in a bush and make a noise like lettuce.'],
 [
  'What do you call a spider that just got married?', 'A newly web.'],
 [
  'What do you call a duck that robs banks?', 'A safe quacker.'],
 [
  "What's furry, meows and chases mice underwater?", 'A catfish.'],
 [
  "What's a funny egg called?", 'A practical yolker.'],
 [
  "What's green on the outside and yellow inside?", 'A banana disguised as a cucumber.'],
 [
  'What did the elephant say to the lemon?', "Let's play squash."],
 [
  'What weighs 4 tons, has a trunk and is bright red?', 'An embarrassed elephant.'],
 [
  "What's gray, weighs 4 tons, and wears glass slippers?", 'Cinderelephant.'],
 [
  "What's an elephant in a fridge called?", 'A very tight squeeze.'],
 [
  'What did the elephant say to her naughty child?', 'Tusk!  Tusk!'],
 [
  'What did the peanut say to the elephant?', "Nothing -- Peanuts can't talk."],
 [
  'What do elephants say when they bump into each other?', "Small world, isn't it?"],
 [
  'What did the cashier say to the register?', "I'm counting on you."],
 [
  'What did the flea say to the other flea?', 'Shall we walk or take the cat?'],
 [
  'What did the big hand say to the little hand?', 'Got a minute.'],
 [
  'What does the sea say to the sand?', 'Not much.  It usually waves.'],
 [
  'What did the stocking say to the shoe?', 'See you later, I gotta run.'],
 [
  'What did one tonsil say to the other tonsil?', 'It must be spring, here comes a swallow.'],
 [
  'What did the soil say to the rain?', 'Stop, or my name is mud.'],
 [
  'What did the puddle say to the rain?', 'Drop in sometime.'],
 [
  'What did the bee say to the rose?', 'Hi, bud.'],
 [
  'What did the appendix say to the kidney?', "The doctor's taking me out tonight."],
 [
  'What did the window say to the venetian blinds?', "If it wasn't for you it'd be curtains for me."],
 [
  'What did the doctor say to the sick orange?', 'Are you peeling well?'],
 [
  'What do you get if you cross a chicken with a banjo?', 'A self-plucking chicken.'],
 [
  'What do you get if you cross a hyena with a bouillon cube?', 'An animal that makes a laughing stock of itself.'],
 [
  'What do you get if you cross a rabbit with a spider?', 'A hare net.'],
 [
  'What do you get if you cross a germ with a comedian?', 'Sick jokes.'],
 [
  'What do you get if you cross a hyena with a mynah bird?', 'An animal that laughs at its own jokes.'],
 [
  'What do you get if you cross a railway engine with a stick of gum?', 'A chew-chew train.'],
 [
  'What would you get if you crossed an elephant with a computer?', 'A big know-it-all.'],
 [
  'What would you get if you crossed an elephant with a skunk?', 'A big stinker.'],
 [
  'Why did ' + MickeyMouse + ' take a trip to outer space?', 'He wanted to find ' + Pluto + '.']]
lToonHQ = 'Toon HQ'
Flippy = 'Flippy'
lHQOfficerF = 'HQ Officer'
lHQOfficerM = 'HQ Officer'
TutorialHQOfficerName = 'HQ Harry'
NPC_REGULAR = 0
NPC_CLERK = 1
NPC_TAILOR = 2
NPC_HQ = 3
NPC_BLOCKER = 4
NPC_FISHERMAN = 5
NPC_PETCLERK = 6
NPC_KARTCLERK = 7
NPC_PARTYPERSON = 8
NPC_SPECIALQUESTGIVER = 9
NPC_FLIPPYTOONHALL = 10
NPC_SCIENTIST = 11
NPC_SMART = 13
NPC_BANKER = 14
NPC_YIN = 15
NPC_YANG = 16
NPCToonNames = {20000: 'Tutorial Tom', 998: 'Talkative Tyler', 
   999: 'Toon Tailor', 
   1000: lToonHQ, 
   20001: Flippy, 
   20002: 'Tutorial Tom', 
   2001: Flippy, 
   2002: 'Banker Bob', 
   2003: 'Professor Pete', 
   2004: 'Tammy the Tailor', 
   2005: 'Librarian Larry', 
   2006: 'Clerk Clark', 
   2011: 'Clerk Clara', 
   2007: lHQOfficerM, 
   2008: lHQOfficerM, 
   2009: lHQOfficerF, 
   2010: lHQOfficerF, 
   2012: 'Fisherman Freddy', 
   2018: 'Duff..err..TIP Man', 
   2013: 'Clerk Poppy', 
   2014: 'Clerk Peppy', 
   2015: 'Clerk Pappy', 
   2016: 'Party Planner Pumpkin', 
   2017: 'Party Planner Polly', 
   2018: 'Doctor Surlee', 
   2019: 'Doctor Dimm', 
   2020: 'Professor Prepostera', 
   2021: 'Yin', 
   2022: 'Yang', 
   2101: 'Dentist Daniel', 
   2102: 'Sheriff Sherry', 
   2103: 'Sneezy Kitty', 
   2104: lHQOfficerM, 
   2105: lHQOfficerM, 
   2106: lHQOfficerF, 
   2107: lHQOfficerF, 
   2108: 'Dogity', 
   2109: 'Sir Babbles A Lot', 
   2110: 'Bill Board', 
   2111: 'Dancing Diego', 
   2112: 'Dr. Tom', 
   2113: 'Rollo The Amazing', 
   2114: 'Roz Berry', 
   2115: 'Patty Papercut', 
   2116: 'Bruiser McDougal', 
   2117: 'Ma Putrid', 
   2118: 'Jesse Jester', 
   2119: 'Honey Haha', 
   2120: 'Professor Binky', 
   2121: 'Madam Chuckle', 
   2122: 'Harry Ape', 
   2123: 'Spamonia Biggles', 
   2124: 'T.P. Rolle', 
   2125: 'Lazy Hal', 
   2126: 'Professor Guffaw', 
   2127: 'Woody Nickel', 
   2128: 'Loony Louis', 
   2129: 'Frank Furter', 
   2130: 'Joy Buzzer', 
   2131: 'Feather Duster', 
   2132: 'Daffy Don', 
   2133: 'Dr. Euphoric', 
   2134: 'Silent Simone', 
   2135: 'Mary', 
   2136: 'Sal Snicker', 
   2137: 'Happy Heikyung', 
   2138: 'Muldoon', 
   2139: 'Dan Dribbles', 
   2140: 'Fisherman Billy', 
   2201: 'Postmaster Pete', 
   2202: 'Shirley U. Jest', 
   2203: lHQOfficerM, 
   2204: lHQOfficerM, 
   2205: lHQOfficerF, 
   2206: lHQOfficerF, 
   2207: 'Will Wiseacre', 
   2208: 'Sticky Lou', 
   2209: 'Charlie Chortle', 
   2210: 'Tee Hee', 
   2211: 'Sally Spittake', 
   2212: 'Weird Warren', 
   2213: 'Lucy Tires', 
   2214: 'Sam Stain', 
   2215: 'Sid Seltzer', 
   2216: 'Nona Seeya', 
   2217: 'Sharky Jones', 
   2218: 'Fanny Pages', 
   2219: 'Chef Knucklehead', 
   2220: 'Rick Rockhead', 
   2221: 'Clovinia Cling', 
   2222: 'Shorty Fuse', 
   2223: 'Sasha Sidesplitter', 
   2224: 'Smokey Joe', 
   2225: 'Fisherman Droopy', 
   2301: 'Dr. Pulyurleg', 
   2302: 'Professor Wiggle', 
   2303: 'Nurse Nancy', 
   2304: lHQOfficerM, 
   2305: lHQOfficerM, 
   2306: lHQOfficerF, 
   2307: lHQOfficerF, 
   2308: 'Nancy Gas', 
   2309: 'Big Bruce', 
   2311: 'Franz Neckvein', 
   2312: 'Dr. Sensitive', 
   2313: 'Lucy Shirtspot', 
   2314: 'Ned Slinger', 
   2315: 'Chewy Morsel', 
   2316: 'Cindy Sprinkles', 
   2318: 'Tony Maroni', 
   2319: 'Zippy', 
   2320: 'Crunchy Alfredo', 
   2321: 'Fisherman Punchy', 
   2322: 'JJ', 
   1001: 'Clerk Will', 
   1002: 'Clerk Bill', 
   1003: lHQOfficerM, 
   1004: lHQOfficerF, 
   1005: lHQOfficerM, 
   1006: lHQOfficerF, 
   1007: 'Longjohn Leroy', 
   1008: 'Fisherman Furball', 
   1009: 'Clerk Barky', 
   1010: 'Clerk Purr', 
   1011: 'Clerk Bloop', 
   1012: 'Party Planner Pickles', 
   1013: 'Party Planner Patty', 
   1101: 'Billy Budd', 
   1102: 'Captain Carl', 
   1103: 'Fishy Frank', 
   1104: 'Doctor Squall', 
   1105: 'Admiral Hook', 
   1106: 'Mrs. Starch', 
   1107: 'Cal Estenicks', 
   1108: lHQOfficerM, 
   1109: lHQOfficerF, 
   1110: lHQOfficerM, 
   1111: lHQOfficerF, 
   1112: 'Gary Glubglub', 
   1113: 'Lisa Luff', 
   1114: 'Charlie Chum', 
   1115: 'Sheila Squid, Atty', 
   1116: 'Barnacle Bessie', 
   1117: 'Captain Yucks', 
   1118: 'Choppy McDougal', 
   1121: 'Linda Landlubber', 
   1122: 'Salty Stan', 
   1123: 'Electra Eel', 
   1124: 'Flappy Docksplinter', 
   1125: 'Eileen Overboard', 
   1126: 'Fisherman Barney', 
   1201: 'Barnacle Barbara', 
   1202: 'Art', 
   1203: 'Ahab', 
   1204: 'Rocky Shores', 
   1205: lHQOfficerM, 
   1206: lHQOfficerF, 
   1207: lHQOfficerM, 
   1208: lHQOfficerF, 
   1209: 'Professor Plank', 
   1210: 'Gang Wei', 
   1211: 'Wynn Bag', 
   1212: 'Toby Tonguestinger', 
   1213: 'Dante Dolphin', 
   1214: 'Gusty Kate', 
   1215: 'Dinah Down', 
   1216: 'Rod Reel', 
   1217: 'CC Weed', 
   1218: 'Pacific Tim', 
   1219: 'Brian Beachead', 
   1220: 'Carla Canal', 
   1221: 'Blisters McKee', 
   1222: 'Shep Ahoy', 
   1223: 'Sid Squid', 
   1224: 'Emily Eel', 
   1225: 'Bonzo Bilgepump', 
   1226: 'Heave Ho', 
   1227: 'Coral Reef', 
   1228: 'Fisherman Reed', 
   1301: 'Alice', 
   1302: 'Melville', 
   1303: 'Claggart', 
   1304: 'Svetlana', 
   1305: lHQOfficerM, 
   1306: lHQOfficerF, 
   1307: lHQOfficerM, 
   1308: lHQOfficerF, 
   1309: 'Seafoam', 
   1310: 'Ted Tackle', 
   1311: 'Topsy Turvey', 
   1312: 'Ethan Keel', 
   1313: 'William Wake', 
   1314: 'Rusty Ralph', 
   1315: 'Doctor Drift', 
   1316: 'Wilma Wobble', 
   1317: 'Paula Pylon', 
   1318: 'Dinghy Dan', 
   1319: 'Davey Drydock', 
   1320: 'Ted Calm', 
   1321: 'Dinah Docker', 
   1322: 'Whoopie Cushion', 
   1323: 'Stinky Ned', 
   1324: 'Pearl Diver', 
   1325: 'Ned Setter', 
   1326: 'Felicia Chips', 
   1327: 'Cindy Splat', 
   1328: 'Fred Flounder', 
   1329: 'Shelly Seaweed', 
   1330: 'Porter Hole', 
   1331: 'Rudy Rudder', 
   1332: 'Fisherman Shane', 
   3001: 'Betty Freezes', 
   3002: lHQOfficerM, 
   3003: lHQOfficerF, 
   3004: lHQOfficerM, 
   3005: lHQOfficerM, 
   3006: 'Clerk Lenny', 
   3007: 'Clerk Penny', 
   3008: 'Warren Bundles', 
   3009: 'Fisherman Frizzy', 
   3010: 'Clerk Skip', 
   3011: 'Clerk Dip', 
   3012: 'Clerk Kipp', 
   3013: 'Party Planner Pete', 
   3014: 'Party Planner Penny', 
   3101: 'Mr. Cow', 
   3102: 'Auntie Freeze', 
   3103: 'Fred', 
   3104: 'Bonnie', 
   3105: 'Frosty Freddy', 
   3106: 'Gus Gooseburger', 
   3107: 'Patty Passport', 
   3108: 'Toboggan Ted', 
   3109: 'Kate', 
   3110: 'Chicken Boy', 
   3111: 'Snooty Sinjin', 
   3112: 'Lil Oldman', 
   3113: 'Hysterical Harry', 
   3114: 'Henry the Hazard', 
   3115: lHQOfficerM, 
   3116: lHQOfficerF, 
   3117: lHQOfficerM, 
   3118: lHQOfficerM, 
   3119: 'Creepy Carl', 
   3120: 'Mike Mittens', 
   3121: 'Joe Shockit', 
   3122: 'Lucy Luge', 
   3123: 'Frank Lloyd Ice', 
   3124: 'Lance Iceberg', 
   3125: 'Colonel Crunchmouth', 
   3126: 'Colestra Awl', 
   3127: 'Ifalla Yufalla', 
   3128: 'Sticky George', 
   3129: 'Baker Bridget', 
   3130: 'Sandy', 
   3131: 'Lazy Lorenzo', 
   3132: 'Ashy', 
   3133: 'Dr. Friezeframe', 
   3134: 'Lounge Lassard', 
   3135: 'Soggy Nell', 
   3136: 'Happy Sue', 
   3137: 'Mr. Freeze', 
   3138: 'Chef Bumblesoup', 
   3139: 'Granny Icestockings', 
   3140: 'Fisherman Lucille', 
   3201: 'Aunt Arctic', 
   3202: 'Shakey', 
   3203: 'Walt', 
   3204: 'Dr. Ivanna Cee', 
   3205: 'Bumpy Noggin', 
   3206: 'Vidalia VaVoom', 
   3207: 'Dr. Mumbleface', 
   3208: 'Grumpy Phil', 
   3209: 'Giggles McGhee', 
   3210: 'Simian Sam', 
   3211: 'Fanny Freezes', 
   3212: 'Frosty Fred', 
   3213: lHQOfficerM, 
   3214: lHQOfficerF, 
   3215: lHQOfficerM, 
   3216: lHQOfficerM, 
   3217: 'Sweaty Pete', 
   3218: 'Blue Lou', 
   3219: 'Tom Tandemfrost', 
   3220: 'Mr. Sneeze', 
   3221: 'Nelly Snow', 
   3222: 'Mindy Windburn', 
   3223: 'Chappy', 
   3224: 'Freida Frostbite', 
   3225: 'Blake Ice', 
   3226: 'Santa Paws', 
   3227: 'Solar Ray', 
   3228: 'Wynne Chill', 
   3229: 'Hernia Belt', 
   3230: 'Balding Benjy', 
   3231: 'Choppy', 
   3232: 'Fisherman Albert', 
   3301: 'Paisley Patches', 
   3302: 'Bjorn Bord', 
   3303: 'Dr. Peepers', 
   3304: 'Eddie the Yeti', 
   3305: 'Mack Ramay', 
   3306: 'Paula Behr', 
   3307: 'Fisherman Fredrica', 
   3308: 'Donald Frump', 
   3309: 'Bootsy', 
   3310: 'Professor Flake', 
   3311: 'Connie Ferris', 
   3312: 'March Harry', 
   3313: lHQOfficerM, 
   3314: lHQOfficerF, 
   3315: lHQOfficerM, 
   3316: lHQOfficerF, 
   3317: 'Kissy Krissy', 
   3318: 'Johnny Cashmere', 
   3319: 'Sam Stetson', 
   3320: 'Fizzy Lizzy', 
   3321: 'Pickaxe Paul', 
   3322: 'Flue Lou', 
   3323: 'Dallas Borealis', 
   3324: 'Snaggletooth Stu', 
   3325: 'Groovy Garland', 
   3326: 'Blanche', 
   3327: 'Chuck Roast', 
   3328: 'Shady Sadie', 
   3329: 'Treading Ed', 
   4001: 'Molly Molloy', 
   4002: lHQOfficerM, 
   4003: lHQOfficerF, 
   4004: lHQOfficerF, 
   4005: lHQOfficerF, 
   4006: 'Clerk Doe', 
   4007: 'Clerk Ray', 
   4008: 'Tailor Harmony', 
   4009: 'Fisherman Fanny', 
   4010: 'Clerk Chris', 
   4011: 'Clerk Neil', 
   4012: 'Clerk Westin Girl', 
   4013: 'Party Planner Preston', 
   4014: 'Party Planner Penelope', 
   4101: 'Tom', 
   4102: 'Fifi', 
   4103: 'Dr. Fret', 
   4104: lHQOfficerM, 
   4105: lHQOfficerF, 
   4106: lHQOfficerF, 
   4107: lHQOfficerF, 
   4108: 'Cleff', 
   4109: 'Carlos', 
   4110: 'Metra Gnome', 
   4111: 'Tom Hum', 
   4112: 'Fa', 
   4113: 'Madam Manners', 
   4114: 'Offkey Eric', 
   4115: 'Barbara Seville', 
   4116: 'Piccolo', 
   4117: 'Mandy Lynn', 
   4118: 'Attendant Abe', 
   4119: 'Moe Zart', 
   4120: 'Viola Padding', 
   4121: 'Gee Minor', 
   4122: 'Minty Bass', 
   4123: 'Lightning Ted', 
   4124: 'Riff Raff', 
   4125: 'Melody Wavers', 
   4126: 'Mel Canto', 
   4127: 'Happy Feet', 
   4128: 'Luciano Scoop', 
   4129: 'Tootie Twostep', 
   4130: 'Metal Mike', 
   4131: 'Abraham Armoire', 
   4132: 'Lowdown Sally', 
   4133: 'Scott Poplin', 
   4134: 'Disco Dave', 
   4135: 'Sluggo Songbird', 
   4136: 'Patty Pause', 
   4137: 'Tony Deff', 
   4138: 'Cliff Cleff', 
   4139: 'Harmony Swell', 
   4140: 'Clumsy Ned', 
   4141: 'Fisherman Jed', 
   4201: 'Tina', 
   4202: 'Barry', 
   4203: 'Lumber Jack', 
   4204: lHQOfficerM, 
   4205: lHQOfficerF, 
   4206: lHQOfficerF, 
   4207: lHQOfficerF, 
   4208: 'Hedy', 
   4209: 'Corny Canter', 
   4211: 'Carl Concerto', 
   4212: 'Detective Dirge', 
   4213: 'Fran Foley', 
   4214: 'Tina Toehooks', 
   4215: 'Tim Tailgater', 
   4216: 'Gummy Whistle', 
   4217: 'Handsome Anton', 
   4218: 'Wilma Wind', 
   4219: 'Sid Sonata', 
   4220: 'Curtis Finger', 
   4221: 'Moe Madrigal', 
   4222: 'John Doe', 
   4223: 'Penny Prompter', 
   4224: 'Jungle Jim', 
   4225: 'Holly Hiss', 
   4226: 'Thelma Throatreacher', 
   4227: 'Quiet Francesca', 
   4228: 'August Winds', 
   4229: 'June Loon', 
   4230: 'Julius Wheezer', 
   4231: 'Steffi Squeezebox', 
   4232: 'Hedly Hymn', 
   4233: 'Charlie Carp', 
   4234: 'Leed Guitar', 
   4235: 'Fisherman Larry', 
   4301: 'Yuki', 
   4302: 'Anna', 
   4303: 'Leo', 
   4304: lHQOfficerM, 
   4305: lHQOfficerF, 
   4306: lHQOfficerF, 
   4307: lHQOfficerF, 
   4308: 'Tabitha', 
   4309: 'Marshall', 
   4310: 'Martha Mopp', 
   4311: 'Sea Shanty', 
   4312: 'Moe Saj', 
   4313: 'Dumb Dolph', 
   4314: 'Dana Dander', 
   4315: 'Karen Clockwork', 
   4316: 'Tim Tango', 
   4317: 'Stubby Toe', 
   4318: 'Bob Marlin', 
   4319: 'Rinky Dink', 
   4320: 'Cammy Coda', 
   4321: 'Luke Lute', 
   4322: 'Randy Rythm', 
   4323: 'Hanna Hogg', 
   4324: 'Ellie', 
   4325: 'Banker Bran', 
   4326: 'Fran Fret', 
   4327: 'Flim Flam', 
   4328: 'Wagner', 
   4329: 'Telly Prompter', 
   4330: 'Quentin', 
   4331: 'Mellow Costello', 
   4332: 'Ziggy', 
   4333: 'Harry', 
   4334: 'Fast Freddie', 
   4335: 'Fisherman Walden', 
   5001: lHQOfficerM, 
   5002: lHQOfficerM, 
   5003: lHQOfficerF, 
   5004: lHQOfficerF, 
   5005: 'Clerk Peaches', 
   5006: 'Clerk Herb', 
   5007: 'Bonnie Blossom', 
   5008: 'Fisherman Flora', 
   5009: 'Clerk Bo Tanny', 
   5010: 'Clerk Tom A. Dough', 
   5011: 'Clerk Doug Wood', 
   5012: 'Party Planner Pierce', 
   5013: 'Party Planner Peggy', 
   5101: 'Artie', 
   5102: 'Susan', 
   5103: 'Bud', 
   5104: 'Flutterby', 
   5105: 'Jack', 
   5106: 'Barber Bjorn', 
   5107: 'Postman Felipe', 
   5108: 'Innkeeper Janet', 
   5109: lHQOfficerM, 
   5110: lHQOfficerM, 
   5111: lHQOfficerF, 
   5112: lHQOfficerF, 
   5113: 'Dr. Spud', 
   5114: 'Wilt', 
   5115: 'Honey Dew', 
   5116: 'Vegetable Vern', 
   5117: 'Petal', 
   5118: 'Pop Corn', 
   5119: 'Barry Medly', 
   5120: 'Gopher', 
   5121: 'Paula Peapod', 
   5122: 'Leif Pyle', 
   5123: 'Diane Vine', 
   5124: 'Soggy Bottom', 
   5125: 'Sanjay Splash', 
   5126: 'Madam Mum', 
   5127: 'Polly Pollen', 
   5128: 'Shoshanna Sap', 
   5129: 'Fisherman Sally', 
   5201: 'Jake', 
   5202: 'Cynthia', 
   5203: 'Lisa', 
   5204: 'Bert', 
   5205: 'Dan D. Lion', 
   5206: 'Vine Green', 
   5207: 'Sofie Squirt', 
   5208: 'Samantha Spade', 
   5209: lHQOfficerM, 
   5210: lHQOfficerM, 
   5211: lHQOfficerF, 
   5212: lHQOfficerF, 
   5213: 'Big Galoot', 
   5214: 'Itchie Bumps', 
   5215: 'Tammy Tuber', 
   5216: 'Stinky Jim', 
   5217: 'Greg Greenethumb', 
   5218: 'Rocky Raspberry', 
   5219: 'Lars Bicep', 
   5220: 'Lacy Underalls', 
   5221: 'Pink Flamingo', 
   5222: 'Whiny Wilma', 
   5223: 'Wet Will', 
   5224: 'Uncle Bumpkin', 
   5225: 'Pamela Puddle', 
   5226: 'Pete Moss', 
   5227: 'Begonia Biddlesmore', 
   5228: 'Digger Mudhands', 
   5229: 'Fisherman Lily', 
   5301: lHQOfficerM, 
   5302: lHQOfficerM, 
   5303: lHQOfficerM, 
   5304: lHQOfficerM, 
   5305: 'Crystal', 
   5306: 'S. Cargo', 
   5307: 'Fun Gus', 
   5308: 'Naggy Nell', 
   5309: 'Ro Maine', 
   5310: 'Timothy', 
   5311: 'Judge McIntosh', 
   5312: 'Eugene', 
   5313: 'Coach Zucchini', 
   5314: 'Aunt Hill', 
   5315: 'Uncle Mud', 
   5316: 'Uncle Spud', 
   5317: 'Detective Lima', 
   5318: 'Caesar', 
   5319: 'Rose', 
   5320: 'April', 
   5321: 'Professor Ivy', 
   5322: 'Fisherman Rose', 
   8001: 'Graham Pree', 
   8002: 'Ivona Race', 
   8003: 'Anita Winn', 
   8004: 'Phil Errup', 
   9001: "Snoozin' Susan", 
   9002: 'Sleeping Tom', 
   9003: 'Drowsy Dennis', 
   9004: lHQOfficerF, 
   9005: lHQOfficerF, 
   9006: lHQOfficerM, 
   9007: lHQOfficerM, 
   9008: 'Clerk Jill', 
   9009: 'Clerk Phil', 
   9010: 'Worn Out Waylon', 
   9011: 'Fisherman Freud', 
   9012: 'Clerk Sarah Snuze', 
   9013: 'Clerk Kat Knap', 
   9014: 'Clerk R. V. Winkle', 
   9015: 'Party Planner Pebbles', 
   9016: 'Party Planner Pearl', 
   9101: 'Ed', 
   9102: 'Big Mama', 
   9103: 'P.J.', 
   9104: 'Sweet Slumber', 
   9105: 'Professor Yawn', 
   9106: 'Max', 
   9107: 'Snuggles', 
   9108: 'Winky Wilbur', 
   9109: 'Dreamy Daphne', 
   9110: 'Kathy Nip', 
   9111: 'Powers Erge', 
   9112: 'Lullaby Lou', 
   9113: 'Jacques Clock', 
   9114: 'Smudgy Mascara', 
   9115: 'Babyface MacDougal', 
   9116: 'Dances with Sheep', 
   9117: 'Afta Hours', 
   9118: 'Starry Knight', 
   9119: 'Rocco', 
   9120: 'Sarah Slumber', 
   9121: 'Serena Shortsheeter', 
   9122: 'Puffy Ayes', 
   9123: 'Teddy Blair', 
   9124: 'Nina Nitelight', 
   9125: 'Dr. Bleary', 
   9126: 'Wyda Wake', 
   9127: 'Tabby Tucker', 
   9128: "Hardy O'Toole", 
   9129: 'Bertha Bedhog', 
   9130: 'Charlie Chamberpot', 
   9131: 'Susan Siesta', 
   9132: lHQOfficerF, 
   9133: lHQOfficerF, 
   9134: lHQOfficerF, 
   9135: lHQOfficerF, 
   9136: 'Fisherman Taylor', 
   9201: 'Bernie', 
   9202: 'Orville', 
   9203: 'Nat', 
   9204: 'Claire de Loon', 
   9205: 'Zen Glen', 
   9206: 'Skinny Ginny', 
   9207: 'Jane Drain', 
   9208: 'Drowsy Dave', 
   9209: 'Dr. Floss', 
   9210: 'Master Mike', 
   9211: 'Dawn', 
   9212: 'Moonbeam', 
   9213: 'Rooster Rick', 
   9214: 'Dr. Blinky', 
   9215: 'Rip', 
   9216: 'Cat', 
   9217: 'Lawful Linda', 
   9218: 'Waltzing Matilda', 
   9219: 'The Countess', 
   9220: 'Grumpy Gordon', 
   9221: 'Zari', 
   9222: 'Cowboy George', 
   9223: 'Mark the Lark', 
   9224: 'Sandy Sandman', 
   9225: 'Fidgety Bridget', 
   9226: 'William Teller', 
   9227: 'Bed Head Ted', 
   9228: 'Whispering Willow', 
   9229: 'Rose Petals', 
   9230: 'Tex', 
   9231: 'Harry Hammock', 
   9232: 'Honey Moon', 
   9233: lHQOfficerM, 
   9234: lHQOfficerM, 
   9235: lHQOfficerM, 
   9236: lHQOfficerM, 
   9237: 'Fisherman Jung', 
   9301: 'Phil Bettur', 
   9302: 'Emma Phatic', 
   9303: 'GiggleMesh', 
   9304: 'Anne Ville', 
   9305: 'Bud Erfingerz', 
   9306: 'J.S. Bark', 
   9307: 'Bea Sharpe', 
   9308: 'Otto Toon', 
   9309: 'Al Capella', 
   9310: 'Des Traction', 
   9311: 'Dee Version', 
   9312: 'Bo Nanapeel', 
   7001: 'N. Prisoned', 
   7002: 'R.E. Leaseme', 
   7003: 'Lemmy Owte', 
   7004: 'T. Rapped', 
   7005: 'Little Helphere', 
   7006: 'Gimmy Ahand', 
   7007: 'Dewin Tymme', 
   7008: 'Ima Cagedtoon', 
   7009: 'Jimmy Thelock'}
zone2TitleDict = {2513: ('Toon Hall', ''), 2514: (
        'Toontown Bank', ''), 
   2516: (
        'Toontown School House', ''), 
   2518: (
        'Toontown Library', ''), 
   2519: (
        'Gag Shop', ''), 
   2520: (
        lToonHQ, ''), 
   2521: (
        'Clothing Shop', ''), 
   2522: (
        'Pet Shop', ''), 
   2601: (
        'All Smiles Tooth Repair', ''), 
   2602: (
        '', ''), 
   2603: (
        "It's Time To Read", ''), 
   2604: (
        'Hogwash & Dry', ''), 
   2605: (
        'Toontown Sign Factory', ''), 
   2606: (
        '', ''), 
   2607: (
        'Jumping Beans', ''), 
   2610: (
        'Dr. Tom Foolery', ''), 
   2611: (
        '', ''), 
   2616: (
        "Weird Beard's Disguise Shop", ''), 
   2617: (
        'Silly Stunts', ''), 
   2618: (
        'All That Razz', ''), 
   2621: (
        'Paper Airplanes', ''), 
   2624: (
        'Happy Hooligans', ''), 
   2625: (
        'House of Bad Pies', ''), 
   2626: (
        "Jesse's Joke Repair", ''), 
   2629: (
        "The Laughin' Place", ''), 
   2632: (
        'Clown Class', ''), 
   2633: (
        'Tee-Hee Tea Shop', ''), 
   2638: (
        'Toontown Playhouse', ''), 
   2639: (
        'Monkey Tricks', ''), 
   2643: (
        'Canned Bottles', ''), 
   2644: (
        'Impractical Jokes', ''), 
   2649: (
        'All Fun and Games Shop', ''), 
   2652: (
        '', ''), 
   2653: (
        "JJ's Diner", ''), 
   2654: (
        'Laughing Lessons', ''), 
   2655: (
        'Funny Money Savings & Loan', ''), 
   2656: (
        'Used Clown Cars', ''), 
   2657: (
        "Frank's Pranks", ''), 
   2659: (
        'Joy Buzzers to the World', ''), 
   2660: (
        'Tickle Machines', ''), 
   2661: (
        'Daffy Taffy', ''), 
   2662: (
        'Dr. I.M. Euphoric', ''), 
   2663: (
        'Toontown Cinerama', ''), 
   2664: (
        'The Merry Mimes', ''), 
   2665: (
        "Mary's Go Around Travel Company", ''), 
   2666: (
        'Laughing Gas Station', ''), 
   2667: (
        'Happy Times', ''), 
   2669: (
        "Muldoon's Maroon Balloons", ''), 
   2670: (
        'Soup Forks', ''), 
   2671: (
        '', ''), 
   2701: (
        '', ''), 
   2704: (
        'Movie Multiplex', ''), 
   2705: (
        "Wiseacre's Noisemakers", ''), 
   2708: (
        'Blue Glue', ''), 
   2711: (
        'Toontown Post Office', ''), 
   2712: (
        'Chortle Cafe', ''), 
   2713: (
        'Laughter Hours Cafe', ''), 
   2714: (
        'Kooky CinePlex', ''), 
   2716: (
        'Soup and Crack Ups', ''), 
   2717: (
        'Bottled Cans', ''), 
   2720: (
        'Crack Up Auto Repair', ''), 
   2725: (
        '', ''), 
   2727: (
        'Seltzer Bottles and Cans', ''), 
   2728: (
        'Vanishing Cream', ''), 
   2729: (
        '14 Karat Goldfish', ''), 
   2730: (
        'News for the Amused', ''), 
   2731: (
        '', ''), 
   2732: (
        'Spaghetti and Goofballs', ''), 
   2733: (
        'Cast Iron Kites', ''), 
   2734: (
        'Suction Cups and Saucers', ''), 
   2735: (
        'The Kaboomery', ''), 
   2739: (
        "Sidesplitter's Mending", ''), 
   2740: (
        'Used Firecrackers', ''), 
   2741: (
        '', ''), 
   2742: (
        '', ''), 
   2743: (
        'Ragtime Dry Cleaners', ''), 
   2744: (
        '', ''), 
   2747: (
        'Visible Ink', ''), 
   2748: (
        'Jest for Laughs', ''), 
   2801: (
        'Sofa Whoopee Cushions', ''), 
   2802: (
        'Inflatable Wrecking Balls', ''), 
   2803: (
        'The Karnival Kid', ''), 
   2804: (
        'Dr. Pulyurleg, Chiropractor', ''), 
   2805: (
        '', ''), 
   2809: (
        'The Punch Line Gym', ''), 
   2814: (
        'Toontown Theatre', ''), 
   2818: (
        'The Flying Pie', ''), 
   2821: (
        '', ''), 
   2822: (
        'Rubber Chicken Sandwiches', ''), 
   2823: (
        'Sundae Funnies Ice Cream', ''), 
   2824: (
        'Punchline Movie Palace', ''), 
   2829: (
        'Phony Baloney', ''), 
   2830: (
        "Zippy's Zingers", ''), 
   2831: (
        "Professor Wiggle's House of Giggles", ''), 
   2832: (
        '', ''), 
   2833: (
        '', ''), 
   2834: (
        'Funny Bone Emergency Room', ''), 
   2836: (
        '', ''), 
   2837: (
        'Hardy Harr Seminars', ''), 
   2839: (
        'Barely Palatable Pasta', ''), 
   2841: (
        '', ''), 
   1506: (
        'Gag Shop', ''), 
   1507: (
        'Toon Headquarters', ''), 
   1508: (
        'Clothing Shop', ''), 
   1510: (
        '', ''), 
   1602: (
        'Used Life Preservers', ''), 
   1604: (
        'Wet Suit Dry Cleaners', ''), 
   1606: (
        "Hook's Clock Repair", ''), 
   1608: (
        "Luff 'N Stuff", ''), 
   1609: (
        'Every Little Bait', ''), 
   1612: (
        'Dime & Quarterdeck Bank', ''), 
   1613: (
        'Squid Pro Quo, Attorneys at Law', ''), 
   1614: (
        'Trim the Nail Boutique', ''), 
   1615: (
        "Yacht's All, Folks!", ''), 
   1616: (
        "Blackbeard's Beauty Parlor", ''), 
   1617: (
        'Out to See Optics', ''), 
   1619: (
        'Disembark! Tree Surgeons', ''), 
   1620: (
        'From Fore to Aft', ''), 
   1621: (
        'Poop Deck Gym', ''), 
   1622: (
        'Bait and Switches Electrical Shop', ''), 
   1624: (
        'Soles Repaired While U Wait', ''), 
   1626: (
        'Salmon Chanted Evening Formal Wear', ''), 
   1627: (
        "Billy Budd's Big Bargain Binnacle Barn", ''), 
   1628: (
        'Piano Tuna', ''), 
   1629: (
        '', ''), 
   1701: (
        'Buoys and Gulls Nursery School', ''), 
   1703: (
        'Wok the Plank Chinese Food', ''), 
   1705: (
        'Sails for Sale', ''), 
   1706: (
        'Peanut Butter and Jellyfish', ''), 
   1707: (
        'Gifts With a Porpoise', ''), 
   1709: (
        'Windjammers and Jellies', ''), 
   1710: (
        'Barnacle Bargains', ''), 
   1711: (
        'Deep Sea Diner', ''), 
   1712: (
        'Able-Bodied Gym', ''), 
   1713: (
        "Art's Smart Chart Mart", ''), 
   1714: (
        "Reel 'Em Inn", ''), 
   1716: (
        'Mermaid Swimwear', ''), 
   1717: (
        'Be More Pacific Ocean Notions', ''), 
   1718: (
        'Run Aground Taxi Service', ''), 
   1719: (
        "Duck's Back Water Company", ''), 
   1720: (
        'The Reel Deal', ''), 
   1721: (
        'All For Nautical', ''), 
   1723: (
        "Squid's Seaweed", ''), 
   1724: (
        "That's  a Moray!", ''), 
   1725: (
        "Ahab's Prefab Sea Crab Center", ''), 
   1726: (
        'Root Beer Afloats', ''), 
   1727: (
        'This Oar That', ''), 
   1728: (
        'Good Luck Horseshoe Crabs', ''), 
   1729: (
        '', ''), 
   1802: (
        'Nautical But Nice', ''), 
   1804: (
        'Mussel Beach Gymnasium', ''), 
   1805: (
        'Tackle Box Lunches', ''), 
   1806: (
        'Cap Size Hat Store', ''), 
   1807: (
        'Keel Deals', ''), 
   1808: (
        'Knots So Fast', ''), 
   1809: (
        'Rusty Buckets', ''), 
   1810: (
        'Anchor Management', ''), 
   1811: (
        "What's Canoe With You?", ''), 
   1813: (
        'Pier Pressure Plumbing', ''), 
   1814: (
        'The Yo Ho Stop and Go', ''), 
   1815: (
        "What's Up, Dock?", ''), 
   1818: (
        'Seven Seas Cafe', ''), 
   1819: (
        "Docker's Diner", ''), 
   1820: (
        'Hook, Line, and Sinker Prank Shop', ''), 
   1821: (
        "King Neptoon's Cannery", ''), 
   1823: (
        'The Clam Bake Diner', ''), 
   1824: (
        'Dog Paddles', ''), 
   1825: (
        'Wholly Mackerel! Fish Market', ''), 
   1826: (
        "Claggart's Clever Clovis Closet", ''), 
   1828: (
        "Alice's Ballast Palace", ''), 
   1829: (
        'Seagull Statue Store', ''), 
   1830: (
        'Lost and Flounder', ''), 
   1831: (
        'Kelp Around the House', ''), 
   1832: (
        "Melville's Massive Mizzenmast Mart", ''), 
   1833: (
        'This Transom Man Custom Tailored Suits', ''), 
   1834: (
        'Rudderly Ridiculous!', ''), 
   1835: (
        '', ''), 
   4503: (
        'Gag Shop', ''), 
   4504: (
        'Toon Headquarters', ''), 
   4506: (
        'Clothing Shop', ''), 
   4508: (
        '', ''), 
   4603: (
        "Tom-Tom's Drums", ''), 
   4604: (
        'In Four-Four Time', ''), 
   4605: (
        "Fifi's Fiddles", ''), 
   4606: (
        'Casa De Castanets', ''), 
   4607: (
        'Catchy Toon Apparel', ''), 
   4609: (
        'Do, Rae, Me Piano Keys', ''), 
   4610: (
        'Please Refrain', ''), 
   4611: (
        'Tuning Forks and Spoons', ''), 
   4612: (
        "Dr. Fret's Dentistry", ''), 
   4614: (
        'Shave and a Haircut for a Song', ''), 
   4615: (
        "Piccolo's Pizza", ''), 
   4617: (
        'Happy Mandolins', ''), 
   4618: (
        'Rests Rooms', ''), 
   4619: (
        'More Scores', ''), 
   4622: (
        'Chin Rest Pillows', ''), 
   4623: (
        'Flats Sharpened', ''), 
   4625: (
        'Tuba Toothpaste', ''), 
   4626: (
        'Notations', ''), 
   4628: (
        'Accidental Insurance', ''), 
   4629: (
        "Riff's Paper Plates", ''), 
   4630: (
        'Music Is Our Forte', ''), 
   4631: (
        'Canto Help You', ''), 
   4632: (
        'Dance Around the Clock Shop', ''), 
   4635: (
        'Tenor Times', ''), 
   4637: (
        'For Good Measure', ''), 
   4638: (
        'Hard Rock Shop', ''), 
   4639: (
        'Four Score Antiques', ''), 
   4641: (
        'Blues News', ''), 
   4642: (
        'Ragtime Dry Cleaners', ''), 
   4645: (
        'Club 88', ''), 
   4646: (
        '', ''), 
   4648: (
        'Carry a Toon Movers', ''), 
   4649: (
        '', ''), 
   4652: (
        'Full Stop Shop', ''), 
   4653: (
        '', ''), 
   4654: (
        'Pitch Perfect Roofing', ''), 
   4655: (
        "The Treble Chef's Cooking School", ''), 
   4656: (
        '', ''), 
   4657: (
        'Barbershop Quartet', ''), 
   4658: (
        'Plummeting Pianos', ''), 
   4659: (
        '', ''), 
   4701: (
        'The Schmaltzy Waltz School of Dance', ''), 
   4702: (
        'Timbre! Equipment for the Singing Lumberjack', ''), 
   4703: (
        'I Can Handel It!', ''), 
   4704: (
        "Tina's Concertina Concerts", ''), 
   4705: (
        'Zither Here Nor There', ''), 
   4707: (
        "Doppler's Sound Effects Studio", ''), 
   4709: (
        'On Ballet! Climbing Supplies', ''), 
   4710: (
        'Hurry Up, Slow Polka! School of Driving', ''), 
   4712: (
        'C-Flat Tire Repair', ''), 
   4713: (
        'B-Sharp Fine Menswear', ''), 
   4716: (
        'Four-Part Harmonicas', ''), 
   4717: (
        'Sonata Your Fault! Discount Auto Insurance', ''), 
   4718: (
        'Chopin Blocks and Other Kitchen Supplies', ''), 
   4719: (
        'Madrigal Motor Homes', ''), 
   4720: (
        'Name That Toon', ''), 
   4722: (
        'Overture Understudies', ''), 
   4723: (
        'Haydn Go Seek Playground Supplies', ''), 
   4724: (
        'White Noise for Girls and Boys', ''), 
   4725: (
        'The Baritone Barber', ''), 
   4727: (
        'Vocal Chords Braided', ''), 
   4728: (
        "Sing Solo We Can't Hear You", ''), 
   4729: (
        'Double Reed Bookstore', ''), 
   4730: (
        'Lousy Lyrics', ''), 
   4731: (
        'Toon Tunes', ''), 
   4732: (
        'Etude Brute? Theatre Company', ''), 
   4733: (
        '', ''), 
   4734: (
        '', ''), 
   4735: (
        'Accordions, If You Want In, Just Bellow!', ''), 
   4736: (
        'Her and Hymn Wedding Planners', ''), 
   4737: (
        'Harp Tarps', ''), 
   4738: (
        'Canticle Your Fancy Gift Shop', ''), 
   4739: (
        '', ''), 
   4801: (
        "Marshall's Stacks", ''), 
   4803: (
        'What a Mezzo! Maid Service', ''), 
   4804: (
        'Mixolydian Scales', ''), 
   4807: (
        'Relax the Bach', ''), 
   4809: (
        "I Can't Understanza!", ''), 
   4812: (
        '', ''), 
   4817: (
        'The Ternary Pet Shop', ''), 
   4819: (
        "Yuki's Ukeleles", ''), 
   4820: (
        '', ''), 
   4821: (
        "Anna's Cruises", ''), 
   4827: (
        'Common Time Watches', ''), 
   4828: (
        "Schumann's Shoes for Men", ''), 
   4829: (
        "Pachelbel's Canonballs", ''), 
   4835: (
        'Ursatz for Kool Katz', ''), 
   4836: (
        'Reggae Regalia', ''), 
   4838: (
        'Kazoology School of Music', ''), 
   4840: (
        'Coda Pop Musical Beverages', ''), 
   4841: (
        'Lyre, Lyre, Pants on Fire!', ''), 
   4842: (
        'The Syncopation Corporation', ''), 
   4843: (
        '', ''), 
   4844: (
        'Con Moto Cycles', ''), 
   4845: (
        "Ellie's Elegant Elegies", ''), 
   4848: (
        'Lotsa Lute Savings & Loan', ''), 
   4849: (
        '', ''), 
   4850: (
        'The Borrowed Chord Pawn Shop', ''), 
   4852: (
        'Flowery Flute Fleeces', ''), 
   4853: (
        "Leo's Fenders", ''), 
   4854: (
        "Wagner's Vocational Violin Videos", ''), 
   4855: (
        'The Teli-Caster Network', ''), 
   4856: (
        '', ''), 
   4862: (
        "Quentin's Quintessen\x03tial Quadrilles", ''), 
   4867: (
        "Mr. Costello's Yellow Cellos", ''), 
   4868: (
        '', ''), 
   4870: (
        "Ziggy's Zoo of Zigeuner\x03musik", ''), 
   4871: (
        "Harry's House of Harmonious Humbuckers", ''), 
   4872: (
        "Fast Freddie's Fretless Fingerboards", ''), 
   4873: (
        '', ''), 
   5501: (
        'Gag Shop', ''), 
   5502: (
        lToonHQ, ''), 
   5503: (
        'Clothing Shop', ''), 
   5505: (
        '', ''), 
   5601: (
        'Eye of the Potato Optometry', ''), 
   5602: (
        "Artie Choke's Neckties", ''), 
   5603: (
        'Lettuce Alone', ''), 
   5604: (
        'Cantaloupe Bridal Shop', ''), 
   5605: (
        'Vege-tables and Chairs', ''), 
   5606: (
        'Petals', ''), 
   5607: (
        'Compost Office', ''), 
   5608: (
        'Mom and Pop Corn', ''), 
   5609: (
        'Berried Treasure', ''), 
   5610: (
        "Black-eyed Susan's Boxing Lessons", ''), 
   5611: (
        "Gopher's Gags", ''), 
   5613: (
        'Crop Top Barbers', ''), 
   5615: (
        "Bud's Bird Seed", ''), 
   5616: (
        'Dew Drop Inn', ''), 
   5617: (
        "Flutterby's Butterflies", ''), 
   5618: (
        "Peas and Q's", ''), 
   5619: (
        "Jack's Beanstalks", ''), 
   5620: (
        'Rake It Inn', ''), 
   5621: (
        'Grape Expectations', ''), 
   5622: (
        'Petal Pusher Bicycles', ''), 
   5623: (
        'Bubble Bird Baths', ''), 
   5624: (
        "Mum's the Word", ''), 
   5625: (
        'Leaf It Bees', ''), 
   5626: (
        'Pine Needle Crafts', ''), 
   5627: (
        '', ''), 
   5701: (
        'From Start to Spinach', ''), 
   5702: (
        "Jake's Rakes", ''), 
   5703: (
        "Photo Cynthia's Camera Shop", ''), 
   5704: (
        'Lisa Lemon Used Cars', ''), 
   5705: (
        'Poison Oak Furniture', ''), 
   5706: (
        '14 Carrot Jewelers', ''), 
   5707: (
        'Musical Fruit', ''), 
   5708: (
        "We'd Be Gone Travel Agency", ''), 
   5709: (
        'Astroturf Mowers', ''), 
   5710: (
        'Tuft Guy Gym', ''), 
   5711: (
        'Garden Hosiery', ''), 
   5712: (
        'Silly Statues', ''), 
   5713: (
        'Trowels and Tribulations', ''), 
   5714: (
        'Spring Rain Seltzer Bottles', ''), 
   5715: (
        'Hayseed News', ''), 
   5716: (
        'Take It or Leaf It Pawn Shop', ''), 
   5717: (
        'The Squirting Flower', ''), 
   5718: (
        'The Dandy Lion Exotic Pets', ''), 
   5719: (
        'Trellis the Truth! Private Investi\x03gators', ''), 
   5720: (
        'Vine and Dandy Menswear', ''), 
   5721: (
        'Root 66 Diner', ''), 
   5725: (
        'Barley, Hops, and Malt Shop', ''), 
   5726: (
        "Bert's Dirt", ''), 
   5727: (
        'Gopher Broke Savings & Loan', ''), 
   5728: (
        '', ''), 
   5802: (
        lToonHQ, ''), 
   5804: (
        'Just Vase It', ''), 
   5805: (
        'Snail Mail', ''), 
   5809: (
        'Fungi Clown School', ''), 
   5810: (
        'Honeydew This', ''), 
   5811: (
        'Lettuce Inn', ''), 
   5815: (
        'Grass Roots', ''), 
   5817: (
        'Apples and Oranges', ''), 
   5819: (
        'Green Bean Jeans', ''), 
   5821: (
        'Squash and Stretch Gym', ''), 
   5826: (
        'Ant Farming Supplies', ''), 
   5827: (
        'Dirt. Cheap.', ''), 
   5828: (
        'Couch Potato Furniture', ''), 
   5830: (
        'Spill the Beans', ''), 
   5833: (
        'The Salad Bar', ''), 
   5835: (
        'Flower Bed and Breakfast', ''), 
   5836: (
        "April's Showers and Tubs", ''), 
   5837: (
        'School of Vine Arts', ''), 
   9501: (
        'Lullaby Library', ''), 
   9503: (
        'The Snooze Bar', ''), 
   9504: (
        'Gag Shop', ''), 
   9505: (
        lToonHQ, ''), 
   9506: (
        'Clothing Shop', ''), 
   9508: (
        '', ''), 
   9601: (
        'Snuggle Inn', ''), 
   9602: (
        'Forty Winks for the Price of Twenty', ''), 
   9604: (
        "Ed's Red Bed Spreads", ''), 
   9605: (
        'Cloud Nine Design', ''), 
   9607: (
        "Big Mama's Bahama Pajamas", ''), 
   9608: (
        'Cat Nip for Cat Naps', ''), 
   9609: (
        'Deep Sleep for Cheap', ''), 
   9613: (
        'Clock Cleaners', ''), 
   9616: (
        'Lights Out Electric Co.', ''), 
   9617: (
        'Crib Notes - Music to Sleep By', ''), 
   9619: (
        'Relax to the Max', ''), 
   9620: (
        "PJ's Taxi Service", ''), 
   9622: (
        'Sleepy Time Pieces', ''), 
   9625: (
        'Curl Up Beauty Parlor', ''), 
   9626: (
        'Bed Time Stories', ''), 
   9627: (
        'The Sleepy Teepee', ''), 
   9628: (
        'Call It a Day Calendars', ''), 
   9629: (
        'Silver Lining Jewelers', ''), 
   9630: (
        'Rock to Sleep Quarry', ''), 
   9631: (
        'Down Time Watch Repair', ''), 
   9633: (
        'The Dreamland Screening Room', ''), 
   9634: (
        'Mind Over Mattress', ''), 
   9636: (
        'Insomniac Insurance', ''), 
   9639: (
        'House of Hibernation', ''), 
   9640: (
        'Nightstand Furniture Company', ''), 
   9642: (
        'Sawing Wood Slumber Lumber', ''), 
   9643: (
        'Shut-Eye Optometry', ''), 
   9644: (
        'Pillow Fights Nightly', ''), 
   9645: (
        'The All Tucked Inn', ''), 
   9647: (
        'Make Your Bed! Hardware Store', ''), 
   9649: (
        'Snore or Less', ''), 
   9650: (
        'Crack of Dawn Repairs', ''), 
   9651: (
        'For Richer or Snorer', ''), 
   9652: (
        '', ''), 
   9703: (
        'Fly By Night Travel Agency', ''), 
   9704: (
        'Night Owl Pet Shop', ''), 
   9705: (
        'Asleep At The Wheel Car Repair', ''), 
   9706: (
        'Tooth Fairy Dentistry', ''), 
   9707: (
        "Dawn's Yawn & Garden Center", ''), 
   9708: (
        'Bed Of Roses Florist', ''), 
   9709: (
        'Pipe Dream Plumbers', ''), 
   9710: (
        'REM Optometry', ''), 
   9711: (
        'Wake-Up Call Phone Company', ''), 
   9712: (
        "Counting Sheep - So You Don't Have To!", ''), 
   9713: (
        'Wynken, Blynken & Nod, Attorneys at Law', ''), 
   9714: (
        'Dreamboat Marine Supply', ''), 
   9715: (
        'First Security Blanket Bank', ''), 
   9716: (
        'Wet Blanket Party Planners', ''), 
   9717: (
        "Baker's Dozin' Doughnuts", ''), 
   9718: (
        "Sandman's Sandwiches", ''), 
   9719: (
        'Armadillo Pillow Company', ''), 
   9720: (
        'Talking In Your Sleep Voice Training', ''), 
   9721: (
        'Snug As A Bug Rug Dealer', ''), 
   9722: (
        'Dream On Talent Agency', ''), 
   9725: (
        "Cat's Pajamas", ''), 
   9727: (
        'You Snooze, You Lose', ''), 
   9736: (
        'Dream Jobs Employment Agency', ''), 
   9737: (
        "Waltzing Matilda's Dance School", ''), 
   9738: (
        'House of Zzzzzs', ''), 
   9740: (
        'Hit The Sack Fencing School', ''), 
   9741: (
        "Don't Let The Bed Bugs Bite Exterminators", ''), 
   9744: (
        "Rip Van Winkle's Wrinkle Cream", ''), 
   9752: (
        'Midnight Oil & Gas Company', ''), 
   9753: (
        "Moonbeam's Ice Creams", ''), 
   9754: (
        'Sleepless in the Saddle All Night Pony Rides', ''), 
   9755: (
        'Bedknobs & Broomsticks Movie House', ''), 
   9756: (
        '', ''), 
   9759: (
        'Sleeping Beauty Parlor', ''), 
   3507: (
        'Gag Shop', ''), 
   3508: (
        lToonHQ, ''), 
   3509: (
        'Clothing Shop', ''), 
   3511: (
        '', ''), 
   3601: (
        'Northern Lights Electric Company', ''), 
   3602: (
        "Nor'easter Bonnets", ''), 
   3605: (
        '', ''), 
   3607: (
        'The Blizzard Wizard', ''), 
   3608: (
        'Nothing to Luge', ''), 
   3610: (
        "Mike's Massive Mukluk Mart", ''), 
   3611: (
        "Mr. Cow's Snow Plows", ''), 
   3612: (
        'Igloo Design', ''), 
   3613: (
        'Ice Cycle Bikes', ''), 
   3614: (
        'Snowflakes Cereal Company', ''), 
   3615: (
        'Fried Baked Alaskas', ''), 
   3617: (
        'Cold Air Balloon Rides', ''), 
   3618: (
        'Snow Big Deal! Crisis Management', ''), 
   3620: (
        'Skiing Clinic', ''), 
   3621: (
        'The Melting Ice Cream Bar', ''), 
   3622: (
        '', ''), 
   3623: (
        'The Mostly Toasty Bread Company', ''), 
   3624: (
        'Subzero Sandwich Shop', ''), 
   3625: (
        "Auntie Freeze's Radiator Supply", ''), 
   3627: (
        'St. Bernard Kennel Club', ''), 
   3629: (
        'Pea Soup Cafe', ''), 
   3630: (
        'Icy London, Icy France Travel Agency', ''), 
   3634: (
        'Easy Chair Lifts', ''), 
   3635: (
        'Used Firewood', ''), 
   3636: (
        'Affordable Goosebumps', ''), 
   3637: (
        "Kate's Skates", ''), 
   3638: (
        'Toboggan or Not Toboggan', ''), 
   3641: (
        "Fred's Red Sled Beds", ''), 
   3642: (
        'Eye of the Storm Optics', ''), 
   3643: (
        'Snowball Hall', ''), 
   3644: (
        'Melted Ice Cubes', ''), 
   3647: (
        'The Sanguine Penguin Tuxedo Shop', ''), 
   3648: (
        'Instant Ice', ''), 
   3649: (
        'Hambrrrgers', ''), 
   3650: (
        'Antarctic Antiques', ''), 
   3651: (
        "Frosty Freddy's Frozen Frankfurters", ''), 
   3653: (
        'Ice House Jewelry', ''), 
   3654: (
        '', ''), 
   3702: (
        'Winter Storage', ''), 
   3703: (
        '', ''), 
   3705: (
        'Icicles Built for Two', ''), 
   3706: (
        "Shiverin' Shakes Malt Shop", ''), 
   3707: (
        'Snowplace Like Home', ''), 
   3708: (
        "Pluto's Place", ''), 
   3710: (
        'Dropping Degrees Diner', ''), 
   3711: (
        '', ''), 
   3712: (
        'Go With the Floe', ''), 
   3713: (
        'Chattering Teeth, Subzero Dentist', ''), 
   3715: (
        "Aunt Arctic's Soup Shop", ''), 
   3716: (
        'Road Salt and Pepper', ''), 
   3717: (
        'Juneau What I Mean?', ''), 
   3718: (
        'Designer Inner Tubes', ''), 
   3719: (
        'Ice Cube on a Stick', ''), 
   3721: (
        "Noggin's Toboggan Bargains", ''), 
   3722: (
        'Snow Bunny Ski Shop', ''), 
   3723: (
        "Shakey's Snow Globes", ''), 
   3724: (
        'The Chattering Chronicle', ''), 
   3725: (
        'You Sleigh Me', ''), 
   3726: (
        'Solar Powered Blankets', ''), 
   3728: (
        'Lowbrow Snowplows', ''), 
   3729: (
        '', ''), 
   3730: (
        'Snowmen Bought & Sold', ''), 
   3731: (
        'Portable Fireplaces', ''), 
   3732: (
        'The Frozen Nose', ''), 
   3734: (
        'Icy Fine, Do You? Optometry', ''), 
   3735: (
        'Polar Ice Caps', ''), 
   3736: (
        'Diced Ice at a Nice Price', ''), 
   3737: (
        'Downhill Diner', ''), 
   3738: (
        "Heat-Get It While It's Hot", ''), 
   3739: (
        '', ''), 
   3801: (
        'Toon HQ', ''), 
   3806: (
        'Alpine Chow Line', ''), 
   3807: (
        'Used Groundhog Shadows', ''), 
   3808: (
        'The Sweater Lodge', ''), 
   3809: (
        'Ice Saw It Too', ''), 
   3810: (
        'A Better Built Quilt', ''), 
   3811: (
        'Your Snow Angel', ''), 
   3812: (
        'Mittens for Kittens', ''), 
   3813: (
        "Snowshoes You Can't Refuse", ''), 
   3814: (
        'Malt in Your Mouth Soda Fountain', ''), 
   3815: (
        'The Toupee Chalet', ''), 
   3816: (
        'Just So Mistletoe', ''), 
   3817: (
        'Winter Wonderland Walking Club', ''), 
   3818: (
        'The Shovel Hovel', ''), 
   3819: (
        'Clean Sweep Chimney Service', ''), 
   3820: (
        'Snow Whitening', ''), 
   3821: (
        'Hibernation Vacations', ''), 
   3823: (
        'Precipitation Foundation', ''), 
   3824: (
        'Open Fire Chestnut Roasting', ''), 
   3825: (
        'Cool Cat Hats', ''), 
   3826: (
        'Oh My Galoshes!', ''), 
   3827: (
        'Choral Wreaths', ''), 
   3828: (
        "Snowman's Land", ''), 
   3829: (
        'Pinecone Zone', ''), 
   3830: (
        'Wait and See Goggle Defogging', '')}
NPCToonDict = {5120: (
        5611, NPCToonNames[5120], '00/03/02/22/00/22/02/22/01/01/01/03/03/19/00', 0), 
   5121: (
        5618, NPCToonNames[5121], '01/03/00/23/00/23/02/23/01/01/00/09/09/25/00', 0), 
   5123: (
        5621, NPCToonNames[5123], '01/07/01/07/03/07/01/07/01/01/25/11/11/00/00', 0), 
   5124: (
        5622, NPCToonNames[5124], '00/05/03/21/00/21/01/21/00/00/00/08/08/04/00', 0), 
   4101: (
        4603, NPCToonNames[4101], '00/00/03/16/01/16/01/16/01/01/00/07/07/06/00', 0), 
   4102: (
        4605, NPCToonNames[4102], '01/00/02/09/01/09/01/09/01/01/10/11/11/00/00', 0), 
   4103: (
        4612, NPCToonNames[4103], '00/00/01/02/02/02/02/02/01/01/00/08/08/19/00', 0), 
   4104: (
        4659, NPCToonNames[4104], '00/01/07/16/01/16/02/16/01/01/00/08/08/16/00', 3), 
   4105: (
        4659, NPCToonNames[4105], '01/01/04/09/02/09/02/09/01/01/11/21/21/00/00', 3), 
   4106: (
        4659, NPCToonNames[4106], '01/08/03/24/00/24/02/24/00/00/19/22/22/00/00', 3), 
   4107: (
        4659, NPCToonNames[4107], '01/08/02/16/04/16/02/16/00/00/17/22/22/00/00', 3), 
   4108: (
        4626, NPCToonNames[4108], '00/08/01/08/01/08/02/08/00/00/00/10/10/00/00', 0), 
   4109: (
        4606, NPCToonNames[4109], '00/03/03/22/00/22/02/22/00/00/00/11/11/18/00', 0), 
   4110: (
        4604, NPCToonNames[4110], '01/03/00/16/05/16/02/16/00/00/03/24/24/02/00', 0), 
   4112: (
        4609, NPCToonNames[4112], '01/07/01/24/01/24/02/24/00/00/11/25/25/00/00', 0), 
   4113: (
        4610, NPCToonNames[4113], '01/05/02/15/05/15/02/15/01/01/14/25/25/00/00', 0), 
   4114: (
        4611, NPCToonNames[4114], '00/05/00/07/01/07/02/07/01/01/01/11/11/20/00', 0), 
   4115: (
        4614, NPCToonNames[4115], '01/00/03/23/02/23/02/23/01/01/10/26/26/00/00', 0), 
   4116: (
        4615, NPCToonNames[4116], '00/00/02/15/00/15/01/15/01/01/01/12/12/14/00', 0), 
   4117: (
        4617, NPCToonNames[4117], '01/00/01/07/04/07/01/07/01/01/01/00/00/25/00', 0), 
   4119: (
        4619, NPCToonNames[4119], '00/01/04/14/00/14/01/14/00/00/01/00/00/01/00', 0), 
   4120: (
        4622, NPCToonNames[4120], '01/01/05/07/05/07/01/07/00/00/26/01/01/00/00', 0), 
   4121: (
        4623, NPCToonNames[4121], '00/08/02/21/01/21/01/21/00/00/01/01/01/16/00', 0), 
   4122: (
        4625, NPCToonNames[4122], '01/08/01/14/01/14/01/14/00/00/17/02/02/00/00', 0), 
   4123: (
        4628, NPCToonNames[4123], '00/03/03/06/02/06/01/06/00/00/01/02/02/10/00', 0), 
   4124: (
        4629, NPCToonNames[4124], '00/03/00/20/01/20/01/20/00/00/01/02/02/04/00', 0), 
   3101: (
        3611, NPCToonNames[3101], '00/07/01/16/02/16/02/16/01/01/01/01/01/06/00', 0), 
   3104: (
        3602, NPCToonNames[3104], '01/00/03/16/00/16/02/16/00/00/03/04/04/02/00', 0), 
   3106: (
        3636, NPCToonNames[3106], '00/08/03/08/02/08/02/08/10/00/07/00/00/11/02', 0), 
   3107: (
        3630, NPCToonNames[3107], '01/01/07/15/01/15/02/15/00/00/04/05/05/04/00', 0), 
   3109: (
        3637, NPCToonNames[3109], '01/08/03/23/03/23/01/23/01/01/12/06/06/00/00', 0), 
   3110: (
        3629, NPCToonNames[3110], '00/08/00/10/01/10/02/10/16/00/05/04/04/04/10', 0), 
   1201: (
        1710, NPCToonNames[1201], '01/00/00/12/02/12/00/12/00/00/01/00/00/24/00', 0), 
   3112: (
        3607, NPCToonNames[3112], '00/03/03/21/02/21/01/21/01/01/01/05/05/09/00', 0), 
   3113: (
        3618, NPCToonNames[3113], '00/03/00/14/01/14/01/14/01/01/00/05/05/02/00', 0), 
   3114: (
        3620, NPCToonNames[3114], '00/03/01/07/00/07/01/07/00/00/00/06/06/20/00', 0), 
   3115: (
        3654, NPCToonNames[3115], '00/07/01/21/02/21/01/21/00/00/00/07/07/17/00', 3), 
   3116: (
        3654, NPCToonNames[3116], '01/05/03/14/02/14/01/14/00/00/00/11/11/12/00', 3), 
   3117: (
        3654, NPCToonNames[3117], '00/05/00/06/00/06/01/06/00/00/00/07/07/11/00', 3), 
   3118: (
        3654, NPCToonNames[3118], '00/00/03/20/02/20/01/20/00/00/00/08/08/06/00', 3), 
   3119: (
        3653, NPCToonNames[3119], '00/00/02/14/01/14/01/14/00/00/00/08/08/01/00', 0), 
   3120: (
        3610, NPCToonNames[3120], '00/00/01/06/00/06/01/06/01/01/00/08/08/19/00', 0), 
   3121: (
        3601, NPCToonNames[3121], '00/01/07/20/02/20/01/20/01/01/00/08/08/16/00', 0), 
   3122: (
        3608, NPCToonNames[3122], '01/01/04/13/04/13/02/13/01/01/10/21/21/00/00', 0), 
   3123: (
        3612, NPCToonNames[3123], '00/01/05/06/01/06/02/06/01/01/00/09/09/10/00', 0), 
   3124: (
        3613, NPCToonNames[3124], '00/08/02/20/00/20/02/20/01/01/00/09/09/04/00', 0), 
   2101: (
        2601, NPCToonNames[2101], '00/03/03/15/01/15/02/15/00/00/00/09/09/06/00', 0), 
   2103: (
        2616, NPCToonNames[2103], '00/00/02/05/00/09/00/08/00/00/02/11/11/10/00', 0), 
   2104: (
        2671, NPCToonNames[2104], '00/07/01/15/01/15/01/15/01/01/00/10/10/16/00', 3), 
   2105: (
        2671, NPCToonNames[2105], '00/05/02/07/00/07/01/07/01/01/00/10/10/13/00', 3), 
   2106: (
        2671, NPCToonNames[2106], '01/05/00/23/05/23/01/23/01/01/24/23/23/00/00', 3), 
   2107: (
        2671, NPCToonNames[2107], '01/00/03/14/03/14/01/14/01/01/07/24/24/04/00', 3), 
   2108: (
        2603, NPCToonNames[2108], '00/01/04/14/02/18/01/14/01/01/00/02/02/06/00', 0), 
   2110: (
        2605, NPCToonNames[2110], '00/01/07/14/02/14/01/14/00/00/00/00/00/15/00', 0), 
   2112: (
        2610, NPCToonNames[2112], '00/08/03/20/00/20/01/20/00/00/00/00/00/09/00', 0), 
   2113: (
        2617, NPCToonNames[2113], '00/08/02/14/02/14/01/14/00/00/00/00/00/02/00', 0), 
   2114: (
        2618, NPCToonNames[2114], '01/08/01/06/03/06/01/06/00/00/23/00/00/00/00', 0), 
   2115: (
        2621, NPCToonNames[2115], '01/03/03/22/01/22/02/22/01/01/26/01/01/00/00', 0), 
   2116: (
        2624, NPCToonNames[2116], '00/03/00/13/02/13/02/13/01/01/01/01/01/14/00', 0), 
   2117: (
        2625, NPCToonNames[2117], '01/03/01/06/03/06/02/06/01/01/25/02/02/00/00', 0), 
   2118: (
        2626, NPCToonNames[2118], '00/07/01/20/00/20/02/20/01/01/01/01/01/06/00', 0), 
   2119: (
        2629, NPCToonNames[2119], '01/05/03/13/00/13/02/13/01/01/19/03/03/00/00', 0), 
   2120: (
        2632, NPCToonNames[2120], '00/05/00/05/02/05/02/05/01/01/01/02/02/19/00', 0), 
   2121: (
        2633, NPCToonNames[2121], '01/00/03/21/02/21/02/21/00/00/04/04/04/04/00', 0), 
   2122: (
        2639, NPCToonNames[2122], '00/00/02/13/00/13/02/13/00/00/01/03/03/13/00', 0), 
   2123: (
        2643, NPCToonNames[2123], '01/00/01/04/04/04/02/04/00/00/14/05/05/00/00', 0), 
   2124: (
        2644, NPCToonNames[2124], '01/01/07/21/03/21/02/21/00/00/08/05/05/21/00', 0), 
   2125: (
        2649, NPCToonNames[2125], '00/01/04/12/00/12/02/12/00/00/01/04/04/00/00', 0), 
   2126: (
        2654, NPCToonNames[2126], '01/01/05/04/05/04/02/04/00/00/03/06/06/07/00', 0), 
   2127: (
        2655, NPCToonNames[2127], '00/08/02/19/01/19/02/19/00/00/01/05/05/15/00', 0), 
   2128: (
        2656, NPCToonNames[2128], '00/08/00/12/00/12/02/12/01/01/01/05/05/12/00', 0), 
   2129: (
        2657, NPCToonNames[2129], '00/03/03/04/00/04/02/04/01/01/01/05/05/09/00', 0), 
   2130: (
        2659, NPCToonNames[2130], '01/03/00/19/04/19/02/19/01/01/07/08/08/07/00', 0), 
   2131: (
        2660, NPCToonNames[2131], '01/03/01/12/02/12/02/12/01/01/01/08/08/26/00', 0), 
   2132: (
        2661, NPCToonNames[2132], '00/07/01/04/00/04/02/04/01/01/01/06/06/17/00', 0), 
   2133: (
        2662, NPCToonNames[2133], '00/05/03/18/02/18/02/18/01/01/01/06/06/14/00', 0), 
   2135: (
        2665, NPCToonNames[2135], '01/05/01/03/01/03/02/03/00/00/02/12/12/26/00', 0), 
   2136: (
        2666, NPCToonNames[2136], '00/00/02/18/02/18/02/18/00/00/01/08/08/01/00', 0), 
   2137: (
        2667, NPCToonNames[2137], '01/00/00/11/03/11/02/11/00/00/24/21/21/00/00', 0), 
   2138: (
        2669, NPCToonNames[2138], '00/01/07/03/00/03/02/03/00/00/01/09/09/16/00', 0), 
   2140: (
        2156, NPCToonNames[2140], '00/01/05/10/02/10/02/10/01/01/01/09/09/10/00', 5), 
   1117: (
        1615, NPCToonNames[1117], '00/08/01/05/00/05/02/05/00/00/01/09/09/12/00', 0), 
   1118: (
        1616, NPCToonNames[1118], '00/03/03/19/02/19/02/19/00/00/01/09/09/09/00', 0), 
   5216: (
        5707, NPCToonNames[5216], '00/00/03/13/00/13/02/13/00/00/01/02/02/01/00', 0), 
   1122: (
        1620, NPCToonNames[1122], '00/05/03/12/01/12/02/12/00/00/00/11/11/14/00', 0), 
   1123: (
        1622, NPCToonNames[1123], '01/05/00/04/01/04/02/04/01/01/23/23/23/00/00', 0), 
   1124: (
        1624, NPCToonNames[1124], '00/00/03/19/02/19/02/19/01/01/00/11/11/06/00', 0), 
   1125: (
        1628, NPCToonNames[1125], '01/00/02/12/03/12/02/12/01/01/25/24/24/00/00', 0), 
   1126: (
        1129, NPCToonNames[1126], '00/00/01/04/01/04/02/04/01/01/00/11/11/19/00', 5), 
   5223: (
        5714, NPCToonNames[5223], '00/08/01/05/00/05/00/05/01/01/01/04/04/18/00', 0), 
   5224: (
        5715, NPCToonNames[5224], '00/03/03/19/02/19/00/19/01/01/01/05/05/15/00', 0), 
   4201: (
        4704, NPCToonNames[4201], '01/07/00/14/00/14/02/14/00/00/11/06/06/00/00', 0), 
   4202: (
        4725, NPCToonNames[4202], '00/07/01/06/02/06/02/06/00/00/00/05/05/13/00', 0), 
   4203: (
        4702, NPCToonNames[4203], '00/05/02/21/01/21/02/21/00/00/00/05/05/10/00', 0), 
   4204: (
        4739, NPCToonNames[4204], '00/05/00/14/00/14/02/14/00/00/00/06/06/04/00', 3), 
   4205: (
        4739, NPCToonNames[4205], '01/00/03/06/05/06/02/06/01/01/10/08/08/00/00', 3), 
   4206: (
        4739, NPCToonNames[4206], '01/00/00/22/03/22/02/22/01/01/25/08/08/00/00', 3), 
   4207: (
        4739, NPCToonNames[4207], '01/00/01/14/02/14/02/14/01/01/17/09/09/00/00', 3), 
   4208: (
        4730, NPCToonNames[4208], '01/01/06/06/00/06/02/06/01/01/10/09/09/00/00', 0), 
   4209: (
        4701, NPCToonNames[4209], '01/01/04/22/04/22/02/22/01/01/01/11/11/09/00', 0), 
   4211: (
        4703, NPCToonNames[4211], '00/08/02/05/00/05/02/05/01/01/00/08/08/20/00', 0), 
   4212: (
        4705, NPCToonNames[4212], '00/08/01/20/02/20/02/20/00/00/00/09/09/17/00', 0), 
   4213: (
        4707, NPCToonNames[4213], '01/03/03/13/03/13/02/13/00/00/24/21/21/00/00', 0), 
   4215: (
        4710, NPCToonNames[4215], '00/07/00/19/02/19/02/19/00/00/00/10/10/06/00', 0), 
   4216: (
        4712, NPCToonNames[4216], '00/07/01/13/01/13/00/13/00/00/00/10/10/01/00', 0), 
   4217: (
        4713, NPCToonNames[4217], '00/05/02/05/01/05/00/05/00/00/00/10/10/19/00', 0), 
   4218: (
        4716, NPCToonNames[4218], '01/05/00/21/00/21/00/21/01/01/26/23/23/00/00', 0), 
   4221: (
        4719, NPCToonNames[4221], '00/00/01/19/00/19/00/19/01/01/00/11/11/04/00', 0), 
   4222: (
        4720, NPCToonNames[4222], '00/01/06/12/02/12/00/12/01/01/00/11/11/00/00', 0), 
   4223: (
        4722, NPCToonNames[4223], '01/01/04/03/03/03/00/03/01/01/24/25/25/00/00', 0), 
   3202: (
        3723, NPCToonNames[3202], '00/03/02/06/00/06/02/06/01/01/01/12/12/13/00', 0), 
   3203: (
        3712, NPCToonNames[3203], '00/03/00/20/02/20/02/20/01/01/01/12/12/10/00', 0), 
   3204: (
        3734, NPCToonNames[3204], '01/07/00/13/04/13/02/13/01/01/04/26/26/05/00', 0), 
   3206: (
        3722, NPCToonNames[3206], '01/05/02/21/00/21/02/21/01/01/11/00/00/00/00', 0), 
   3207: (
        3713, NPCToonNames[3207], '00/05/00/13/02/13/02/13/00/00/01/00/00/15/00', 0), 
   3208: (
        3732, NPCToonNames[3208], '00/00/03/05/01/05/02/05/00/00/01/01/01/12/00', 0), 
   3209: (
        3737, NPCToonNames[3209], '00/00/00/19/00/19/02/19/00/00/01/01/01/09/00', 0), 
   3210: (
        3728, NPCToonNames[3210], '00/04/01/13/02/13/00/13/02/02/05/01/01/02/00', 0), 
   3212: (
        3707, NPCToonNames[3212], '00/01/04/19/00/19/00/19/00/00/01/02/02/17/00', 0), 
   3213: (
        3739, NPCToonNames[3213], '00/08/03/12/02/12/00/12/01/01/01/02/02/14/00', 3), 
   3214: (
        3739, NPCToonNames[3214], '01/08/02/04/04/04/00/04/01/01/03/04/04/01/00', 3), 
   3215: (
        3739, NPCToonNames[3215], '00/08/01/19/01/19/00/19/01/01/01/03/03/06/00', 3), 
   3216: (
        3739, NPCToonNames[3216], '00/03/03/12/00/12/00/12/01/01/01/04/04/01/00', 3), 
   3217: (
        3738, NPCToonNames[3217], '00/03/00/04/02/04/00/04/01/01/01/04/04/19/00', 0), 
   3218: (
        3702, NPCToonNames[3218], '00/07/00/18/01/18/00/18/01/01/01/04/04/16/00', 0), 
   3219: (
        3705, NPCToonNames[3219], '00/07/01/12/00/12/00/12/00/00/01/05/05/13/00', 0), 
   3220: (
        3706, NPCToonNames[3220], '00/05/02/04/02/04/00/04/00/00/01/05/05/10/00', 0), 
   3221: (
        3708, NPCToonNames[3221], '01/05/00/19/03/19/00/19/00/00/07/08/08/12/00', 0), 
   3223: (
        3718, NPCToonNames[3223], '00/00/02/04/02/04/01/04/00/00/01/06/06/18/00', 0), 
   3224: (
        3719, NPCToonNames[3224], '01/00/01/18/04/18/01/18/00/00/17/09/09/00/00', 0), 
   2201: (
        2711, NPCToonNames[2201], '00/01/04/13/00/13/02/13/01/01/00/06/06/17/00', 0), 
   2203: (
        2742, NPCToonNames[2203], '00/08/00/19/01/19/00/19/00/00/00/07/07/11/00', 3), 
   2204: (
        2742, NPCToonNames[2204], '00/08/01/13/00/13/00/13/00/00/00/07/07/06/00', 3), 
   2205: (
        2742, NPCToonNames[2205], '01/03/02/04/04/04/00/04/00/00/16/11/11/00/00', 3), 
   2206: (
        2742, NPCToonNames[2206], '01/03/00/21/03/21/00/21/00/00/00/12/12/08/00', 3), 
   2207: (
        2705, NPCToonNames[2207], '00/07/00/12/00/12/00/12/00/00/00/08/08/16/00', 0), 
   2208: (
        2708, NPCToonNames[2208], '00/07/01/04/02/04/00/04/01/01/00/08/08/13/00', 0), 
   2209: (
        2712, NPCToonNames[2209], '00/05/02/19/01/19/00/19/01/01/00/08/08/10/00', 0), 
   2210: (
        2713, NPCToonNames[2210], '01/05/00/12/01/12/00/12/01/01/01/21/21/24/00', 0), 
   2211: (
        2716, NPCToonNames[2211], '01/00/03/03/00/03/00/03/01/01/25/22/22/00/00', 0), 
   2212: (
        2717, NPCToonNames[2212], '00/00/00/18/02/18/00/18/01/01/00/09/09/18/00', 0), 
   2213: (
        2720, NPCToonNames[2213], '01/00/01/12/02/12/00/12/01/01/11/23/23/00/00', 0), 
   2215: (
        2727, NPCToonNames[2215], '00/01/04/18/02/18/01/18/00/00/00/11/11/09/00', 0), 
   2216: (
        2728, NPCToonNames[2216], '01/08/03/11/03/11/01/11/00/00/12/25/25/00/00', 0), 
   2217: (
        2729, NPCToonNames[2217], '00/08/02/04/00/04/01/04/00/00/00/12/12/20/00', 0), 
   2219: (
        2732, NPCToonNames[2219], '00/03/03/10/01/10/01/10/00/00/00/00/00/14/00', 0), 
   2220: (
        2733, NPCToonNames[2220], '00/03/00/03/00/03/01/03/01/01/00/12/12/11/00', 0), 
   2222: (
        2735, NPCToonNames[2222], '00/07/01/10/02/10/01/10/01/01/00/00/00/01/00', 0), 
   2224: (
        2740, NPCToonNames[2224], '00/05/00/17/00/17/01/17/01/01/00/01/01/16/00', 0), 
   2225: (
        2236, NPCToonNames[2225], '00/00/03/09/02/09/01/09/01/01/00/01/01/13/00', 5), 
   1202: (
        1713, NPCToonNames[1202], '00/00/01/04/00/04/00/04/00/00/01/00/00/14/00', 0), 
   1204: (
        1712, NPCToonNames[1204], '00/01/04/12/01/12/00/12/01/01/01/01/01/06/00', 0), 
   1205: (
        1729, NPCToonNames[1205], '00/08/03/04/00/04/00/04/01/01/01/01/01/01/00', 3), 
   1206: (
        1729, NPCToonNames[1206], '01/08/00/19/05/19/00/19/01/01/07/02/02/11/00', 3), 
   1207: (
        1729, NPCToonNames[1207], '00/08/01/12/01/12/00/12/01/01/01/02/02/16/00', 3), 
   1208: (
        1729, NPCToonNames[1208], '01/03/02/03/02/03/01/03/01/01/23/03/03/00/00', 3), 
   1209: (
        1701, NPCToonNames[1209], '01/03/00/19/00/19/01/19/00/00/17/04/04/00/00', 0), 
   1211: (
        1705, NPCToonNames[1211], '00/07/01/04/01/04/01/04/00/00/01/04/04/00/00', 0), 
   1212: (
        1706, NPCToonNames[1212], '00/05/02/18/00/18/01/18/00/00/01/04/04/18/00', 0), 
   1213: (
        1707, NPCToonNames[1213], '00/05/00/10/02/10/01/10/00/00/01/04/04/15/00', 0), 
   1214: (
        1709, NPCToonNames[1214], '01/00/03/02/03/02/01/02/00/00/01/07/07/12/00', 0), 
   1215: (
        1711, NPCToonNames[1215], '01/00/00/18/01/18/01/18/00/00/25/07/07/00/00', 0), 
   1216: (
        1714, NPCToonNames[1216], '00/00/01/10/02/10/01/10/01/01/01/05/05/02/00', 0), 
   1218: (
        1717, NPCToonNames[1218], '00/01/04/17/01/17/01/17/01/01/01/06/06/17/00', 0), 
   1219: (
        1718, NPCToonNames[1219], '00/08/03/09/00/09/01/09/01/01/01/06/06/14/00', 0), 
   1220: (
        1719, NPCToonNames[1220], '01/08/02/02/04/02/01/02/01/01/07/09/09/23/00', 0), 
   1223: (
        1723, NPCToonNames[1223], '00/03/00/02/02/02/02/02/00/00/01/08/08/19/00', 0), 
   1224: (
        1724, NPCToonNames[1224], '01/07/00/17/03/17/02/17/00/00/07/21/21/09/00', 0), 
   1225: (
        1726, NPCToonNames[1225], '00/07/01/09/00/09/02/09/00/00/01/09/09/13/00', 0), 
   1226: (
        1727, NPCToonNames[1226], '00/05/02/02/02/02/02/02/00/00/01/09/09/10/00', 0), 
   1227: (
        1728, NPCToonNames[1227], '01/05/00/17/03/17/02/17/00/00/03/22/22/07/00', 0), 
   1228: (
        1236, NPCToonNames[1228], '00/00/03/08/01/08/02/08/01/01/01/09/09/00/00', 5), 
   4127: (
        4632, NPCToonNames[4127], '01/05/03/22/04/22/01/22/01/01/23/04/04/00/00', 0), 
   4302: (
        4821, NPCToonNames[4302], '01/08/01/03/02/03/02/03/01/01/02/02/02/03/00', 0), 
   4301: (
        4819, NPCToonNames[4301], '01/08/00/12/04/12/02/12/01/01/17/02/02/00/00', 0), 
   4304: (
        4873, NPCToonNames[4304], '00/03/00/12/02/12/01/12/00/00/00/02/02/15/00', 3), 
   4305: (
        4873, NPCToonNames[4305], '01/07/00/03/03/03/01/03/00/00/26/04/04/00/00', 3), 
   4306: (
        4873, NPCToonNames[4306], '01/05/03/19/01/19/01/19/00/00/04/05/05/25/00', 3), 
   4308: (
        4835, NPCToonNames[4308], '01/00/00/06/04/06/01/06/03/03/00/05/05/14/00', 0), 
   4309: (
        4801, NPCToonNames[4309], '00/00/03/18/01/18/01/18/00/00/00/04/04/17/00', 0), 
   4312: (
        4807, NPCToonNames[4312], '00/01/06/18/01/18/01/18/01/01/00/05/05/09/00', 0), 
   4132: (
        4641, NPCToonNames[4132], '01/01/07/06/01/06/02/06/00/00/17/07/07/00/00', 0), 
   4314: (
        4817, NPCToonNames[4314], '01/08/03/02/05/02/01/02/01/01/12/08/08/00/00', 0), 
   4303: (
        4853, NPCToonNames[4303], '00/03/02/18/00/18/02/18/01/01/00/02/02/18/00', 0), 
   4316: (
        4828, NPCToonNames[4316], '00/08/01/09/00/09/01/09/01/01/00/06/06/14/00', 0), 
   4317: (
        4829, NPCToonNames[4317], '00/03/02/03/02/03/02/03/00/00/00/07/07/11/00', 0), 
   4318: (
        4836, NPCToonNames[4318], '00/03/00/17/01/17/02/17/00/00/00/08/08/06/00', 0), 
   4133: (
        4642, NPCToonNames[4133], '00/01/04/20/02/20/02/20/00/00/01/05/05/14/00', 0), 
   4320: (
        4840, NPCToonNames[4320], '01/07/01/01/00/01/02/01/00/00/11/21/21/00/00', 0), 
   4321: (
        4841, NPCToonNames[4321], '00/05/02/17/02/17/02/17/00/00/00/09/09/16/00', 0), 
   4322: (
        4842, NPCToonNames[4322], '00/05/01/09/01/09/02/09/00/00/00/09/09/13/00', 0), 
   4323: (
        4844, NPCToonNames[4323], '01/00/03/01/00/01/02/01/01/01/24/21/21/00/00', 0), 
   4324: (
        4845, NPCToonNames[4324], '01/00/00/17/05/17/02/17/01/01/10/22/22/00/00', 0), 
   3301: (
        3810, NPCToonNames[3301], '01/01/06/11/01/11/01/11/00/00/02/22/22/11/00', 0), 
   3302: (
        3806, NPCToonNames[3302], '00/01/05/04/02/04/01/04/00/00/01/10/10/01/00', 0), 
   3303: (
        3830, NPCToonNames[3303], '00/08/03/18/01/18/01/18/00/00/01/10/10/19/00', 0), 
   3304: (
        3828, NPCToonNames[3304], '00/04/03/00/02/00/02/00/01/01/01/05/05/06/00', 0), 
   3305: (
        3812, NPCToonNames[3305], '00/08/01/03/02/03/01/03/00/00/01/11/11/13/00', 0), 
   3306: (
        3821, NPCToonNames[3306], '01/02/00/00/03/00/01/00/31/22/08/00/00/11/00', 0), 
   3111: (
        3627, NPCToonNames[3111], '00/01/06/06/02/06/00/06/14/10/01/00/00/14/00', 0), 
   3308: (
        3815, NPCToonNames[3308], '00/07/00/03/00/03/01/03/01/01/01/11/11/00/00', 0), 
   3309: (
        3826, NPCToonNames[3309], '00/05/03/17/02/17/01/17/01/01/01/11/11/18/00', 0), 
   3310: (
        3823, NPCToonNames[3310], '00/04/03/10/01/10/01/10/60/49/00/00/00/13/00', 0), 
   3312: (
        3813, NPCToonNames[3312], '00/03/00/04/01/04/02/04/05/05/01/02/02/10/00', 0), 
   3313: (
        3801, NPCToonNames[3313], '00/00/00/09/01/09/02/09/00/00/01/00/00/02/00', 3), 
   3314: (
        3801, NPCToonNames[3314], '01/00/01/01/01/01/02/01/00/00/03/00/00/25/00', 3), 
   3315: (
        3801, NPCToonNames[3315], '00/01/06/17/02/17/02/17/00/00/01/00/00/17/00', 3), 
   3316: (
        3801, NPCToonNames[3316], '01/01/04/10/04/10/02/10/00/00/10/01/01/00/00', 3), 
   3317: (
        3816, NPCToonNames[3317], '01/08/03/01/02/01/02/01/00/00/03/02/02/24/00', 0), 
   3318: (
        3808, NPCToonNames[3318], '00/01/04/18/01/18/01/18/57/46/12/01/01/01/00', 0), 
   3319: (
        3825, NPCToonNames[3319], '00/08/01/09/02/09/02/09/01/01/01/02/02/01/00', 0), 
   3320: (
        3814, NPCToonNames[3320], '01/03/02/01/02/01/02/01/01/01/12/03/03/00/00', 0), 
   3321: (
        3818, NPCToonNames[3321], '00/03/00/16/00/16/02/16/01/01/01/02/02/16/00', 0), 
   3323: (
        3811, NPCToonNames[3323], '00/07/01/22/01/22/02/22/01/01/01/03/03/10/00', 0), 
   2301: (
        2804, NPCToonNames[2301], '00/00/03/10/01/10/01/10/01/01/00/03/03/06/00', 0), 
   2302: (
        2831, NPCToonNames[2302], '00/00/00/03/01/03/01/03/01/01/00/03/03/01/00', 0), 
   2304: (
        2832, NPCToonNames[2304], '00/01/04/09/00/09/01/09/00/00/01/10/10/12/00', 3), 
   2305: (
        2832, NPCToonNames[2305], '00/01/04/08/00/08/01/08/01/01/01/00/00/09/00', 3), 
   2306: (
        2832, NPCToonNames[2306], '01/08/03/24/04/24/01/24/01/01/16/00/00/00/00', 3), 
   2307: (
        2832, NPCToonNames[2307], '01/08/02/16/02/16/01/16/01/01/03/01/01/01/00', 3), 
   2308: (
        2801, NPCToonNames[2308], '01/08/01/08/00/08/01/08/01/01/14/01/01/00/00', 0), 
   2309: (
        2802, NPCToonNames[2309], '00/03/02/22/02/22/01/22/01/01/01/01/01/14/00', 0), 
   2311: (
        2809, NPCToonNames[2311], '00/07/00/07/00/07/01/07/00/00/01/02/02/06/00', 0), 
   2312: (
        2837, NPCToonNames[2312], '01/07/01/24/05/24/01/24/00/00/04/03/03/06/00', 0), 
   2314: (
        2818, NPCToonNames[2314], '00/05/00/07/01/07/01/07/00/00/01/03/03/16/00', 0), 
   2315: (
        2822, NPCToonNames[2315], '00/00/03/21/00/21/01/21/00/00/01/03/03/13/00', 0), 
   2316: (
        2823, NPCToonNames[2316], '01/00/02/15/04/15/02/15/00/00/00/05/05/23/00', 0), 
   2318: (
        2829, NPCToonNames[2318], '00/01/06/21/00/21/02/21/01/01/01/04/04/00/00', 0), 
   2319: (
        2830, NPCToonNames[2319], '00/01/04/14/02/14/02/14/01/01/01/05/05/18/00', 0), 
   2321: (
        2341, NPCToonNames[2321], '00/08/02/21/00/21/02/21/01/01/00/05/05/12/00', 5), 
   2322: (
        2653, NPCToonNames[2322], '00/07/01/07/01/07/01/07/02/02/01/03/03/11/00', 0), 
   4126: (
        4631, NPCToonNames[4126], '00/07/01/06/00/06/01/06/01/01/01/03/03/18/00', 0), 
   1301: (
        1828, NPCToonNames[1301], '01/07/01/16/04/16/01/16/01/01/14/08/08/00/00', 0), 
   1302: (
        1832, NPCToonNames[1302], '00/05/02/08/01/08/01/08/01/01/00/06/06/18/00', 0), 
   1303: (
        1826, NPCToonNames[1303], '00/05/01/22/00/22/01/22/01/01/00/06/06/15/00', 0), 
   1304: (
        1804, NPCToonNames[1304], '01/00/03/15/04/15/01/15/01/01/23/09/09/00/00', 0), 
   1305: (
        1835, NPCToonNames[1305], '00/00/00/07/01/07/01/07/01/01/00/07/07/09/00', 3), 
   1306: (
        1835, NPCToonNames[1306], '01/00/01/24/01/24/01/24/00/00/00/12/12/07/00', 3), 
   1307: (
        1835, NPCToonNames[1307], '00/01/06/15/02/15/01/15/00/00/00/08/08/20/00', 3), 
   1308: (
        1835, NPCToonNames[1308], '01/01/04/08/03/08/01/08/00/00/04/21/21/05/00', 3), 
   1309: (
        1802, NPCToonNames[1309], '01/08/03/23/01/23/02/23/00/00/01/21/21/12/00', 0), 
   1310: (
        1805, NPCToonNames[1310], '00/08/02/15/00/15/02/15/00/00/00/09/09/11/00', 0), 
   1312: (
        1807, NPCToonNames[1312], '00/03/02/21/01/21/02/21/01/01/00/09/09/01/00', 0), 
   1313: (
        1808, NPCToonNames[1313], '00/03/00/14/00/14/02/14/01/01/00/10/10/19/00', 0), 
   1314: (
        1809, NPCToonNames[1314], '00/07/00/06/02/06/02/06/01/01/00/10/10/16/00', 0), 
   1316: (
        1811, NPCToonNames[1316], '01/05/02/14/01/14/02/14/01/01/07/24/24/07/00', 0), 
   1317: (
        1813, NPCToonNames[1317], '01/05/00/07/05/07/02/07/01/01/26/25/25/00/00', 0), 
   1318: (
        1814, NPCToonNames[1318], '00/00/03/20/01/20/02/20/00/00/00/12/12/00/00', 0), 
   1319: (
        1815, NPCToonNames[1319], '00/00/02/14/00/14/02/14/00/00/00/00/00/18/00', 0), 
   1321: (
        1819, NPCToonNames[1321], '01/01/06/22/04/22/02/22/00/00/07/00/00/05/00', 0), 
   1322: (
        1820, NPCToonNames[1322], '01/01/04/13/02/13/01/13/00/00/26/00/00/00/00', 0), 
   1323: (
        1821, NPCToonNames[1323], '00/08/03/06/00/06/01/06/00/00/01/00/00/02/00', 0), 
   1324: (
        1823, NPCToonNames[1324], '01/08/02/22/04/22/01/22/00/00/10/01/01/00/00', 0), 
   1326: (
        1825, NPCToonNames[1326], '01/03/03/06/01/06/01/06/01/01/10/02/02/00/00', 0), 
   1328: (
        1830, NPCToonNames[1328], '00/03/01/13/01/13/01/13/01/01/01/02/02/06/00', 0), 
   1329: (
        1831, NPCToonNames[1329], '01/07/01/04/01/04/01/04/01/01/25/03/03/00/00', 0), 
   1330: (
        1833, NPCToonNames[1330], '00/05/02/19/02/19/01/19/01/01/01/03/03/19/00', 0), 
   1331: (
        1834, NPCToonNames[1331], '00/05/00/12/02/12/01/12/00/00/01/03/03/16/00', 0), 
   1332: (
        1330, NPCToonNames[1332], '00/00/03/05/01/05/01/05/00/00/01/04/04/13/00', 5), 
   4136: (
        4652, NPCToonNames[4136], '01/08/00/21/00/21/02/21/00/00/07/09/09/04/00', 0), 
   4319: (
        4838, NPCToonNames[4319], '01/07/00/10/02/10/02/10/00/00/01/12/12/23/00', 0), 
   5125: (
        5623, NPCToonNames[5125], '00/05/00/14/02/14/01/14/00/00/00/09/09/00/00', 0), 
   9305: (
        -1, NPCToonNames[9305], '00/05/03/08/02/08/02/08/01/00/01/03/00/16/00', 0), 
   3125: (
        3614, NPCToonNames[3125], '00/08/01/13/02/13/02/13/01/01/00/09/09/00/00', 0), 
   9217: (
        9713, NPCToonNames[9217], '01/07/00/17/01/17/01/17/20/00/05/26/26/12/00', 0), 
   3126: (
        3615, NPCToonNames[3126], '01/03/03/06/02/06/02/06/00/00/17/24/24/00/00', 0), 
   4307: (
        4873, NPCToonNames[4307], '01/05/02/11/05/11/01/11/00/00/17/05/05/00/00', 3), 
   3127: (
        3617, NPCToonNames[3127], '01/03/00/21/01/21/02/21/00/00/19/24/24/00/00', 0), 
   5108: (
        5616, NPCToonNames[5108], '01/07/00/02/02/02/02/02/00/00/24/11/11/00/00', 0), 
   7001: (
        -1, NPCToonNames[7001], '01/02/00/25/04/25/01/25/06/00/00/12/00/02/00', 0), 
   9101: (
        9604, NPCToonNames[9101], '00/00/00/14/02/14/02/14/01/01/00/01/01/11/00', 0), 
   3128: (
        3621, NPCToonNames[3128], '00/03/01/13/02/13/02/13/00/00/00/11/11/12/00', 0), 
   4137: (
        4654, NPCToonNames[4137], '00/03/03/13/02/13/02/13/01/01/01/06/06/19/00', 0), 
   3129: (
        3623, NPCToonNames[3129], '01/07/01/04/03/04/02/04/00/00/23/25/25/00/00', 0), 
   5126: (
        5624, NPCToonNames[5126], '01/05/01/07/03/07/01/07/00/00/14/21/21/00/00', 0), 
   9103: (
        9620, NPCToonNames[9103], '00/01/06/20/00/20/02/20/00/00/00/02/02/01/00', 0), 
   3130: (
        3624, NPCToonNames[3130], '01/05/03/21/01/21/02/21/00/00/25/26/26/00/00', 0), 
   4325: (
        4848, NPCToonNames[4325], '00/00/01/09/01/09/02/09/01/01/00/09/09/00/00', 0), 
   9104: (
        9642, NPCToonNames[9104], '01/01/04/14/05/14/02/14/00/00/00/03/03/23/00', 0), 
   9218: (
        9737, NPCToonNames[9218], '01/01/04/23/04/23/02/23/24/15/11/00/00/00/00', 0), 
   3131: (
        3634, NPCToonNames[3131], '00/05/00/12/02/12/02/12/00/00/00/12/12/20/00', 0), 
   4326: (
        4850, NPCToonNames[4326], '01/01/06/01/01/01/02/01/01/01/14/23/23/00/00', 0), 
   9229: (
        9708, NPCToonNames[9229], '01/00/00/04/05/04/01/04/22/00/04/21/21/21/00', 0), 
   4128: (
        4635, NPCToonNames[4128], '00/05/00/13/01/13/01/13/01/01/01/03/03/12/00', 0), 
   4327: (
        4852, NPCToonNames[4327], '01/01/04/16/05/16/02/16/01/01/07/23/23/01/00', 0), 
   7002: (
        -1, NPCToonNames[7002], '00/06/00/07/01/07/02/07/18/00/04/11/00/03/00', 0), 
   9106: (
        9619, NPCToonNames[9106], '00/08/02/20/00/20/02/20/00/00/00/03/03/13/00', 0), 
   3133: (
        3642, NPCToonNames[3133], '00/00/02/19/01/19/02/19/01/01/00/12/12/14/00', 0), 
   4328: (
        4854, NPCToonNames[4328], '00/08/03/08/01/08/02/08/01/01/00/11/11/12/00', 0), 
   4138: (
        4655, NPCToonNames[4138], '00/03/02/05/01/05/02/05/01/01/01/07/07/16/00', 0), 
   3134: (
        3643, NPCToonNames[3134], '00/00/01/12/00/12/02/12/01/01/00/00/00/11/00', 0), 
   4329: (
        4855, NPCToonNames[4329], '01/08/02/24/02/24/02/24/00/00/26/25/25/00/00', 0), 
   5127: (
        5625, NPCToonNames[5127], '01/00/02/23/01/23/01/23/00/00/02/22/22/02/00', 0), 
   9108: (
        9602, NPCToonNames[9108], '00/03/03/06/01/06/02/06/01/01/00/04/04/04/00', 0), 
   3135: (
        3644, NPCToonNames[3135], '01/01/07/04/04/04/02/04/01/01/04/00/00/12/00', 0), 
   9311: (
        -1, NPCToonNames[9311], '01/07/00/24/03/24/00/24/03/00/00/01/00/13/00', 0), 
   9109: (
        9605, NPCToonNames[9109], '01/03/00/22/02/22/02/22/01/01/10/06/06/00/00', 0), 
   9219: (
        9712, NPCToonNames[9219], '01/05/03/10/03/10/02/10/09/09/12/22/22/00/00', 0), 
   3136: (
        3647, NPCToonNames[3136], '01/01/04/19/02/19/02/19/01/01/25/01/01/00/00', 0), 
   4135: (
        4648, NPCToonNames[4135], '00/08/02/05/01/05/02/05/00/00/01/06/06/06/00', 0), 
   3307: (
        3329, NPCToonNames[3307], '01/03/00/11/02/11/01/11/01/01/01/24/24/09/00', 5), 
   3137: (
        3648, NPCToonNames[3137], '00/01/05/12/00/12/02/12/01/01/00/01/01/19/00', 0), 
   9117: (
        9628, NPCToonNames[9117], '01/01/06/04/05/04/01/04/00/00/02/11/11/09/00', 0), 
   4332: (
        4870, NPCToonNames[4332], '00/03/00/22/01/22/02/22/00/00/00/00/00/17/00', 0), 
   7003: (
        -1, NPCToonNames[7003], '01/06/00/21/04/21/01/21/45/00/07/00/00/06/00', 0), 
   3138: (
        3649, NPCToonNames[3138], '01/08/02/03/05/03/02/03/01/01/26/02/02/00/00', 0), 
   4333: (
        4871, NPCToonNames[4333], '00/07/00/15/00/15/02/15/00/00/00/00/00/14/00', 0), 
   4139: (
        4657, NPCToonNames[4139], '01/03/01/21/00/21/02/21/01/01/14/11/11/00/00', 0), 
   3139: (
        3650, NPCToonNames[3139], '01/08/00/19/03/19/02/19/00/00/16/02/02/00/00', 0), 
   4334: (
        4872, NPCToonNames[4334], '00/07/01/08/02/08/02/08/00/00/00/00/00/11/00', 0), 
   3140: (
        3136, NPCToonNames[3140], '01/03/03/11/01/11/02/11/00/00/12/03/03/00/00', 5), 
   4335: (
        4345, NPCToonNames[4335], '00/05/02/22/01/22/02/22/01/01/00/00/00/06/00', 5), 
   9220: (
        9716, NPCToonNames[9220], '00/07/01/07/01/07/02/07/00/00/01/00/00/10/00', 0), 
   9107: (
        9601, NPCToonNames[9107], '01/08/01/13/05/13/02/13/00/00/03/05/05/02/00', 0), 
   9234: (
        9756, NPCToonNames[9234], '00/00/01/14/00/14/02/14/01/01/00/05/05/19/00', 3), 
   9209: (
        9706, NPCToonNames[9209], '00/04/03/13/00/13/01/13/08/08/01/12/12/12/00', 0), 
   4140: (
        4658, NPCToonNames[4140], '00/07/01/12/02/12/02/12/01/01/01/07/07/10/00', 0), 
   5129: (
        5139, NPCToonNames[5129], '01/01/07/07/04/07/01/07/00/00/17/23/23/00/00', 5), 
   9221: (
        9738, NPCToonNames[9221], '01/08/00/22/04/22/02/22/45/34/00/00/00/06/00', 0), 
   9121: (
        9634, NPCToonNames[9121], '01/08/01/19/04/19/01/19/01/01/16/12/12/00/00', 0), 
   9216: (
        9725, NPCToonNames[9216], '01/00/02/14/03/14/01/14/01/01/03/07/07/07/00', 0), 
   5321: (
        5837, NPCToonNames[5321], '01/00/00/18/01/18/01/18/01/01/17/01/01/00/00', 0), 
   4141: (
        4148, NPCToonNames[4141], '00/05/03/04/01/04/02/04/01/01/01/08/08/04/00', 5), 
   1101: (
        1627, NPCToonNames[1101], '00/08/03/14/02/14/01/14/01/01/01/03/03/09/00', 0), 
   4231: (
        4735, NPCToonNames[4231], '01/05/02/11/00/11/01/11/01/01/08/02/02/00/00', 0), 
   4003: (
        4504, NPCToonNames[4003], '01/08/02/21/04/21/01/21/00/00/10/03/03/00/00', 3), 
   1102: (
        1612, NPCToonNames[1102], '00/08/02/07/01/07/01/07/01/01/01/03/03/02/00', 0), 
   9124: (
        9640, NPCToonNames[9124], '01/03/01/19/04/19/01/19/01/01/08/22/22/09/00', 0), 
   9222: (
        9754, NPCToonNames[9222], '00/05/02/10/02/10/02/10/52/41/12/00/00/00/00', 0), 
   9215: (
        9744, NPCToonNames[9215], '00/00/02/18/02/18/02/18/11/00/00/04/04/04/00', 0), 
   9125: (
        9643, NPCToonNames[9125], '00/07/01/10/01/10/02/10/01/01/00/09/09/04/00', 0), 
   5322: (
        5318, NPCToonNames[5322], '01/00/01/10/00/10/01/10/00/00/11/02/02/00/00', 5), 
   1105: (
        1606, NPCToonNames[1105], '00/03/00/06/01/06/01/06/00/00/01/04/04/14/00', 0), 
   3325: (
        3827, NPCToonNames[3325], '00/05/00/08/02/08/02/08/00/00/01/04/04/00/00', 0), 
   9128: (
        9647, NPCToonNames[9128], '00/00/03/10/01/10/02/10/00/00/00/11/11/15/00', 0), 
   3326: (
        3820, NPCToonNames[3326], '01/00/03/24/04/24/02/24/00/00/12/06/06/00/00', 0), 
   4009: (
        4000, NPCToonNames[4009], '01/05/02/19/05/19/01/19/01/01/12/06/06/00/00', 5), 
   9223: (
        9714, NPCToonNames[9223], '00/08/02/20/01/20/01/20/43/32/00/00/00/00/00', 0), 
   1108: (
        1629, NPCToonNames[1108], '00/05/02/06/02/06/02/06/00/00/01/06/06/01/00', 3), 
   4313: (
        4809, NPCToonNames[4313], '00/01/04/10/00/10/01/10/01/01/00/05/05/02/00', 0), 
   3327: (
        3824, NPCToonNames[3327], '00/00/00/15/01/15/02/15/00/00/01/05/05/15/00', 0), 
   9130: (
        9650, NPCToonNames[9130], '00/00/01/18/00/18/02/18/00/00/00/12/12/09/00', 0), 
   4129: (
        4637, NPCToonNames[4129], '01/05/01/06/00/06/02/06/01/01/26/05/05/00/00', 0), 
   1109: (
        1629, NPCToonNames[1109], '01/05/00/22/02/22/02/22/00/00/14/08/08/00/00', 3), 
   3328: (
        3807, NPCToonNames[3328], '01/01/07/08/03/08/02/08/00/00/14/25/25/00/00', 0), 
   1110: (
        1629, NPCToonNames[1110], '00/00/03/13/00/13/02/13/01/01/01/06/06/16/00', 3), 
   5302: (
        5802, NPCToonNames[5302], '01/07/00/04/00/04/02/04/00/00/17/12/12/00/00', 3), 
   3329: (
        3817, NPCToonNames[3329], '00/01/07/06/01/06/02/06/00/00/01/01/01/01/00', 0), 
   9132: (
        9652, NPCToonNames[9132], '01/01/04/02/02/02/02/02/00/00/00/00/00/00/00', 3), 
   1111: (
        1629, NPCToonNames[1111], '01/00/02/06/05/06/02/06/01/01/02/09/09/02/00', 3), 
   9133: (
        9652, NPCToonNames[9133], '00/01/05/17/00/17/02/17/01/01/00/12/12/17/00', 3), 
   1112: (
        1602, NPCToonNames[1112], '00/00/01/20/01/20/02/20/01/01/01/07/07/10/00', 0), 
   9309: (
        -1, NPCToonNames[9309], '00/06/00/02/01/02/02/02/00/00/00/04/00/06/00', 0), 
   9134: (
        9652, NPCToonNames[9134], '00/08/02/10/02/10/02/10/01/01/00/00/00/14/00', 3), 
   9224: (
        9718, NPCToonNames[9224], '01/00/00/01/01/01/01/01/06/06/06/08/08/08/00', 0), 
   1113: (
        1608, NPCToonNames[1113], '01/01/07/13/01/13/02/13/01/01/00/11/11/00/00', 0), 
   9135: (
        9652, NPCToonNames[9135], '00/08/01/03/01/03/02/03/01/01/00/00/00/11/00', 3), 
   1114: (
        1609, NPCToonNames[1114], '00/01/04/05/02/05/02/05/01/01/01/07/07/00/00', 0), 
   9122: (
        9636, NPCToonNames[9122], '00/03/03/12/01/12/01/12/01/01/00/08/08/16/00', 0), 
   20000: (
         -1, NPCToonNames[20000], '00/01/05/07/01/07/01/07/02/02/02/06/06/16/00', 9), 
   20001: (
         -1, NPCToonNames[20001], '00/01/04/17/01/17/01/17/03/03/07/03/03/02/00', 4), 
   20002: (
         -1, NPCToonNames[20002], '00/01/05/06/01/06/01/06/00/00/02/10/10/09/00', 9), 
   1115: (
        1613, NPCToonNames[1115], '01/08/03/21/03/21/02/21/01/01/25/12/12/00/00', 0), 
   9203: (
        9741, NPCToonNames[9203], '00/04/01/05/02/05/00/05/37/26/07/00/00/04/00', 0), 
   4125: (
        4630, NPCToonNames[4125], '01/03/01/14/02/14/01/14/01/01/08/03/03/06/00', 0), 
   1116: (
        1614, NPCToonNames[1116], '01/08/02/13/02/13/02/13/01/01/01/12/12/25/00', 0), 
   5213: (
        5701, NPCToonNames[5213], '00/07/01/13/00/13/02/13/01/01/01/01/01/14/00', 0), 
   9225: (
        9717, NPCToonNames[9225], '01/03/00/11/04/11/01/11/40/29/00/00/00/00/00', 0), 
   5214: (
        5705, NPCToonNames[5214], '01/05/02/06/04/06/02/06/01/01/17/02/02/00/00', 0), 
   4315: (
        4827, NPCToonNames[4315], '01/08/00/18/03/18/01/18/01/01/26/09/09/00/00', 0), 
   5316: (
        5828, NPCToonNames[5316], '00/07/00/10/02/10/01/10/01/01/01/12/12/13/00', 0), 
   5304: (
        5802, NPCToonNames[5304], '01/05/02/12/02/12/02/12/01/01/19/12/12/00/00', 3), 
   9123: (
        9639, NPCToonNames[9123], '00/03/00/04/00/04/01/04/01/01/00/09/09/13/00', 0), 
   9210: (
        9740, NPCToonNames[9210], '00/05/02/06/02/06/02/06/01/01/00/00/00/00/00', 0), 
   9312: (
        -1, NPCToonNames[9312], '01/04/00/09/03/09/02/09/00/00/11/08/00/00/00', 0), 
   5202: (
        5703, NPCToonNames[5202], '01/00/03/07/02/07/02/07/01/01/11/23/23/00/00', 0), 
   5217: (
        5708, NPCToonNames[5217], '00/00/02/05/02/05/02/05/00/00/01/03/03/19/00', 0), 
   8003: (
        8501, NPCToonNames[8003], '01/04/03/01/00/01/02/01/00/00/02/11/11/10/00', 7), 
   9226: (
        9715, NPCToonNames[9226], '00/07/01/12/01/12/00/12/03/03/06/10/10/10/00', 0), 
   5219: (
        5710, NPCToonNames[5219], '00/01/06/13/00/13/02/13/00/00/01/03/03/13/00', 0), 
   5221: (
        5712, NPCToonNames[5221], '01/08/03/21/04/21/02/21/00/00/25/06/06/00/00', 0), 
   5203: (
        5704, NPCToonNames[5203], '01/00/00/23/00/23/02/23/01/01/19/24/24/00/00', 0), 
   5101: (
        5602, NPCToonNames[5101], '00/01/06/10/01/10/02/10/01/01/00/04/04/11/00', 0), 
   9237: (
        9255, NPCToonNames[9237], '00/01/05/14/00/14/02/14/00/00/00/07/07/10/00', 5), 
   9227: (
        9721, NPCToonNames[9227], '00/00/01/13/00/13/00/13/08/08/03/05/05/18/00', 0), 
   5225: (
        5716, NPCToonNames[5225], '01/03/00/12/03/12/00/12/01/01/10/07/07/00/00', 0), 
   9310: (
        -1, NPCToonNames[9310], '00/08/02/17/02/17/01/17/04/00/00/04/00/10/00', 0), 
   5226: (
        5721, NPCToonNames[5226], '00/03/01/04/00/04/00/04/01/01/01/05/05/09/00', 0), 
   5204: (
        5726, NPCToonNames[5204], '00/00/01/14/02/14/02/14/00/00/01/12/12/04/00', 0), 
   5227: (
        5725, NPCToonNames[5227], '01/07/01/19/05/19/00/19/01/01/23/08/08/00/00', 0), 
   9307: (
        -1, NPCToonNames[9307], '01/04/01/14/02/14/00/14/00/00/05/11/00/09/00', 0), 
   9228: (
        9720, NPCToonNames[9228], '01/08/00/04/03/04/00/04/15/11/08/05/05/05/00', 0), 
   5229: (
        5245, NPCToonNames[5229], '01/05/00/03/01/03/00/03/00/00/16/11/11/00/00', 5), 
   5307: (
        5809, NPCToonNames[5307], '00/00/00/12/01/12/02/12/01/01/01/09/09/02/00', 0), 
   5303: (
        5802, NPCToonNames[5303], '00/05/03/19/02/19/02/19/01/01/01/08/08/18/00', 3), 
   5228: (
        5727, NPCToonNames[5228], '00/05/02/12/01/12/00/12/01/01/01/06/06/20/00', 0), 
   9308: (
        -1, NPCToonNames[9308], '00/02/02/12/02/12/02/12/01/00/01/10/00/13/00', 0), 
   9214: (
        9710, NPCToonNames[9214], '00/03/03/18/02/18/02/18/10/00/00/00/00/13/00', 0), 
   5308: (
        5810, NPCToonNames[5308], '01/00/01/04/01/04/02/04/01/01/10/22/22/00/00', 0), 
   9127: (
        9645, NPCToonNames[9127], '01/05/00/19/05/19/02/19/00/00/10/24/24/00/00', 0), 
   9204: (
        9704, NPCToonNames[9204], '01/08/02/19/03/19/00/19/21/00/08/10/10/23/00', 0), 
   5206: (
        5720, NPCToonNames[5206], '00/01/04/21/00/21/02/21/00/00/01/00/00/18/00', 0), 
   5201: (
        5702, NPCToonNames[5201], '00/05/01/15/02/15/02/15/01/01/01/10/10/16/00', 0), 
   5104: (
        5617, NPCToonNames[5104], '00/08/02/10/01/10/02/10/01/01/00/05/05/19/00', 0), 
   9230: (
        9719, NPCToonNames[9230], '00/07/00/08/00/08/00/08/53/42/13/00/00/00/00', 0), 
   5305: (
        5804, NPCToonNames[5305], '01/05/01/04/00/04/02/04/01/01/16/21/21/00/00', 0), 
   7008: (
        -1, NPCToonNames[7008], '01/02/01/23/05/23/00/23/15/00/00/06/00/18/00', 0), 
   9211: (
        9707, NPCToonNames[9211], '01/03/03/03/00/03/00/03/22/00/06/22/22/22/00', 0), 
   5207: (
        5717, NPCToonNames[5207], '01/08/03/14/05/14/02/14/00/00/26/00/00/00/00', 0), 
   5320: (
        5836, NPCToonNames[5320], '01/00/03/02/03/02/01/02/01/01/17/01/01/00/00', 0), 
   9231: (
        9722, NPCToonNames[9231], '00/01/07/06/00/06/00/06/27/18/03/00/00/08/00', 0), 
   5310: (
        5815, NPCToonNames[5310], '00/01/05/12/01/12/02/12/00/00/01/11/11/14/00', 0), 
   9129: (
        9649, NPCToonNames[9129], '01/00/02/03/01/03/02/03/00/00/25/25/25/00/00', 0), 
   9126: (
        9644, NPCToonNames[9126], '01/05/02/03/01/03/02/03/01/01/23/23/23/00/00', 0), 
   5208: (
        5719, NPCToonNames[5208], '01/08/02/07/03/07/02/07/00/00/01/00/00/12/00', 0), 
   5106: (
        5613, NPCToonNames[5106], '00/03/02/18/02/18/02/18/01/01/00/06/06/13/00', 0), 
   9003: (
        9501, NPCToonNames[9003], '00/08/01/22/01/22/02/22/01/01/00/05/05/14/00', 0), 
   9232: (
        9759, NPCToonNames[9232], '01/04/00/21/05/21/01/21/00/00/13/00/00/00/00', 0), 
   4225: (
        4724, NPCToonNames[4225], '01/08/02/12/05/12/00/12/00/00/11/00/00/00/00', 0), 
   9004: (
        9505, NPCToonNames[9004], '01/03/03/16/01/16/02/16/01/01/03/07/07/08/00', 3), 
   3231: (
        3736, NPCToonNames[3231], '00/03/00/09/01/09/01/09/00/00/01/09/09/12/00', 0), 
   4226: (
        4727, NPCToonNames[4226], '01/08/01/03/03/03/00/03/00/00/11/00/00/00/00', 0), 
   4227: (
        4728, NPCToonNames[4227], '01/03/03/19/02/19/00/19/00/00/23/00/00/00/00', 0), 
   5209: (
        5728, NPCToonNames[5209], '00/08/01/21/00/21/02/21/00/00/01/00/00/09/00', 3), 
   5301: (
        5802, NPCToonNames[5301], '01/03/00/13/01/13/02/13/00/00/01/11/11/12/00', 3), 
   4228: (
        4729, NPCToonNames[4228], '01/03/00/11/00/11/00/11/00/00/00/01/01/01/00', 0), 
   9301: (
        -1, NPCToonNames[9301], '00/04/00/20/01/20/02/20/26/00/15/00/00/00/00', 0), 
   4229: (
        4731, NPCToonNames[4229], '01/03/01/03/04/03/01/03/00/00/26/01/01/00/00', 0), 
   9233: (
        9756, NPCToonNames[9233], '01/00/02/22/02/22/02/22/01/01/12/07/07/00/00', 3), 
   4230: (
        4732, NPCToonNames[4230], '00/07/01/18/01/18/01/18/01/01/00/01/01/14/00', 0), 
   9009: (
        9504, NPCToonNames[9009], '00/05/00/22/02/22/02/22/00/00/00/07/07/13/00', 1), 
   9001: (
        9503, NPCToonNames[9001], '01/08/03/16/00/16/02/16/00/00/26/06/06/00/00', 0), 
   3232: (
        3236, NPCToonNames[3232], '00/03/01/03/00/03/01/03/00/00/01/10/10/09/00', 5), 
   5312: (
        5819, NPCToonNames[5312], '00/08/00/18/00/18/01/18/00/00/01/12/12/06/00', 0), 
   9005: (
        9505, NPCToonNames[9005], '01/03/00/09/05/09/02/09/01/01/19/08/08/00/00', 3), 
   9006: (
        9505, NPCToonNames[9006], '00/03/01/22/01/22/02/22/01/01/00/06/06/01/00', 3), 
   9007: (
        9505, NPCToonNames[9007], '00/07/01/15/01/15/02/15/01/01/00/06/06/19/00', 3), 
   9008: (
        9504, NPCToonNames[9008], '01/05/03/08/00/08/02/08/01/01/12/09/09/00/00', 1), 
   4232: (
        4736, NPCToonNames[4232], '00/05/00/03/02/03/01/03/01/01/01/02/02/06/00', 0), 
   9010: (
        9506, NPCToonNames[9010], '00/00/03/15/01/15/02/15/00/00/00/08/08/10/00', 2), 
   9011: (
        9000, NPCToonNames[9011], '00/00/02/07/00/07/02/07/00/00/00/08/08/04/00', 5), 
   5210: (
        5728, NPCToonNames[5210], '00/03/02/14/00/14/02/14/01/01/01/00/00/02/00', 3), 
   9013: (
        9508, NPCToonNames[9013], '01/01/07/15/03/15/02/15/00/00/10/21/21/00/00', 6), 
   9014: (
        9508, NPCToonNames[9014], '00/01/04/07/00/07/02/07/00/00/01/09/09/15/00', 6), 
   4233: (
        4737, NPCToonNames[4233], '00/00/03/17/01/17/01/17/01/01/01/02/02/01/00', 0), 
   9016: (
        9000, NPCToonNames[9016], '01/03/01/21/04/06/02/21/01/01/00/11/11/11/00', 8), 
   9012: (
        9508, NPCToonNames[9012], '01/00/01/23/05/23/02/23/00/00/10/21/21/00/00', 6), 
   9302: (
        -1, NPCToonNames[9302], '01/02/02/20/01/20/01/20/03/00/05/04/00/18/00', 0), 
   8001: (
        8501, NPCToonNames[8001], '00/04/02/13/01/13/01/13/00/00/02/11/11/10/00', 7), 
   8002: (
        8501, NPCToonNames[8002], '01/04/02/23/05/23/00/23/00/00/02/11/11/10/00', 7), 
   4235: (
        4240, NPCToonNames[4235], '00/00/01/03/02/03/01/03/01/01/01/03/03/16/00', 5), 
   8004: (
        8501, NPCToonNames[8004], '00/04/01/16/01/16/02/16/00/00/02/11/11/10/00', 7), 
   5311: (
        5817, NPCToonNames[5311], '01/08/03/03/01/03/01/03/00/00/12/24/24/00/00', 0), 
   5313: (
        5821, NPCToonNames[5313], '00/08/01/10/02/10/01/10/00/00/01/12/12/01/00', 0), 
   9015: (
        9000, NPCToonNames[9015], '00/03/00/20/02/21/02/20/00/00/00/12/12/11/00', 8), 
   9205: (
        9736, NPCToonNames[9205], '00/01/06/15/01/15/01/15/45/34/02/00/00/17/00', 0), 
   5211: (
        5728, NPCToonNames[5211], '01/03/00/06/04/06/02/06/01/01/23/01/01/00/00', 3), 
   9213: (
        9711, NPCToonNames[9213], '00/08/02/02/00/02/01/02/37/26/07/00/00/18/00', 0), 
   9303: (
        -1, NPCToonNames[9303], '00/02/03/11/00/11/00/11/03/00/01/06/00/02/00', 0), 
   5109: (
        5627, NPCToonNames[5109], '00/07/01/17/00/17/02/17/00/00/00/07/07/00/00', 3), 
   7004: (
        -1, NPCToonNames[7004], '00/04/00/16/02/16/02/16/27/00/07/00/00/16/00', 0), 
   7005: (
        -1, NPCToonNames[7005], '01/04/01/05/05/05/00/05/25/00/10/00/00/00/00', 0), 
   7006: (
        -1, NPCToonNames[7006], '00/02/03/18/01/18/00/18/15/00/09/04/00/03/00', 0), 
   7007: (
        -1, NPCToonNames[7007], '00/04/01/11/02/11/00/11/46/00/05/00/00/16/00', 0), 
   9235: (
        9756, NPCToonNames[9235], '00/01/07/06/02/06/02/06/01/01/00/06/06/16/00', 3), 
   7009: (
        -1, NPCToonNames[7009], '00/06/03/01/00/01/00/01/01/00/00/06/00/06/00', 0), 
   9201: (
        9752, NPCToonNames[9201], '00/04/02/09/00/09/01/09/17/00/07/11/11/20/00', 0), 
   5318: (
        5833, NPCToonNames[5318], '00/05/02/18/00/18/01/18/01/01/01/00/00/04/00', 0), 
   9212: (
        9753, NPCToonNames[9212], '01/04/00/16/04/16/01/16/45/34/00/00/00/03/00', 0), 
   5212: (
        5728, NPCToonNames[5212], '01/07/00/22/02/22/02/22/01/01/10/01/01/00/00', 3), 
   9304: (
        -1, NPCToonNames[9304], '01/06/02/13/03/13/02/13/01/00/00/02/00/10/00', 0), 
   9236: (
        9756, NPCToonNames[9236], '00/01/04/20/01/20/02/20/00/00/00/06/06/13/00', 3), 
   9206: (
        9727, NPCToonNames[9206], '01/03/01/08/05/08/02/08/25/16/10/00/00/00/00', 0), 
   9202: (
        9703, NPCToonNames[9202], '00/01/04/21/00/21/00/21/08/08/01/03/03/17/00', 0), 
   5315: (
        5827, NPCToonNames[5315], '00/03/00/18/00/18/01/18/01/01/01/12/12/16/00', 0), 
   5001: (
        5502, NPCToonNames[5001], '00/08/01/14/02/14/00/14/01/01/00/07/07/20/00', 3), 
   5002: (
        5502, NPCToonNames[5002], '00/03/03/06/01/06/00/06/00/00/00/08/08/17/00', 3), 
   5003: (
        5502, NPCToonNames[5003], '01/03/00/22/01/22/00/22/00/00/26/12/12/00/00', 3), 
   5004: (
        5502, NPCToonNames[5004], '01/03/01/13/05/13/00/13/00/00/04/21/21/11/00', 3), 
   5005: (
        5501, NPCToonNames[5005], '01/07/01/06/04/06/00/06/00/00/02/21/21/03/00', 1), 
   5006: (
        5501, NPCToonNames[5006], '00/05/02/20/01/20/00/20/00/00/00/09/09/01/00', 1), 
   5007: (
        5503, NPCToonNames[5007], '01/05/00/13/00/13/00/13/00/00/03/22/22/02/00', 2), 
   5008: (
        5000, NPCToonNames[5008], '01/00/03/04/04/04/00/04/01/01/19/22/22/00/00', 5), 
   5009: (
        5505, NPCToonNames[5009], '01/00/02/21/02/21/01/21/01/01/08/23/23/23/00', 6), 
   5010: (
        5505, NPCToonNames[5010], '00/00/01/13/00/13/01/13/01/01/00/10/10/10/00', 6), 
   5011: (
        5505, NPCToonNames[5011], '00/01/07/05/02/05/01/05/01/01/00/10/10/04/00', 6), 
   5012: (
        5000, NPCToonNames[5012], '00/01/05/12/01/13/01/12/00/00/00/01/01/06/00', 8), 
   5013: (
        5000, NPCToonNames[5013], '01/01/04/03/04/01/01/03/01/01/00/05/05/05/00', 8), 
   9110: (
        9608, NPCToonNames[9110], '01/07/00/13/00/13/02/13/01/01/25/06/06/00/00', 0), 
   9112: (
        9617, NPCToonNames[9112], '00/05/02/19/01/19/01/19/01/01/00/05/05/12/00', 0), 
   9113: (
        9622, NPCToonNames[9113], '00/05/00/13/00/13/01/13/01/01/00/05/05/09/00', 0), 
   9114: (
        9625, NPCToonNames[9114], '01/00/03/04/05/04/01/04/00/00/10/08/08/00/00', 0), 
   5103: (
        5615, NPCToonNames[5103], '00/08/03/18/02/18/02/18/01/01/00/05/05/01/00', 0), 
   9116: (
        9627, NPCToonNames[9116], '00/00/01/12/00/12/01/12/00/00/00/07/07/17/00', 0), 
   3226: (
        3725, NPCToonNames[3226], '00/01/04/03/00/03/01/03/01/01/01/07/07/09/00', 0), 
   9119: (
        9630, NPCToonNames[9119], '00/08/03/12/01/12/01/12/00/00/00/08/08/06/00', 0), 
   4002: (
        4504, NPCToonNames[4002], '00/08/03/05/00/05/01/05/00/00/01/02/02/17/00', 3), 
   3227: (
        3726, NPCToonNames[3227], '00/08/03/17/02/17/01/17/01/01/01/07/07/02/00', 0), 
   4004: (
        4504, NPCToonNames[4004], '01/08/01/13/02/13/01/13/01/01/02/03/03/11/00', 3), 
   4005: (
        4504, NPCToonNames[4005], '01/03/03/04/00/04/01/04/01/01/24/04/04/00/00', 3), 
   4006: (
        4503, NPCToonNames[4006], '01/03/00/21/04/21/01/21/01/01/08/04/04/08/00', 1), 
   4007: (
        4503, NPCToonNames[4007], '00/03/01/12/01/12/01/12/01/01/01/03/03/19/00', 1), 
   4008: (
        4506, NPCToonNames[4008], '01/07/01/04/01/04/01/04/01/01/07/05/05/09/00', 2), 
   3228: (
        3730, NPCToonNames[3228], '01/08/02/11/02/11/01/11/01/01/25/12/12/00/00', 0), 
   4010: (
        4508, NPCToonNames[4010], '00/05/00/12/01/12/01/12/00/00/01/05/05/10/00', 6), 
   4011: (
        4508, NPCToonNames[4011], '00/00/03/04/00/04/01/04/00/00/01/05/05/04/00', 6), 
   4012: (
        4508, NPCToonNames[4012], '01/00/02/19/00/19/01/19/00/00/10/08/08/00/00', 6), 
   4013: (
        4000, NPCToonNames[4013], '00/02/03/19/02/03/00/19/00/00/01/08/08/12/00', 8), 
   4014: (
        4000, NPCToonNames[4014], '01/02/00/19/04/24/01/19/00/00/00/24/24/12/00', 8), 
   3229: (
        3731, NPCToonNames[3229], '01/08/01/02/01/02/01/02/01/01/00/12/12/07/00', 0), 
   9136: (
        9153, NPCToonNames[9136], '00/03/03/17/00/17/02/17/01/01/01/00/00/06/00', 5), 
   9306: (
        -1, NPCToonNames[9306], '00/01/06/05/01/05/00/05/01/00/00/00/00/04/00', 0), 
   3230: (
        3735, NPCToonNames[3230], '00/03/03/17/02/17/01/17/01/01/01/08/08/14/00', 0), 
   3002: (
        3508, NPCToonNames[3002], '00/00/01/04/01/04/01/04/01/01/00/09/09/18/00', 3), 
   3003: (
        3508, NPCToonNames[3003], '01/01/06/19/00/19/01/19/01/01/25/22/22/00/00', 3), 
   3004: (
        3508, NPCToonNames[3004], '00/01/04/12/02/12/01/12/01/01/00/10/10/12/00', 3), 
   3005: (
        3508, NPCToonNames[3005], '00/08/03/04/01/04/01/04/00/00/00/11/11/09/00', 3), 
   3006: (
        3507, NPCToonNames[3006], '00/08/02/18/00/18/01/18/00/00/00/11/11/02/00', 1), 
   3007: (
        3507, NPCToonNames[3007], '01/08/01/12/05/12/01/12/00/00/08/25/25/05/00', 1), 
   3008: (
        3509, NPCToonNames[3008], '00/03/03/04/01/04/02/04/00/00/00/12/12/17/00', 2), 
   3009: (
        3000, NPCToonNames[3009], '01/03/00/19/02/19/02/19/00/00/04/26/26/23/00', 5), 
   3010: (
        3511, NPCToonNames[3010], '00/03/01/10/00/10/02/10/00/00/00/12/12/11/00', 6), 
   3011: (
        3511, NPCToonNames[3011], '01/07/01/03/04/03/02/03/01/01/26/26/26/00/00', 6), 
   3012: (
        3511, NPCToonNames[3012], '00/05/02/18/01/18/02/18/01/01/00/12/12/01/00', 6), 
   3013: (
        3000, NPCToonNames[3013], '00/00/01/17/00/18/01/17/01/01/01/07/07/09/00', 8), 
   3014: (
        3000, NPCToonNames[3014], '01/00/00/16/03/17/01/16/00/00/00/24/24/09/00', 8), 
   9207: (
        9709, NPCToonNames[9207], '01/05/00/24/00/24/00/24/36/25/09/00/00/00/00', 0), 
   9208: (
        9705, NPCToonNames[9208], '00/01/06/20/01/20/00/20/46/35/06/00/00/00/00', 0), 
   2001: (
        2513, NPCToonNames[2001], '00/01/04/17/01/17/01/17/03/03/09/09/09/04/00', 0), 
   2002: (
        2514, NPCToonNames[2002], '00/05/00/04/02/04/02/04/00/00/01/03/03/18/00', 14), 
   2003: (
        2516, NPCToonNames[2003], '00/00/03/18/01/18/02/18/00/00/01/04/04/15/00', 0), 
   2004: (
        2521, NPCToonNames[2004], '01/03/03/07/04/15/01/05/03/03/00/05/05/03/00', 2), 
   2005: (
        2518, NPCToonNames[2005], '00/00/01/04/02/04/02/04/00/00/01/04/04/09/00', 0), 
   2006: (
        2519, NPCToonNames[2006], '00/01/06/18/02/18/02/18/01/01/01/04/04/02/00', 1), 
   2007: (
        2520, NPCToonNames[2007], '00/01/04/10/01/10/02/10/01/01/01/05/05/20/00', 3), 
   2008: (
        2520, NPCToonNames[2008], '00/08/03/03/00/03/02/03/01/01/01/05/05/17/00', 3), 
   2009: (
        2520, NPCToonNames[2009], '01/08/02/18/04/18/02/18/01/01/11/08/08/00/00', 3), 
   2010: (
        2520, NPCToonNames[2010], '01/08/01/11/02/11/02/11/01/01/08/08/08/04/00', 3), 
   2011: (
        2519, NPCToonNames[2011], '01/03/03/02/01/02/02/02/01/01/23/09/09/00/00', 1), 
   2012: (
        2000, NPCToonNames[2012], '00/03/00/17/02/17/02/17/01/01/01/06/06/01/00', 5), 
   2013: (
        2522, NPCToonNames[2013], '00/03/01/09/01/09/02/09/00/00/01/07/07/19/00', 6), 
   2014: (
        2522, NPCToonNames[2014], '01/07/01/02/01/02/01/02/00/00/01/12/12/00/00', 6), 
   2015: (
        2522, NPCToonNames[2015], '00/05/02/17/02/17/01/17/00/00/01/08/08/13/00', 6), 
   2016: (
        2000, NPCToonNames[2016], '00/06/01/09/02/10/01/09/00/00/00/03/03/18/00', 8), 
   2017: (
        2000, NPCToonNames[2017], '01/06/00/09/05/10/01/09/00/00/00/23/23/05/00', 8), 
   2018: (
        2513, NPCToonNames[2018], '00/08/03/15/00/15/00/15/99/86/39/00/00/00/00', 11), 
   2019: (
        2513, NPCToonNames[2019], '00/04/01/09/02/09/02/09/98/86/38/00/00/00/00', 11), 
   2020: (
        2513, NPCToonNames[2020], '00/05/00/20/01/20/01/20/97/86/37/00/00/00/00', 11), 
   1001: (
        1506, NPCToonNames[1001], '00/03/00/10/01/10/02/10/00/00/00/11/11/00/00', 1), 
   1002: (
        1506, NPCToonNames[1002], '00/07/00/03/00/03/02/03/01/01/00/10/10/18/00', 1), 
   1003: (
        1507, NPCToonNames[1003], '00/07/01/17/00/17/02/17/01/01/00/11/11/15/00', 3), 
   1004: (
        1507, NPCToonNames[1004], '01/05/02/10/04/10/02/10/01/01/24/24/24/00/00', 3), 
   1005: (
        1507, NPCToonNames[1005], '00/05/00/03/01/03/02/03/01/01/00/11/11/09/00', 3), 
   1006: (
        1507, NPCToonNames[1006], '01/00/03/18/00/18/02/18/01/01/19/25/25/00/00', 3), 
   1007: (
        1508, NPCToonNames[1007], '00/00/02/09/02/09/01/09/01/01/00/12/12/20/00', 2), 
   1008: (
        1000, NPCToonNames[1008], '00/00/01/03/01/03/01/03/00/00/00/00/00/17/00', 5), 
   1009: (
        1510, NPCToonNames[1009], '00/01/06/17/00/17/01/17/00/00/00/00/00/14/00', 6), 
   1010: (
        1510, NPCToonNames[1010], '01/01/04/10/05/10/01/10/00/00/26/00/00/00/00', 6), 
   1011: (
        1510, NPCToonNames[1011], '01/08/03/01/03/01/01/01/00/00/04/01/01/25/00', 6), 
   1012: (
        1000, NPCToonNames[1012], '00/08/01/03/01/14/02/03/00/00/00/01/01/13/00', 8), 
   1013: (
        1000, NPCToonNames[1013], '01/08/00/03/01/02/01/03/01/01/05/06/06/06/00', 8), 
   5110: (
        5627, NPCToonNames[5110], '00/05/02/10/02/10/02/10/00/00/00/08/08/18/00', 3), 
   5111: (
        5627, NPCToonNames[5111], '01/05/00/02/02/02/02/02/00/00/07/12/12/04/00', 3), 
   5112: (
        5627, NPCToonNames[5112], '01/00/03/17/01/17/02/17/00/00/14/21/21/00/00', 3), 
   5113: (
        5601, NPCToonNames[5113], '01/00/00/10/05/10/02/10/00/00/03/21/21/02/00', 0), 
   5114: (
        5603, NPCToonNames[5114], '00/00/01/02/01/02/02/02/01/01/00/09/09/02/00', 0), 
   5115: (
        5604, NPCToonNames[5115], '01/01/06/17/01/17/02/17/01/01/10/22/22/00/00', 0), 
   5116: (
        5605, NPCToonNames[5116], '00/01/04/09/02/09/02/09/01/01/00/09/09/17/00', 0), 
   5117: (
        5606, NPCToonNames[5117], '01/08/03/01/04/01/02/01/01/01/17/23/23/00/00', 0), 
   5118: (
        5608, NPCToonNames[5118], '00/08/02/16/01/16/02/16/01/01/00/10/10/11/00', 0), 
   5119: (
        5609, NPCToonNames[5119], '00/08/01/09/00/09/02/09/01/01/00/10/10/06/00', 0)}
NPCEnter_Pointless_Dialogue = [
 'Hello there.', 'How are you, %s?', 'Hi there.', 'Hello, %s.',
 'Hello there, %s.', 'Hi, %s.', 'Can I help you?', 'You can unlock new areas in Toontown by completing Quests.',
 'You can tell the difference between Cog departments by looking at their suit design.',
 'Play minigames at the Minigame Area to earn jellybeans.',
 "Have you seen The Karnival Kid? It's right at the beginning of Punchline Place.",
 'Visit Toon Cinemas and watch old Mickey Mouse cartoons to refill your Laff meter!',
 'Unlock new Gag tracks by completing Quests.',
 'You can see what District you are in by looking in your Shticker Book.',
 'If you encounter any glitches or strange things during gameplay, you can report them to\nduckyduck1553@coginvasion.com.',
 'Remember to pick up the jellybeans that Cogs drop when they explode!',
 'Defeat Cogs to gain experience and unlock new Gags!',
 'Complete Quests to gain Laff points!',
 "I'm a little busy right now, %s.",
 'Yes?',
 'Return completed Quests to any HQ Officer or the Toon that gave you the Quest.',
 'Get new Quests from any HQ Officer in any Toon HQ building.',
 'Watch out for Cog Tournaments! They can be difficult to do alone.',
 'You can leave any Cog battle you are in by teleporting away using your Shticker Book.',
 'Throw wisely! Using a gag that is too strong for a Cog will not give you any experience towards that Gag track.',
 'You can see all of your unlocked Gags on the Inventory page in your Shticker Book.',
 'You can switch out Gags that you want to use on the Backpack page in your Shticker Book.',
 'I heard Coach is selling Pie Turrets that can aid you in Cog Battles!',
 'Welcome to %s!']
NPCEnter_MFCO_Dialogue = ['%s, you must finish the current Quest I gave you before returning.',
 'Please finish the Quest I gave to you before returning.',
 'Back so soon, %s? Finish your Quest, then come back.',
 "You're back early, %s. You have to finish the Quest I gave you."]
NPCEnter_HQ_PickQuest = 'Choose a Quest.'
NPCEnter_HQ_FinishCurrentQuest = 'Sorry, but you need to finish your current Quest before I can give you another one.'
zone2NpcDict = None
if zone2NpcDict == None:
    zone2NpcDict = {}
    for id, npcData in NPCToonDict.items():
        zoneId = npcData[0]
        if zoneId in zone2NpcDict:
            zone2NpcDict[zoneId].append(id)
        else:
            zone2NpcDict[zoneId] = [
             id]

PunchlinePlace = 'Punchline Place'
SillyStreet = 'Silly Street'
LoopyLane = 'Loopy Lane'
BarnacleBoulevard = 'Barnacle Boulevard'
SeaweedStreet = 'Seaweed Street'
LighthouseLane = 'Lighthouse Lane'
AltoAvenue = 'Alto Avenue'
BaritoneBoulevard = 'Baritone Boulevard'
TenorTerrace = 'Tenor Terrace'
ElmStreet = 'Elm Street'
MapleStreet = 'Maple Street'
OakStreet = 'Oak Street'
SleetStreet = 'Sleet Street'
WalrusWay = 'Walrus Way'
PolarPlace = 'Polar Place'
LullabyLane = 'Lullaby Lane'
PajamaPlace = 'Pajama Place'
WallStreet = 'Wall Street'
ProprietaryPlace = 'Proprietary Place'
LimitedLiabilityLane = 'Limited Liability Lane'
BranchZone2StreetName = {2100: SillyStreet, 
   2300: PunchlinePlace, 
   2200: LoopyLane, 
   1300: LighthouseLane, 
   1200: SeaweedStreet, 
   1100: BarnacleBoulevard, 
   4100: AltoAvenue, 
   4200: BaritoneBoulevard, 
   4300: TenorTerrace, 
   3100: WalrusWay, 
   3200: SleetStreet, 
   3300: PolarPlace, 
   9100: LullabyLane, 
   9200: PajamaPlace, 
   5100: ElmStreet, 
   5200: MapleStreet, 
   5300: OakStreet, 
   22100: WallStreet, 
   22300: ProprietaryPlace, 
   22200: LimitedLiabilityLane, 
   21300: LighthouseLane, 
   21200: SeaweedStreet, 
   21100: BarnacleBoulevard, 
   24100: AltoAvenue, 
   24200: BaritoneBoulevard, 
   24300: TenorTerrace, 
   23100: WalrusWay, 
   23200: SleetStreet, 
   23300: PolarPlace, 
   29100: LullabyLane, 
   29200: PajamaPlace, 
   25100: ElmStreet, 
   25200: MapleStreet, 
   25300: OakStreet}
ToonTips = [
 "Look for a sign labeled 'Cog Battle' in any playground to be taken to battle.",
 'Try to use weaker gags when around weaker Cogs to conserve Jellybeans.',
 'You can use the Gags page in your Shticker Book to change the Gags you can use.',
 'Press ALT or click the Throw Gag button to use a Gag!',
 'You can click on other Toons to make friends with them!',
 'The Friends List is unlimited for now!',
 'Any blank spots you see on the Gags page in your Shticker Book represent Gags that are not implemented yet.',
 'Be sure to report a bug or crash when you run into one!',
 'Play Minigames at the Minigame Area to earn more Jellybeans!',
 'The only Minigame that works as single player is UNO.',
 'Different Minigames give different amounts of jellybeans.',
 'You can choose between Capture the Flag, King of the Hill, and Casual Mode in Toon Battle!',
 'You can choose between the Pistol, Shotgun, and the Sniper in Toon Battle!',
 'You can play with up to 7 other Toons in Toon Battle!',
 'You can choose between the Blue Bloodsuckers and the Red Robber Barons in Toon Battle!',
 'Wild Cards in UNO allow you to choose any color you want.',
 'When playing the Race Game, try to not press the same arrow key more than once, without pressing the other one.',
 'In the Race Game, everytime your Power Bar hits the top, your Boost Bar starts to fill!',
 'In the Race Game, press CONTROL to use Boost when the bar is full.',
 'Winning Toon Battle gives the most Jellybeans!',
 'It takes 5 seconds for your Camera to recharge in Camera Shy.',
 'Pictures only register in Camera Shy if the view finder is green.',
 'Waltz right in to any Gag Shop around OToontown to restock your gags!',
 'You can talk to Goofy in any Cog Battle area to restock your gags.',
 'You can talk to Coach in any Cog Battle area to buy Pie Turrets and Laff points.',
 "Make sure to put your Pie Turret in the best spot you can -- it can't be moved after it's been placed!",
 'Level 12 Cogs can do up to 36 damage!',
 'Each area has different level Cogs.',
 'When taking over Cog Office Buildings, make sure to have all your Laff points!',
 'You can go to the Minigame Area by using your Shticker Book.',
 'You can change your screen resolution on the Options page in your Shticker Book.',
 'You can change whether you play the game in fullscreen or in a window using the Options page in your Shticker Book.',
 'You can turn Anti-Aliasing off and on using the Options Page in your Shticker Book.',
 'You can turn Anisotropic Filtering off and on using the Options page in your Shticker Book.',
 'You can change the way the game looks using the Options Page in the Shticker Book.',
 'You can switch Districts by using the Districts Page in your Shticker Book.',
 'You can see the population of the District you are in on the Districts Page in your Shticker Book.',
 'The types of events that happen during Cog battles in playgrounds are all random.',
 'Watch out for Cog Tournaments -- they can be tricky to do alone!',
 'A Cog Invasion is the most common type of Cog spawn in playground battles.',
 'You can enter a playground Cog battle with up to 8 Toons!',
 'You must wait until a used Gag has completed before being able to use another one.',
 'Use Toon-Up gags to heal fellow Toons at any time!',
 'Use Squirt or Throw gags on fellow Toons to heal them up!',
 'Some gags (mostly Drop gags) require you to aim where you want them to go using your mouse.']