#!/usr/bin/env python2

"""
Solution to https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python

How can you tell an extrovert from an introvert at NSA? Va gur ryringbef,
gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can
decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13)
is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces,
punctuation, numbers etc. Test examples:

rot13("EBG13 rknzcyr.") == "ROT13 example.";
rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"
"""


lower_ords = set(range(97, 123))
upper_ords = set(range(65, 91))


def rot13(message):
    return ''.join(rot_one(c, 13) for c in message)


def rot_one(ch, n):
    if ord(ch) in lower_ords:
        offset = 97
    elif ord(ch) in upper_ords:
        offset = 65
    else:
        return ch
    return chr((((ord(ch) - offset) + n) % 26) + offset)
