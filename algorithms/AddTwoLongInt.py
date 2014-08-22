__author__ = 'TeaEra'


def add_two_long_int(str1, str2):
    """
    zh:
    长整数相加
    """
    try:
        if not (str1.isdigit() and str2.isdigit()):
            raise Exception("Invalid input.")
    except Exception as e:
        return e
    #
    len1 = len(str1)
    len2 = len(str2)
    reverse_str1 = str1[::-1]
    reverse_str2 = str2[::-1]
    carry_bit = 0
    reverse_res_int = []
    for i in range(max(len1, len2)):
        temp_sum = 0
        if i < len1:
            temp_sum += int(reverse_str1[i])
        if i < len2:
            temp_sum += int(reverse_str2[i])
        temp_sum += carry_bit
        reverse_res_int.append(temp_sum % 10)
        carry_bit = temp_sum / 10
    if carry_bit:
        reverse_res_int.append(carry_bit)
    reverse_res_str = [str(each) for each in reverse_res_int]
    reverse_result = ''.join(reverse_res_str)
    return reverse_result[::-1]

if __name__ == "__main__":
    #
    print("---")
    print(add_two_long_int("", ""))
    #
    print("---")
    print(add_two_long_int("999", "1"))
    #
    print("---")
    print(add_two_long_int("123456789", "369"))