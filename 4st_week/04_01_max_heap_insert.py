class MaxHeap:
    def __init__(self):
        self.items = [None]
# 1. 2n = 왼쪽 자식 노드
# 2. 2n + 1 = 오른쪽 자식 노드
# 3. n // 2 = 부모 노드
    def insert(self, value):
        self.items.append(value)
        new_node_index = len(self.items) - 1

        while new_node_index != 1:
            parent_node_index = new_node_index // 2

            if self.items[new_node_index] > self.items[parent_node_index]:
                self.items[new_node_index], self.items[parent_node_index] = self.items[parent_node_index], self.items[new_node_index]
                new_node_index = parent_node_index
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!