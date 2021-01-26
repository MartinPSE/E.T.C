class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):  # 맨 앞에 데이터 넣기 list.append() 와 동일
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head


    def pop(self):  # 맨 앞에 데이터 빼기
        if self.is_empty():
            return "Stack is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data


    def peek(self):  # 맨 앞에 데이터 보기
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data



    def is_empty(self):  # is_empty?
        return self.head is None



