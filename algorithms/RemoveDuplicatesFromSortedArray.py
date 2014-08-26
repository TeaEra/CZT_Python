__author__ = 'TeaEra'


def remove_duplicates(A):
    size = len(A)
    if size == 0 or size == 1:
        return size
    idx = 0
    A[idx] = A[0]
    for i in range(1, size):
        if A[i] != A[idx]:
            idx += 1
            A[idx] = A[i]
    return idx+1

if __name__ == "__main__":
    #
    print("---")
    arr = [1, 1, 2]
    print(arr[:remove_duplicates(arr)])