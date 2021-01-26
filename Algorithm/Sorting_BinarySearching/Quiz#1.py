# <문제> 떡볶이 떡 만들기
# 떡볶이 떡은 떡의 길이가 일정하지가 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다
# 절단기에 높이(H) 를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고
# 낮은 떡은 잘리지 않는다.
# Ex) 높이가 19, 14, 10, 17 cm 인 떡이 나란히 있고 절단기 높이를 15cm 로 지정하면 자른 뒤 떡의 높이는
#           15  14  10  15 cm --> 잘린 떡의 길이는 4, 0, 0, 2 cm 이다. 즉 손님은 6cm 를 가져 가는것이다.
# 손님이 왔을 때 요청한 총 길이가 M 일때 '적어도 M 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램'

N, M = list(map(int, input().split(' ')))

height = list(map(int, input().split()))

"""
idea 1. 절단기는 무조건 떡의 길이의 최댓값보다 작거나 같아야 한다. ( 아니면 떡을 얻을 수 가 없어 ) 
idea 2. 큰 탐색 범위를 보면 '이진 탐색' 을 떠올려야 한다.
idea 3. 짜른 떡들의 결과값을 따로 저장해준다

"""

start = 0
end = max(height)
result = 0

while (start <= end ):
    mid = ( start + end ) // 2
    total = 0
    for x in height:
        if x > mid:
            total += x - mid
    if total < M:
        end = mid -1
    else:
        result = mid
        start = mid + 1


print(result)

