# DFS / BFS
# 그래프 탐색 알고리즘
# 탐색(Search) --> 많은 양의 데이터 중에서 '원하는 데이터를 찾는 과정'
""" 반드시 숙지 !!!"""

# Stack 자료 구조(LIFO) --> 선입후출
# 즉 입구와 출구가 동일한 형태! 즉, 박스 쌓기 (즉, 박스 stack)

# stack 은 list 를 이용하고 append / pop 을 써서 활용.

list = []
list.append(5)
list.append(4)
print(list)
list.pop()
print(list)

# Que(FIFO) --> 선입선출
# 입구와 출구가 모두 뚫려 있는 터널과 같은 형태
# 큐는 from collections import deque
# 추가는 append, 삭제는 popleft
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(7)
queue.popleft()
print(queue)
