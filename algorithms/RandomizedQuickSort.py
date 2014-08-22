# _*_ coding: utf-8 _*_

__author__ = 'TeaEra'

import random


def randomized_quick_sort(arr):
    """
    en:
    Randomized QuickSort

    zh:
    随机化快速排序
    """
    size = len(arr)
    if size <= 1:
        return arr
    random_index = random.randint(0, size-1)
    pivot = arr[random_index]
    less_part = list()
    mort_part = list()
    for i in range(size):
        if i != random_index:
            if arr[i] < pivot:
                less_part.append(arr[i])
            else:
                mort_part.append(arr[i])
    sorted_less_part = randomized_quick_sort(less_part)
    sorted_more_part = randomized_quick_sort(mort_part)
    return sorted_less_part + [pivot] + sorted_more_part

if __name__ == "__main__":
    #
    print("---")
    print(randomized_quick_sort([]))
    #
    print("---")
    print(randomized_quick_sort([9, 1, 3, 7, 4, 2, 8, 5, 0]))