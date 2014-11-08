#!/usr/bin/python
# _*_ coding: utf-8 _*_
#
# Author: TeaEra
# Created date: 2014-11-08

# Two blank lines;


def is_valid(s):
    #
    if s == "":
        return True
    #
    res_s = list()
    for each in s:
        if each == ")" or each == "]" or each == "}":
            if len(res_s) == 0:
                return False
            else:
                comb = res_s[-1] + each
                if comb == "()" or comb == "[]" or comb == "{}":
                    res_s.pop()
                else:
                    return False
        else:
            res_s.append(each)
    if len(res_s) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    #
    print is_valid("()[]{}")