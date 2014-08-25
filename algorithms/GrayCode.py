__author__ = 'TeaEra'


def gray_code(n):
    # TODO: wrong answer!!!???
    """
    """
    if n == 0:
        return []
    elif n == 1:
        return [0, 1]
    pos_arr = [0]
    oper = 1
    min_pos = 0
    max_pos = n-1
    intervals = 2**n - 1
    for i in range(1, intervals):
        if pos_arr[i-1] == min_pos:
            oper = 1
        elif pos_arr[i-1] == max_pos:
            oper = -1
        pos_arr.append(pos_arr[i-1] + oper)
    print(pos_arr)
    #
    temp_str = ''.join(['0' for i in range(n)])
    str_arr = list()
    str_arr.append(temp_str)
    for i in range(intervals):
        temp_str = str_arr[i]
        temp_pos = pos_arr[i]
        changed_bit = '0' if temp_str[temp_pos] == '1' else '1'
        temp_str = temp_str[:temp_pos] + changed_bit + temp_str[temp_pos+1:]
        str_arr.append(temp_str)
    int_arr = list()
    for i in range(2**n):
        int_arr.append(int(str_arr[i], 2))
    return int_arr

if __name__ == "__main__":
    #
    print("---")
    print(gray_code(3))
    #
    print("---")
    print(gray_code(4))