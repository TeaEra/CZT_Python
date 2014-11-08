#!/usr/bin/python
# _*_ coding: utf-8 _*_
#
# Author: TeaEra
# Created date: 2014-11-08

# Two blank lines;


def is_palindrome(s):
    #
    if s == "":
        return True
    #
    alpha_s_list = list()
    for each in s:
        if each.isalnum():
            alpha_s_list.append(each.lower())
    alpha_s = "".join(alpha_s_list)
    size = len(alpha_s)
    left_part = alpha_s[:size/2]
    mid_point = size/2-1 if size % 2 == 0 else size/2
    right_part = alpha_s[:mid_point:-1]
    if left_part == right_part:
        return True
    return False


if __name__ == "__main__":
    #
    print is_palindrome("A man, a plan, a canal: Panama")