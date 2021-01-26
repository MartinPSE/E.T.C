
# 링크드 리스트 원소 찾기 / 원소 추가

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
        count = 0              # index 만큼 움직여줘야하잖아!
        while count < index:
            node = node.next
            count += 1
        return node


linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(1).data)
