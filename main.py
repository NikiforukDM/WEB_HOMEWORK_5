from multiprocessing import Pool, cpu_count
from datetime import datetime


def factorize_with_one_process(*number):

    num_list = []
    for num in number:
        one_num_list = []
        for numb in range(1, num+1):
            if not num % numb:
                one_num_list.append(numb)
            else:
                continue
        num_list.append(one_num_list)
    return num_list


def factorize_with_processes(number):
    one_num_list = []
    for numb in range(1, number + 1):
        if not number % numb:
            one_num_list.append(numb)
        else:
            continue
    return one_num_list


if __name__ == '__main__':
    number_list = [128, 255, 99999, 10651060]
    start = datetime.now()
    print(factorize_with_one_process(128, 255, 99999, 10651060))
    print(f'With one process: {datetime.now() - start} sec')

    start = datetime.now()
    with Pool(cpu_count()) as pool:
        print(pool.map(factorize_with_processes, number_list))
    print(f'With {cpu_count()} processes: {datetime.now() - start} sec')





