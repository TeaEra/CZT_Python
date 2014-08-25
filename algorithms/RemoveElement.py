__author__ = 'TeaEra'


def remove_element(A, elem):
    if not A:
        return 0
    size = len(A)
    diff_size = 0
    for i in range(size):
        if A[i] != elem:
            temp = A[diff_size]
            A[diff_size] = A[i]
            A[i] = temp
            diff_size += 1
    return diff_size

if __name__ == "__main__":
    #
    print("---")
    arr = [1]
    print(arr[0: remove_element(arr, 1)])