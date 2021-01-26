input = 100  # fibo_recursion(3) = fibo_recursion(2) + fibo_recursion(1)

# Fibo(1) = Fibo(2) = 1 / 탈출조건
#
# 1. Fibo(3)
# Fibo(2), Fibo(1) 더 하면 된다.
# 1 + 1 -> 2
# 2. Fibo(4)
# ->Fibo(3) + Fibo(2)
#   ->Fibo(2) + Fibo(1)] + 1
#   -> 연산량 2번
# -> 2 + 1 // 연산량 2번 + 연산량 1번 --> 3번
#
# 3. Fibo(5)
# Fibo(4) + Fibo(3)
# Fibo(4) -> 2의 과정
# Fibo(3) -> 1의 과정
#
# -> Fibo(4) -> Fibo(3) + 1
#             -> Fibo(2) + Fibo(1) + 1
#
# -> Fibo(3) -> Fibo(2) + Fibo(1)

def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))
