from collections import deque

a = [2, 1, 3, 5, 3, 2]


# Dict 를 써보자
# key : value
# value += 1
# value == 2?
# return key
# 숫자니깐 가능한거야!

def firstDuplicate(a):
    letter = {}
    found = 0

    for i in range(len(a)):  # i = 0 /    i  = 1
        if a[i] in letter:  # 2  in [] ? / a[1] / 1 in letter ?
            letter[a[i]] += 1
        else:  # letter = [1] /
            letter[a[i]] = 1

        if (letter[a[i]]) == 2:
            return a[i]

    if not found:
        return -1


firstDuplicate(a)
