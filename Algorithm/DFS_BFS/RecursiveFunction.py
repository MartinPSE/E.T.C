# 재귀 함수
# 즉, 자기 자신을 다시 호출하는 함수
# dfs 구현할 때 자주 사용!

# def recursive_function(i):
#     if i == 2:
#         return
#     print(i,'번째 재귀함수에서',i+1,'번째재귀 함수를 호출합니다.')
#
#     recursive_function(i+1)
#     print(i,"종료")
#
# recursive_function(1)

""" 팩토리얼 구현"""


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(4))


# 반복문으로 구현한 n!

def factorial_iternative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("반복문", factorial_iternative(3))
