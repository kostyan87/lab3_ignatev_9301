from binary_heap import BinaryHeap, create_heap
import unittest

my_heap = create_heap([8, 5, 2, 9, 3, 65, 1, 66, 599, 80, 10, 70, 77, 36, 6])

my_heap.remove(80)

my_heap2 = create_heap([8, 5, 2, 9, 3, 65, 1, 66, 599, 80, 10, 70, 77, 36, 6])

my_heap2.remove(1)

my_heap3 = create_heap([8, 5, 2, 9, 3, 65, 1, 66, 599, 80, 10, 70, 77, 36, 6])

my_heap3.remove(10)

class RemoveTests(unittest.TestCase):
   
   def test_remove(self):
      self.assertEqual(my_heap.heap_list, [1, 3, 2, 9, 6, 65, 5, 66, 599, 8, 10, 70, 77, 36])
      self.assertEqual(my_heap2.heap_list, [2, 3, 5, 9, 8, 65, 6, 66, 599, 80, 10, 70, 77, 36])
      self.assertEqual(my_heap3.heap_list, [1, 3, 2, 9, 6, 65, 5, 66, 599, 80, 8, 70, 77, 36])

if __name__ == '__name__':
   unittest.main()

# command to run tests: python -m unittest -v iterators_test.py