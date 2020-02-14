# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.directutil.Verify
wantVerifyPdb = 0

def verify(assertion):
    if not assertion:
        print '\n\nverify failed:'
        import sys
        print '    File "%s", line %d' % (
         sys._getframe(1).f_code.co_filename,
         sys._getframe(1).f_lineno)
        if wantVerifyPdb:
            import pdb
            pdb.set_trace()
        raise AssertionError


if not hasattr(__builtins__, 'verify'):
    __builtins__['verify'] = verify