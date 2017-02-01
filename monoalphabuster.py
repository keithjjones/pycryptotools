import argparse
from library.statistics import *


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
