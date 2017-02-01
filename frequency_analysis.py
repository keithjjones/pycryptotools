import argparse
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


def main():
    parser = argparse.ArgumentParser(description='Calculates letter frequencies of given cipher text in a cipher file.')
    parser.add_argument('CipherFile',
                        help='The cipher file to analyze.')
    parser.add_argument("-s", "--spaces", action='store_true',
                        help="Counts spaces as a valid cipher character instead of ignoring them."
                             "", required=False)
    parser.add_argument("-p", "--punctuation", action='store_true',
                        help="Counts punctuation as valid cipher characters instead of ignoring them."
                             "", required=False)

    args = parser.parse_args()

    cipherfile = args.CipherFile

    with open(cipherfile, 'r') as cf:
        ciphertext = cf.read()

    totalletters, cipherlettercounts, cipherletterprobs = build_single_character_probabilities(ciphertext,
                                                                                               args.spaces,
                                                                                               args.punctuation)

    print("Cipher text:")
    print(ciphertext)
    print("")
    print("Total Letters: {0}".format(totalletters))
    print("")
    print("Letter Count:")
    for c in cipherlettercounts:
        print("{0} = {1}".format(c, cipherlettercounts[c]))
    print("")
    print("Letter Frequency:")
    for c in cipherletterprobs:
        print("{0} = {1}".format(c, cipherletterprobs[c]))

if __name__ == "__main__":
    main()