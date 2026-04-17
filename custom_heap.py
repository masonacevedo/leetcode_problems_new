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
    def __init__(self, priorities_and_items):
        pass

    def push(self, priority, item):
        pass
    
    def pop(self):
        pass
    