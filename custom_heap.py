import math

# Recall: 
# A heap is a tree data structure
# where every node is larger than it's left neighbor
# and greater than it's right neighbor. 

# the classic way to implement a heap is to use a dynamically-sized array. 
# also note that in order to make this work, we need a "dense" tree, i.e. 
# a maximally bushy tree. The word for this is a "COMPLETE" tree. 
# element at index i has
#   left parent at index 2i+1
#   right parent at index 2i+2
#   (note: this implies that for index i, it's parent is floor((i-1)/2))
#
#   to add an element to the heap, we compare the new element to 
#   the tip. If it's bigger, we know it goes in the right tree.
#   if it's smaller, we know it goes in the left tree. 
class MinHeap:
    def __init__(self, items):
        self.vals = []
        for item in items:
            self.push(item)

    def push(self, item):
        self.vals.append(item)
        self.__percolate_up__()
    
    def __heap_property_satisfied__(self):
        for i in reversed(range(1, len(self.vals))):
            parent_i = math.floor((i-1)/2)
            entry = h.vals[i]
            parent_entry = h.vals[parent_i]
            assert(entry >= parent_entry)


    def pop(self):

        if len(self.vals) <= 2:
            ans = self.vals[0]
            del self.vals[0]
            return ans


        ans = self.vals[0]
        last_item = self.vals[-1]
        self.vals[0] = last_item

        i = 0
        current_entry = self.vals[i]
        left_child = self.vals[(2*i)+1]
        right_child = self.vals[(2*i)+2]


        while ((current_entry > left_child) or (current_entry > right_child)) \
            and (self.__left_child_in_tree__(i)) and (self.__right_child_in_tree(i)):

            current_entry = self.vals[i]
            left_child = self.vals[(2*i)+1]
            right_child = self.vals[(2*i)+2]

            if current_entry > left_child or current_entry > right_child:
                if left_child < right_child:
                    temp = self.vals[i]
                    self.vals[i] = self.vals[(2*i)+1]
                    self.vals[(2*i)+1] = temp
                    i = (2*i)+1
                else:
                    temp = self.vals[i]
                    self.vals[i] = self.vals[(2*i)+2]
                    self.vals[(2*i)+2] = temp
                    i = (2*i)+2
            else:
                break


        
        if (self.__left_child_in_tree__(i)) and not(self.__right_child_in_tree(i)):
            current_entry = self.vals[i]
            child_entry = self.vals[(2*i)+1]
            if current_entry > child_entry:
                self.vals[(2*i)+1] = current_entry
                self.vals[i] = child_entry
        del self.vals[-1]
        self.__heap_property_satisfied__()
        return ans
    
    def __left_child_in_tree__(self, i):
        left_child_index = (2*i)+1
        return left_child_index < len(self.vals)

    def __right_child_in_tree(self, i):
        right_child_index = (2*i)+2
        return right_child_index < len(self.vals)


    def __percolate_up__(self):
        i = len(self.vals)-1

        current_entry = self.vals[i]
        parent_entry = self.vals[math.floor((i-1)/2)]
        while parent_entry > current_entry and i != 0:


            self.vals[i] = parent_entry
            self.vals[math.floor((i-1)/2)] = current_entry


            i = math.floor((i-1)/2)
            current_entry = self.vals[i]
            parent_entry = self.vals[math.floor((i-1)/2)]

    def __repr__(self):
        return str(self.vals)

    def __len__(self):
        return len(self.vals)

h = MinHeap([])

import random

random.seed(42)

for i in range(0, 30):
    h.push(random.randint(1,1000))

for i in reversed(range(1, len(h.vals))):
    parent_i = math.floor((i-1)/2)

    entry = h.vals[i]
    parent_entry = h.vals[parent_i]
    assert(entry >= parent_entry)

normal_sorted = sorted(h.vals)
heap_sorted = []
while len(h) > 0:
    heap_sorted.append(h.pop())

assert(heap_sorted == normal_sorted)