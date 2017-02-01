import argparse
from collections import OrderedDict

# Source for these statistics:  Cryptography and Network Security, Principles and Practice,
# William Stallings, 7th Edition, page 77, Figure 3.5
english_letter_probabilities = {
    'a': 8.167/100,
    'b': 1.492/100,
    'c': 2.782/100,
    'd': 4.253/100,
    'e': 12.702/100,
    'f': 2.228/100,
    'g': 2.015/100,
    'h': 6.094/100,
    'i': 6.996/100,
    'j': 0.153/100,
    'k': 0.772/100,
    'l': 4.025/100,
    'm': 2.406/100,
    'n': 6.749/100,
    'o': 7.507/100,
    'p': 1.929/100,
    'q': 0.095/100,
    'r': 5.987/100,
    's': 6.327/100,
    't': 9.056/100,
    'u': 2.758/100,
    'v': 0.978/100,
    'w': 2.360/100,
    'x': 0.150/100,
    'y': 1.974/100,
    'z': 0.074/100
}

# Information from http://www.data-compression.com/english.html
dc_english_letter_probabilities = {
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
}


def buildcharprobabilities(inputtext=None):
    """
    Builds single letter probabilities from input text.

    :param inputtext:  A string to analyze.
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


def fit_probability_errors(plaintextcharprobs, ciphercharprobs):
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
        print("{0} -> {1} Error: {2}".format(cipherchar, minplainchar, minerror))

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
        print("{0} {1}".format(ct[i][0], pt[i][0]))
        ciphertoplain[ct[i][0]] = pt[i][0]

    return ciphertoplain


def main():
    parser = argparse.ArgumentParser(description='Attempts to decrypt mono alpha ciphers.')
    parser.add_argument('CipherFile',
                        help='The cipher file to decrypt.')

    args = parser.parse_args()

    cipherfile = args.CipherFile

    with open(cipherfile, 'r') as cf:
        ciphertext = cf.read()

    totalletters, cipherlettercounts, cipherletterprobs = buildcharprobabilities(ciphertext)

    print("Cipher Text:")
    print(ciphertext)

    print(cipherletterprobs)

    # Sort our english probabilities...
    en_sorted = sorted(english_letter_probabilities, key=english_letter_probabilities.__getitem__, reverse=True)
    en_sorted_dict = OrderedDict()
    for c in en_sorted:
        en_sorted_dict[c] = english_letter_probabilities[c]

    #ciphertoplain = fit_probability_errors(english_letter_probabilities, cipherletterprobs)
    ciphertoplain = fit_characters_sorted_probabilities(en_sorted_dict, cipherletterprobs)

    print(ciphertoplain)

    print("Plain Text: \n")

    print(en_sorted_dict)

    plaintext = ""
    for c in ciphertext:
        if c in ciphertoplain:
            plaintext += ciphertoplain[c]
        else:
            plaintext += c

    print(plaintext)

if __name__ == "__main__":
    main()
