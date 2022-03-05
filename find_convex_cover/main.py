import numpy as np
import math

def find_convex_cover(pvertices,clist):
    """

    :param pvertices: an array
    :param clist: a list
    :return: a list
    """
    assert type(pvertices) is np.ndarray
    assert isinstance(clist, list)

    aList = np.array(clist)
    theIndex = []
    anotherList = []
    for i in pvertices:
        aList = np.array(clist)
        aList -= i
        aList = np.sqrt(np.sum(aList ** 2, axis = -1))
        theIndex.append(np.argmin(aList))
        anotherList.append(aList)
    aDic = {}
    for i in range(len(theIndex)):
        if theIndex[i] not in aDic:
            aDic[theIndex[i]] = anotherList[i][theIndex[i]]
        else:
            aDic[theIndex[i]] = max(aDic[theIndex[i]], anotherList[i][theIndex[i]])
    ans = [0] * len(clist)
    for theKey in aDic:
        ans[theKey] = aDic[theKey]
    return ans

# if __name__ == "__main__":
#     pvertices = np.array([[0.573, 0.797],
#                           [0.688, 0.402],
#                           [0.747, 0.238],
#                           [0.802, 0.426],
#                           [0.757, 0.796],
#                           [0.589, 0.811]])
#     clist = [(0.7490863467660889, 0.4917635308023209),
#              (0.6814339441396109, 0.6199470305156477),
#              (0.7241617773773865, 0.6982813914515696),
#              (0.6600700275207232, 0.7516911829987891),
#              (0.6315848053622062, 0.7730550996176769),
#              (0.7348437356868305, 0.41342916986639894),
#              (0.7597683050755328, 0.31729154508140384)]
#     print(find_convex_cover(pvertices,clist))