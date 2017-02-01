def ngram2_matrix_error(expectedmatrix, calculatedmatrix):
    error = 0
    for r in expectedmatrix:
        for c in expectedmatrix[r]:
            if r not in calculatedmatrix:
                calculatedvalue = 0
            else:
                if c not in calculatedmatrix[r]:
                    calculatedvalue = 0
                else:
                    calculatedvalue = calculatedmatrix[r][c]

            error += abs(expectedmatrix[r][c] - calculatedvalue)

    return error
