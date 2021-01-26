#  Maxheap!!
#  노드를 맨 끝에 추가한다.
#  지금 넣은 새노드를 부모노드와 비교한다. 만약 부모보다 크다면 교체한다.
#  꼭대기까지 과정 반복.
# O(logN) 만큼의 시간 복잡도.

class Maxheap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1  # 현재 넣은 노드에 인덱스를 알아야지!
        while cur_index > 1:  # cur_index 가 1 이면 멈추자!
            parent_index = cur_index // 2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index] , self.items[cur_index]
                cur_index = parent_index
            else:
                break



max_heap = Maxheap()
print(type(max_heap))
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)