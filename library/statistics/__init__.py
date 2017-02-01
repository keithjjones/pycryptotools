from collections import OrderedDict
from curses.ascii import ispunct


def sort_prob_dict_by_value_reverse( indict ):
    """
    Returns an OrderedDict that has been sorted on value.

    :param indict:  A dict representing ngram probabilities.
    :return: An OrderedDict, sorted in reverse (largest to smallest)
    """
    outdict = OrderedDict()

    indictsorted = sorted(indict, key=indict.__getitem__, reverse=True)

    for i in indictsorted:
        outdict[i] = indict[i]

    return outdict

# Source for these statistics:  Cryptography and Network Security, Principles and Practice,
# William Stallings, 7th Edition, page 77, Figure 3.5
stallings_english_letter_probabilities = sort_prob_dict_by_value_reverse({
    'a': 8.167 / 100,
    'b': 1.492 / 100,
    'c': 2.782 / 100,
    'd': 4.253 / 100,
    'e': 12.702 / 100,
    'f': 2.228 / 100,
    'g': 2.015 / 100,
    'h': 6.094 / 100,
    'i': 6.996 / 100,
    'j': 0.153 / 100,
    'k': 0.772 / 100,
    'l': 4.025 / 100,
    'm': 2.406 / 100,
    'n': 6.749 / 100,
    'o': 7.507 / 100,
    'p': 1.929 / 100,
    'q': 0.095 / 100,
    'r': 5.987 / 100,
    's': 6.327 / 100,
    't': 9.056 / 100,
    'u': 2.758 / 100,
    'v': 0.978 / 100,
    'w': 2.360 / 100,
    'x': 0.150 / 100,
    'y': 1.974 / 100,
    'z': 0.074 / 100
})
"""Source for these statistics:  Cryptography and Network Security, Principles and Practice,
William Stallings, 7th Edition, page 77, Figure 3.5"""

# Information from http://www.data-compression.com/english.html
dc_english_letter_probabilities = sort_prob_dict_by_value_reverse({
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
})
"""Probabilities published http://www.data-compression.com/english.html"""

# Information from http://norvig.com/mayzner.html
mayzner_english_digram_probabilities = sort_prob_dict_by_value_reverse({
    'th': 3.56 / 100,
    'he': 3.07 / 100,
    'in': 2.43 / 100,
    'er': 2.05 / 100,
    'an': 1.99 / 100,
    're': 1.85 / 100,
    'on': 1.76 / 100,
    'at': 1.49 / 100,
    'en': 1.45 / 100,
    'nd': 1.35 / 100,
})
"""Probabilities publised http://norvig.com/mayzner.html"""

def build_monogram_probabilities(inputtext=None, countspaces=False, countpunctuation=False):
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

    orderedlettercounts = sort_prob_dict_by_value_reverse(lettercounts)
    orderedletterprobs = sort_prob_dict_by_value_reverse(letterprobs)

    return totalletters, orderedlettercounts, orderedletterprobs


def build_digram_probabilities(inputtext=None, countspace=False, countpunctuation=False):
    # Show there is an error...
    if inputtext is None:
        return None

    totaldigrams = 0
    digramcounts = dict()

    for i in range(len(inputtext)-1):
        digram = ""
        founddigram = False
        if inputtext[i].isalpha() or (countspace is True and inputtext[i] == ' ') or (countpunctuation is True
                                                                                      and ispunct(inputtext[i])
                                                                                      and inputtext[i] != '\n'):
            digram += inputtext[i]
            for j in range(i+1, len(inputtext)):
                if inputtext[j].isalpha() or (countspace is True and inputtext[j] == ' ') or (countpunctuation is True
                                                                                              and ispunct(inputtext[j])
                                                                                              and inputtext[j] != '\n'):
                    digram += inputtext[j]
                    founddigram = True
                    break

            if founddigram is True:
                if digram in digramcounts:
                    digramcounts[digram] += 1
                else:
                    digramcounts[digram] = 1
                totaldigrams += 1

    digramprobs = dict()
    for i in digramcounts:
        digramprobs[i] = digramcounts[i]/totaldigrams

    ordereddigramcounts = sort_prob_dict_by_value_reverse(digramcounts)
    ordereddigramprobs = sort_prob_dict_by_value_reverse(digramprobs)

    return totaldigrams, ordereddigramcounts, ordereddigramprobs


def fit_probability_min_errors(plaintextcharprobs, ciphercharprobs):
    """
    Fits the cipher characters to the most probable plain text characters, based upon the lowest probability error.

    :param plaintextcharprobs:  An OrderedDict of plain text probability characters.
    :param ciphercharprobs:  An OrderedDict of cipher text probability characters.
    :return: A dict with cipher character key and plain text character value.
    """
    ciphertoplain = dict()
    usedchars = list()
    for cipherchar in ciphercharprobs:
        minerror = None
        for plainchar in plaintextcharprobs:
            error = abs(ciphercharprobs[cipherchar] - plaintextcharprobs[plainchar])
            if minerror is None or minerror > error:
                if plainchar not in usedchars:
                    minerror = error
                    minplainchar = plainchar
        ciphertoplain[cipherchar] = minplainchar
        usedchars.append(minplainchar)

    return ciphertoplain


def fit_characters_sorted_probabilities(plaintextcharprobs, ciphercharprobs):
    """
    Fits the cipher characters to the probable plain text characters by descending probabilities.

    :param plaintextcharprobs:  An OrderedDict of plain text probability characters.
    :param ciphercharprobs:  An OrderedDict of cipher text probability characters.
    :return: A dict with cipher character key and plain text character value.
    """
    ciphertoplain = dict()

    ct = list(ciphercharprobs.items())
    pt = list(plaintextcharprobs.items())

    for i in range(len(ct)):
        ciphertoplain[ct[i][0]] = pt[i][0]

    return ciphertoplain