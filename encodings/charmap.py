# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: encodings.charmap
import codecs

class Codec(codecs.Codec):
    encode = codecs.charmap_encode
    decode = codecs.charmap_decode


class IncrementalEncoder(codecs.IncrementalEncoder):

    def __init__(self, errors='strict', mapping=None):
        codecs.IncrementalEncoder.__init__(self, errors)
        self.mapping = mapping

    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, self.mapping)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def __init__(self, errors='strict', mapping=None):
        codecs.IncrementalDecoder.__init__(self, errors)
        self.mapping = mapping

    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, self.mapping)[0]


class StreamWriter(Codec, codecs.StreamWriter):

    def __init__(self, stream, errors='strict', mapping=None):
        codecs.StreamWriter.__init__(self, stream, errors)
        self.mapping = mapping

    def encode(self, input, errors='strict'):
        return Codec.encode(input, errors, self.mapping)


class StreamReader(Codec, codecs.StreamReader):

    def __init__(self, stream, errors='strict', mapping=None):
        codecs.StreamReader.__init__(self, stream, errors)
        self.mapping = mapping

    def decode(self, input, errors='strict'):
        return Codec.decode(input, errors, self.mapping)


def getregentry():
    return codecs.CodecInfo(name='charmap', encode=Codec.encode, decode=Codec.decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)