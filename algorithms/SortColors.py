__author__ = 'TeaEra'


def sort_colors(A):
    idx_0 = 0
    idx_1 = 0
    idx_2 = 0
    for i in range(len(A)):
        if A[i] == 0:
            A[idx_2] = 2
            idx_2 += 1
            A[idx_1] = 1
            idx_1 += 1
            A[idx_0] = 0
            idx_0 += 1
        elif A[i] == 1:
            A[idx_2] = 2
            idx_2 += 1
            A[idx_1] = 1
            idx_1 += 1
        elif A[i] == 2:
            A[idx_2] = 2
            idx_2 += 1

if __name__ == "__main__":
    #
    A = [1, 2, 1, 0, 1, 2, 1]
    sort_colors(A)
    print(A)