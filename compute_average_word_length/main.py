def compute_average_word_length(instring, unique=False):
    '''
    Write a compute_average_word_length(instring,unique=False) function
    to compute the average length of the words in the input string (instring).
    If the unique option is True, then exclude duplicated words.
    For example, in the example input text above,
    the word the should be counted exactly once for the average word length if unique=True.
    Note that the words are case sensitive.

    :param instring: the input string
    :param unique: If the unique option is True, then exclude duplicated words.
    :return: the average word length
    '''
    assert isinstance(instring, str)
    assert isinstance(unique, bool)

    instring_list = instring.split()
    if unique:
        temp = set(instring_list)
        instring_list = list(temp)

    sum = 0
    for i in instring_list:
        sum += len(i)
    return sum / len(instring_list)


# test = '''Mary had a little lamb
# its fleece was white as snow
# and everywhere that Mary went
# the lamb was sure to go'''
# print(compute_average_word_length(test, True))