# QUEUE 연습! FIFO!! 놀이기구 생각해보자~
# enqueue(data) : 맨 뒤에 데이터 추가하기
# dequeue(): 맨 앞에 데이터 뽑기!
# peek() : 맨 앞에 데이터 보기!
# isEmpty() : Queue  가 비었는지 안비었는지 여부 반환!
# Data 넣고 빼고 자주하면 Linked List  로 구현하자!

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # head      ?        tail
    # head     tail    new_node
    # [ 3 ] , [ 4 ] ,    [ 5 ]

    # head, tail
    #   [3]

    def enqueue(self, value):  # Queue  에 데이터를 넣어보자!
        new_tail = Node(value)  # 초기값을 고려해줘야해, 처음에 None 이기 때문에 !
        if self.is_empty():  # Queue  의 data  가 1개니깐, 그 data  는 head  이자, tail  입니다!
            self.head = new_tail
            self.tail = new_tail
            return
        self.tail.next = new_tail
        self.tail = new_tail

        # head            tail
        # [3] , [6] ,[4] , [5]  -> 3을 ?
        #       head      tail
        #
        #

    def dequeue(self):  # 맨 처음 데이터를 추출해보자!
        if self.is_empty():
            return "Queue is Empty!"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):  # 맨 앞에 데이터를 보여주기만하자!
        if self.is_empty():
            return "Queue is Empty!"
        return self.head.data

    def is_empty(self):
        return self.head is None


queue = Queue()
queue.enqueue(3)
print(queue.peek())  # [3]
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())

