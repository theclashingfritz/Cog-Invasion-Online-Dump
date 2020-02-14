# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.LazySort
from itertools import tee

def itersorted(iterable, cmp=cmp, key=lambda x: x, reverse=False):
    stack = []
    layer = ()
    init = True
    if reverse:
        rev = -1
    else:
        rev = 1
    a = ((key(x), x) for x in iterable)
    while 1:
        if not stack:
            k, val = a.next()
            while not init and cmp(k, lLimit) != rev:
                k, val = a.next()

            a, b = tee(a)
            stack.append([k, b, [val]])
        layer = stack[-1]
        b = layer[1]
        for k, val in b:
            if cmp(k, layer[0]) != rev and (init or cmp(k, lLimit) == rev):
                if cmp(k, layer[0]) == -rev:
                    b, layer[1] = tee(b)
                    stack.append([k, b, []])
                    layer = stack[-1]
                layer[2].append(val)
                continue

        init = False
        lLimit, b, vals = stack.pop()
        for val in vals:
            yield val