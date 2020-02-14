# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: compiler.syntax
from compiler import ast, walk

def check(tree, multi=None):
    v = SyntaxErrorChecker(multi)
    walk(tree, v)
    return v.errors


class SyntaxErrorChecker:

    def __init__(self, multi=None):
        self.multi = multi
        self.errors = 0

    def error(self, node, msg):
        self.errors = self.errors + 1
        if self.multi is not None:
            print '%s:%s: %s' % (node.filename, node.lineno, msg)
        else:
            raise SyntaxError, '%s (%s:%s)' % (msg, node.filename, node.lineno)
        return

    def visitAssign(self, node):
        pass