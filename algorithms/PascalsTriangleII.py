# _*_ coding: utf-8 _*_
#
# Author: TeaEra
# Created date: 2014-08-28

def ger_row(row_index):
    arr = list()
    for i in range(row_index):
        arr.append(i)
    if row_index == 1:
        return [1]
    if row_index == 2:
        return [1, 2, 1]
    #
    # TODO: not finished?

if __name__ == "__main__":
    print(ger_row(3))