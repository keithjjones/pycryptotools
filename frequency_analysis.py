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
    parser.add_argument("-k", "--knownprobabilities", action='store_true',
                        help="Displays known letter probabilities from various sources."
                             "", required=False)

    args = parser.parse_args()

    cipherfile = args.CipherFile

    with open(cipherfile, 'r') as cf:
        ciphertext = cf.read()

    totalletters, cipherlettercounts, cipherletterprobs = build_monogram_probabilities(ciphertext,
                                                                                       args.spaces,
                                                                                       args.punctuation)
    totaldigrams, cipherdigramcounts, cipherdigramprobs = build_digram_probabilities(ciphertext,
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
    print("")
    print("Digram Count:")
    for c in cipherdigramcounts:
        print("{0} = {1}".format(c, cipherdigramcounts[c]))
    print("")
    print("Digram Frequency:")
    for c in cipherdigramprobs:
        print("{0} = {1}".format(c, cipherdigramprobs[c]))
    print("")

    if args.knownprobabilities is True:
        print("Single Letter, No Spaces, Source = Stallings:")
        for c in stallings_english_letter_probabilities:
            print("{0} = {1}".format(c, stallings_english_letter_probabilities[c]))
        print("")
        print("Digram, No Spaces, Source = Mayzner:")
        for c in mayzner_english_digram_probabilities:
            print("{0} = {1}".format(c, mayzner_english_digram_probabilities[c]))

if __name__ == "__main__":
    main()
