#!/usr/bin/python
# _*_ coding: utf-8 _*_
#
# Author: TeaEra
# Created date: 2014-11-08

# Two blank lines;


def is_palindrome(x):
    #
    if x < 0:
        return False
    #
    backup_x = x
    if backup_x < 10:
        return True
    rev_x = 0
    while backup_x != 0:
        rev_x = rev_x * 10 + backup_x % 10
        backup_x /= 10
    if rev_x == abs(x):
        return True
    else:
        return False


if __name__ == "__main__":
    #
    print is_palindrome(123)