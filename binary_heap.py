from dft_iterator import IteratorDFT
from bft_iterator import IteratorBFT

class BinaryHeap():

   def __init__(self):
      self.heap_list = []

   def sift_up(self, elem_index):

      if elem_index % 2 == 0:
         root_index = int((elem_index - 2) / 2)
      else:
         root_index = int((elem_index - 1) / 2)

      if root_index >= 0: 
         if self.heap_list[elem_index] < self.heap_list[root_index]:
            self.heap_list[elem_index], self.heap_list[root_index] = self.heap_list[root_index], self.heap_list[elem_index]
            self.heapify(root_index)

   def sift_down(self, elem_index):

      left_child = (2 * elem_index) + 1
      right_child = (2 * elem_index) + 2

      if right_child < len(self.heap_list) and (self.heap_list[left_child] < self.heap_list[elem_index] or self.heap_list[right_child] < self.heap_list[elem_index]):
         if self.heap_list[right_child] > self.heap_list[left_child]:
            self.heap_list[left_child], self.heap_list[elem_index] = self.heap_list[elem_index], self.heap_list[left_child]
            self.heapify(left_child)
         else:
            self.heap_list[right_child], self.heap_list[elem_index] = self.heap_list[elem_index], self.heap_list[right_child]
            self.heapify(right_child)
         
      elif left_child < len(self.heap_list) and self.heap_list[left_child] < self.heap_list[elem_index]:
         self.heap_list[left_child], self.heap_list[elem_index] = self.heap_list[elem_index], self.heap_list[left_child]
         self.heapify(left_child)

   def heapify(self, elem_index):
      
      self.sift_up(elem_index)
      self.sift_down(elem_index)

   def insert(self, value):
      if len(self.heap_list) == 0:
         self.heap_list.append(value)
      else:
         self.heap_list.append(value)
         self.heapify(len(self.heap_list) - 1)

   # search == contains, but returns the key of element
   def search(self, value):
      for i in range(0, len(self.heap_list)):
         if self.heap_list[i] == value:
            return i
      return None

   def remove(self, value):
      remove_index = self.search(value)

      if remove_index == None:
         raise Exception('No such item in the heap')
      if remove_index == len(self.heap_list) - 1:
         del self.heap_list[len(self.heap_list) - 1]
      else:
         self.heap_list[remove_index], self.heap_list[len(self.heap_list) - 1] = self.heap_list[len(self.heap_list) - 1], self.heap_list[remove_index]
         del self.heap_list[len(self.heap_list) - 1]
         self.heapify(remove_index)

   # returns the index of the current element
   def create_dft_iterator(self):
      return IteratorDFT(len(self.heap_list), self.heap_list)

   def create_bft_iterator(self):
      return IteratorBFT(len(self.heap_list), self.heap_list)

   # checks if a binary tree satisfies properties
   def check_heap(self):

      for i in range(0, len(self.heap_list) // 2):
         if self.heap_list[i] > self.heap_list[2 * i + 1]:
            return False
         if (2 * i + 2 < len(self.heap_list)):
            if self.heap_list[i] > self.heap_list[2 * i + 2]:
               return False
      return True

def create_heap(list):

   my_heap = BinaryHeap()
   
   for i in list:
      my_heap.insert(i)

   return my_heap

def example():
   # example of heap creation and depth-first traversal
   my_heap = create_heap([8, 5, 2, 9, 3, 65, 1, 66, 599, 80, 10, 70, 77, 36, 6])
   
   my_iterator = my_heap.create_dft_iterator()
   
   print(f'Heap: {my_heap.heap_list}')
   
   print('Depth-first traversal:')
   for i in my_iterator:
      print(i)

   # example of heap creation and breadth-first traversal

   my_heap = create_heap([8, 5, 2, 9, 3, 65, 1, 66, 599, 80, 10, 70, 77, 36, 6])
   
   my_iterator = my_heap.create_bft_iterator()

   print(f'Heap: {my_heap.heap_list}')
   
   print('Breadth-first traversal:')
   for i in my_iterator:
      print(i)

if __name__ == "__main__":

   example()