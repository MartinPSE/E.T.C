# 링크드 리스트에서 K 번째 값 추출하기.
# Method 1. List  의 길이를 구한뒤  ->             0(N)
#           length - k  위치의 노드를 추출한다.->   0(N-K)
#           O(N)  의 시간 복잡도.

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

    def get_kth_node_from_list(self, k):           # linked_List  의 길이를 알아내자
        cur = self.head                            # 길이에서 구하고자하는 N  번째 자릿수를 뺀 자리의 Node 값을 추출.
        length = 1

        while cur.next is not None:  # Linked_List  의 길이를 구하는과정
            cur = cur.next
            length += 1

        end_length = length - k  # 원하는 뒤에서 N  번째 자리 지정.
        cur = self.head
        print(end_length)

        for i in range(end_length):  # N  번째 자리 까지 Node 이동후 그 값 추출.

            cur = cur.next
        return cur
        # 0 7 8
        #   k


linked_list = LinkedList(0)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)

print(linked_list.get_kth_node_from_list(2).data)  # 7이 나와야해!
