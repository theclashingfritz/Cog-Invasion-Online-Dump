# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: encodings.quopri_codec
import codecs, quopri
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

def quopri_encode(input, errors='strict'):
    f = StringIO(str(input))
    g = StringIO()
    quopri.encode(f, g, 1)
    output = g.getvalue()
    return (
     output, len(input))


def quopri_decode(input, errors='strict'):
    f = StringIO(str(input))
    g = StringIO()
    quopri.decode(f, g)
    output = g.getvalue()
    return (
     output, len(input))


class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return quopri_encode(input, errors)

    def decode(self, input, errors='strict'):
        return quopri_decode(input, errors)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return quopri_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        return quopri_decode(input, self.errors)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='quopri', encode=quopri_encode, decode=quopri_decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)