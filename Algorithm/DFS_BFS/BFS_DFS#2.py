# <문제> 미로 탈출
#  형석이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리 괴물이 있어
#  이를 피해서 탈출해야 한다. 형석이의 위치는 (1,1)이며 미로의 출구는 (N,M)의 위치에 존재하며
#  한번에 한 칸씩 이동할 수 있습니다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
#  미로는 반드시 탈출 할 수 있는 형태로 제시된다.
#  이때 형석이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구해라.
#  칸은 시작칸과 마지막칸까지 더해서 계산.


"""
idea 1. BFS 는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색
idea 2. 상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일
 -> (1, 1) 지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록 하면 해결

"""
from collections import deque

N, M = map(int, input().split())

stage = []
for i in range(N):
    stage.append(list(map(int, input())))

dx = [1, 0]
dy = [0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if stage[nx][ny] == 0:
                continue
            if stage[nx][ny] == 1:
                stage[nx][ny] = stage[x][y] + 1
                queue.append((nx, ny))
    return stage[N - 1][M - 1]


print(bfs(0, 0))
