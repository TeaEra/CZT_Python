__author__ = 'TeaEra'


def merge_sort(int_list):
    """
    en:
    MergeSort

    zh:
    归并排序
    """
    if not int_list:
        return "Invalid input"
    size = len(int_list)
    if size == 1:
        return int_list
    mid = size / 2
    left_int_list = merge_sort(int_list[0:mid])
    right_in_list = merge_sort(int_list[mid:size])
    return merge(left_int_list, right_in_list)


def merge(left_int_list, right_int_list):
    size1 = len(left_int_list)
    size2 = len(right_int_list)
    idx1 = 0
    idx2 = 0
    out_int_list = list()
    while idx1 < size1 and idx2 < size2:
        if left_int_list[idx1] < right_int_list[idx2]:
            out_int_list.append(left_int_list[idx1])
            idx1 += 1
        else:
            out_int_list.append(right_int_list[idx2])
            idx2 += 1
    while idx1 < size1:
        out_int_list.append(left_int_list[idx1])
        idx1 += 1
    while idx2 < size2:
        out_int_list.append(right_int_list[idx2])
        idx2 += 1
    return out_int_list

if __name__ == "__main__":
    #
    print("---")
    print(merge_sort([]))
    #
    print("---")
    print(merge_sort(["abc", "123", "234", "bcx", "zyd"]))
    #
    print("---")
    print(merge_sort([9, 1, 2, 7, 5, 3, 4, 6, 8]))
    #
    print("---")
    print(merge_sort([123, "123", 456, "abc"]))