from binary_heap import BinaryHeap
import unittest

# depth-first traversal
my_list = [8, 5, 2, 9, 3, 65, 1, 66, 599, 80, 10, 70, 77, 36, 6]
   
my_heap = BinaryHeap()

for i in my_list:
   my_heap.insert(i)

my_iterator = my_heap.create_dft_iterator()

dft = []

for i in my_iterator:
   dft.append(i)

# breadth-first traversal
my_list2 = [8, 5, 2, 9, 3, 65, 1, 66, 599, 80, 10, 70, 77, 36, 6]
   
my_heap2 = BinaryHeap()

for i in my_list2:
   my_heap2.insert(i)

my_iterator2 = my_heap2.create_bft_iterator()

bft = []

for i in my_iterator2:
   bft.append(i)

class IteratorsTests(unittest.TestCase):
   
   def test_iterator_dft(self):
      self.assertEqual(dft, [1, 3, 9, 66, 599, 8, 80, 10, 2, 65, 70, 77, 5, 36, 6])

   def test_iterator_bft(self):
      self.assertEqual(bft, [1, 3, 2, 9, 8, 65, 5, 66, 599, 80, 10, 70, 77, 36, 6])

if __name__ == '__name__':
   unittest.main()

# command to run tests: python -m unittest -v iterators_test.py