import argparse
from library.ciphers import *
from library.statistics import *
from library.data import *
import os
import string
import random

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
    parser.add_argument("-m", "--mayzner", action='store_true',
                        help="Use Mayzner statistical data."
                             "", required=False)


    args = parser.parse_args()

    cipherfile = args.CipherFile

    # Read the cipher text...
    with open(cipherfile, 'r') as cf:
        ciphertext = cf.read()

    # Load our statistical data
    print("Loading statistical data...")

    if args.mayzner:
        ngram_data = mayzner_data(os.path.join('data',
                                               'mayzner',
                                               'ngrams4.csv'))
    else:
        ngram_data = practical_cryptography_data(os.path.join('data',
                                                              'practicalcryptography.com',
                                                              'english_quadgrams.txt'))

    # Setup our initial keys....
    cipherlettercounts = build_ngram_counts(ciphertext, 1, args.spaces, args.punctuation)

    # Build our initial cipher key based upon frequency...
    plainvalues = list(string.ascii_lowercase)
    cipherkey = plainvalues.copy()

    # cipherkey = list()
    # for c in cipherlettercounts:
    #     cipherkey.append(c)
    #
    # # Find any missing values in our initial cipher key...
    # ckset = set(cipherkey)
    # missingset = set(plainvalues) - ckset
    # for m in missingset:
    #     cipherkey.append(m)
    #
    # print(cipherkey)
    # print(len(cipherkey))

    # Print the cipher text...
    print("Cipher Text:")
    print("")
    print(ciphertext)

    # Get the initial error for the key...
    testciphertext = MonoAlphaSubstitution(cipherkey, plainvalues).decrypt(ciphertext)
    max_score = ngram_data.score(testciphertext)
    max_score_cipher_key = cipherkey.copy()

    print("Looping continuously, press ctl-c when you have your plain text!")

    i = 0
    while True:
        i += 1

        parentcipherkey = max_score_cipher_key.copy()
        random.shuffle(parentcipherkey)

        testciphertext = MonoAlphaSubstitution(parentcipherkey, plainvalues).decrypt(ciphertext)
        parent_score = ngram_data.score(testciphertext)

        count = 0
        while count < 1000:
            childcipherkey = parentcipherkey.copy()
            # Swap two characters in the cipherkey to test score.
            first = random.randint(0, len(childcipherkey)-1)
            second = random.randint(0, len(childcipherkey)-1)
            tmp = childcipherkey[first]
            childcipherkey[first] = childcipherkey[second]
            childcipherkey[second] = tmp

            testciphertext = MonoAlphaSubstitution(childcipherkey, plainvalues).decrypt(ciphertext)
            child_score = ngram_data.score(testciphertext)
            if child_score > parent_score:
                parent_score = child_score
                parentcipherkey = childcipherkey.copy()
                count = 0
            count += 1

        if parent_score > max_score:
            testciphertext = MonoAlphaSubstitution(parentcipherkey, plainvalues).decrypt(ciphertext)
            print("*****")
            print("Iteration {0} better score {1}".format(i, parent_score))
            print("Current Cipher Key/Plain Values:")
            print(parentcipherkey)
            print(plainvalues)
            print("Cipher Text:")
            print(ciphertext)
            print("Current Plain Text:")
            print(testciphertext)
            max_score = parent_score
            max_score_cipher_key = parentcipherkey.copy()

if __name__ == "__main__":
    main()
