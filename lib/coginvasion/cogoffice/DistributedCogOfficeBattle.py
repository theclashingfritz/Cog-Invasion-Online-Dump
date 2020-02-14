# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogoffice.DistributedCogOfficeBattle
from panda3d.core import Point3, Vec3, NodePath, TextureStage
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObject import DistributedObject
from direct.distributed.ClockDelta import globalClockDelta
from direct.interval.IntervalGlobal import LerpPosInterval, LerpHprInterval, Sequence, Wait, Func, LerpQuatInterval, Parallel
from direct.fsm import ClassicFSM, State
from lib.coginvasion.minigame import DistributedMinigame
from lib.coginvasion.nametag import NametagGlobals
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.cog import Dept, SuitBank
from ElevatorUtils import *
from ElevatorConstants import *
from CogOfficeConstants import *
import random
PROPS = {'photo_frame': 'phase_7/models/props/photo_frame.egg', 'photo_frame_bh': 'phase_7/models/props/photo_frame_blackholes.bam', 
   'rug': 'phase_3.5/models/modules/rug.bam', 
   'rugA': 'phase_5.5/models/estate/rugA.bam', 
   'rugB': 'phase_5.5/models/estate/rugB.bam', 
   'couch_2person': 'phase_3.5/models/modules/couch_2person.bam', 
   'LB_chairA': 'phase_11/models/lawbotHQ/LB_chairA.bam', 
   'computer_monitor': 'phase_7/models/props/computer_monitor.egg', 
   'coffee_cup': 'phase_7/models/props/coffee_cup.egg', 
   'fax_paper': 'phase_7/models/props/fax_paper.egg', 
   'phone': [
           'phase_3.5/models/props/phone.bam',
           'phase_3.5/models/props/receiver.bam'], 
   'bookshelfB': 'phase_11/models/lawbotHQ/LB_bookshelfB.bam', 
   'bookshelfA': 'phase_11/models/lawbotHQ/LB_bookshelfA.bam', 
   'plant': 'phase_11/models/lawbotHQ/LB_pottedplantA.bam', 
   'clock': 'phase_7/models/props/clock.egg', 
   'meeting_table': 'phase_7/models/props/meeting_table.egg', 
   'square_shadow': 'phase_3/models/props/square_drop_shadow.bam', 
   'shadow': 'phase_3/models/props/drop_shadow.bam', 
   'BR_sky': 'phase_3.5/models/props/BR_sky.bam', 
   'tv_on_wall': 'phase_7/models/props/cogtv.egg'}

class Elevator:
    BLDG = 0
    COGDO = 1

    def __init__(self, elevatorMdl, cogdoElev):
        self.elevatorMdl = elevatorMdl
        self.cogdoElev = cogdoElev
        self.activeElev = None
        self.leftDoor = None
        self.rightDoor = None
        return

    def setActiveElev(self, index):
        if self.activeElev is not None:
            self.activeElev.reparentTo(hidden)
        if index == Elevator.BLDG:
            print 'setting active elev to BLDG'
            self.activeElev = self.elevatorMdl
        else:
            if index == Elevator.COGDO:
                print 'setting active elev to COGDO'
                self.activeElev = self.cogdoElev
        self.activeElev.reparentTo(render)
        self.leftDoor = getLeftDoor(self.activeElev)
        self.rightDoor = getRightDoor(self.activeElev)
        return

    def getRightDoor(self):
        return self.rightDoor

    def getLeftDoor(self):
        return self.leftDoor

    def getElevatorModel(self):
        return self.activeElev

    def cleanup(self):
        self.elevatorMdl.removeNode()
        del self.elevatorMdl
        self.cogdoElev.removeNode()
        del self.cogdoElev
        del self.rightDoor
        del self.leftDoor
        del self.activeElev


class CogTV(NodePath):

    def __init__(self):
        NodePath.__init__(self, 'cogtv')
        self.mdl = loader.loadModel(PROPS['tv_on_wall'])
        self.mdl.reparentTo(self)
        ts = TextureStage('tvts')
        self.videoTex = loader.loadTexture('phase_7/videos/cogtv.avi')
        self.find('**/tv_screen').setTexture(ts, self.videoTex)
        self.find('**/tv_screen').setTexRotate(ts, 90)
        self.videoTex.setLoop(1)
        self.videoTex.play()

    def removeNode(self):
        self.mdl.removeNode()
        del self.mdl
        self.videoTex.stop()
        del self.videoTex
        NodePath.removeNode(self)


