# <문제> 정렬된 배열에서 특정 수의 개수 구하기
# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다. 이때 이 수열에서 x가 등장하는 횟수를 계산
# Ex) 1,1,2,2,2,2,3 이 있을때 x=2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.


"""
idea 1. 데이터가 정렬 되어있다.
idea 2. O(logN) 동작해야해
idea 3. 이진 탐색을 수행하자!
"""


from bisect import bisect_left, bisect_right
N,X = map(int,input().split(" "))
array = list(map(int,input().split()))

def count_in_range(array,left_value,right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index

count = count_in_range(array,X,X)

if count == 0:
    print(-1)
else:
    print(count)
