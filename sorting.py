from util import *
import numpy as np
import matplotlib.pyplot as plt


def bubble_sort(l):
    n = len(l)-1
    for i in range(n):
        for j in range(n-i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
            j += 1

    # print("This is inside bubble function", l)


def selection_sort(l):
    # for pos starting from i
    # traverse till end
    # find min and swap with ith postion
    # repeat same from i+1 till end
    n = len(l)
    i = 0
    while i < n:
        min_index = i
        for j in range(i+1, n):
            if l[j] < l[min_index]:
                min_index = j
        temp = l[i]
        l[i] = l[min_index]
        l[min_index] = temp
        i += 1


def merge_sort(arr):
    start_ = 0
    end_ = len(arr)
    store_ = list(np.zeros(end_))

    def sort(a=arr, start=start_, end=end_, store=store_):
        if start == end-1:
            return
        else:
            # divide the arr in two parts
            mid = int((start + end)/2)
            sort(a, start, mid)
            sort(a, mid, end)
            merge(a, start, mid, end, store)
    sort()


def merge(arr, start, mid, end, store):
    k = start
    i = start
    j = mid
    # print("Before merge: ", store)
    # print(f"merge {start} to {mid} and {mid} to {end}")
    while (i < mid) and (j < end):
        if arr[i] <= arr[j]:
            store[k] = arr[i]
            i += 1
        else:
            store[k] = arr[j]
            j += 1
        k += 1
    if i == mid:
        store[k:end] = arr[j:end]
    else:
        store[k:end] = arr[i:mid]
    arr[start:end] = store[start:end]


def quick_sort(arr, low=0, high=None):
    """
    """
    if high is None:
        high = len(arr)-1
    if low >= high:
        return
    else:
        pivot = arr[high]
        i_pivot = high
        i = low
        while i < i_pivot:
            if arr[i] <= pivot:
                i += 1
            else:
                arr[i_pivot] = arr[i]
                arr[i] = arr[i_pivot - 1]
                i_pivot = i_pivot - 1
                arr[i_pivot] = pivot
        quick_sort(arr, low, i_pivot-1)
        quick_sort(arr, i_pivot+1, high)


if __name__ == '__main__':
    # setup experiment
    n_samples = 2000
    trials = 20
    funcs = {bubble_sort: [], selection_sort: [], merge_sort: [], quick_sort: []}
    sample_size = list(range(100, n_samples, 200))

    # run experiment to get time values for lists of varying length
    for len_sample in sample_size:
        for func in funcs.keys():
            funcs[func].append(avg_time(func, len_sample, trials))

    # plot time data for all sorting algorithms
    plt.figure(figsize=(8, 5));
    for key, value in funcs.items():
        plt.plot(sample_size, value, 'o-', label=key.__name__)
    plt.title('Sorting Algorithms')
    plt.ylabel('time/(s)')
    plt.xlabel('n')
    plt.grid()
    plt.legend()
    plt.show()