from multiprocessing import Process, Pool, Queue, Manager, Pipe, JoinableQueue
from datetime import datetime


def factorize(man, *number):
    num_list = []
    start = datetime.now()
    for num in number:
        one_num_list = []
        for numb in range(1, num+1):
            if not num % numb:
                one_num_list.append(numb)
            else:
                continue
        num_list.append(one_num_list)

    end = datetime.now()
    print(end - start)
    return num_list

#
# a, b, c, d = factorize(128, 255, 99999, 10651060)
# [a, b, c, d]()
# for a in [a, b, c, d]:
#     a()


print(factorize(128, 255, 99999, 1065106))
