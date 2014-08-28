# _*_ coding: utf-8 _*_
#
# Author: TeaEra
# Created date: 2014-08-28

def subsets(S):
    if not S:
        return [[]]
    if len(S) == 1:
        return [[], S]
    temp_arr = S[1:]
    sub_subsets = subsets(temp_arr)
    rest_subsets = [S[:1] + x for x in sub_subsets]
    all_subsets = sub_subsets + rest_subsets
    for each in all_subsets:
        each.sort()
    all_subsets.sort()
    return all_subsets

if __name__ == "__main__":
    print(subsets([1, 2, 3]))