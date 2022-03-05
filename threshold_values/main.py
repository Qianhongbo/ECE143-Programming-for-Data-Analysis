def threshold_values(seq,threshold=1):
    """
    From gather_values, we can group the results of the random samples.
    Now, we want to threshold those values based upon their frequency and value.
    Given threshold=2, we want to keep only those bitstrings with the two highest frequency counts of the 1 value.

    :param seq: a list
    :param threshold: a number(int)
    :return: a dictionary
    """
    assert isinstance(seq, list)
    assert isinstance(threshold, int)
    assert threshold >= 0

    result = {}
    for bitString in seq:
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
            result[bitString] = 0
            result[bitString] += temp
        else:
            result[bitString] += temp
    ls = sorted(result.items(), key = lambda x: (x[1], -int(x[0])), reverse = True)
    temp = 0
    for j in range(len(ls)):
        if temp < threshold:
            result[ls[j][0]] = 1
            temp += 1
        else:
            result[ls[j][0]] = 0
    return result

# x=['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']
# print(threshold_values(x,3))

# seq= ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101', '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011', '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000', '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011', '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001', '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001']
# print(threshold_values(seq,3) )