from heapq import heapify

class BinaryHeap():

   def __init__(self, heap_list):
      self.heap_list = heap_list
      self.heap_size = len(self.heap_list)
      self.build_heap(self.heap_list)

   def heapify(self, root_index):
      
      left_child_index = (2 * root_index) + 1
      right_child_index = (2 * root_index) + 2

      if left_child_index < self.heap_size and self.heap_list[left_child_index] < self.heap_list[root_index]:
         self.heap_list[root_index], self.heap_list[left_child_index] = self.heap_list[left_child_index], self.heap_list[root_index]
         self.heapify(left_child_index)

      if right_child_index < self.heap_size and self.heap_list[right_child_index] < self.heap_list[root_index]:
         self.heap_list[root_index], self.heap_list[right_child_index] = self.heap_list[right_child_index], self.heap_list[root_index]
         self.heapify(right_child_index)

   def build_heap(self, heap_list):

      for i in range(len(self.heap_list) // 2, -1, -1):
         self.heapify(i)
      '''for i in range(0, self.heap_size):
         self.heapify(i)'''

my_list = [8, 5, 2, 9, 3, 65, 1, 66, 599, 80]
my_list2 = [8, 5, 2, 9, 3, 65, 1, 66, 599, 80]

my_heap = BinaryHeap(my_list2)

heapify(my_list)

print(f"Мой класс: {my_heap.heap_list}")

print(f"Библиотечный класс: {my_list}")