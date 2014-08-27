__author__ = 'TeaEra'


def add_binary(a, b):
    int_arr_a = [int(x) for x in a[::-1]]
    int_arr_b = [int(x) for x in b[::-1]]
    len_a = len(a)
    len_b = len(b)
    carry = 0
    int_arr_res = list()
    for i in range(max(len_a, len_b)):
        temp_res = carry
        if i < len_a:
            temp_res ^= int_arr_a[i]
        if i < len_b:
            temp_res ^= int_arr_b[i]
        #
        int_arr_res.append(temp_res)
        #
        if i < len_a and i < len_b:
            carry = \
                (int_arr_a[i] & int_arr_b[i]) \
                | (int_arr_a[i] & carry) \
                | (int_arr_b[i] & carry)
        elif i < len_a:
            carry &= int_arr_a[i]
        elif i < len_b:
            carry &= int_arr_b[i]
    if carry:
        int_arr_res.append(carry)
    out_str = ''.join([str(x) for x in int_arr_res[::-1]])
    return out_str

def add_binary_2(a, b):
    int_arr_a = [int(x) for x in a[::-1]]
    int_arr_b = [int(x) for x in b[::-1]]
    len_a = len(a)
    len_b = len(b)
    carry = 0
    int_arr_res = list()
    for i in range(max(len_a, len_b)):
        temp_res = carry
        if i < len_a:
            temp_res += int_arr_a[i]
        if i < len_b:
            temp_res += int_arr_b[i]
        #
        int_arr_res.append(temp_res % 2)
        carry = temp_res / 2
    if carry:
        int_arr_res.append(carry)
    out_str = ''.join([str(x) for x in int_arr_res[::-1]])
    return out_str

if __name__ == "__main__":
    #
    print("---")
    print(add_binary_2("1", "111"))