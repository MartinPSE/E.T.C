# < 문제 > 음료수 얼려 먹기
# N * M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성

# EX) 4*5 얼음 틀에서는 아이스크림 총 3개 생성된다.

# 00110
# 00011
# 11111
# 00000    ---> 아이스크림 3개 생성

"""
1. DFS / BFS 이용
2. 주변의 값이 '0'이고 아직 방문하지 않은 지점이 있으면 지점 방문
3. 방문한 지점에서 다시 상,하,좌,우 살펴보고 -> 방문을 진행하는 과정 반복 --> 연결된 모든 지점을 방문
4. --> 방문하지 않은 지점의 수를 카운트
"""

# N * M
N, M = map(int, input().split())


# 2차원 리스트의 맵(stage)정보 입력 받고
stage = []
for i in range(N):
    stage.append(list(map(int, input())))
print(stage)


# DFS로 특정 노드를 방문하고 연결된 모든 노드들 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if stage[x][y] == 0:
        # 해당 노드 방문 처리
        stage[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False

# 모든 노드(위치)에 대하여 방문처리, 즉 아이스크림 채우기
result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)
