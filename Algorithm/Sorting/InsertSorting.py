# 삽입정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.
# 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작.
"""
idea 1. 매번 위치 바꿔가면서 비교!!
idea 2. O(N^2)
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):  # 0
    for j in range(i, 0, -1):  # 인덱스 i부터 0까지 1씩 감소하며 반복하는 문법 !
        if array[j] < array[j-1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춘다.
            break
print(array)
