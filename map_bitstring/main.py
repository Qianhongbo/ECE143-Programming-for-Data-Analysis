def map_bitstring(x):
    """
    Write a function map_bitstring that takes a list of bitstrings (i.e., 0101) and maps each bitstring to 0
    if the number of 0s in the bitstring strictly exceeds the number of 1s. Otherwise, map that bitstring to 1.

    :param x: a list of bitstrings (i.e., 0101)
    :return: The output of your function is a dictionary of the so-described key-value pairs.
    """
    assert isinstance(x, list)

    result = {}
    for bitString in x:
        assert bitString.isdigit()
        assert int(bitString) <= int('1' * len(bitString))

        bitStringToInt = str(bitString)
        bitList = list(bitStringToInt)
        numOfZero = 0
        numOfOne = 0
        for b in bitList:
            if b == '0': numOfZero += 1
            if b == '1': numOfOne += 1
        result[bitString] = int(numOfZero < numOfOne)
    return result

x= ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']
print(map_bitstring(x) )