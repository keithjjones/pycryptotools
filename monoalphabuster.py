import argparse
import pandas
from library.statistics import *
from library.data import *
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

    totalletters, cipherlettercounts, cipherletterprobs = build_monogram_probabilities(ciphertext,
                                                                                       args.spaces,
                                                                                       args.punctuation)
    totaldigrams, cipherdigramcounts, cipherdigramprobs = build_digram_probabilities(ciphertext,
                                                                                     args.spaces,
                                                                                     args.punctuation)
    totaltrigrams, ciphertrigramcounts, ciphertrigramprobs = build_trigram_probabilities(ciphertext,
                                                                                         args.spaces,
                                                                                         args.punctuation)

    ngram1 = pandas.read_csv(os.path.join('data','ngrams1.csv'), keep_default_na=False, na_values=['_'])
    ngram2 = pandas.read_csv(os.path.join('data','ngrams2.csv'), keep_default_na=False, na_values=['_'])
    ngram3 = pandas.read_csv(os.path.join('data','ngrams3.csv'), keep_default_na=False, na_values=['_'])

    ngram2 = ngram2[['2-gram','*/*']]
    ngram2matrix = ngram2_data_to_matrix(ngram2)

    print(ngram2matrix)

    print("Cipher Text:")
    print("")
    print(ciphertext)

    #ciphertoplain = fit_probability_errors(english_letter_probabilities, cipherletterprobs)
    #ciphertoplain = fit_characters_sorted_probabilities(en_sorted_dict, cipherletterprobs)

    #print(ciphertoplain)

    print("Plain Text: \n")

    # plaintext = ""
    # for c in ciphertext:
    #    if c in ciphertoplain:
    #        plaintext += ciphertoplain[c]
    #    else:
    #        plaintext += c

    # print(plaintext)

if __name__ == "__main__":
    main()
