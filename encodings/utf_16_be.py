# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: encodings.utf_16_be
import codecs
encode = codecs.utf_16_be_encode

def decode(input, errors='strict'):
    return codecs.utf_16_be_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return codecs.utf_16_be_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_16_be_decode


class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_16_be_encode


class StreamReader(codecs.StreamReader):
    decode = codecs.utf_16_be_decode


def getregentry():
    return codecs.CodecInfo(name='utf-16-be', encode=encode, decode=decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)