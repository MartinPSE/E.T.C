# 링크드 리스트에서 K 번째 값 추출하기.
# Method #2  시작 < -K- > 끝
#              K  만큼의 거리를 두고 노드를 같이 이동시킨다.


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

        # 1. 노드를 2개 잡는다.
        # 2. 한 노드를 다른 노드보다 K  만큼 떨어지게 한다.
        # 3. 계속 한 칸 씩 같이 이동한다.           -> O(N)
        # 4. 만약 더 빠른 노드가 끝에 도달했다면      -> O(N-K) 동일 하게 이동.
        # 느린 노드는 끝에서 K 만큼 떨어진 노드가 되므로 -> 이 값을 return.

    def get_kth_node_from_list(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

            return slow

linked_list = LinkedList(0)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)

print(linked_list.get_kth_node_from_list(2).data)