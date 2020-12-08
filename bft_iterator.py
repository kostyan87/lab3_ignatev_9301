import sys; sys.path.append(r'.\data_structures')

from data_structures.queue import Queue

class IteratorBFT:

    def __init__(self, heap_size, heap_list):
        self.current_elem = 0
        self.heap_list = heap_list
        self.end = heap_size - 1
        self.count = 0
        self.queue = Queue()
        self.queue.push(0)

    def __iter__(self):
        return self
        
    def has_left_child(self, index):
        if (2 * index) + 1 <= self.end:
            return True
        return False

    def has_right_child(self, index):
        if (2 * index) + 2 <= self.end:
            return True
        return False

    def __next__(self):
        if self.count <= self.end:
            current_elem = self.current_elem

            if self.has_left_child(self.current_elem):
                self.queue.push((2 * self.current_elem) + 1)

            if self.has_right_child(self.current_elem):
                self.queue.push((2 * self.current_elem) + 2)
            
            self.queue.pop()
            if self.count != self.end:
               self.current_elem = self.queue.get_top()
            
            self.count += 1
            
            return self.heap_list[current_elem]
        else:
            raise StopIteration