#!/usr/bin/env python3

import math

# Framework for heap sort. We'll build this from scratch as proof of concept
class Heap:
    size = 0
    height = 0
    array = []

    def __init__(self, nums):
        self.array = nums
        self.size = len(nums)
        self.height = math.ceil(math.log2(self.size+1))
    
    # Return the index of the left child
    def left(self, index):
        index += 1
        index *= 2
        index -= 1
        return index
    
    def right(self, index):
        index += 1
        index *= 2
        return index
    
    # Return the index of the parent
    def parent(self, index):
        index += 1
        index = int(index / 2)
        index -= 1
        return index

    # Assume the trees at left(index) and right(index) are heapified, but that array[index] might be out of place
    # dir = 1 for max heapifying; dir = -1 for min heapifying
    def heapify(self, index, dir):
        l = self.left(index)
        r = self.right(index)

        # Find the largest out of l, index, and r
        largest = index
        for x in [l, r]:
            if x < self.size:
                if self.array[x]*dir > self.array[largest]*dir:
                    largest = x

        # Do a swap if required
        if largest != index:
            #self.array[index], self.array[largest] = self.array[largest], self.array[index]
            temp = self.array[index]
            self.array[index] = self.array[largest]
            self.array[largest] = temp


            self.heapify(largest, dir)

    # Use heapify() to max heapify the whole heap
    def build_heap(self, dir):
        self.size = len(self.array)
        for i in range(int(self.size/2), -1, -1):
            self.heapify(i, dir)

    # For testing
    def print_tree(self):
        n = 0
        for h in range(self.height):
            for x in range(2 ** h):
                print(self.array[n], end = " ")

                n += 1
                if n == self.size:
                    print()
                    return
            print()