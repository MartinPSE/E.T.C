# 문제 : 곱하기 혹은 더하기
# 각 자리가 숫자 (0부터 9) 로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽 하나씩 모든 숫자를 확인하여 숫자 사이에
# "x" 혹은 "+" 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성
# ( 단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 부터 순서대로 이루어진다)


'''
idea 1. 숫자가 0,1 일때는 무조건 더 해줘야해
idea 2. 데이터로 받는 값을 int로 저장하는게 중요해!
idea 3. 그 뒤론 그냥
'''

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <=1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
