__author__ = 'TeaEra'


def reverse_words(s):
    """
    Status: accepted;
    """
    words = list()
    word = list()
    for i in range(len(s)):
        if s[i] != " ":
            word.append(s[i])
        else:
            if len(word) != 0:
                words.append(''.join(word))
            word = list()
    if len(word) != 0:
        words.append(''.join(word))
    return ' '.join(list(reversed(words)))

if __name__ == "__main__":
    #
    print("---")
    print(reverse_words(""))
    #
    print("---")
    print(reverse_words("the sky is blue"))