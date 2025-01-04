# queue 직접 구현
# 구현 가능하지만 실제 사용 시에는 라이브러리를 사용한다.
# stack은 list를 사용하지만, queue는 collections.deque 라는 라이브러리를 사용해야 한다. (성능이슈)
# 성능 이슈의 원인은 list의 경우 array의 형태를 가지고 있기 때문에 요소를 삽입할 때 O(n)의 시간복잡도가 걸린다. (뒤에 있는 요소를 전부 한 칸 씩 땡겨야 하기 때문)
# 하지만 deque의 경우 양방향 링크드 리스트로 구현이 되어 있기 때문에 삽입, 삭제의 시간복잡도가 O(1) 이다.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        dequeue_head = self.head
        self.head = self.head.next
        return dequeue_head

    def peek(self):
        if self.is_empty():
            return "queue is empty"
        return self.head.data

    def is_empty(self):
        return self.head is None




queue = Queue()
queue.enqueue(1)
print(queue.peek())

queue.enqueue(2)
print(queue.peek())

queue.enqueue(3)
print(queue.peek())

queue.dequeue()
print(queue.peek())

queue.dequeue()
print(queue.peek())

queue.dequeue()
print(queue.peek())