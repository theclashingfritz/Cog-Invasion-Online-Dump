# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.extensions_native.core_extensions
import sys
main_dir = Filename()
if sys.argv and sys.argv[0]:
    main_dir = Filename.from_os_specific(sys.argv[0])
if main_dir.empty():
    main_dir = ExecutionEnvironment.get_cwd()
else:
    main_dir.make_absolute()
    main_dir = Filename(main_dir.get_dirname())
ExecutionEnvironment.shadow_environment_variable('MAIN_DIR', main_dir.to_os_specific())
del sys
del main_dir

def Dtool_funcToMethod(func, cls, method_name=None):
    func.im_func = func
    func.im_self = None
    if not method_name:
        method_name = func.__name__
    cls.DtoolClassDict[method_name] = func
    return