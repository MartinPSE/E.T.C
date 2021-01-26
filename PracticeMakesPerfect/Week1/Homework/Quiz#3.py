input = 20


def isprime(number):
    if number != 1:
        for f in range(2, number):
            if number % f == 0:
                return False
    else:
        True


# 20
# 2      3     4    5  ....
# 2/1   3/2   4/3  5/4
#       3/1   4/2  5/3
#             4/1  5/2
#                  5/1
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in range(2, number):
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(input)
print(result)