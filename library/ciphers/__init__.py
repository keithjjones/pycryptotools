class MonoAlphaSubstitution(object):
    def __init__(self, cipherkey, plainvalues):
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
            plaintext += ciphertoplain[c]

        return plaintext

    def ciphertoplain(self):
        """
        Returns a dictionary with key the cipher key and the value the plain text value.

        :return: A dictionary useful for deciphering text.
        """
        c2p = dict()
        for i in range(len(self.cipherkey)):
            c2p[self.cipherkey[i]] = self.plainvalues[i]
        return c2p
