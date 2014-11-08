#!/usr/bin/python
# _*_ coding: utf-8 _*_
#
# Author: TeaEra
# Created date: 2014-11-08

# Two blank lines;

def count_and_say(n):
    if n == 1:
        return "1"
    else:
        str_prev = count_and_say(n-1)
        str_curr = ""
        curr_char = ""
        curr_count = 0
        for each in str_prev:
            if each != curr_char:
                if curr_count > 0:
                    str_curr += str(curr_count) + curr_char
                curr_char = each
                curr_count = 1
            else:
                curr_count += 1
        if curr_count > 0:
            str_curr += str(curr_count) + curr_char
        return str_curr

if __name__ == "__main__":
    #
    print count_and_say(1)
    #
    print count_and_say(5)