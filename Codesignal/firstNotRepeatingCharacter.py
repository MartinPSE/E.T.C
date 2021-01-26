from collections import Counter

# collections 에 counter 라는 함수는
# 자동으로 key : value 에
# 컨테이너에 동일한 객체가 몇개인지 추출할때 사용
# value 값이 높은 순대로 내림차순 정렬

s = "abacabad"


def firstNotRepeatingCharacter(s):
    c = Counter(s)
    k = len(s)
    check = False
    for i in c:
        if c[i] == 1 and (s.index(i) <= k):
            check = True
            k = s.index(i)
    if check:
        return print(s[k])
    else:
        return print('_')


firstNotRepeatingCharacter(s)

#
# def firstNonRep(word):
#     count = {}
#     for c in word:  # a /
#         if c not in count:  #
#             count[c] = 0  # count[a]
#         count[c] += 1
#
#         print(count)
#     for c in word:
#         if count[c] == 1:
#             return print(c)

#
# def firstNotRepeatingCharacter(s):
#     for i in range(len(s)):
#         repeat = False
#         for j in range(len(s)):
#             if s[i] == s[j] and i != j:
#                 repeat = True
#
#         if not repeat:
#             return print(s[i])
#
#     return "_"
