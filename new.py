# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: new
from warnings import warnpy3k
warnpy3k("The 'new' module has been removed in Python 3.0; use the 'types' module instead.", stacklevel=2)
del warnpy3k
from types import ClassType as classobj
from types import FunctionType as function
from types import InstanceType as instance
from types import MethodType as instancemethod
from types import ModuleType as module
from types import CodeType as code