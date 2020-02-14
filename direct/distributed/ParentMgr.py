# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.ParentMgr
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.PythonUtil import isDefaultValue
import types

class ParentMgr:
    notify = DirectNotifyGlobal.directNotify.newCategory('ParentMgr')

    def __init__(self):
        self.token2nodepath = {}
        self.pendingParentToken2children = {}
        self.pendingChild2parentToken = {}

    def destroy(self):
        del self.token2nodepath
        del self.pendingParentToken2children
        del self.pendingChild2parentToken

    def privRemoveReparentRequest(self, child):
        if child in self.pendingChild2parentToken:
            self.notify.debug("cancelling pending reparent of %s to '%s'" % (
             repr(child),
             self.pendingChild2parentToken[child]))
            parentToken = self.pendingChild2parentToken[child]
            del self.pendingChild2parentToken[child]
            self.pendingParentToken2children[parentToken].remove(child)

    def requestReparent(self, child, parentToken):
        if parentToken in self.token2nodepath:
            self.privRemoveReparentRequest(child)
            self.notify.debug("performing wrtReparent of %s to '%s'" % (
             repr(child), parentToken))
            child.wrtReparentTo(self.token2nodepath[parentToken])
        else:
            if isDefaultValue(parentToken):
                self.notify.error('child %s requested reparent to default-value token: %s' % (repr(child), parentToken))
            self.notify.debug("child %s requested reparent to parent '%s' that is not (yet) registered" % (
             repr(child), parentToken))
            self.privRemoveReparentRequest(child)
            self.pendingChild2parentToken[child] = parentToken
            self.pendingParentToken2children.setdefault(parentToken, [])
            self.pendingParentToken2children[parentToken].append(child)
            child.reparentTo(hidden)

    def registerParent(self, token, parent):
        if token in self.token2nodepath:
            self.notify.error("registerParent: token '%s' already registered, referencing %s" % (
             token, repr(self.token2nodepath[token])))
        if isDefaultValue(token):
            self.notify.error('parent token (for %s) cannot be a default value (%s)' % (repr(parent), token))
        if type(token) is types.IntType:
            if token > 4294967295L:
                self.notify.error('parent token %s (for %s) is out of uint32 range' % (token, repr(parent)))
        self.notify.debug("registering %s as '%s'" % (repr(parent), token))
        self.token2nodepath[token] = parent
        if token in self.pendingParentToken2children:
            children = self.pendingParentToken2children[token]
            del self.pendingParentToken2children[token]
            for child in children:
                self.notify.debug("performing reparent of %s to '%s'" % (
                 repr(child), token))
                child.reparentTo(self.token2nodepath[token])
                del self.pendingChild2parentToken[child]

    def unregisterParent(self, token):
        if token not in self.token2nodepath:
            self.notify.warning("unregisterParent: unknown parent token '%s'" % token)
            return
        self.notify.debug("unregistering parent '%s'" % token)
        del self.token2nodepath[token]