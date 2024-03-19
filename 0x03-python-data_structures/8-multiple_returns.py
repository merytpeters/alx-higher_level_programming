#!/usr/bin/python3
def multiple_returns(sentence):
    lenSent = len(sentence)

    if lenSent == 0:
        sentence[0] = None
        return (lenSent, sentence[0])
    else:
        return (lenSent, sentence[0])
