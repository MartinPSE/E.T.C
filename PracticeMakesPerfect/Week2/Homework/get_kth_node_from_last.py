class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_list(self, k):  # 6 7 8 9 10
        cur = self.head
        length = 1

        while cur.next is not None:
            cur = cur.next
            length += 1

        end_length = length - k
        cur = self. head
        for i in range(end_length):
            cur = cur.next

        return cur






linked_list = Linkedlist(6)
linked_list.append(7)
linked_list.append(9)
linked_list.append(8)
linked_list.append(10)
print(linked_list.get_kth_node_from_list(2).data)

