def gather_values(x):
    """
    Now that you have get_sample working, generate n samples and tally the number of times an existing key is repeated.
    Generate a new dictionary with bitstrings as keys and with values as lists
    that contain the corresponding mapped values from map_bitstring.

    :param x: generate through get_sample function
    :return: a new dictionary
    """
    assert isinstance(x, list)

    result = {}
    for bitString in x:
        bitList = list(bitString)
        numOfZero = 0
        numOfOne = 0
        for b in bitList:
            if b == '0': numOfZero += 1
            if b == '1': numOfOne += 1
        temp = int(numOfZero <= numOfOne)
        numOfZero = 0
        numOfOne = 0
        if bitString not in result:
            result[bitString] = []
            result[bitString].append(temp)
        else:
            result[bitString].append(temp)
    return result

# x = ['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']
# print(gather_values(x))
