import pandas
from collections import OrderedDict
from math import log10

# Data from http://norvig.com/mayzner.html
# Math and scoring process adopted from
# http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/#a-python-implementation
class mayzner_data(object):
    """
    Object to hold data from http://norvig.com/mayzner.html
    """
    def __init__(self, filename):
        """
        Object to hold data from http://norvig.com/mayzner.html

        :param filename:  CSV file name to read.
        """
        self.filename = filename
        self.pandas_data = pandas.read_csv(self.filename, keep_default_na=False, na_values=['_'])
        self.type_of_file = self.pandas_data.columns[0]

        pd = self.pandas_data[[self.type_of_file, '*/*']]

        self.log_prob = OrderedDict()
        self.N = pd['*/*'].sum()

        for i, row in pd.iterrows():
            self.log_prob[row[self.type_of_file].lower()] = log10(float(row['*/*'])/self.N)
            self.n = len(row[self.type_of_file])

        self.lowest_value = log10(0.01/self.N)

    def score(self, plaintext):
        """
        Creates a additive score based upon the log frequency of the n-grams.

        :param plaintext: Plain text to score.
        :return: The score.
        """
        score = 0
        ngrams = self.log_prob.__getitem__
        for i in range(len(plaintext)-self.n+1):
            if plaintext[i:i + self.n] in self.log_prob:
                score += ngrams(plaintext[i:i + self.n])
            else:
                score += self.lowest_value
        return score


# Data from http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/#a-python-implementation
# Math and scoring process adopted from that site as well.
class practical_cryptography_data(object):
    """
    Object to hold n-gram data from http://practicalcryptography.com
    """
    def __init__(self, filename):
        """
        Object to hold n-gram data from http://practicalcryptography.com

        :param filename: TXT file name to read.
        """
        self.filename = filename
        self.pandas_data = pandas.read_csv(self.filename, header=None, delimiter=' ', names=['gram', 'count'],
                                           keep_default_na=False, na_values=['_'])

        self.log_prob = OrderedDict()
        self.N = self.pandas_data['count'].sum()

        for i, row in self.pandas_data.iterrows():
            self.log_prob[row['gram'].lower()] = log10(float(row['count'])/self.N)
            self.n = len(row['gram'])

        self.lowest_value = log10(0.01/self.N)

    def score(self, plaintext):
        """
        Creates a additive score based upon the log frequency of the n-grams.

        :param plaintext: Plain text to score.
        :return: The score.
        """
        score = 0
        ngrams = self.log_prob.__getitem__
        for i in range(len(plaintext)-self.n+1):
            if plaintext[i:i + self.n] in self.log_prob:
                score += ngrams(plaintext[i:i + self.n])
            else:
                score += self.lowest_value
        return score