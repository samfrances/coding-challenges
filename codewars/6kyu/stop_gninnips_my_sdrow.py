#!#!/usr/bin/env python


def spin_words(sentence):
    words = sentence.split()
    spun_words = (word if len(word) < 5 else word[::-1] for word in words)
    return ' '.join(spun_words)
