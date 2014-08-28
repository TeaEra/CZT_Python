# _*_ coding: utf-8 _*_
#
# Author: TeaEra
# Created date: 2014-08-28

def word_break(s, d):
    if not s:
        return [""]
    idx = 0
    temp = ""
    while idx < len(s):
        temp += s[idx]
        if temp in d:
            rest_break = word_break(s[idx+1:], d)
            return [temp + " " + x for x in rest_break]
        #
        idx += 1
    # TODO: not finished?

if __name__ == "__main__":
    #
    print("---")
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    print(word_break(s, word_dict))