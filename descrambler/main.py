import itertools

def descrambler(w,k):
    """
    You are given a sequence of n lower-case letters and a k-tuple of integers
    that indicate partition-lengths of the sequence.
    Also, you have a dictionary of commonly used words.
    The n letters represent a phrase of k words where the length of the jth word is the jth element of the tuple.

    :param w: a str
    :param k: a list
    :return: a list
    """
    assert isinstance(w, str)
    assert isinstance(k, tuple)

    # open the file, read the data
    wordSet = set()
    f = open("tmp/google-10000-english-no-swears.txt", encoding='utf-8')
    line = f.readline()
    while line:
        wordSet.add(line.replace('\n', ''))
        line = f.readline()
    f.close()

    def getDict(w):
        wList = list(w)
        dict = {}
        for character in wList:
            if character not in dict:
                dict[character] = 1
            else:
                dict[character] += 1
        return dict

    result = []
    for num in k:
        temp = set()
        for i in itertools.permutations(w, num):
            wd = ''.join(i)
            if wd in wordSet:
                temp.add(wd)
        result.append(list(temp))

    for i in itertools.product(*result):
        dict = getDict(w)
        wSum = ''.join(i)
        for character in list(wSum):
            dict[character] -= 1
        val = dict.values()
        temp2 = 0
        for v in val:
            if v < 0:
                temp2 += 1
        if temp2 != 0:
            continue
        yield(' '.join(i))


# print(list(descrambler('trleeohelh',(5,5))))
# print(list(descrambler('choeounokeoitg',(3,5,6))))
# print(list(descrambler('qeodwnsciseuesincereins', (4,7,12))))
