def write_columns(data,fname):
    """
    Write a function that can write the following formula to three columns to a comma-separated file:
    data_value, data_value**2, (data_value+data_value**2)/3.
    Your written floating-point values should be formatted to the hundreths place.

    :param data: data must be a list
    :param fname: fname is a string
    :return: a file
    """
    assert isinstance(data, list)
    assert isinstance(fname, str)

    newList = [[str(i), str(i**2), str(round((i + i**2) / 3, 2))] for i in data]
    text = ''
    for i in range(len(data)):
        temp = ', '.join(newList[i])
        temp = ''.join([temp, '\n'])
        text = ''.join([text, temp])

    f = open(fname, 'w')  # write mode
    f.write(text)
    f.close()


# data = [5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]
# fname = 'test'
# write_columns(data,fname)