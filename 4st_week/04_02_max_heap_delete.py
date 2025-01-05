class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        return_value = self.items.pop()

        cur_index = 1
        while cur_index <= len(self.items) - 1:
            max_index = cur_index

            if cur_index * 2 <= len(self.items) - 1 and self.items[cur_index * 2] > self.items[cur_index]:
                max_index = cur_index * 2

            if cur_index * 2 + 1 <= len(self.items) - 1 and self.items[cur_index * 2 + 1] > self.items[cur_index]:
                max_index = cur_index * 2 + 1

            if cur_index == max_index:
                break

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return return_value  # 8 을 반환해야 합니다.


#     7             1
#  6    4           2, 3
#2   5 8            4, 5, 6
#   전체 개수 = 7(None 포함) - 1 = 6

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]