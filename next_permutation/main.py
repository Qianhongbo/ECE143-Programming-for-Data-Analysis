def next_permutation(t):
    """
    next permutation
    """
    assert isinstance(t, tuple)

    t = list(t)
    for i in range(len(t) - 2, -1, -1):
        assert isinstance(t[i], int)
        assert t[i] <= len(t)
        assert len(list(set(t))) == len(t)
        
        if t[i] < t[i + 1]:
            theIndex = findSmallest(t[i:]) + i
            t[i], t[theIndex] = t[theIndex], t[i]
            t[i + 1:] = reversed(t[i + 1:])
            break
        elif i == 0:
            t = reversed(t)
    return tuple(t)


def findSmallest(t):
    theSmallest = t[1]
    for i in range(1, len(t)):
        if t[i] >= t[0]:
            theSmallest = min(theSmallest, t[i])
    return t.index(theSmallest)

# if __name__ == "__main__":
    # print(next_permutation((2,3,1)))
    # print(next_permutation((0, 5, 2, 1, 4, 7, 3, 6)))
    # print(next_permutation((3,2,1,0)))