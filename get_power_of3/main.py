import itertools
def get_power_of3(value):
    """
    Given a set of weights {1,3,9,27}, write a function to construct any number between 1 and 40.
    In other words, using the set above and the addition and subtraction operations,
    construct any integer between 1 and 40 without re-using elements.
    For example, 4 = 1+1+1+1 is not acceptable.

    :param value: A number between 1 to 40
    :return: A 4-element list of the decomposition
    """
    assert value >=1
    assert value <=40
    temp = {}
    for i, j in enumerate(itertools.product([-1, 0, 1], repeat=4)):
        if i > 40:
            temp[i - 40] = list(reversed(j))
    return temp[value]
