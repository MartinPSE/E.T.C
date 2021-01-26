# Factorial(N) = N * Factorial(N-1)
# ....
# Factorial(1) = 1

# 5 * 4 * factorial(3) * ... * 1
def factorial(n):  # 5 / 4 / 1

    if n == 1:     # 5 != 1 / 4 != 1 / .... /  1 == 1
        return 1


    return n * factorial(n-1)  # 5 * factorial(4) / 4 * factorial(3) / 3 * ... / 1


print(factorial(6))











