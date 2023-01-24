#!/usr/bin/env python3

import math
import sys

# Insertion sort: dir = 1 for ascending; dir = -1 for descending
def insertion_sort(nums, dir = 1):
    for i in range(1, len(nums)):
        curr = nums[i]
        j = i - 1
        
        while j>=0 and nums[j]*dir>curr*dir:
            nums[j+1] = nums[j]
            j -= 1
        
        nums[j+1] = curr
    
    return nums

# Helper function for merge_sort
def merge(nums, p, q, r, dir = 1):
    # Seperate the two sides
    lnums = nums[p:q+1]
    rnums = nums[q+1:r+1]
    lnums.append(sys.maxsize * 2 * dir)
    rnums.append(sys.maxsize * 2 * dir)
    
    # Merge
    i = 0
    j = 0
    for k in range(p, r+1):
        if lnums[i]*dir < rnums[j]*dir:
            nums[k] = lnums[i]
            i += 1
        else:
            nums[k] = rnums[j]
            j += 1

    return nums

def merge_sort(nums, p = 0, r = sys.maxsize, dir = 1):
    if r == sys.maxsize:
        r = len(nums) - 1
    
    if p < r:
        q = int((p + r) / 2)
        nums = merge_sort(nums, p, q, dir)
        nums = merge_sort(nums, q + 1, r, dir)
        nums = merge(nums, p, q, r, dir)
    
    return nums

def bubble_sort(nums, dir = 1):
    for i in range(len(nums) - 1):
        for j in range(len(nums)-1, i, -1):
            if nums[j]*dir < nums[j-1]*dir:
                # Swap nums[j] and nums[j-1]
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = temp

    return nums

# Framework for heap sort. We'll build this from scratch as proof of concept
class heap:
    size = 0
    height = 0
    array = []

    def __init__(self, nums):
        self.array = nums
        self.size = len(nums)
        self.height = math.ceil(math.log2(self.size+1))
    
    # Return the *index* of the left child
    def left(self, index):
        index += 1
        index *= 2
        index -= 1
        return index
    
    def right(self, index):
        index += 1
        index *= 2
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

def heap_sort(nums, dir = 1):
    # Build a max heap out of the unsorted list
    h = heap(nums)
    h.build_heap(dir)
    # Sort
    for i in range(h.size-1, 0, -1):
        temp = h.array[0]
        h.array[0] = h.array[i]
        h.array[i] = temp
        h.size -= 1
        h.heapify(0, dir)
        h.print_tree()

    return h.array

# Use the sorting functions:
def get_list():
    nums = []
    str = input("Enter a list, comma-separated: ")
    for num in str.replace(" ", "").split(","):
        try:
            nums.append(int(num))
        except ValueError:
            print(f"Not a number: \"{num}\"\n")
            return get_list()

    return nums

# Provide a user interface
def main():
    print("Welcome to the sorter.\n")
    nums = get_list()

    str = input("How would you like to sort this list? ")
    while (str != "exit"):
        if str in ["insertion", "insertion ascending"]:
            nums = insertion_sort(nums)
            break
        elif str == "insertion descending":
            nums = insertion_sort(nums, -1)
            break
        elif str in ["merge", "merge ascending"]:
            nums = merge_sort(nums)
            break
        elif str == "merge descending":
            nums = merge_sort(nums, dir = -1)
            break
        elif str in ["bubble", "bubble ascending"]:
            nums = bubble_sort(nums)
            break
        elif str == "bubble descending":
            nums = bubble_sort(nums, -1)
            break
        elif str in ["heap", "heap ascending"]:
            nums = heap_sort(nums)
            break
        elif str == "heap descending":
            nums = heap_sort(nums, -1)
            break
        
        str = input("Option not recognised - try again: ")
    
    print(f"\nSorted list: {nums}")

if __name__ == "__main__":
    main()