from binary_heap import BinaryHeap
import unittest

my_list = [8, 5, 4, 9, 3, 65, 1, 66, 599, 80]

my_heap = BinaryHeap()

for i in my_list:
   my_heap.insert(i)

class InsertTests(unittest.TestCase):
   
   def test_insert(self):
      my_heap.insert(2)
      self.assertTrue(my_heap.check_heap)
      my_heap.insert(0)
      self.assertTrue(my_heap.check_heap)
      my_heap.insert(500)
      self.assertTrue(my_heap.check_heap)

if __name__ == '__name__':
   unittest.main()

# command to run tests: python -m unittest -v insert_test.py