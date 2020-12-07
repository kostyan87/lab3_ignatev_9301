class BinaryHeap():

   def __init__(self, heap_list):
      self.heap_list = heap_list
      self.heap_size = len(self.heap_list)
      self.build_heap()

   def heapify(self, root_index):
      
      left_child_index = (2 * root_index) + 1
      right_child_index = (2 * root_index) + 2

      if left_child_index < self.heap_size and self.heap_list[left_child_index] < self.heap_list[root_index]:
         self.heap_list[root_index], self.heap_list[left_child_index] = self.heap_list[left_child_index], self.heap_list[root_index]
         self.heapify(left_child_index)

      if right_child_index < self.heap_size and self.heap_list[right_child_index] < self.heap_list[root_index]:
         self.heap_list[root_index], self.heap_list[right_child_index] = self.heap_list[right_child_index], self.heap_list[root_index]
         self.heapify(right_child_index)

   def build_heap(self):

      for i in range(self.heap_size // 2, -1, -1):
         self.heapify(i)

   def check_heap(self):

      for i in range(0, self.heap_size // 2 - 1):
         if self.heap_list[i] > self.heap_list[2 * i + 1] or self.heap_list[i] > self.heap_list[2 * i + 2]:
            return False
      return True

my_list = [8, 5, 2, 9, 3, 65, 1, 66, 599, 80]

my_heap = BinaryHeap(my_list)

print(f"My heap: {my_heap.heap_list}")

print(f"Check heap: {my_heap.check_heap()}")