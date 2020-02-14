# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: lib.coginvasion.base.Logger
import os, sys, time

class Logger:

    def __init__(self, orig, log):
        self.orig = orig
        self.log = log

    def write(self, string):
        self.log.write(string)
        self.log.flush()
        try:
            self.orig.write(string)
            self.orig.flush()
        except:
            pass

    def flush(self):
        self.log.flush()
        try:
            self.orig.flush()
        except:
            pass


class Starter:

    def __init__(self, log_prefix='coginvasion-', log_extension='.log', path='logs/'):
        log_suffix = time.strftime('%d-%m-%Y-%H-%M-%S')
        if not os.path.exists(path):
            os.mkdir(path)
        logfile = os.path.join(path, log_prefix + log_suffix + log_extension)
        log = open(logfile, 'a')
        logOut = Logger(sys.stdout, log)
        logErr = Logger(sys.stderr, log)
        sys.stdout = logOut
        sys.stderr = logErr