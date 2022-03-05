def split_by_n(fname, n=3):
    '''
    Split files into sub files of near same size

    :param fname: Input file name
    :param n: the number of segments
    :return: nothing
    '''
    assert isinstance(fname, str)
    assert isinstance(n, int)
    assert n > 1

    totalNumOfBytes = 139055
    divideNum = totalNumOfBytes / n
    with open(fname, "r") as f1:
        for i in range(n):
            with open(fname + "_{num}.txt".format(num = '{0:03}'.format(i)), "wt") as f2:
                data = f1.readline()
                temp = len(data)
                f2.write(data)
                while True:
                    fine_num = f1.tell()
                    data = f1.readline()
                    temp += len(data)
                    if temp > divideNum and i != n - 1:
                        f1.seek(fine_num)
                        break
                    f2.write(data)


# if __name__ == '__main__':
#     split_by_n("pg5200.txt", 12)
#     temp = 0
#     with open("pg5200.txt_007.txt", "r") as f1:
#         data = f1.readline()
#         temp += len(data)
#         while data:
#             data = f1.readline()
#             temp += len(data)
#     print(temp)