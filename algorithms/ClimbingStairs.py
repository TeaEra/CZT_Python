#_*_ coding: utf-8 _*_

__author__ = 'TeaEra'


def climb_stairs(n):
    # Time Limit Exceeded
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs(n-1) + climb_stairs(n-2)

def climb_stairs_2(n):
    """
    [en]
    The following solution is OK;
    Climbing stairs in 1 or 2 step is actually the fibonacci problem;

    [zh]
    """
    fib = list()
    fib.append(1)
    fib.append(1)
    if n == 0 or n == 1:
        return fib[n]
    for i in range(2, n+1):
        temp = fib[i-1] + fib[i-2]
        fib.append(temp)
    return fib[n]

if __name__ == "__main__":
    print(climb_stairs_2(5))