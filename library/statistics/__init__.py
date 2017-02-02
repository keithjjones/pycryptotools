from collections import OrderedDict
from curses.ascii import ispunct


def sort_dict_by_value_reverse(indict):
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
stallings_english_letter_probabilities = sort_dict_by_value_reverse({
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
dc_english_letter_probabilities = sort_dict_by_value_reverse({
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


def build_ngram_counts(inputtext=None, n=1, countspace=False, countpunctuation=False):
    if inputtext is None or n < 1:
        return None

    ngrams = dict()
    for c in range(len(inputtext)):
        if not (inputtext[c].isalpha() or
                (ispunct(inputtext[c]) and countpunctuation is True and inputtext[c] != '\n') or
                (inputtext[c] == ' ' and countspace is True)):
            continue

        i = 0
        ngram = ""
        while len(ngram) < n and c+i < len(inputtext):
            if (inputtext[c+i].isalpha() or
                (ispunct(inputtext[c+i]) and countpunctuation is True and inputtext[c+i] != '\n') or
                    (inputtext[c+i] == ' ' and countspace is True)):
                ngram += inputtext[c+i]
                print("n {0} ngram {1} c {2} i {3}".format(n,ngram,c,i))
            i += 1

        if len(ngram) == n:
            if ngram in ngrams:
                ngrams[ngram] += 1
            else:
                ngrams[ngram] = 1
            print(ngrams)

    return sort_dict_by_value_reverse(ngrams)

class ngram_score(object):
