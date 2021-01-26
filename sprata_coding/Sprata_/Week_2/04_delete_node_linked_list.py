# 링크드 리스트 원소 찾기 / 원소 추가
# 1. index  가 0일때 고려!
# 2. node  는 point, data  를 통해서 원소를 없애거나 추가하거나 한다!
# 3. 순서를 건너 뛰자!

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        print("I'll show you all!")
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0  # index 만큼 움직여줘야하잖아!
        while count < index:
            node = node.next
            count += 1
        return node

    #  index                  next_node
    # [ 시작 ] ->          ->   [ 중간 ]     -> [ 끝 ]
    #            new_node
    #           [ 넣을 것 ]
    # index.next = new_node -> new_node.next = next_node

    # 몇번째에 무슨 데이터를 넣을지 받아야 하잖아!
    def add_node(self, index, value):
        new_node = Node(value)  # 넣을것
        if index == 0: # 하지만 index  가 0이면 -1 (?) 처리 해줘야한다.
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index - 1)  # class 내부함수 부르려면 ->> self.함수이름 / index 번째 노드를 가져오자!
        # 우리가 원하는 index  는 -1 !


        next_node = node.next # next_node 날라가면 안되니깐 저장해놓고!
        node.next = new_node  # [넣을 것] 을 [ 시작 ] 에 다음으로 !
        new_node.next = next_node  # [ 넣을 것 ] 에 다음을 [ 중간 ] 으로!
    def delete_node(self, index):
        if index == 0:  # index  가 -1 일때 고려!
            self.head = self.head.next  # head  노드를 [0] -> [1] 번째로 바꿔준다.
            if self.head is None:
                return ""
        node = self.get_node(index - 1)  # [1] [2] [3]     -> 2를 빼고 싶으면
        node.next = node.next.next       # [1] [3] 으로 읽게 하는거야!


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

#     node - > new node -> next node
# 5 -  12 -     6       ->      8


# node     new node
#  5     -    6       - 12 - 8

linked_list.add_node(1, 6)
linked_list.print_all()

# 5 - 6 - 12 - 8
# 5 - 12 - 8

linked_list.delete_node(1)
linked_list.print_all()