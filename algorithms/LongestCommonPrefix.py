#!/usr/bin/python
# _*_ coding: utf-8 _*_
#
# Author: TeaEra
# Created date: 2014-11-08

# Two blank lines;


def longest_common_prefix(strs):
    #
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    #
    i = -1
    for i in range(-1, len(strs[0])):
        prefix = strs[0][:i+1]
        count = 0
        for j in range(1, len(strs)):
            if strs[j].startswith(prefix):
                count += 1
        if count == len(strs) - 1:
            continue
        else:
            i -= 1
            break
    #
    return strs[0][:i+1]


if __name__ == "__main__":
    #
    print longest_common_prefix(["abc", "abc", "abde"])
    #
    print longest_common_prefix(["c", "c", "c"])