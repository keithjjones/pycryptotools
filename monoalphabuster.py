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

    args = parser.parse_args()

    cipherfile = args.CipherFile

    # Read the cipher text...
    with open(cipherfile, 'r') as cf:
        ciphertext = cf.read()

    # Load our statistical data
    print("Loading statistical data...")
    md = mayzner_data(os.path.join('data', 'ngrams4.csv'))

    # Setup our initial keys....
    plainvalues = list(string.ascii_lowercase)
    cipherkey = list(string.ascii_lowercase)

    # Print the cipher text...
    print("Cipher Text:")
    print("")
    print(ciphertext)

    # Get the initial error for the key...
    testciphertext = MonoAlphaSubstitution(cipherkey, plainvalues).decrypt(ciphertext)
    max_score = md.score(testciphertext)
    max_score_cipher_key = cipherkey

    print("Looping continuously, press ctl-c when you have your plain text!")

    i = 1
    while True:
        i += 1
        random.shuffle(cipherkey)
        testciphertext = MonoAlphaSubstitution(cipherkey, plainvalues).decrypt(ciphertext)
        current_score = md.score(testciphertext)

        if current_score > max_score:
            print("*****")
            print("Iteration {0} better score {1} with cipher key {2}:".format(i, current_score, cipherkey))
            print("Current Plain Text:")
            print(testciphertext)
            max_score = current_score
            max_score_cipher_key = cipherkey

if __name__ == "__main__":
    main()
