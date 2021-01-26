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


def _get_linked_list_sum(linked_list):
    sum = 0
    head = linked_list.head
    while head is not None:
        sum = sum * 10 + head.data
        head = head.next
    return sum


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = _get_linked_list_sum(linked_list_1)
    sum_2 = _get_linked_list_sum(linked_list_2)

    return sum_1 + sum_2





linked_list_1 = Linkedlist(6)
linked_list_1.append(8)
linked_list_1.append(8)

linked_list_2 = Linkedlist(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
