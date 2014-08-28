# _*_ coding: utf-8 _*_
#
# Author: TeaEra
# Created date: 2014-08-28

def find_median_sorted_arrays(A, B):
    if not A and not B:
        return 0
    len_a = len(A)
    len_b = len(B)
    if not A or not B:
        temp_arr = A if A else B
        len_temp = len(temp_arr)
        if len_temp == 1:
            return temp_arr[0]
        if len_temp % 2 == 0:
            return (temp_arr[len_temp / 2 - 1] + temp_arr[len_temp / 2]) / 2.0
        if len_temp % 2 == 1:
            return temp_arr[len_temp / 2]
    idx_a = 0
    idx_b = 0
    arr = list()
    while idx_a < len_a and idx_b < len_b:
        if A[idx_a] < B[idx_b]:
            arr.append(A[idx_a])
            idx_a += 1
        else:
            arr.append(B[idx_b])
            idx_b += 1
    while idx_a < len_a:
        arr.append(A[idx_a])
        idx_a += 1
    while idx_b < len_b:
        arr.append(B[idx_b])
        idx_b += 1
    mid = (len_a + len_b) / 2
    if (len_a + len_b) % 2 == 0:
        return (arr[mid-1] + arr[mid])/2.0
    else:
        return arr[mid]

if __name__ == "__main__":
    print(find_median_sorted_arrays([1, 2, 3], [4, 5, 6]))