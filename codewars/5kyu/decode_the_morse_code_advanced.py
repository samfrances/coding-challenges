#!/usr/bin/env python2

"""
Solution to https://www.codewars.com/kata/54b72c16cd7f5154e9000457/

In this kata you have to write a Morse code decoder for wired electrical
telegraph.

Electric telegraph is operated on a 2-wire line with a key that, when pressed,
connects the wires together, which can be detected on a remote station. The
Morse code encodes every character being transmitted as a sequence of "dots"
(short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:

    "Dot" – is 1 time unit long.
    "Dash" – is 3 time units long.
    Pause between dots and dashes in a character – is 1 time unit long.
    Pause between characters inside a word – is 3 time units long.
    Pause between words – is 7 time units long.

However, the standard does not specify how long that "time unit" is. And in
fact different operators would transmit at different speed. An amateur person
may need a few seconds to transmit a single character, a skilled professional
can transmit 60 words per minute, and robotic transmitters may go way faster.

For this kata we assume the message receiving is performed automatically by the
hardware that checks the line periodically, and if the line is connected (the
key at the remote station is down), 1 is recorded, and if the line is not
connected (remote key is up), 0 is recorded. After the message is fully
received, it gets to you for decoding as a string containing only
symbols 0 and 1.

For example, the message HEY JUDE, that is ···· · −·−− ·−−− ··− −·· · may be
received as follows:

1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

As you may see, this transmission is perfectly accurate according to the
standard, and the hardware sampled the line exactly two times per "dot".

That said, your task is to implement two functions:

    Function decodeBits(bits), that should find out the transmission rate of
    the message, correctly decode the message to dots ., dashes - and spaces
    (one between characters, three between words) and return those as a string.
    Note that some extra 0's may naturally occur at the beginning and the end
    of a message, make sure to ignore them. Also if you have trouble discerning
    if the particular sequence of 1's is a dot or a dash, assume it's a dot.

    Function decodeMorse(morseCode), that would take the output of the previous
    function and return a human-readable string.

NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode
characters.

The Morse code table is preloaded for you as MORSE_CODE dictionary; in Java
MorseCode class is provided; in Haskell the codes are in a Map String String
and can be accessed like this: morseCodes ! ".--" - feel free to use it.

All the test strings would be valid to the point that they could be reliably
decoded as described above, so you may skip checking for errors and exceptions,
just do your best in figuring out what the message is!

Good luck!
"""

MORSE_CODE = {
    '.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
    '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R', '.--': 'W',
    '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F', '.': 'E', '.-..': 'L',
    '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K',
    '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P',
    '.-.-.-': '.', '--': 'M', '-.': 'N', '....': 'H', '.----.': "'",
    '...-': 'V', '--...': '7', '-.-.-.': ';', '-....-': '-', '..--.-': '_',
    '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q', '--..': 'Z',
    '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y',
    '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
    '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'
}


def transmission_rate(bits):
    shortest_run = len(bits)
    current_run = 1
    prev_bit = bits[0]
    for bit in bits[1:]:
        if bit == prev_bit:
            current_run += 1
        else:
            shortest_run = min(shortest_run, current_run)
            current_run = 1
        prev_bit = bit
    return shortest_run


def decodeBits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    stripped_bits = bits.strip("0")
    rate = transmission_rate(stripped_bits)
    return (
        stripped_bits
        .replace('0' * rate * 7, '   ')
        .replace('1' * rate * 3, '-')
        .replace('0' * rate * 3, ' ')
        .replace('1' * rate, '.')
        .replace('0' * rate, '')
    )


def decodeMorseWord(word):
    letters = word.split()
    return ''.join(MORSE_CODE[letter] for letter in letters)


def decodeMorse(morse_code):
    words = morse_code.strip().split("   ")
    return ' '.join(decodeMorseWord(word) for word in words)
