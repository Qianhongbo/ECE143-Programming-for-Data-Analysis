def slide_window(x,width,increment):
    """
    Implement a sliding window for an arbitrary input list.
    The function should take the window width and the window increment as inputs
    and should produce a sequence of overlapping lists from the input list.

    :param x: x is a list
    :param width: width>0
    :param increment:  increment>0
    :return:
    """
    assert isinstance(x, list)
    assert width > 0
    assert increment > 0

    result = []
    for i in range(0, len(x), increment):
        if i + width <= len(x):
            result.append(x[i: i+width])
    return result

# x = list(range(10))
# width = 5
# increment = 2
# print(slide_window(x,width,increment))