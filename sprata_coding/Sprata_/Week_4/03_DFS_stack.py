graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# 1. 시작 노드를 스택에 넣습니다.
# 2. 현재 스택의 노드를 빼서 visited 에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중에서 방문한지 않은 노드를 -> stack 에 추가!


def dfs_stack(adjacent_graph, start_node) -> object:
    stack = [start_node]  # 1 / stack 저장
    visited = []  # [] / 방문한거 저장
    while stack:  # 1 / stack 이 '비지 않았다' 까지!
        current_node = stack.pop()  # stack : []  /  current_node = 1
        visited.append(current_node)  # vistied : [1]
        for adjacent_node in adjacent_graph[current_node]:  # adjacent_node in [2, 5, 9]
            if adjacent_node not in visited:  # visited[1] vs  node[2,5,9]  방문하지 않은것!
                stack.append(adjacent_node)  # [2,5,9]  stack 에 추가 stack = [2,5,9]

    return visited


print(dfs_stack(graph, 1))
