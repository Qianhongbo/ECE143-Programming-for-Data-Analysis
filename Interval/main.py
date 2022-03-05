class Interval(object):
    """
    Interval represents a one-dimensional open interval on the real line.
    This main purpose of this class is to simplify overlapping continuous intervals.
    """
    def __init__(self, a, b):
        """
        :a: integer
        :b: integer
        """
        assert a < b
        assert isinstance(a, int)
        assert isinstance(b, int)
        self._a = a
        self._b = b

    def __repr__(self):
        pass

    def __eq__(self, other):
        return True if (self._a == other._a and self._b == other._b) else False

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass

    def __add__(self, other):
        if self == other: return self
        aMin, bMax = min(self._a, other._a), max(self._b, other._b)
        if (aMin == self._a and bMax == self._b): return self
        if (aMin == other._a and bMax == other._b): return other
        if (aMin == self._a and bMax == other._b):
            if self._b > other._a: return Interval(aMin, bMax)
            else: return [Interval(aMin, self._b), Interval(other._a, bMax)]
        if (aMin == other._a and bMax == self._b):
            if other._b > self._a: return Interval(aMin, bMax)
            else: return [Interval(aMin, other._b), Interval(self._a, bMax)]


# if __name__ == '__main__':
#     a = Interval(1, 3)
#     b = Interval(2, 4)
#     c = Interval(5, 10)
#     print((a + b)[0] == Interval(1, 4))
#     print((b + c) == [Interval(2, 4), Interval(5, 10)])


