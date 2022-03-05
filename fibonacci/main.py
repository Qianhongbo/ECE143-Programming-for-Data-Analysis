def fibonacci(n):
    """
    The Fibonacci numbers are defined by the following recursion: F[n] = F[n-1]+F[n-2] with initial values F[1]=F[0]=1.
    Write a generator to compute the first n Fibonacci numbers.

    :param n: A number(int)
    :return: generator
    """
    assert isinstance(n, int)
    assert n > 0

    i = 0
    a, b = 0, 1
    while i < n:
        yield b
        a, b = b, a + b
        i += 1

# print(list(fibonacci(10)))