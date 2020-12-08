from dft_iterator import IteratorDFT

class BinaryHeap():

   def __init__(self):
      self.heap_list = []

   def heapify(self, elem_index):
      
      if elem_index % 2 == 0:
         root_index = int((elem_index - 2) / 2)
      else:
         root_index = int((elem_index - 1) / 2)

      if root_index >= 0: 
         if self.heap_list[elem_index] < self.heap_list[root_index]:
            self.heap_list[elem_index], self.heap_list[root_index] = self.heap_list[root_index], self.heap_list[elem_index]
            self.heapify(root_index)

   def insert(self, value):
      if len(self.heap_list) == 0:
         self.heap_list.append(value)
      else:
         self.heap_list.append(value)
         self.heapify(len(self.heap_list) - 1)

   # search == contains, but returns the key element
   def search(self, value):
      pass

   def remove(self, value):
      pass

   # returns the index of the current element
   def create_dft_iterator(self):
      return IteratorDFT(len(self.heap_list))

   def create_bft_iterator(self):
      pass

   # checks if a binary tree satisfies properties
   def check_heap(self):

      for i in range(0, len(self.heap_list) // 2):
         if self.heap_list[i] > self.heap_list[2 * i + 1]:
            return False
         if (2 * i + 2 < len(self.heap_list)):
            if self.heap_list[i] > self.heap_list[2 * i + 2]:
               return False
      return True

my_list = [8, 5, 2, 9, 3, 65, 1, 66, 599, 80, 10, 70, 77, 36, 6]

my_heap = BinaryHeap()

for i in my_list:
   my_heap.insert(i)

my_iterator = my_heap.create_dft_iterator()

print(my_heap.heap_list)

for i in range(0, len(my_heap.heap_list)):
   print(my_heap.heap_list[next(my_iterator)])