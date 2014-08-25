__author__ = 'TeaEra'


def merge(A, m, B, n):
    if m == 0:
        for i in range(n):
            A[i] = B[i]
    pre_idx = 0
    for i in range(n):
        curr = B[i]
        idx = pre_idx
        while A[idx] < curr and idx < m + i:
            idx += 1
        for j in range(m+i, idx-1, -1):
            A[j] = A[j-1]
        A[idx] = curr
        pre_idx = idx

if __name__ == "__main__":
    #
    print("---")
    arr_A = [1]
    len_m = len(arr_A)
    arr_B = [2]
    len_n = len(arr_B)
    arr_A = arr_A + arr_B
    merge(arr_A, len_m, arr_B, len_n)
    print(arr_A)