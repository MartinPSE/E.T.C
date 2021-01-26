graph = {
    1: [2, 3, 4],
    2: [5],
    3: [6, 7],
    4: [8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


# 1 번 : queue에 root node 값 대입
# 2 번 : visited 에 root node 값 pop ---- > visited [1]
# 3 번 : [1] 에 인접한 node 중 방문하지 않은 값을 ---> queue 에 추가 [ 2,3,4]  ---? [3,4]
# 4 번 : 다시 pop ---> visitied = [1,2]


def bfs_queue(adj_graph, start_node):
    queue = [start_node]  # 1
    visited = []
    while queue:
        current_node = queue.pop(0)  # 1
        visited.append(current_node)  # visited = [1]
        for adjacent_node in adj_graph[current_node]:  # 1 / [2,3,4]
            if adjacent_node not in visited:
                queue.append(adj_graph[current_node])
    return visited


print(bfs_queue(graph, 1))
