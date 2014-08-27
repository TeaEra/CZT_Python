__author__ = 'TeaEra'


def reverse(x):
    pos_x = abs(x)
    res = 0
    while pos_x > 0:
        temp = pos_x % 10
        res = res*10 + temp
        pos_x /= 10
    return res if x > 0 else - res

def reverse_2(x):
    sign_num = -1 if x < 0 else 1
    pos_x = abs(x)
    res = 0
    while pos_x > 0:
        temp = pos_x % 10
        import sys
        if res > sys.maxint / 10:
            return res * sign_num, False
        if res*10 > sys.maxint - temp:
            return res * 10 * sign_num, False
        res = res*10 + temp
        pos_x /= 10
    return res * sign_num, True

if __name__ == "__main__":
    #
    print("---")
    print(reverse_2(-2147483648))