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

    def get_kth_node_from_last(self, k):
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next

        return cur


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)
linked_list.append(11)
linked_list.append(12)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!