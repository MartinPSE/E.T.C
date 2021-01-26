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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        if count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.ext = new_node
        new_node.next = next_node

    def delete_node(self, index):  # 0
        node = self.get_node(index - 1)  # (1) , 4, 5
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                return ""
        node.next = node.next.next




practice = Linkedlist(5)
practice.append(12)

practice.print_all()
print("----")

practice.delete_node(0)
practice.print_all()