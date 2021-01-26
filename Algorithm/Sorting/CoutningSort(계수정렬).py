# 계수 정렬
# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
#   : 계숙 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을때 사용
# 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K 일때 최악의 경우에도 수행시간 O(N+K)를 보장

"""
idea 1. '동일한 값의 데이터가 여러 개 등장할때' 효율 적이다!
idea 2. O(N^2)
"""

array = [7, 5, 9, 0, 10, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

list = [0] * (max(array) + 1)

for i in range(len(array)): 
    list[array[i]] += 1

for i in range(len(list)):
    for j in range(list[i]):
        print(i, end=" ")
