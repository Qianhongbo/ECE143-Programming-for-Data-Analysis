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


def square_root_rational(x, abs_tol=Rational(1,1000)):
    """

    :param x: an input rational number x
    :param abs_tol:
    :return: a Rational number instance as output
    """
    assert isinstance(x, Rational)
    assert isinstance(abs_tol, Rational)

    val1 = Rational(1,1000)
    val2 = x
    temp = (val1 + val2) / 2
    while abs(float(x - temp * temp)) > float(abs_tol):
        temp = (val1 + val2) / 2
        if temp * temp > x:
            val2 = temp
        else:
            val1 = temp
    return temp


# if __name__ == "__main__":
#     print(square_root_rational(Rational(1112,3),abs_tol=Rational(1,1000)))
#     print(float(square_root_rational(Rational(1112,3),abs_tol=Rational(1,1000))))
#     print(math.sqrt(float(Rational(1112,3))))

