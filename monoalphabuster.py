import argparse
import pandas
from library.statistics import *
from library.data import *
from library.math import *
import os

def main():
    parser = argparse.ArgumentParser(description='Attempts to decrypt mono alpha ciphers.')
    parser.add_argument('CipherFile',
                        help='The cipher file to decrypt.')
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

    ngram1 = pandas.read_csv(os.path.join('data','ngrams1.csv'), keep_default_na=False, na_values=['_'])
    ngram2 = pandas.read_csv(os.path.join('data','ngrams2.csv'), keep_default_na=False, na_values=['_'])
    ngram3 = pandas.read_csv(os.path.join('data','ngrams3.csv'), keep_default_na=False, na_values=['_'])

    ngram1 = ngram1[['1-gram','*/*']]
    ngram1sorted = ngram1_to_ordered_dict(ngram1)

    ngram2 = ngram2[['2-gram','*/*']]
    ngram2sorted = ngram2_to_ordered_dict(ngram2)

    # with open('data/mobydick.txt', 'r') as mb:
    #     exampletext = mb.read()
    #     exampletext = exampletext.lower()

    # totalletters, exlettercounts, exletterprobs = build_monogram_probabilities(exampletext,
    #                                                                            args.spaces,
    #                                                                            args.punctuation)
    # totaldigrams, exdigramcounts, exdigramprobs = build_digram_probabilities(exampletext,
    #                                                                          args.spaces,
    #                                                                          args.punctuation)

    print("Cipher Text:")
    print("")
    print(ciphertext)

    ciphertoplain = minimize_digram_error(ciphertext, ngram1sorted, ngram2sorted,
                                          args.spaces, args.punctuation)
    # ciphertoplain = minimize_digram_error(ciphertext, exletterprobs, exdigramprobs,
    #                                       args.spaces, args.punctuation)

    print("Plain Text: \n")

    plaintext = ""
    for c in ciphertext:
       if c in ciphertoplain:
           plaintext += ciphertoplain[c]
       else:
           plaintext += c

    print(plaintext)


if __name__ == "__main__":
    main()
