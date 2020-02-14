# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: encodings.undefined
import codecs

class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        raise UnicodeError('undefined encoding')

    def decode(self, input, errors='strict'):
        raise UnicodeError('undefined encoding')


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        raise UnicodeError('undefined encoding')


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        raise UnicodeError('undefined encoding')


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='undefined', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)