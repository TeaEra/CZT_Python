__author__ = 'TeaEra'


def search_insert(A, target):
    if not A:
        return 0
    # A is alredy sorted;
    idx = 0
    while idx < len(A) and target > A[idx]:
        idx += 1
    return idx

if __name__ == "__main__":
    #
    print("---")
    print(search_insert([1, 3, 5, 6], 5))
    #
    print("---")
    print(search_insert([1, 3, 5, 6], 2))
    #
    print("---")
    print(search_insert([1, 3, 5, 6], 7))
    #
    print("---")
    print(search_insert([1, 3, 5, 6], 0))