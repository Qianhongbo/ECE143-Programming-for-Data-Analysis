def write_chunks_of_five(words,fname):
    """
    Using corpus of 10,000 common English words,
    create a new file that consists of each consecutive non-overlapping sequence of five lines merged into one line.

    :param words: a list of words from the above corpus
    :param fname: output filename string
    :return:
    """
    assert isinstance(words, list)
    assert isinstance(fname, str)

    text = ''
    for i,w in enumerate(words):
        assert isinstance(w, str)

        text = ' '.join([text, w])
        if (i + 1) % 5 == 0:
            text = ''.join([text, '\n'])

    f = open(fname, 'w')
    f.write(text)
    f.close()

# words = ["the","of","and","to","a","in","for","is","on","that","by","this","with","i"]
# fname = "test"
# write_chunks_of_five(words,fname)