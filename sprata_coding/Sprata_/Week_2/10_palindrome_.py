# 재귀함수
# -------

input = "아"

'''
def is_palindrome(string):
    n = len(string)
    count = 0
    for i in range(n):
        count += 1
        if string[i] != string[n - 1 - i]:  # string의 길이를 생각해보자!

            return False
    print(count)
    return True

print(is_palindrome(input))
'''

# a b c c b a   - > b c c b -> c c -> c == c
#
#
# def is_palindrome(string):        # input 값 시작!
#     if string[0] != string[-1]:   # 맨앞과 맨뒤가 다르다면! False !
#         return False
#     if len(string) <= 1:
#         return True
#
#     return is_palindrome(string[1:-1])
#
#
#
# print(is_palindrome(input))

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome(input))
