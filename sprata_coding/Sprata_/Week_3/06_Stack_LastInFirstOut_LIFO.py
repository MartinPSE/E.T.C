# Last in First Out
# LIFO
# LinkedList  를 쓰는게 최고 좋아! Data  를 넣었다 뺐다 하잖아!

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.head = None

    def push(self, value):  # [3] <-- [4]         [4] [3]  // 맨 앞에 데이터 넣기
        # Python  list  의 append 와 동일.

        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def pop(self):  # [3] [4] ... [3]              [4] -> Head  # 맨 끝(위)의 데이터 뽑기
        if self.is_empty():
            return "Stack is empty!"
        cur0 = self.head
        self.head = self.head.next
        return cur0.data

    def peek(self):  # 맨 앞의 데이터 보기
        if self.is_empty():
            return "Stack is empty!"
        return self.head.data

    def is_empty(self):  # 스택이 비었는지 안 비었는지 여부 반환
        return self.head is None


stack = stack()
stack.push(3)
print(stack.peek())

stack.push(4)
print(stack.peek())
print(stack.pop())
print(stack.is_empty())

print(stack.peek())
print(stack.pop())
print(stack.is_empty())
