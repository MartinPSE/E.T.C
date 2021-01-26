# 전부탐색 -> BFS
# 1. 현재 위치를 청소한다.
# 2차원 배열에 넣자
# 0 은 청소하지 않은 곳
# 1 은 청소하지 못하는 곳.
# 2 는 청소한곳.

# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로
# 탐색을 진행한다.
## 방향!
#    r  c
# 북 -1  0
# 동 0  +1
# 남 +1  0
# 서 0  -1
#     북  동  남  서
dr = [-1, 0, 1, 0]
dc = [ 0, 1, 0,-1]


# 회전
# 북 -> 왼쪽 회전 : 서쪽 0 -> 3   # 3을 더한다음에 % 4를 한 값이다.
# 동 -> 왼쪽 회전 : 북쪽 1 -> 0
# 남 -> 왼쪽 회전 : 동쪽 2 -> 1
# 서 -> 왼쪽 회전 : 남쪽 3 -> 2

def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4


# b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고
# 2번으로 돌아간다.
# -> 현재 본 방향에서 청소할 곳이 없다면 다시 왼쪽으로 회전해라!

# c. 4방향 모두 청소가 되어있거나, 벽인 경우에는
# 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# -> 모든 방향이 청소되어있다면 뒤로 한칸 후진해라.
# 북 후진 -> 남 0 -> 2   + 2를 해서 % 4를 한값.
# 동 후진 -> 서 1 -> 3
# 남 후진 -> 북 2 -> 0
# 서 후진 -> 동 3 -> 1

def get_d_index_when_go_back(d):
    return (d + 2) % 4


# d. 네 방향 모두 청소가 이미 되어있거나 벽이면서,
# 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.


current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_departments_cleaned = 1
    room_map[r][c] = 2
    queue = list([[r, c, d]])

    while queue:
        r, c, d = queue.pop(0)
        temp_d = d  # 방향을 계속 돌려야하니깐

        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break

            elif i == 3:
                new_r, new_c = r + dr[get_d_index_when_go_back(temp_d)], c + dc[get_d_index_when_go_back(temp_d)]
                queue.append([new_r, new_c, temp_d])
                if room_map[new_r][new_c] == 1:  # 4번째 조건
                    return count_of_departments_cleaned





# 52 가 출력되어야 합니다! -- > 57 이출력됩니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))




