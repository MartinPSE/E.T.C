# 1. 코니의 위치는 -> input + 0.5*(n(n+1))
# queue = deque()

# queue.append(input + 0.5*(n(n+1))
# 2. 브라운의 위치는 -> input + (input - 1)
#                          + (input + 1)
#                               *2*input
# BFS -> 모든경우의수 다 나열
# - 코니의 위치가 > 200,000 or 코니 = 브라운 // 똑같은시간에 똑같은 위치
#  규칙적인건 -> 배열
#  자유자재 -> 딕셔너리

#  각 시간마다 브라운이 갈 수 있는 위치를 저장해보자.
#

from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치와 시간 동시에 넣어주자
    visited = [{} for _ in range(200001)]  # 각 초에 어디갔는지

    while cony_loc <= 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

        new_time = current_time + 1

        new_position = current_position - 1
        if 0 <= new_position <= 200000:
            queue.append((new_position, new_time))

        new_position = current_position + 1
        if 0 <= new_position <= 200000:
            queue.append((new_position, new_time))

        new_position = current_position * 2
        if 0 <= new_position <= 200000:
            queue.append((new_position, new_time))

    time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!
