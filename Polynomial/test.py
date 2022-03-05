



if __name__ == "__main__":
    dic1 = {0: -1, 2: 1}
    dic2 = {0: -1, 1: 1}
    keyList = list(dic1.keys())
    for theKey in range(max(keyList)):
        if theKey not in dic1:
            dic1[theKey] = 0
    print(dic1)
    l3 = [dic1[theKey] for theKey in reversed(sorted(list(dic1.keys())))]
    l4 = [dic2[theKey] for theKey in reversed(sorted(list(dic2.keys())))]
    print(l3)
    print(l4)
    l1 = [1, 0, -1]
    l2 = [1, -1]
    diff = len(l1) - len(l2)
    ans = []
    for i in range(diff + 1):
        coeff = l1[i] // l2[0]
        ans.append(coeff)
        for j in range(len(l2)):
            l1[j + i] -= l2[j] * coeff
    if l1 != [0] * len(l1):
        raise NotImplementedError
    print(l1)
    print(ans)
    #
    #
    # xishu = l1[0] / l2[0]
    # l1[0] -= l2[0]
    # l1[1] -= l2 [1]
    # print(l1)
    # print(l2)
    # l1[0 + 1] -= l2[0]
    # l1[1 + 1] -= l2[1]
    # print(l1)
    # print(l2)
