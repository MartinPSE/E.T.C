# BFS (Breadth-First Search)

# '너비 우선 탐색' 이라고도 하며, 그래프에서 '가까운 노드부터 우선적으로 탐색하는 알고리즘'
# BFS 는 queue 자료구조를 이용하며, 구체적인 동작은 다음과 같다.
# 탐색 시작 노드를 '큐'에 삽입하고 방문 처리를 한다.
# '큐'에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 더 이상 2번의 과정을 수행할 수 없을때 까지 반복

""" 매우 중요하다. 특정 조건에서 최단경로 !"""

from collections import deque


# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end="\t")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현 ( 2차원 리스트 )
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# BFS (Breadth-First Search)

# '너비 우선 탐색' 이라고도 하며, 그래프에서 '가까운 노드부터 우선적으로 탐색하는 알고리즘'
# BFS 는 queue 자료구조를 이용하며, 구체적인 동작은 다음과 같다.
# 탐색 시작 노드를 '큐'에 삽입하고 방문 처리를 한다.
# '큐'에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 더 이상 2번의 과정을 수행할 수 없을때 까지 반복

""" 매우 중요하다. 특정 조건에서 최단경로 !"""

from collections import deque


# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end="\t")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 표현 ( 2차원 리스트 )
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9


# 정의된 DFS 함수 호출
print("BFS")
bfs(graph, 1, visited)

