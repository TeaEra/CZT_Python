#_*_ coding: utf-8 _*_

__author__ = 'TeaEra'


def gray_code(n):
    """
    n=2:
    00
    01
    11
    10

    n=3:
    000
    001
    011
    010
    110
    111
    101
    100

    ...

    [zh]
    思路： 可以递归解决，将n=2时的情况前面+0，与n=2前面+1再翻转，concatenate即可得到结果；
    """
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    arr = gray_code(n-1)
    top_part = list()
    bottom_part = list()
    for each in arr:
        top_part.append(each)
    for each in arr[::-1]:
        bottom_part.append((1 << (n-1)) + each)
    return top_part + bottom_part

if __name__ == "__main__":
    #
    print("---")
    print(gray_code(2))
    #
    print("---")
    print(gray_code(3))