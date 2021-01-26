# 이진 탐색 알고리즘
# 순차 탐색 : 리스트 안에 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 이진 탐색 : 정렬되어 있는 리스트에서 범위를 절반씩 좁혀가며 데이터를 탐색 하는 방법
#          : 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정

"""
bisect
from bisect import bisect_left, bisect_right
bisect_left,right(a,x)
: x를 a 배열에서 정렬 유지하면서 삽입할 가장 왼쪽/오른쪽 인데스 반환
"""



# 이진 탐색 소스코드 ( 재귀 함수 )
def binary(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간값 인덱스 반환
    if target == array[mid]:
        return mid
    # 중간값의 값보다 찾고자 하는 값이 큰 경우 오른쪽
    elif target > array[mid]:
        return binary(array, target, mid + 1, end)
    # 반대의 경우 왼쪽
    else:
        return binary(array, target, start, mid - 1)


# 입력 받자
n, target = map(int, input().split())
array = list(map(int, input().split()))

# 수행 결과 출력
result = binary(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)

