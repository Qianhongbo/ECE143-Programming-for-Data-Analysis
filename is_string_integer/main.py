def is_string_integer(x):
    '''
    Write a function that takes a single string character (i.e., 'a','b','c') as input
    and returns True or False if that character represents a valid integer in base 10.

    :param x: input character
    :return: True or False
    '''
    assert isinstance(x, str)
    assert len(x) == 1

    temp = ord(x)
    if temp >= 48 and temp <= 57:
        return True
    return False


# print(is_string_integer('r'))
# print(int('a'))
