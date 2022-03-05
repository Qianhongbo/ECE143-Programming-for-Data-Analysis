def convert_hex_to_RGB(x):
    """
    Given a list of color hex-codes (e.g., ['#FFAABB']),
    write a function to convert these into a list of RGB-tuples.
    For example, [(255,170,187)] corresponds to the example above.

    :param x: a list of hex-codes
    :return: a list of RGB tuples
    """
    assert isinstance(x,list)

    result = []
    for j in range(len(x)):
        assert isinstance(x[j], str)
        assert len(x[j]) == 7

        value = x[j].lstrip('#')
        result.append(tuple(int(value[i:i + 2], 16) for i in (0, 2, 4)))
    return result


# print(convert_hex_to_RGB(['#FFAABB', '#FFAABB', '#FFAABB']))