import numpy as np
import time


def create_samples(len_sample):
    # get a sample of size len_sample
    return list(np.random.randint(0, 1000, len_sample))


def timer(func, sample):
    t1 = time.perf_counter()
    func(sample)
    t2 = time.perf_counter()
    # print(t2-t1)
    return t2-t1


def avg_time(func, len_sample=2, trials=1):
    sum_time = 0
    i = 0
    while i < trials:
        sample = create_samples(len_sample)
        sum_time += timer(func, sample)
        i += 1
    return sum_time/trials
    # print(f"{func.__name__} avg_time taken for list of size {len(sample)} iterations: {avg_time}")