# from pip._vendor.requests import delete
# O(logN)
# 최대, 최소를 빨리 뽑을때 써먹자.

class Maxheap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1  # 현재 넣은 노드에 인덱스를 알아야지!
        while cur_index > 1:  # cur_index 가 1 이면 멈추자!
            parent_index = cur_index // 2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break
    # 1. 루트 노드를 (맨 아래 레벨과 맨 오른쪽 노드) self.items[마지막원소(-1)] 바꾼다.
    # 2. 루트 노드를 배열에서 제거 한뒤, 저장해 둔다. -> 반환 값이잖아
    # 3. 현재 꼭대기에 올라간 (원래 마지막) 노드를 자식 노드들과 비교하면서 내려보낸다.
    #     ( 더 큰 자식 노드와 비교! )
    # 4. 자식들 보다 마지막노드가 더 크거나 / 바닥에 내려갈때.
    def delete(self):
        # 1
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        # [ None, 4, 7, 6, 2, 5, 8 ]
        prev_max = self.items.pop()  # 8
        # [ None, 4, 7, 6, 2, 5 ]
        cur_index = 1
        while cur_index <= len(self.items) - 1:  # 더 이상 자식노드가 없을때까지
            left_child_index = cur_index * 2  # 2
            right_child_index = cur_index * 2 + 1  # 3
            max_index = cur_index  # 내가 제일 크다고 시작
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index
            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index
            if max_index == cur_index:
                break

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return prev_max


max_heap = Maxheap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)
print(max_heap.delete())
print(max_heap.items)
