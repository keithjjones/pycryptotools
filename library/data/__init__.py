import pandas


def ngram2_data_to_matrix(indata):

    matrix = dict()

    total = indata['*/*'].sum()

    for i, row in indata.iterrows():
        digram = list()
        digram.append(row['2-gram'][0].lower())
        digram.append(row['2-gram'][1].lower())
        value = row['*/*']/total
        if digram[0] not in matrix:
            matrix[digram[0]] = dict()
        matrix[digram[0]][digram[1]] = value

    return matrix

def calculatedprob_to_matrix(indata):

    matrix = dict()

    for c in indata:
        digram = list()
        digram.append(c[0].lower())
        digram.append(c[1].lower())
        value = indata[c]

        if digram[0] not in matrix:
            matrix[digram[0]] = dict()
        matrix[digram[0]][digram[1]] = value

    return matrix
