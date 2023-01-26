#!/usr/bin/env python3

""" Reconstruct min and max priority queues from heaps"""

from heap import Heap
from sort import get_list

# Replicate basic features of Python's queue.PriorityQueue
class PriorityQueue:
    h = Heap([])
    dir = 1

    def __init__(self, nums):
        self.h = Heap(nums)
        self.h.build_heap(self.dir)
    
    # Remove and return the element with the largest key if max queue, or smallest if min
    def heap_extract(self):
        if len(self.h.array) == 0:
            print("Heap underflow")
            return
        
        max = self.h.array[0]
        self.h.array[0] = self.h.array[-1]
        self.h.size -= 1
        self.h.heapify(0, self.dir)

        return max
    
    # Increase or decrease element index's key to key, where key >= index's current key
    def crease_key(self, index, key):
        if dir==1 and key<self.h.array[index]:
            print("Error: new key is smaller than current key")
            return
        if dir==-1 and key>self.h.array[index]:
            print("Error: new key is greater than current key")
            return
        
        self.h.array[index] = key
        while index>0 and self.h.array[self.h.parent(index)]*self.dir<self.h.array[index]*self.dir:
            # Excahnge array[index] with array[parent(index)]
            self.h.array[index], self.h.array[self.h.parent(index)] = self.h.array[self.h.parent(index)], self.h.array[index]
            index = self.h.parent(index)
    
    # Insert element key into a max priority queue
    def heap_insert(self, key):
        self.h.size += 1
        self.h.array.append(0)
        self.crease_key(self.h.size-1, key)

class MinPriorityQueue(PriorityQueue):
    def __init__(self, nums):
        self.dir = -1
        self = PriorityQueue(nums)