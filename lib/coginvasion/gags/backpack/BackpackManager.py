# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.gags.backpack.BackpackManager
from lib.coginvasion.gags.backpack.SmallPouch import SmallPouch
from lib.coginvasion.gags.backpack.AdminPouch import AdminPouch
import copy
backpacks = [
 SmallPouch, AdminPouch]
clientPacks = []

def getBackpack(index):
    backpack = None
    if index < len(backpacks) and index >= 0:
        backpack = backpacks[index]
    if backpack:
        backpack = copy.copy(backpack)
        if game.process == 'client':
            clientPacks.append(backpack)
    return backpack()


def getIndex(backpack):
    if not backpack:
        return
    for pack in backpacks:
        if pack == backpack:
            return backpacks.index(pack)


def getClientPack(backpack):
    if not backpack:
        return
    return clientPacks[backpack]


def getClientPackIndex(backpack):
    return clientPacks.index(backpack)


def getBackpacks():
    packs = []
    for pack in backpacks:
        packs.append(pack())

    return packs