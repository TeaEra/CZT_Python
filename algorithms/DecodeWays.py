__author__ = 'TeaEra'


def num_decodings(s):
    #
    # TODO: not finished;
    #
    if not s.isdigit():
        return 0
    if not s:
        return 0
    if len(s) == 1:
        if int(s) == 0:
            return 0
        else:
            return 1
    if len(s) == 2:
        if int(s) == 0:
            return 0
        elif int(s) <= 26:
            if int(s[0]) == 0:
                return 0
            if int(s) == 10 or int(s) == 20:
                return 1
            else:
                return 2
        else:
            return 1
    first_char = s[0]
    second_char = s[1]
    if int(first_char) == 0:
        return 0
    elif int(first_char) == 1 or int(second_char) == 2:
        if int(second_char) == 0:
            return num_decodings(s[2:])
        elif int(second_char) <= 6:
            return num_decodings(s[1:]) + num_decodings(s[2:])
        else:
            return 0
    else:
        return 0

if __name__ == "__main__":
    print(num_decodings("101"))