def count_paths(m,n,blocks):
    """

    :param m: the number of rows
    :param n: the number of columns
    :param blocks: a list of tuples indicating the blocked # entries in the grid
    :return: the number of connected paths between the top-left square and the bottom right square
    by traversing only the intermediate squares with the . symbol
    """
    assert isinstance(m, int)
    assert isinstance(n, int)
    assert m > 0
    assert n > 0
    assert isinstance(blocks, list)

    theRow = [0] * n
    firstRow = [0] * n
    firstRow[0] = 1
    theMatrix = [firstRow] + [theRow] * (m - 1)

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif (i, j) in blocks:
                theMatrix[i][j] = 0
            elif i == 0:
                theMatrix[i][j] = theMatrix[i][j - 1]
            elif j == 0:
                theMatrix[i][j] = theMatrix[i - 1][j]
            else:
                theMatrix[i][j] = theMatrix[i][j - 1] + theMatrix[i - 1][j]

    return theMatrix[m - 1][n - 1]


# if __name__ == "__main__":
#     print(count_paths(3,4,[(0,3),(1,1)]))