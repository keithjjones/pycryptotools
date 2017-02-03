class MonoAlphaSubstitution(object):
    """
    A monoalpha cipher object.
    """
    def __init__(self, cipherkey, plainvalues):
        """
        Creates a mono alpha cipher object.

        :param cipherkey:  A list or string corresponding to the plain text values.
        :param plainvalues: The corresponding plain text values.
        """
        if len(cipherkey) != len(plainvalues):
            raise Exception("Cipher key and plain values are not the same size!")
        if len(cipherkey) < 1:
            raise Exception("Cipher key must be one or more characters!")
        if len(plainvalues) < 1 :
            raise Exception("Plan values must be one or more characters!")

        self.cipherkey = cipherkey
        self.plainvalues = plainvalues

    def decrypt(self, ciphertext):
        """
        Decrypts the cipher text using the key inside this object.

        :param ciphertext:  The cipher text to decrypt.
        :return: The plain text version of the cipher, using the key inside this object.
        """
        ciphertoplain = self.ciphertoplain()

        plaintext = ""
        for c in ciphertext:
            if c in ciphertoplain:
                plaintext += ciphertoplain[c]
            else:
                plaintext += c

        return plaintext

    def encrypt(self, plaintext):
        """
        Encrypts the plain text using the key inside this object.

        :param plaintext:  The plain text to encrypt.
        :return: The cipher text version of the plain text, using the key inside this object.
        """
        plaintocipher = self.plaintocipher()

        ciphertext = ""
        for p in plaintext:
            if p in plaintocipher:
                ciphertext += plaintocipher[p]
            else:
                ciphertext += p

        return ciphertext

    def ciphertoplain(self):
        """
        Returns a dictionary with key the cipher key and the value the plain text value.

        :return: A dictionary useful for deciphering text.
        """
        c2p = dict()
        for i in range(len(self.cipherkey)):
            c2p[self.cipherkey[i]] = self.plainvalues[i]
        return c2p

    def plaintocipher(self):
        """
        Returns a dictionary with key the plain text key and the value the cipher text value.

        :return: A dictionary useful for ciphering text.
        """
        p2c = dict()
        for i in range(len(self.plainvalues)):
            p2c[self.plainvalues[i]] = self.cipherkey[i]
        return p2c
