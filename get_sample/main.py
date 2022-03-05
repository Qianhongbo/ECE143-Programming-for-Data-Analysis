import random

def get_sample(nbits=3,prob=None,n=1):
    """
    Given a number of bits, write the get_sample function to return a list n of random samples
    from a finite probability mass function defined by a dictionary with keys defined by a specified number of bits.
    For example, given 3 bits, we have the following dictionary that defines the probability of each of the keys.
    The values of the dictionary correspond of the probability of drawing any one of these.

    :param nbits: how many bits(int), default value is 3
    :param prob: a dictionary or None
    :param n: the number of the list(int), default value is 1
    :return: a list
    """
    assert isinstance(nbits, int)
    assert nbits >= 0
    if prob is not None:
        assert isinstance(prob, dict)
    else:
        return []
    assert isinstance(n, int)
    assert n >= 0

    valueOfDict = prob.values()
    assert sum(valueOfDict) == 1
    for v in valueOfDict:
        assert v >= 0
        assert v <= 1

    keyOfDict = prob.keys()
    keyOfLenN = []

    for k in keyOfDict:
        assert k.isdigit()
        assert int(k) <= int('1' * len(k))

        if len(k) == nbits:
            keyOfLenN.append(k)

    result = []
    if len(keyOfLenN) > 0:
        for j in range(n):
            result.append(keyOfLenN[random.randint(0, len(keyOfLenN) - 1)])
        return result
    else:
        return []


# p = {
#     '000': 0.125,
#     '001': 0.125,
#     '010': 0.125,
#     '011': 0.125,
#     '100': 0.125,
#     '101': 0.125,
#     '110': 0.125,
#     '111': 0.125}
# print(get_sample(nbits=3,prob=p,n=4))

# x=get_sample(nbits=2,prob={'00':1/4,'01':1/4,'10':1/4,'11':1/4},n=20)
# print(x)