# idea 는 "(" --> 시작 --> ")" 끝 ---> True
# ")" --> 시작 ---> False

s = "(())()"


def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        elif string[i] ==")":
            if string[0] == ")":
                return False
            else:
                stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True



print(is_correct_parenthesis(s))
