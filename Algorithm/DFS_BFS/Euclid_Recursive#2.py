# 최대공약수 계산 (유클리드 호제법) 예제
# 2개의 자연수에 대한 최대 공약수를 구하는 대표적인 알고리즘 '유클리드 호제법'
"""유클리드 호제법"""


# 두 자연수 A,B에 대하여 ( A > B ) A를 B로 나눈 나머지를 R 이라고 하자
# 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.

# EX) GCD(192, 162)
#
# 192 162 --> ( a, b)
# 162 30 --> ( b , a%b )
# 30 12 ----> (a % b , a % b % b)
# 12 6 ---> ( a % b % b , a % b % b % b)

def euclid(a, b):
    if a % b == 0:
        return b

    return euclid(b, a % b)


print(euclid(192, 162))

# 스택 라이브러리 대신 재귀 함수를 이용!
# 반복문 <---> 재귀문
