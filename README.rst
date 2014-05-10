Robber langeuage Python library
-------------------------------

This is a library that hooks into the Python codecs library to provide an encoder to and from the so called Robber language. http://en.wikipedia.org/wiki/R%C3%B6varspr%C3%A5ket for more info.

Currently only tested with Python 2.6.6.

Currently implemented:
 - Very basic encoding from English characters to othe robber language.

Todo:
 - Support decoding
 - Detect which locale is used and use that to determine which characters are consonants.
 - Proper Unicode support.
 - Python 3 support.
