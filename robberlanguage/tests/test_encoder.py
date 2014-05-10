from unittest import TestCase

import robberlanguage


class EncoderTestCase(TestCase):

    def test_empty_string(self):
        self.assertEqual('', ''.encode('robberlanguage'))

    def test_string_with_vowels(self):
        self.assertEqual('aei', 'aei'.encode('robberlanguage'))

    def test_consonants_uppercase(self):
        actual = 'BCDFGHJKLMNPQRSTVXZWY'.encode('robberlanguage')
        expected = """OBOOCOODOOFOOGOOHOOJOOKOOLOOMOONOOPOOQOOROOSOOTOOVOOX\
OOZOOWOOYO"""
        self.assertEqual(expected, actual)

    def test_consonants_lowercase(self):
        actual = 'bcdfghjklmnpqrstvxzwy'.encode('robberlanguage')
        expected = """oboocoodoofoogoohoojookooloomoonoopooqooroosootoovoox\
oozoowooyo"""
        self.assertEqual(expected, actual)

    def test_consonants_mixed_lowercase_and_uppercase(self):
        actual = 'BcDfGhJkLmNpQrStVxZwYy'.encode('robberlanguage')
        expected = """OBOocoODOofoOGOohoOJOokoOLOomoONOopoOQOoroOSOotoOVOox\
oOZOowoOYOoyo"""
        self.assertEqual(expected, actual)

    # TODO: add test cases for different locales with different consonants
    # TODO: add test cases for unicode type text strings
    # TODO: Python 3 support
