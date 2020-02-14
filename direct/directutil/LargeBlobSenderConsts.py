# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.directutil.LargeBlobSenderConsts
USE_DISK = 1
ChunkSize = 100
FilePattern = 'largeBlob.%s'

def getLargeBlobPath():
    return config.GetString('large-blob-path', 'i:\\toontown_in_game_editor_temp')