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