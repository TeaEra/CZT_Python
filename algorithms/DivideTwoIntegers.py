#_*_ coding: utf-8 _*_

__author__ = 'TeaEra'


def divide(dividend, divisor):
    """

    [zh]:
    思路介绍，被除数（整数） / 除数（整数） = 商（整数），忽略余数，公式其实为：
        dividend =
            divisor * 2**n * is_used
            + divisor * 2**(n-1) * is_used
            + ...
            + divisor * 2**0 * is_used
            （+ remainder）
        余数 remainder 一定会 < 除数 divisor；
    """
    if divisor == 0:
        return None
    sign_num = 1 \
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) \
        else -1
    abs_dividend = abs(dividend)
    abs_divisor = abs(divisor)
    power_num = 31
    result = 0
    while abs_dividend >= abs_divisor:
        while (power_num > 0) and (abs_divisor << power_num) > abs_dividend:
            power_num -= 1
        abs_dividend -= (abs_divisor << power_num)
        result += (1 << power_num)
    return sign_num * result

if __name__ == "__main__":
    print(divide(-2147483658, -1))