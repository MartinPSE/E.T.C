nput = 20

# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.
# N이 N의 제곱근 보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# '수'가 '수'를 나누면 몫이 발생하는데, 몫 과 나누는 수 둘 중 하나는
# 반드시 N의 제곱근 이하.

def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1): # n< - 2 ~ number + 1
        # n이 20 이라고 한다면
        # i 를 2.... 19... 까지 다 비교 한다.
        # 2 3 X
        # 2 ~ n-1 중에서 소수인 친구들만

        for i in range(2, n):         # 2 - 20 까지 있어.
            if n % i == 0 and i * i <= n:      # n -> i 까지 나머지가 0 일때까지 소수 찾는다.

                break
        else:
            prime_list.append(n)


    return prime_list


result = find_prime_list_under_number(input)
print(result)
