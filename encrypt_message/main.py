def encrypt_message(message, fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.

    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert isinstance(message, str)
    assert isinstance(fname, str)

    dict = {}
    result = []

    with open(fname, "r") as f:
        data = f.readline()
        str_list = data.split()
        for word in str_list:
            if word not in dict:
                dict[word] = []
            dict[word].append((1, str_list.index(word)))
        line = 1
        while data:
            data = f.readline()
            line += 1
            str_list = data.split()
            for word in str_list:
                if word not in dict:
                    dict[word] = []
                dict[word].append((line, str_list.index(word) + 1))

    message_list = message.split()
    for word in message_list:
        if word in dict and dict[word] != []:
            result.append(dict[word].pop(-1))

    return result


def decrypt_message(inlist, fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message.

    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''
    assert isinstance(inlist, list)
    assert isinstance(fname, str)
    assert len(list(set(inlist))) == len(inlist)

    result = [""] * len(inlist)
    lines = [x for (x, _) in inlist]
    indexOfLines = [y for (_, y) in inlist]
    with open(fname, "r") as f:
        data = f.readline()
        line = 1
        while data:
            data = f.readline()
            line += 1
            if line in lines:
                temp = []
                for ind, nums in enumerate(lines):
                    if nums == line:
                        temp.append(ind)
                for t in temp:
                    theIndex = indexOfLines[t] - 1
                    theWord = data.split()[theIndex]
                    result[t] = theWord
    return ' '.join(result)



if __name__ == '__main__':
    # message = "let us not say we met late at the night about the secret"
    # fname = "pg5200.txt"
    # encryptMes = encrypt_message(message, fname)
    # print(encryptMes)
    # print(decrypt_message(encryptMes, fname))
