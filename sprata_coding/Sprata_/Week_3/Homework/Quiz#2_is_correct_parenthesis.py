# 올바른 괄호
#
# "(())()" # True
# "((((" # False
# 괄호의 갯수가 아니라, 열렸으면 반드시 닫혀야 한다!
a = "))()()()"


def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        elif string[i] == ")":
            if string[0] == ")":
                return print("False")
            else:
                stack.pop()

    if len(stack) != 0:
        return print("False")
    else:
        return print("True")


is_correct_parenthesis(a)