class DistributedCogOfficeBattle(DistributedObject):
    notify = directNotify.newCategory('DistributedCogOfficeBattle')
    CEILING_COLOR = (187.0 / 255, 174.0 / 255, 155.0 / 255)
    FLOOR_NAMES = {RECEPTION_FLOOR: 'Reception Floor', EXECUTIVE_FLOOR: 'Executive Floor', 
       CONFERENCE_FLOOR: 'Conference Floor', 
       LOUNGE_FLOOR: 'Lounge Floor'}
    UNIQUE_FLOORS = []
    UNIQUE_FLOOR_NAMES = {Dept.BOSS: {1: 'Stock Floor', 2: 'Board of Directors Floor', 3: 'Human Resources Floor'}, Dept.SALES: {1: 'Marketing Floor', 2: 'Advertising Floor', 3: 'Telemarketing Floor'}, Dept.LAW: {1: "Attorney's Floor", 2: 'Paralegal Floor', 3: 'Document Management Floor'}, Dept.CASH: {1: 'Accounting Floor', 2: 'Budgeting Floor', 3: 'Treasury Floor'}}
    DEPT_2_PAINTING = {Dept.BOSS: [
                 'phase_7/maps/Bossbot_C_E_O_oil.jpg', 'phase_7/maps/BossbotHQ_oil.jpg'], 
       Dept.LAW: [
                'phase_7/maps/Lawbot_C_J_oil.jpg', 'phase_7/maps/LawbotHQ_oil.jpg'], 
       Dept.CASH: [
                 'phase_7/maps/Cashbot_C_F_O_oil.jpg', 'phase_7/maps/CashbotHQ_oil.jpg'], 
       Dept.SALES: [
                  'phase_7/maps/Sellbot_V_P_oil.jpg', 'phase_7/maps/SellbotHQ_oil.jpg', 'phase_7/maps/SellbotBldg_oil.jpg']}
    TOP_FLOOR_TAUNT = "I'm the boss."
    ROOM_DATA = {RECEPTION_FLOOR: {'props': [
                                 [
                                  'photo_frame', -42.86, 0.72, 8.0, 0, 0, 90, 1],
                                 [
                                  'rug', 0, 0, 0, 90, 0, 0, 1],
                                 [
                                  'couch_2person', -23.68, 26.89, 0, 0, 0, 0, 1.25],
                                 [
                                  'LB_chairA', -19.7, -6.5, 0, 180, 0, 0, 1],
                                 [
                                  'LB_chairA', -24, -6.5, 0, 180, 0, 0, 1],
                                 [
                                  'LB_chairA', 2.73, 19.46, 0, 330.95, 0, 0, 1],
                                 [
                                  'computer_monitor', 0.19, 14.21, 3.01, 335.06, 0, 0, 1],
                                 [
                                  'coffee_cup', -1.66, 15.88, 3.01, 0, 0, 0, 1],
                                 [
                                  'phone', 3.17, 13.35, 2.97, 171.47, 0, 0, 1],
                                 [
                                  'fax_paper', -3.32, 17.81, 3.01, 127.2, 0, 0, 1],
                                 [
                                  'fax_paper', -3.32, 17.81, 3.005, 147.53, 0, 0, 1]], 
                         'elevators': [
                                     [
                                      0.74202, -9.50081, 0, 180, 0, 0],
                                     [
                                      -39.49848, 20.74907, 0, 90, 0, 0]], 
                         'room_sections': [], 'room_mdl': 'phase_7/models/modules/cog_bldg_reception_flr.bam', 
                         'grounds': [
                                   '**/floor']}, 
       EXECUTIVE_FLOOR: {'props': [
                                 [
                                  'BR_sky', 0, 0, -125, 0, 0, 0, 1],
                                 [
                                  'rug', -65.579, 10.385, 0, 0, 0, 0, 1],
                                 [
                                  'computer_monitor', -65.39, -8.6, 4, 180, 0, 0, 1],
                                 [
                                  'coffee_cup', -62.89, -8.93, 4, 318.81, 0, 0, 1],
                                 [
                                  'phone', -69.97, -9.22, 4, 18.82, 0, 0, 1],
                                 [
                                  'fax_paper', -67.65, -9.04, 4.01, 19.18, 0, 0, 1],
                                 [
                                  'fax_paper', -67.48, -9.22, 4.02, 343.74, 0, 0, 1],
                                 [
                                  'clock', -23.238, 9.498, 9.774, 0, 0, -90, 1],
                                 [
                                  'plant', -27.48, 17.63, 0, 132.71, 0, 0, 12],
                                 [
                                  'photo_frame_bh', -40.64, -22.54, 7.99, 90, 0, 90, 1],
                                 [
                                  'rug', -0.154, 97.92, 0, -90, 0, 0, 1],
                                 [
                                  'computer_monitor', -7.03, 38.038, 4.041, -19.157, 0, 0, 1],
                                 [
                                  'computer_monitor', 8.556, 61.953, 4.041, 151.592, 0, 0, 1],
                                 [
                                  'phone', 0.248, 37.86, 4.029, 187.058, 0, 0, 1],
                                 [
                                  'phone', 1.401, 62.189, 4.029, -2.193, 0, 0, 1],
                                 [
                                  'coffee_cup', -10.467, 40.465, 4.048, 51.974, 0, 0, 1],
                                 [
                                  'coffee_cup', 11.361, 57.896, 4.048, 222.722, 0, 0, 1],
                                 [
                                  'coffee_cup', -0.512, 61.659, 4.006, 22.722, 0, 0, 1],
                                 [
                                  'fax_paper', 5.12, 62.087, 4.104, -0.707, 0, 0, 1],
                                 [
                                  'fax_paper', 5.916, 61.809, 4.136, -41.476, 0, 0, 1],
                                 [
                                  'fax_paper', 11.564, 55.186, 4.104, -59.581, 0, 0, 1],
                                 [
                                  'fax_paper', 11.298, 53.671, 4.136, 259.65, 0, 0, 1],
                                 [
                                  'fax_paper', -4.269, 37.509, 4.136, -56.235, 0, 0, 1],
                                 [
                                  'fax_paper', -3.449, 37.361, 4.104, 188.545, 0, 0, 1],
                                 [
                                  'fax_paper', 2.398, 37.509, 4.136, 240.206, 0, 0, 1],
                                 [
                                  'fax_paper', 3.218, 37.361, 4.104, 188.545, 0, 0, 1],
                                 [
                                  'LB_chairA', -4.365, 45.791, 0, -26.36, 0, 0, 1],
                                 [
                                  'LB_chairA', 4.786, 53.639, 0, 154.075, 0, 0, 1],
                                 [
                                  'LB_chairA', -65.39, -14.79, 0, 180, 0, 0, 1],
                                 [
                                  'photo_frame', 27.72, 43.508, 8.515, 180, 0, 90, 1],
                                 [
                                  'clock', 1.507, -20.368, 9.956, 90, 180, 90, 1],
                                 [
                                  'plant', -19.403, 102.276, 0, 0, 0, 0, 12],
                                 [
                                  'plant', 20.816, 101.992, 0, 0, 0, 0, 12],
                                 [
                                  'meeting_table', 17.88, 1.69, 0, 0, 0, 0, 1],
                                 [
                                  'square_shadow', 17.88, 1.69, 0, 0, 0, 0, Point3(2, 3.5, 1)],
                                 [
                                  'LB_chairA', 17.86, -12.04, 0, 180, 0, 0, 1],
                                 [
                                  'LB_chairA', 17.86, 14.93, 0, 0, 0, 0, 1],
                                 [
                                  'LB_chairA', 8.932, -2.7, 0, 90, 0, 0, 1],
                                 [
                                  'LB_chairA', 8.932, 5.559, 0, 90, 0, 0, 1],
                                 [
                                  'fax_paper', 17.91, -7.17, 3.42, 0, 0, 0, 1],
                                 [
                                  'fax_paper', 13.67, -2.82, 3.389, 280.499, 0, 0, 1],
                                 [
                                  'fax_paper', 13.67, 5.33, 3.412, 270, 0, 0, 1],
                                 [
                                  'fax_paper', 17.681, 10.56, 3.424, 180, 0, 0, 1]], 
                         'elevators': [
                                     [
                                      -73.22, 11.08, 0, 90, 0, 0],
                                     [
                                      0.22, 105.86, 0, 0, 0, 0]], 
                         'room_sections': [
                                         'short_floor_coll', 'long_floor_coll_part1', 'long_floor_coll_part2'], 
                         'room_mdl': 'phase_7/models/modules/cog_bldg_executive_flr.bam', 
                         'grounds': [
                                   '**/short_floor', '**/long_floor']}, 
       CONFERENCE_FLOOR: {'props': [
                                  [
                                   'BR_sky', 0, 0, -100, 0, 0, 0, 1],
                                  [
                                   'photo_frame', 16.26, 63.84, 8.34, 270.0, 0, 90.0, 1],
                                  [
                                   'bookshelfA', -22.11, 49.88, 0.01, 90.0, 0, 0, 1.5],
                                  [
                                   'bookshelfB', -22.11, 35, 0.01, 90, 0, 0, 1.5],
                                  [
                                   'plant', 20.51, -5.13, 0, 0, 0, 0, 12],
                                  [
                                   'rug', 0, 0, 0, 0, 0, 0, 1],
                                  [
                                   'rug', 0, 52, 0, 0, 0, 0, 1],
                                  [
                                   'clock', 23.68, 20.95, 9.67, 0, 0, 90, 1],
                                  [
                                   'LB_chairA', 20.7, 8.14, 0, 270, 0, 0, 1],
                                  [
                                   'computer_monitor', 13.73, 8.17, 3.99, 270, 0, 0, 1],
                                  [
                                   'coffee_cup', 14.25, 10.65, 3.99, 78.69, 0, 0, 1],
                                  [
                                   'phone', 14.2, 5.29, 3.99, 95.96, 0, 0, 1.2],
                                  [
                                   'fax_paper', 14.54, 13.34, 4.01, 63.43, 0, 0, 1],
                                  [
                                   'fax_paper', 14.43, 0.72, 4.01, 270, 0, 0, 1],
                                  [
                                   'fax_paper', 16.8, 1.14, 4.01, 118.61, 0, 0, 1],
                                  [
                                   'meeting_table', -12.7, 5.94, 0, 0, 0, 0, 1],
                                  [
                                   'LB_chairA', -22.02, 1.57, 0, 90.0, 0, 0, 1],
                                  [
                                   'LB_chairA', -22.02, 10.23, 0, 90.0, 0, 0, 1],
                                  [
                                   'LB_chairA', -13.13, 19.73, 0, 0, 0, 0, 1],
                                  [
                                   'square_shadow', -12.7, 5.94, 0.01, 0, 0, 0, Point3(2, 3.5, 1)],
                                  [
                                   'fax_paper', -16.71, 1.57, 3.4, 270, 0, 0, 1],
                                  [
                                   'fax_paper', -16.71, 10.23, 3.4, 270, 0, 0, 1],
                                  [
                                   'fax_paper', -13.44, 14.8, 3.41, 180, 0, 0, 1],
                                  [
                                   'fax_paper', -13.44, 14.8, 3.4, 150, 0, 0, 1]], 
                          'elevators': [
                                      [
                                       0.23007, 60.47556, 0, 0, 0, 0],
                                      [
                                       0.74202, -9.50081, 0, 180, 0, 0]], 
                          'room_sections': [], 'room_mdl': 'phase_7/models/modules/cog_bldg_conference_flr.bam', 
                          'grounds': [
                                    '**/floor', '**/floor1']}, 
       LOUNGE_FLOOR: {'props': [
                              [
                               'plant', -30.15, 3.54, 0, 0, 0, 0, 12],
                              [
                               'plant', 32.71, 3.54, 0, 0, 0, 0, 12],
                              [
                               'photo_frame', 21, -2.87, 8, 90, 0, 90, 1],
                              [
                               'couch_2person', -17.66, 3.87, 0, 180, 0, 0, 1.5],
                              [
                               'rugB', 0, 7.5, 0, 0, 0, 0, 6.09],
                              [
                               'rugB', -27.03, 63.42, 0, 90, 0, 0, 6.09],
                              [
                               'rug', 0, 40, 0, 0, 0, 0, 1.25],
                              [
                               'plant', -30.18, 77.41, 0, 0, 0, 0, 12],
                              [
                               'clock', -20.46, 82.96, 10.14, 0, 90, 0, 1],
                              [
                               'meeting_table', -30.64, 26.29, 0, 0, 0, 0, Vec3(0.51, 1.08, 1)],
                              [
                               'computer_monitor', -30.92, 18, 3.4, 270, 0, 0, 1],
                              [
                               'computer_monitor', -30.92, 25.7, 3.4, 270, 0, 0, 1],
                              [
                               'computer_monitor', -30.92, 33.78, 3.4, 270, 0, 0, 1],
                              [
                               'LB_chairA', -24, 18.25, 0, 270, 0, 0, 1],
                              [
                               'LB_chairA', -24, 26.03, 0, 270, 0, 0, 1],
                              [
                               'LB_chairA', -24, 33.93, 0, 270, 0, 0, 1],
                              [
                               'fax_paper', -28.86, 19.46, 3.4, 68.2, 0, 0, 1],
                              [
                               'fax_paper', -29, 24.21, 3.4, 102.72, 0, 0, 1],
                              [
                               'fax_paper', -28.75, 24.51, 3.41, 90, 0, 0, 1],
                              [
                               'fax_paper', -28.75, 33.98, 3.4, 90, 0, 0, 1],
                              [
                               'coffee_cup', -28.98, 27.76, 3.4, 59.04, 0, 0, 1],
                              [
                               'phone', -29.83, 29.51, 3.4, 90, 0, 0, 1],
                              [
                               'phone', -29.83, 21.15, 3.4, 90, 0, 0, 1],
                              [
                               'tv_on_wall', 36.44, 82.03, 12, 320, 0, 0, 1],
                              [
                               'LB_chairA', 18.01, 75.03, 0, 100.01, 0, 0, 1],
                              [
                               'LB_chairA', 20.18, 69.08, 0, 120.47, 0, 0, 1],
                              [
                               'LB_chairA', 24.8, 64.49, 0, 149.93, 0, 0, 1],
                              [
                               'LB_chairA', 30.8, 62.41, 0, 173.07, 0, 0, 1],
                              [
                               'couch_2person', 32.78, 13.41, 0, 270, 0, 0, 1.5],
                              [
                               'couch_2person', 32.78, 22.83, 0, 270, 0, 0, 1.5],
                              [
                               'bookshelfA', 34.7, 34.43, 0, 270, 0, 0, 1.5],
                              [
                               'BR_sky', 0, 0, -50, 0, 0, 0, 1],
                              [
                               'square_shadow', -30.64, 26.16, 0.01, 0, 0, 0, Vec3(1.09, 3.69, 1)]], 
                      'gagdoor': [
                                66.50544, 78.29003, 0, 90, 0, 0], 
                      'elevators': [
                                  [
                                   0, 0.5, 0, 180, 0, 0],
                                  [
                                   -33.75, 63.0, 0, 90, 0, 0]], 
                      'room_sections': [], 'room_mdl': 'phase_7/models/modules/cog_bldg_lounge_flr.egg', 
                      'grounds': [
                                '**/gagroom_small_floor', '**/gagroom_big_floor', '**/floor']}}

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.currentFloor = None
        self.numFloors = None
        self.dept = None
        self.deptClass = None
        self.floorModel = None
        self.exteriorZoneId = None
        self.bldgDoId = None
        self.avatars = None
        self.gagDoor = None
        self.floorNameText = DistributedMinigame.getAlertText((0.75, 0.75, 0.75, 1.0), 0.15)
        self.props = []
        self.elevators = []
        self.elevatorResponses = 0
        self.openSfx = base.loadSfx('phase_5/audio/sfx/elevator_door_open.ogg')
        self.closeSfx = base.loadSfx('phase_5/audio/sfx/elevator_door_close.ogg')
        self.rideElevatorMusic = base.loadMusic('phase_7/audio/bgm/tt_elevator.mid')
        self.bottomFloorsMusic = base.loadMusic('phase_7/audio/bgm/encntr_general_bg_indoor.mid')
        self.topFloorMusic = base.loadMusic('phase_7/audio/bgm/encntr_suit_winning_indoor.mid')
        self.intermissionMusic = base.loadMusic('phase_7/audio/bgm/encntr_toon_winning_indoor.mid')
        self.fsm = ClassicFSM.ClassicFSM('DistributedCogOfficeBattle', [State.State('off', self.enterOff, self.exitOff),
         State.State('floorIntermission', self.enterFloorIntermission, self.exitFloorIntermission),
         State.State('bldgComplete', self.enterBldgComplete, self.exitBldgComplete),
         State.State('battle', self.enterBattle, self.exitBattle),
         State.State('rideElevator', self.enterRideElevator, self.exitRideElevator),
         State.State('faceOff', self.enterFaceOff, self.exitFaceOff),
         State.State('victory', self.enterVictory, self.exitVictory)], 'off', 'off')
        self.fsm.enterInitialState()
        return

    def isTopFloor(self):
        return self.currentFloor >= self.numFloors - 1

    def enterBldgComplete(self):
        pass

    def exitBldgComplete(self):
        pass

    def doFaceoff(self, suitId, tauntIndex, timestamp):
        self.fsm.request('faceOff', [suitId, tauntIndex, globalClockDelta.localElapsedTime(timestamp)])

    def openRestockDoors(self):
        lDoorOpen = -3.9
        rDoorOpen = 3.5
        closed = 0.0
        leftDoor = self.gagDoor.find('**/left_door')
        rightDoor = self.gagDoor.find('**/right_door')
        self.gagDoor.find('**/door_collisions').removeNode()
        ival = Parallel(LerpPosInterval(leftDoor, 2.0, (lDoorOpen, 0, 0), (
         closed, 0, 0), blendType='easeOut'), LerpPosInterval(rightDoor, 2.0, (rDoorOpen, 0, 0), (
         closed, 0, 0), blendType='easeOut'))
        ival.start()
        loadout = base.localAvatar.backpack.getLoadout()
        sendLoadout = []
        for gag in loadout:
            sendLoadout.append(gag.getID())

        base.localAvatar.sendUpdate('requestSetLoadout', [sendLoadout])

    def enterVictory(self, ts):
        self.cr.playGame.getPlace().fsm.request('stop')
        base.localAvatar.b_setAnimState('win')
        base.taskMgr.doMethodLater(5.0, self.victoryTask, self.uniqueName('victoryTask'))

    def victoryTask(self, task):
        requestStatus = {'zoneId': self.exteriorZoneId, 
           'hoodId': self.cr.playGame.hood.id, 
           'bldgDoId': self.bldgDoId, 
           'loader': 'townLoader', 
           'where': 'street', 
           'world': CIGlobals.CogTropolis, 
           'shardId': None, 
           'wantLaffMeter': 1, 
           'avId': base.localAvatar.doId, 
           'how': 'elevatorIn'}
        self.cr.playGame.getPlace().fsm.request('teleportOut', [requestStatus])
        return task.done

    def exitVictory(self):
        base.taskMgr.remove(self.uniqueName('victoryTask'))

    def setExteriorZoneId(self, zoneId):
        self.exteriorZoneId = zoneId

    def setBldgDoId(self, doId):
        self.bldgDoId = doId

    def d_readyForNextFloor(self):
        self.sendUpdate('readyForNextFloor')

    def d_loadedFloor(self):
        self.sendUpdate('loadedFloor')

    def elevatorReady(self):
        self.elevatorResponses += 1
        if self.elevatorResponses >= len(self.elevators):
            self.sendUpdate('readyToStart')

    def setNumFloors(self, num):
        self.numFloors = num

    def setState(self, state, timestamp):
        self.fsm.request(state, [globalClockDelta.localElapsedTime(timestamp)])

    def setAvatars(self, avatars):
        self.avatars = avatars

    def setDept(self, dept):
        self.dept = dept
        if dept == 'c':
            self.deptClass = Dept.BOSS
        else:
            if dept == 'l':
                self.deptClass = Dept.LAW
            else:
                if dept == 's':
                    self.deptClass = Dept.SALES
                else:
                    if dept == 'm':
                        self.deptClass = Dept.CASH

    def enterOff(self, ts=0):
        base.transitions.fadeScreen(1)

    def exitOff(self):
        base.transitions.noTransitions()

    def getPoints(self, name):
        if self.currentRoom in self.UNIQUE_FLOORS:
            points = POINTS[self.deptClass][self.currentRoom][name]
        else:
            points = POINTS[self.currentRoom][name]
        return points

    def enterFaceOff(self, suitId, tauntIndex, ts):
        suit = self.cr.doId2do.get(suitId)
        if self.isTopFloor():
            song = self.topFloorMusic
            taunt = DistributedCogOfficeBattle.TOP_FLOOR_TAUNT
        else:
            song = self.bottomFloorsMusic
            taunt = CIGlobals.SuitFaceoffTaunts[suit.suitPlan.getName()][tauntIndex]
        base.playMusic(song, looping=1, volume=0.8)
        base.camLens.setMinFov(30.0 / (4.0 / 3.0))
        camera.reparentTo(suit)
        height = suit.getHeight()
        offsetPnt = Point3(0, 0, height)
        MidTauntCamHeight = height * 0.66
        MidTauntCamHeightLim = height - 1.8
        if MidTauntCamHeight < MidTauntCamHeightLim:
            MidTauntCamHeight = MidTauntCamHeightLim
        TauntCamY = 18
        TauntCamX = 0
        TauntCamHeight = random.choice((MidTauntCamHeight, 1, 11))
        camera.setPos(TauntCamX, TauntCamY, TauntCamHeight)
        camera.lookAt(suit, offsetPnt)

        def setCamRunY():
            camera.setY(camera.getY() + 5)

        self.faceOffTrack = Sequence()
        self.faceOffTrack.append(Func(suit.setAutoClearChat, False))
        self.faceOffTrack.append(Func(suit.setChat, taunt))
        self.faceOffTrack.append(Wait(3.5))
        self.faceOffTrack.append(Func(suit.nametag.clearChatText))
        self.faceOffTrack.append(Func(suit.setAutoClearChat, True))
        self.faceOffTrack.append(Func(base.camLens.setMinFov, CIGlobals.DefaultCameraFov / (4.0 / 3.0)))
        self.faceOffTrack.append(Func(base.localAvatar.attachCamera))
        self.faceOffTrack.append(Func(camera.lookAt, base.localAvatar.smartCamera.getLookAtPoint()))
        self.faceOffTrack.append(Func(setCamRunY))
        runTrack = Parallel()
        for i in xrange(len(self.avatars)):
            avId = self.avatars[i]
            toon = self.cr.doId2do.get(avId)
            if toon:
                toon.stopSmooth()
                toon.wrtReparentTo(render)
                points = self.getPoints('faceoff')
                point = points[i]
                pos = Point3(point[0], point[1], point[2])
                hpr = Vec3(point[3], point[4], point[5])
                toon.headsUp(pos)
                track = Sequence(Func(toon.setAnimState, 'run'), LerpPosInterval(toon, duration=1.0, pos=pos, startPos=toon.getPos(render)), Func(toon.setAnimState, 'walk'), LerpQuatInterval(toon, duration=1.0, hpr=hpr, startHpr=lambda toon=toon: toon.getHpr(render)), Func(toon.setAnimState, 'neutral'))
                runTrack.append(track)

        self.faceOffTrack.append(runTrack)
        self.faceOffTrack.start(ts)

    def exitFaceOff(self):
        self.faceOffTrack.finish()
        del self.faceOffTrack

    def enterRideElevator(self, ts):
        elevator = self.elevators[0]
        NametagGlobals.setWant2dNametags(False)
        base.camLens.setFov(CIGlobals.DefaultCameraFov)
        camera.reparentTo(elevator.getElevatorModel())
        camera.setPos(0, 14, 4)
        camera.setHpr(180, 0, 0)
        base.transitions.noTransitions()
        base.playMusic(self.rideElevatorMusic, volume=0.8, looping=1)
        self.elevatorTrack = getRideElevatorInterval()
        self.elevatorTrack.append(Func(self.__doFloorTextPulse))
        self.elevatorTrack.append(getOpenInterval(self, elevator.getLeftDoor(), elevator.getRightDoor(), self.openSfx, None))
        self.elevatorTrack.start(ts)
        return

    def __doFloorTextPulse(self):
        self.floorNameText.setText(DistributedCogOfficeBattle.FLOOR_NAMES[self.currentRoom])
        ival = DistributedMinigame.getAlertPulse(self.floorNameText, 0.17, 0.15)
        ival.start()

    def exitRideElevator(self):
        if hasattr(self, 'elevatorTrack'):
            self.elevatorTrack.finish()
            del self.elevatorTrack
        self.rideElevatorMusic.stop()
        base.camLens.setMinFov(CIGlobals.DefaultCameraFov / (4.0 / 3.0))

    def __handleEnteredRoomSection(self, entry):
        name = entry.getIntoNodePath().getName()
        index = self.getRoomData('room_sections').index(name)
        self.sendUpdate('enterSection', [index])

    def enterBattle(self, ts):
        NametagGlobals.setWant2dNametags(True)
        base.localAvatar.walkControls.setCollisionsActive(1)
        self.cr.playGame.getPlace().fsm.request('walk')
        base.localAvatar.hideBookButton()
        taskMgr.add(self.monitorHP, self.uniqueName('monitorHP'))
        for path in self.getRoomData('room_sections'):
            self.accept('enter' + path, self.__handleEnteredRoomSection)

    def monitorHP(self, task):
        if base.localAvatar.getHealth() < 1:
            taskMgr.doMethodLater(7.0, self.diedTask, self.uniqueName('diedTask'))
            return task.done
        return task.cont

    def diedTask(self, task):
        self.sendUpdate('iAmDead')
        return task.done

    def exitBattle(self):
        for path in self.getRoomData('room_sections'):
            self.ignore('enter' + path)

        self.bottomFloorsMusic.stop()
        taskMgr.remove(self.uniqueName('monitorHP'))

    def enterFloorIntermission(self, ts):
        self.topFloorMusic.stop()
        base.localAvatar.showBookButton()
        base.playMusic(self.intermissionMusic, looping=1, volume=0.8)

    def exitFloorIntermission(self):
        self.intermissionMusic.stop()

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        base.setBackgroundColor(self.CEILING_COLOR)
        self.cr.playGame.hood.sky.hide()
        self.cr.playGame.hood.setNoFog()
        self.loadElevators()

    def disable(self):
        taskMgr.remove(self.uniqueName('diedTask'))
        taskMgr.remove(self.uniqueName('monitorHP'))
        self.fsm.requestFinalState()
        del self.fsm
        if self.cr.playGame.hood is not None:
            self.cr.playGame.hood.sky.show()
        self.cleanupFloor()
        self.cleanupElevators()
        if self.floorNameText:
            self.floorNameText.destroy()
            self.floorNameText = None
        self.props = None
        self.currentFloor = None
        self.floorModel = None
        self.avatars = None
        self.elevators = None
        self.dept = None
        self.deptClass = None
        self.openSfx = None
        self.closeSfx = None
        self.rideElevatorMusic = None
        self.bottomFloorsMusic = None
        self.intermissionMusic = None
        self.bldgDoId = None
        self.exteriorZoneId = None
        if self.topFloorMusic:
            self.topFloorMusic.stop()
            self.topFloorMusic = None
        base.setBackgroundColor(CIGlobals.DefaultBackgroundColor)
        DistributedObject.disable(self)
        return

    def loadFloor(self, floorNum, room):
        base.transitions.fadeScreen(1.0)
        self.cleanupFloor()
        self.currentFloor = floorNum
        self.currentRoom = room
        self.loadRoom()
        self.loadProps()
        self.repositionElevators()
        if self.getRoomData('gagdoor') is not None:
            posHpr = self.getRoomData('gagdoor')
            self.gagDoor = loader.loadModel('phase_7/models/modules/gagroom_door.bam')
            self.gagDoor.reparentTo(render)
            self.gagDoor.setPosHpr(*posHpr)
        else:
            if self.currentRoom != EXECUTIVE_FLOOR:
                self.gagDoor = render.attachNewNode('gagDoor')
                flr = self.floorModel
                items = ['frame', 'trim', 'trim1', 'trim2', 'trim3', 'frame1', 'left_door', 'right_door', 'door_collisions']
                for item in items:
                    node = flr.find('**/' + item)
                    node.wrtReparentTo(self.gagDoor)

        self.d_loadedFloor()
        return

    def cleanupFloor(self):
        for prop in self.props:
            prop.removeNode()

        self.props = []
        if self.floorModel:
            self.floorModel.removeNode()
            self.floorModel = None
        if self.gagDoor:
            self.gagDoor.removeNode()
            self.gagDoor = None
        return

    def cleanupElevators(self):
        for elevator in self.elevators:
            elevator.cleanup()

        self.elevators = []

    def getRoomData(self, name):
        if self.currentRoom in self.UNIQUE_FLOORS:
            dataList = self.ROOM_DATA[self.deptClass][self.currentRoom].get(name)
        else:
            dataList = self.ROOM_DATA[self.currentRoom].get(name)
        return dataList

    def loadRoom(self):
        path = self.getRoomData('room_mdl')
        grounds = self.getRoomData('grounds')
        self.floorModel = loader.loadModel(path)
        self.floorModel.reparentTo(render)
        for ground in grounds:
            self.floorModel.find(ground).setBin('ground', 18)

    def loadProps(self):
        dataList = self.getRoomData('props')
        for propData in dataList:
            name = propData[0]
            otherProps = []
            if isinstance(PROPS[name], list):
                for i in xrange(len(PROPS[name])):
                    if i == 0:
                        continue
                    path = PROPS[name][i]
                    otherProps.append(path)

            x, y, z = propData[1], propData[2], propData[3]
            h, p, r = propData[4], propData[5], propData[6]
            scale = propData[7]
            if isinstance(PROPS[name], list):
                propMdl = loader.loadModel(PROPS[name][0])
            else:
                if name == 'tv_on_wall':
                    print 'TVONWALL'
                    propMdl = CogTV()
                else:
                    propMdl = loader.loadModel(PROPS[name])
            propMdl.reparentTo(render)
            propMdl.setPosHpr(x, y, z, h, p, r)
            propMdl.setScale(scale)
            if name == 'photo_frame':
                painting = random.choice(self.DEPT_2_PAINTING[self.deptClass])
                propMdl.find('**/photo').setTexture(loader.loadTexture(painting), 1)
            for oPropPath in otherProps:
                oPropMdl = loader.loadModel(oPropPath)
                oPropMdl.reparentTo(propMdl)

            self.props.append(propMdl)

    def loadElevators(self):
        for _ in xrange(2):
            elevMdl = loader.loadModel('phase_4/models/modules/elevator.bam')
            cogdoElevMdl = loader.loadModel('phase_7/models/modules/cogoffice_elevator.bam')
            elevator = Elevator(elevMdl, cogdoElevMdl)
            elevator.setActiveElev(Elevator.BLDG)
            self.elevators.append(elevator)

    def repositionElevators(self):
        dataList = self.getRoomData('elevators')
        if self.currentFloor == 0:
            if not self.isTopFloor():
                self.elevators[0].setActiveElev(Elevator.BLDG)
                self.elevators[1].setActiveElev(Elevator.COGDO)
            else:
                self.elevators[0].setActiveElev(Elevator.BLDG)
                self.elevators[1].setActiveElev(Elevator.BLDG)
        else:
            if self.currentFloor > 0 and self.isTopFloor():
                self.elevators[0].setActiveElev(Elevator.COGDO)
                self.elevators[1].setActiveElev(Elevator.BLDG)
            else:
                self.elevators[0].setActiveElev(Elevator.COGDO)
                self.elevators[1].setActiveElev(Elevator.COGDO)
        messenger.send(self.uniqueName('prepareElevator'))
        for i in xrange(len(dataList)):
            x, y, z, h, p, r = dataList[i]
            elevMdl = self.elevators[i].getElevatorModel()
            elevMdl.setPosHpr(x, y, z, h, p, r)
            npc = elevMdl.findAllMatches('**/floor_light_?;+s')
            for i in xrange(npc.getNumPaths()):
                np = npc.getPath(i)
                floor = int(np.getName()[-1:]) - 1
                if floor < self.numFloors:
                    np.setColor(LIGHT_OFF_COLOR)
                else:
                    np.hide()
                if self.currentFloor == floor:
                    np.setColor(LIGHT_ON_COLOR)