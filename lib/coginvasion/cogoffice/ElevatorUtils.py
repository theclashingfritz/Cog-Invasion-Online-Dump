# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.cogoffice.ElevatorUtils
from panda3d.core import Point3
from direct.interval.IntervalGlobal import Sequence, Wait, Func, LerpPosInterval, SoundInterval, Parallel
from ElevatorConstants import *

def getRightDoor(model):
    door = model.find('**/right-door')
    if door.isEmpty():
        door = model.find('**/right_door')
    return door


def getLeftDoor(model):
    door = model.find('**/left-door')
    if door.isEmpty():
        door = model.find('**/left_door')
    return door


def getDoors(model):
    return [
     getLeftDoor(model), getRightDoor(model)]


def getLeftClosePoint(type):
    width = ElevatorData[type]['width']
    return Point3(width, 0, 0)


def getRightClosePoint(type):
    width = ElevatorData[type]['width']
    return Point3(-width, 0, 0)


def getLeftOpenPoint(type):
    return Point3(0, 0, 0)


def getRightOpenPoint(type):
    return Point3(0, 0, 0)


def closeDoors(leftDoor, rightDoor, type=ELEVATOR_NORMAL):
    closedPosLeft = getLeftClosePoint(type)
    closedPosRight = getRightClosePoint(type)
    leftDoor.setPos(closedPosLeft)
    rightDoor.setPos(closedPosRight)


def openDoors(leftDoor, rightDoor, type=ELEVATOR_NORMAL):
    openPosLeft = getLeftOpenPoint(type)
    openPosRight = getRightOpenPoint(type)
    leftDoor.setPos(openPosLeft)
    rightDoor.setPos(openPosRight)


def getLeftOpenInterval(distObj, leftDoor, type):
    openTime = ElevatorData[type]['openTime']
    closedPos = getLeftClosePoint(type)
    openPos = getLeftOpenPoint(type)
    leftOpenInterval = LerpPosInterval(leftDoor, openTime, openPos, startPos=closedPos, blendType='easeOut', name=distObj.uniqueName('leftDoorOpen'))
    return leftOpenInterval


def getRightOpenInterval(distObj, rightDoor, type):
    openTime = ElevatorData[type]['openTime']
    closedPos = getRightClosePoint(type)
    openPos = getRightOpenPoint(type)
    rightOpenInterval = LerpPosInterval(rightDoor, openTime, openPos, startPos=closedPos, blendType='easeOut', name=distObj.uniqueName('rightDoorOpen'))
    return rightOpenInterval


def getCloseInterval(distObj, leftDoor, rightDoor, closeSfx, finalCloseSfx, type=ELEVATOR_NORMAL):
    left = getLeftCloseInterval(distObj, leftDoor, type)
    right = getRightCloseInterval(distObj, rightDoor, type)
    closeDuration = left.getDuration()
    sfxVolume = ElevatorData[type]['sfxVolume']
    if finalCloseSfx:
        sound = Sequence(SoundInterval(closeSfx, duration=closeDuration, volume=sfxVolume, node=leftDoor), SoundInterval(finalCloseSfx, volume=sfxVolume, node=leftDoor))
    else:
        sound = SoundInterval(closeSfx, volume=sfxVolume, node=leftDoor)
    return Parallel(sound, left, right)


def getOpenInterval(distObj, leftDoor, rightDoor, openSfx, finalOpenSfx, type=ELEVATOR_NORMAL):
    left = getLeftOpenInterval(distObj, leftDoor, type)
    right = getRightOpenInterval(distObj, rightDoor, type)
    openDuration = left.getDuration()
    sfxVolume = ElevatorData[type]['sfxVolume']
    if finalOpenSfx:
        sound = Sequence(SoundInterval(openSfx, duration=openDuration, volume=sfxVolume, node=leftDoor), SoundInterval(finalOpenSfx, volume=sfxVolume, node=leftDoor))
    else:
        sound = SoundInterval(openSfx, volume=sfxVolume, node=leftDoor)
    return Parallel(sound, left, right)


def getLeftCloseInterval(distObj, leftDoor, type):
    closeTime = ElevatorData[type]['closeTime']
    closedPos = getLeftClosePoint(type)
    openPos = getLeftOpenPoint(type)
    leftCloseInterval = LerpPosInterval(leftDoor, closeTime, closedPos, startPos=openPos, blendType='easeOut', name=distObj.uniqueName('leftDoorClose'))
    return leftCloseInterval


def getRightCloseInterval(distObj, rightDoor, type):
    closeTime = ElevatorData[type]['closeTime']
    closedPos = getRightClosePoint(type)
    openPos = getRightOpenPoint(type)
    rightCloseInterval = LerpPosInterval(rightDoor, closeTime, closedPos, startPos=openPos, blendType='easeOut', name=distObj.uniqueName('rightDoorClose'))
    return rightCloseInterval


def getRideElevatorInterval(type=ELEVATOR_NORMAL):
    ival = Sequence(Wait(0.5), LerpPosInterval(camera, 0.5, Point3(0, 14, 3.8), startPos=Point3(0, 14, 4), blendType='easeOut'), LerpPosInterval(camera, 0.5, Point3(0, 14, 4), startPos=Point3(0, 14, 3.8)), Wait(1.0), LerpPosInterval(camera, 0.5, Point3(0, 14, 4.2), startPos=Point3(0, 14, 4), blendType='easeOut'), LerpPosInterval(camera, 1.0, Point3(0, 14, 4), startPos=Point3(0, 14, 4.2)))
    return ival