# List, LinkedList 구현해보자!!
# Node 2가지의 정보를 필요로 한다.
# 1. 칸에 있는 Data
# 2. 다음 칸이 뭔지 ( Pointer )
# -------> Data -> 2개니깐 class -> 묶어보자

# [시작] -> [...]   Node는 data, next(pointer) 2개 필요로 한다.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 많아지면 귀찮아, 일일이 추가해야해!!
'''
node = Node(3)  # test 용
node2 = Node(4)
node.next = node2

print(node.next.data)
'''


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)  # head data 필요로 하잖아!

    #  head 를 따라서 가야지!
    # cur=self.head 할당 -> cur  을 이동시키자! ( 맨 끝 까지 ) -> Next가 None인 지점까지
    # [기관차] -> 뒤에 뭐 뭐 뭐 뭐 붙여보자! -> [new]
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
        print(cur.data)

    # node  들의 값을 다 추출해보자
    def print_all(self):
        print("hihihi")
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(3)

linked_list.append(4)
linked_list.append(5)
linked_list.print_all()
