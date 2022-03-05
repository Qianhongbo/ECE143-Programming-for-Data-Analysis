import random
import itertools
import math

def multinomial_sample(n, p, k=1):
    '''
    Return samples from a multinomial distribution.

    n:= number of trials
    p:= list of probabilities
    k:= number of desired samples
    '''
    assert isinstance(n, int)
    assert isinstance(p, list)
    assert isinstance(k, int)
    assert n > 0
    assert sum(p) == 1
    assert k > 0

    aList = []
    for i in itertools.product(range(0, n + 1), repeat = len(p)):
        if sum(i) == n:
            aList.append(list(i))
    probabilities = [0] * len(aList)

    for l in range(len(aList)):
        temp1 = 1
        temp2 = 1
        for j in range(len(aList[l])):
            temp1 *= math.factorial(aList[l][j])
            temp2 *= p[j]**aList[l][j]
        probabilities[l] = math.factorial(n) * temp2 / temp1

    result = []
    for i in range(k):
        result.append(random_pick(aList, probabilities))
    return result


def random_pick(some_list,probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item,item_probability in zip(some_list,probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item


# if __name__ == '__main__':
#     print(multinomial_sample(10,[1/3,1/3,1/3],k=10))
