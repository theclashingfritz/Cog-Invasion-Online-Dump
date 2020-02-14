# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: dircache
from warnings import warnpy3k
warnpy3k('the dircache module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
import os
__all__ = [
 'listdir', 'opendir', 'annotate', 'reset']
cache = {}

def reset():
    global cache
    cache = {}


def listdir(path):
    try:
        cached_mtime, list = cache[path]
        del cache[path]
    except KeyError:
        cached_mtime, list = -1, []

    mtime = os.stat(path).st_mtime
    if mtime != cached_mtime:
        list = os.listdir(path)
        list.sort()
    cache[path] = (
     mtime, list)
    return list


opendir = listdir

def annotate(head, list):
    for i in range(len(list)):
        if os.path.isdir(os.path.join(head, list[i])):
            list[i] = list[i] + '/'