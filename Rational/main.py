import math

class Rational:
    """
    this a a rational class!
    """
    def __init__(self, val1, val2):
        """
        test
        :param val1: value 1
        :param val2: value 2
        """
        assert isinstance(val1, int)
        assert isinstance(val2, int)
        self.val1 = val1
        self.val2 = val2

    def __repr__(self):
        c = math.gcd(self.val1, self.val2)
        if self.val1 % self.val2 == 0:
            return "{num}".format(num = self.val1 // self.val2)
        elif c != 1:
            return "{num}/{den}".format(num = self.val1 // c, den = self.val2 // c)
        else:
            return "{num}/{den}".format(num = self.val1, den = self.val2)

    def __add__(self, other):
        commonMultiple = self.val2 * other.val2 // math.gcd(self.val2, other.val2)
        numerator = self.val1 * commonMultiple // self.val2 + commonMultiple // other.val2 * other.val1
        return Rational(numerator, commonMultiple)

    def __sub__(self, other):
        commonMultiple = self.val2 * other.val2 // math.gcd(self.val2, other.val2)
        numerator = self.val1 * commonMultiple // self.val2 - commonMultiple // other.val2 * other.val1
        return Rational(numerator, commonMultiple)

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(self.val1 * other, self.val2)
        elif isinstance(other, Rational):
            return Rational(self.val1 * other.val1, self.val2 * other.val2)

    def __truediv__(self, other):
        return Rational(self.val1, self.val2 * other)

    def __rtruediv__(self, other):
        return Rational(self.val2 * other, self.val1 )

    def __lt__(self, other):
        return self.val1 / self.val2 < other.val1 / other.val2

    def __neg__(self):
        return Rational(-self.val1, self.val2)

    def __int__(self):
        return self.val1 // self.val2

    def __float__(self):
        return self.val1 / self.val2

    def __eq__(self, other):
        c1 = math.gcd(self.val1, self.val2)
        c2 = math.gcd(other.val1, other.val2)
        if self.val1 // c1 == other.val1 // c2 and self.val2 // c1 == other.val2 // c2:
            return True
        else:
            return False

# if __name__ == "__main__":
#     r = Rational(3,4)
#     print(repr(r))
#     print(-1/r)
#     print(float(-1 / r))
#     print(int(r))
#     print(int(Rational(10,3)))
#     print(Rational(10,3) * Rational(101,8) - Rational(11,8))
#     print(sorted([Rational(10,3),Rational(9,8), Rational(10,1), Rational(1,100)]))
#     print(Rational(100,10))
#     print(-Rational(12345,128191))
#     print(Rational(101,103) * 30)
#     print(Rational(101,103) * 30 / 44)
#     print(-Rational(12345,128191) + Rational(101,103) * 30/ 44)
#     print(Rational(100,10) == Rational(200,20))
