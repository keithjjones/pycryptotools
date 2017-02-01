from collections import OrderedDict
from curses.ascii import ispunct


def build_single_character_probabilities(inputtext=None, countspaces=False, countpunctuation=False):
    """
    Builds single letter probabilities from input text.

    :param inputtext:  A string to analyze.
    :param countspaces:  Set to True to treat spaces as a valid cipher character.
    :param countpunctuation:  Set to True to treat punctuation as valid cipher character.  Will not count new lines.
    :return: totalletters, lettercounts, letterprobs - totalletters is an int, lettercounts and letterprobs are an
        OrderedDict sorted on value, descending.  None is returned if the inputtext is None.
    """
    # Show there is an error...
    if inputtext is None:
        return None

    totalletters = 0
    lettercounts = dict()

    for c in inputtext:
        if c.isalpha():
            totalletters += 1
            if c in lettercounts:
                lettercounts[c] += 1
            else:
                lettercounts[c] = 1
        if countspaces is True and c == ' ':
            totalletters += 1
            if c in lettercounts:
                lettercounts[c] += 1
            else:
                lettercounts[c] = 1
        if countpunctuation is True and ispunct(c) and c != '\n':
            totalletters += 1
            if c in lettercounts:
                lettercounts[c] += 1
            else:
                lettercounts[c] = 1

    letterprobs = dict()
    for i in lettercounts:
        letterprobs[i] = lettercounts[i]/totalletters

    lettercountssorted = sorted(lettercounts, key=lettercounts.__getitem__, reverse=True)
    letterprobssorted = sorted(letterprobs, key=letterprobs.__getitem__, reverse=True)

    orderedlettercounts = OrderedDict()
    orderedletterprobs = OrderedDict()

    for i in lettercountssorted:
        orderedlettercounts[i] = lettercounts[i]

    for i in letterprobssorted:
        orderedletterprobs[i] = letterprobs[i]

    return totalletters, orderedlettercounts, orderedletterprobs
