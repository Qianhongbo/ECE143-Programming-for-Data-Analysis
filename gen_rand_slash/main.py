import numpy as np
# from matplotlib.pylab import subplots, cm
# import matplotlib.pyplot as plt

def gen_rand_slash(m=6,n=6,direction='back'):
    """
    Each image should represent a forward or backward leaning (shown above) slash symbol.
    Each symbol must consist of at least two non-zero pixels and be contiguous (i.e., no gaps).

    :param m: an int
    :param n: an int
    :param direction: ['back', 'forward']
    :return: a matrix
    """
    assert isinstance(m, int)
    assert isinstance(n, int)
    assert direction in ['back', 'forward']
    assert m > 1
    assert n > 1

    result = np.zeros([m, n])
    if direction == 'back':
        rand_m = np.random.randint(0, m - 1)
        rand_n = np.random.randint(0, n - 1)
        rand_l = np.random.randint(2, min(m, n) + 1)
        # print("m = ", rand_m)
        # print("n = ", rand_n)
        # print("l = ", rand_l)
        for i in range(rand_l):
            if rand_m + i < m and rand_n + i < n:
                result[rand_m + i, rand_n + i] = 1

    if direction == 'forward':
        rand_m = np.random.randint(0, m - 1)
        rand_n = np.random.randint(1, n)
        rand_l = np.random.randint(2, min(m, n) + 1)
        # print("m = ", rand_m)
        # print("n = ", rand_n)
        # print("l = ", rand_l)
        for i in range(rand_l):
            if rand_m + i < n and rand_n - i >= 0:
                result[rand_m + i, rand_n - i] = 1

    return result


# if __name__ == '__main__':
#     fig, axs = subplots(3, 3, sharex=True, sharey=True)
#     for ax in axs.flatten():
#         ax.imshow(gen_rand_slash(m=6,n=6,direction='forward'), cmap=cm.gray_r)
#     plt.show()
#     print(gen_rand_slash(m=6,n=6,direction='forward'))