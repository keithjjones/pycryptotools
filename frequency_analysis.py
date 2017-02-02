import argparse
from library.statistics import *


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

    cipherlettercounts = build_ngram_counts(ciphertext, 1, args.spaces, args.punctuation)
    cipherdigramcounts = build_ngram_counts(ciphertext, 2, args.spaces, args.punctuation)
    ciphertrigramcounts = build_ngram_counts(ciphertext, 3, args.spaces, args.punctuation)
    cipherquadgramcounts = build_ngram_counts(ciphertext, 4, args.spaces, args.punctuation)

    print("**** Cipher Text ****")
    print("")
    print(ciphertext)
    print("")
    print("Letter Counts:")
    for c in cipherlettercounts:
        print("{0} = {1}".format(c, cipherlettercounts[c]))
    print("")
    print("Digram Counts:")
    for c in cipherdigramcounts:
        print("{0} = {1}".format(c, cipherdigramcounts[c]))
    print("")
    print("Trigram Counts:")
    for c in ciphertrigramcounts:
        print("{0} = {1}".format(c, ciphertrigramcounts[c]))
    print("")
    print("Quadgram Counts:")
    for c in cipherquadgramcounts:
        print("{0} = {1}".format(c, cipherquadgramcounts[c]))
    print("")


if __name__ == "__main__":
    main()
