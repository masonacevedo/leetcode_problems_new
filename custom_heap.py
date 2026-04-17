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
    
    def pop(self):
        pass

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


h = MinHeap([])
print(h)
print()


h.push(5)
print(h)
print()

h.push(4)
print(h)
print()

h.push(3)
print(h)

h.push(2)
print(h)

h.push(1)
print(h)
h.push(2.5)
print(h)

import random


for i in range(0, 50):
    h.push(random.randint(1,1000))

for i in reversed(range(1, len(h.vals))):
    parent_i = math.floor((i-1)/2)

    entry = h.vals[i]
    parent_entry = h.vals[parent_i]
    assert(entry >= parent_entry)

