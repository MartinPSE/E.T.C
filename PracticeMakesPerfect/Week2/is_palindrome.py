input = "abcba"


def is_palindrome(string):
    is_palindrome__ = True
    for i in range(len(string) // 2):
        if string[i] != string[-1 - i]:
            is_palindrome__ = False
            break
    print(is_palindrome__)


is_palindrome(input)

