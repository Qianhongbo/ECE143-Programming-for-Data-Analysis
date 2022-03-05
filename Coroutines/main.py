# from time import sleep
# import random
# from datetime import datetime
# import itertools as it
#
#
# def producer():
#     'produce timestamps'
#     starttime = datetime.now()
#     while True:
#         sleep(random.uniform(0, 0.2))
#         yield datetime.now() - starttime


def tracker(p,limit):
    """
    Write a generator that tracks the output of this producer and ultimately returns the number of
    odd numbered seconds that have been iterated over.
    Your tracker generator should also receive input that changes the existing limit.

    :param p: the producer function
    :param limit: The limit keyword argument is the number of odd-numbered seconds to track until completion.
    :return: return the number of odd numbered seconds that have been iterated over
    """
    assert isinstance(limit, int)
    assert limit > 0

    temp = 0
    p.send(None) # initialize
    while True:
        if limit is None:
            limit = temp2
        temp2 = limit
        temp = p.send(None).seconds
        if temp - temp // 2 > limit:
            return
        limit = yield temp - temp // 2


# p = producer()
# # print(list(tracker(p,5)))
#
# t = tracker(p,5)
# next(t)
# t.send(3)
# t.send(2)
# print(list(t))
