import pandas
from collections import OrderedDict
from math import log10

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

        self.lowest_value = log10(.1/self.N)

    def score(self, plaintext):
        """
        Creates a additive score based upon the log frequency of the n-grams.
        :param plaintext: Plain text to score.
        :return: The score.
        """
        myscore = 0
        for l in self.log_prob:
            s = plaintext.split(l)
            if len(s) > 1:
                myscore += (len(s) - 1) * self.log_prob[l]
            else:
                myscore += self.lowest_value
        return myscore