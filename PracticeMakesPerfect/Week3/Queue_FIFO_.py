class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_value = Node(value)
        if self.is_empty():
            self.head = new_value
            self.tail = new_value
        self.tail.next = new_value
        self.tail = new_value
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")

        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        if self.is_empty():
            print("Queue is Empty")
        return self.head.data

    def is_empty(self):
        return self.head is None