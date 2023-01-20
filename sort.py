#!/usr/bin/env python3

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

# Merge sort
def merge_sort(nums, p = 0, r = sys.maxsize, dir = 1):
    if r == sys.maxsize:
        r = len(nums) - 1
    
    if p < r:
        q = int((p + r) / 2)
        nums = merge_sort(nums, p, q, dir)
        nums = merge_sort(nums, q + 1, r, dir)
        nums = merge(nums, p, q, r, dir)
    
    return nums

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
        if str == "insertion" or str == "insertion ascending":
            nums = insertion_sort(nums)
            break
        elif str == "insertion descending":
            nums = insertion_sort(nums, -1)
            break
        elif str == "merge" or str == "merge ascending":
            nums = merge_sort(nums)
            break
        elif str == "merge descending":
            nums = merge_sort(nums, dir = -1)
            break
        
        str = input("Option not recognised - try again: ")
    
    print(f"\nSorted list: {nums}")

if __name__ == "__main__":
    main()