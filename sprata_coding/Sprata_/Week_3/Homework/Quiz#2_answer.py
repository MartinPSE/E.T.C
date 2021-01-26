a = "(())()"


# 순차적으로 탐색 / 1. 열린괄호 계속 저장! Stack 사용
# ( -> ((  -> (() -> (()) -> (())( -> (())() !
# ["("] ["(","("] ["("] []    ["("]     []
# ( -> (( -> ((( -> ((()
# "(" ["(","("] ["(","(","("]  ["(","("]
def is_correct_parenthesis(string):
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)  # 들어가있는지 여부만이 중요!
            print(stack,"1")
        elif string[i] == ")":
            if len(stack) == 0:
                return print("False")
            else:
               stack.pop()
               print(stack,"2")

    if len(stack) != 0:
        return print("False")
    else:
        return print("True")


is_correct_parenthesis(a)
