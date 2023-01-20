#!/usr/bin/env python3

def insertion_sort(nums):
    for i in range(1, len(nums)):
        curr = nums[i]
        j = i - 1
        
        while j>=0 and nums[j]>curr:
            nums[j+1] = nums[j]
            j -= 1
        
        nums[j+1] = curr
    
    return nums

def reverse_insertion_sort(nums):
    for i in range(1, len(nums)):
        curr = nums[i]
        j = i - 1
        
        while j>=0 and nums[j]<curr:
            nums[j+1] = nums[j]
            j -= 1
        
        nums[j+1] = curr
    
    return nums

nums = [5, 2, 4, 6, 1, 3]
print("Insertion sort.")
print(f"Unsorted list: {nums}")
nums = reverse_insertion_sort(nums)
print(f"Sorted list: {nums}")