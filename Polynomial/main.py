class Polynomial:
    """
    the Polynomial class
    """
    def __init__(self, dic):
        """
        :param dic: a dictionary
        """
        assert isinstance(dic, dict)
        for theKey in list(dic.keys()):
            assert isinstance(theKey, int)
            assert theKey >= 0
            assert isinstance(dic[theKey], int)

            if dic[theKey] == 0:
                del dic[theKey]
        self.dic = dic
    
    def __repr__(self):
        res = ""
        keyList = sorted(self.dic.keys())
        for key in keyList:
            if self.dic[key] == 0:
                continue
            theStr = str(self.dic[key]) + " "
            if key == 0:
                res += theStr + "+ "
            elif theStr == "1 ":
                if key == 1:
                    res += "x + "
                else:
                    res += "x^(" + str(key) + ") + "
            else:
                if key == 1:
                    res += theStr + "x + "
                else:
                    res += theStr + "x^(" + str(key) + ") + "
        return res[:-3]

    def __mul__(self, other):
        assert isinstance(other, int) or isinstance(other, Polynomial)
        newDic = {}
        if isinstance(other, int):
            for key in self.dic:
                newDic[key] = other * self.dic[key]
        else:
            for selfKey in self.dic:
                for otherKey in other.dic:
                    newKey = selfKey + otherKey
                    if newKey in newDic:
                        newDic[newKey] += self.dic[selfKey] * other.dic[otherKey]
                    else:
                        newDic[newKey] = self.dic[selfKey] * other.dic[otherKey]
        return Polynomial(newDic)

    def __rmul__(self, anInt):
        assert isinstance(anInt, int)
        newDic = {}
        for key in self.dic:
            newDic[key] = anInt * self.dic[key]
        return Polynomial(newDic)

    def __add__(self, other):
        assert isinstance(other, int) or isinstance(other, Polynomial)
        newDic = self.dic.copy()
        if isinstance(other, int):
            newDic[0] += other
        else:
            for key in other.dic:
                if key in newDic:
                    newDic[key] += other.dic[key]
                else:
                    newDic[key] = other.dic[key]
        return Polynomial(newDic)

    def __sub__(self, other):
        assert isinstance(other, int) or isinstance(other, Polynomial)
        newDic = self.dic.copy()
        if isinstance(other, int):
            newDic[0] -= other
        else:
            for key in other.dic:
                if key in newDic:
                    newDic[key] -= other.dic[key]
                else:
                    newDic[key] = -other.dic[key]
        return Polynomial(newDic)
    
    def subs(self, anInt):
        assert isinstance(anInt, int)
        result = 0
        for key in self.dic:
            result += self.dic[key] * anInt ** key 
        return result
    
    def __eq__(self, other):
        assert isinstance(other, Polynomial) or isinstance(other, int)
        if isinstance(other, Polynomial):
            return self.dic == other.dic
        else:
            if self.dic == {} and other == 0:
                return True
            for key in self.dic:
                if (key != 0 and self.dic[key] != 0) or (key == 0 and self.dic[key] != other):
                    return False
                return True

    def __truediv__(self, other):
        assert isinstance(other, int) or isinstance(other, Polynomial)
        newDic = {}
        if isinstance(other, int):
            for key in self.dic:
                newDic[key] = other // self.dic[key]
        else:
            dic1 = self.dic
            dic2 = other.dic
            keyList1 = list(dic1.keys())
            for theKey in range(max(keyList1)):
                if theKey not in dic1:
                    dic1[theKey] = 0
            keyList2 = list(dic2.keys())
            for theKey in range(max(keyList2)):
                if theKey not in dic2:
                    dic2[theKey] = 0
            l1 = [dic1[theKey] for theKey in reversed(sorted(list(dic1.keys())))]
            l2 = [dic2[theKey] for theKey in reversed(sorted(list(dic2.keys())))]
            diff = len(l1) - len(l2)
            ans = []
            for i in range(diff + 1):
                coeff = l1[i] // l2[0]
                ans.append(coeff)
                for j in range(len(l2)):
                    l1[j + i] -= l2[j] * coeff
            if l1 != [0] * len(l1):
                raise NotImplementedError
            ans.reverse()
            for j in range(len(ans)):
                newDic[j] = ans[j]
            return Polynomial(newDic)


p=Polynomial({0:8,1:2,3:4})
q=Polynomial({0:8,1:2,2:8,4:4})
print(repr(p))
print(p*3)
print(3*p)
print(p+q)
print(p*4 + 5 - 3*p - 1)
print(type(p-p))
print(p*q)
print(p.subs(10))
print((p-p) == 0)
print(p == q)
p=Polynomial({0:8,1:0,3:4})
print(repr(p))
p = Polynomial({2:1,0:-1})
q = Polynomial({1:1,0:-1})
print(p / q)
# print(p / Polynomial({1:1,0:-3}))

m = Polynomial({7:1,5:3,3:4,1:4})
print(m)
n = Polynomial({3:1, 1:2})
print(n)
print(m/n)