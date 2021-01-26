# 1. 방향, 회전, 후진 고려해야한다.
# 2. bfs 의 개념에 대해서 정립.
# 모든것을 훑는다 ---> bfs 를 떠올려야한다.

# 동-> , <-서 , 남 , 북
# c+1    c-1   r+1  r-1
#    북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 회전
# 북 -> 서 / 동 -> 북 / 남 -> 동 / 서 -> 남
# 0 ->  3   1  -> 0   2 ->  1   3  -> 2
def rotation(d):
    return (d + 3)  % 4

# 후진
# 북 -> 남 / 동 -> 서 / 남 -> 북 / 서 -> 동
# 0  -> 2   1  -> 3   2  -> 0    3 -> 1

def go_back(d):
    return (d + 2) % 4

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
    n = len(room_map)  # Row
    m = len(room_map[0])  # Column
    count_clean_points = 1  # 시작지점은 청소 된거라하자!
    room_map[r][c] = 2
    queue = list([[r, c, d]])

    while queue:
        r, c, d = queue.pop(0)
        temp_d = d

        for i in range(4):
            temp_d = rotation(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

        if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:  # 빈 곳을 청소하자.
            count_clean_points += 1
            room_map[new_r][new_c] = 2
            queue.append([new_r, new_c, temp_d])

        elif i == 3:  # 4방향이 청소되어져있다.

            new_r, new_c = r + dr[temp_d], c + dc[temp_d]
            queue.append([new_r, new_c, temp_d])
            if room_map[new_r][new_c] == 1:
                return count_clean_points



# 52 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))