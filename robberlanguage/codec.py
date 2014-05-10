
import codecs


class RobberLanguageCodec(codecs.Codec):

    english_consontants = 'BCDFGHJKLMNPQRSTVXZWY'

    def encode(self, input, errors='strict'):
        output = ''

        for l in input:
            if l in self.english_consontants:
                output += 'O' + l + 'O'
            elif l in self.english_consontants.lower():
                output += 'o' + l + 'o'
            else:
                output += l

        return (output, len(input))

    def decode(self, input, errors='strict'):
        raise NotImplemented()


class RobberLanguageIncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        raise NotImplemented()


class RobberLanguageIncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        raise NotImplemented()


class RobberLanguageStreamReader(RobberLanguageCodec, codecs.StreamReader):
    pass


class RobberLanguageStreamWriter(RobberLanguageCodec, codecs.StreamWriter):
    pass


def find_robberlanguage(encoding):
    encoding_name = 'robberlanguage'

    if encoding == encoding_name:
        return codecs.CodecInfo(
            name=encoding_name,
            encode=RobberLanguageCodec().encode,
            decode=RobberLanguageCodec().decode,
            incrementalencoder=RobberLanguageIncrementalEncoder,
            incrementaldecoder=RobberLanguageIncrementalDecoder,
            streamreader=RobberLanguageStreamReader,
            streamwriter=RobberLanguageStreamWriter
        )

codecs.register(find_robberlanguage)
