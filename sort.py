#!/usr/bin/env python3

"""Various sorting algorithms. Run with -v to print each step"""

import argparse
import os.path
import sys
from time import process_time
from heap import Heap

verbose = False
line = 1

# Print the current line of the sorting process
def print_line(nums):
    if verbose:
        global line
        print(f"{line}. ", end = "")
        print(" ".join(str(num) for num in nums))
        line += 1

# Insertion sort: dir = 1 for ascending; dir = -1 for descending
def insertion_sort(nums, dir = 1):
    for i in range(1, len(nums)):
        curr = nums[i]
        j = i - 1
        
        while j>=0 and nums[j]*dir>curr*dir:
            nums[j+1] = nums[j]
            j -= 1
        
        nums[j+1] = curr
        print_line(nums)
    
    return nums

# Helper function for merge sort
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
        print_line(nums)
    
    return nums

def bubble_sort(nums, dir = 1):
    for i in range(len(nums) - 1):
        for j in range(len(nums)-1, i, -1):
            if nums[j]*dir < nums[j-1]*dir:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                print_line(nums)

    return nums

def heap_sort(nums, dir = 1):
    # Build a max heap out of the unsorted list
    h = Heap(nums)
    h.build_heap(dir)
    # Sort
    for i in range(h.size-1, 0, -1):
        print_line(h.array)
        h.array[0], h.array[i] = h.array[i], h.array[0]
        h.size -= 1
        h.heapify(0, dir)

    return h.array

# Helper function for quick sort
def quick_partition(nums, p, r, dir):
    x = nums[r]                                                             # The pivot
    i = p - 1
    
    for j in range(p, r):
        if nums[j]*dir < x*dir:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1

def quick_sort(nums, p = 0, r = sys.maxsize, dir = 1):
    if r == sys.maxsize:
        r = len(nums) - 1

    if p < r:
        print_line(nums)
        q = quick_partition(nums, p, r, dir)
        nums = quick_sort(nums, p, q - 1, dir)
        print_line(nums)
        nums = quick_sort(nums, q + 1, r, dir)
    
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
    # Map sorting algorithm names to functions
    algo_dict = {
        "insertion": insertion_sort,
        "merge": merge_sort,
        "bubble": bubble_sort,
        "heap": heap_sort,
        "quick": quick_sort
    }

    # Command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sort", help = "Specify a sorting algorithm, e.g. 'merge', 'bubble', 'insertion'")
    parser.add_argument("-i", "--input", help = "Read the unsorted list from a text file")
    parser.add_argument("-o", "--output", help = "Write the sorted list to a text file")
    parser.add_argument("-v", "--verbose", help = "Print each step of the sort", action = "store_true")
    parser.add_argument("-t", "--time", help = "Print time (ms) taken by algorithm, to 2dp", action = "store_true")
    args = parser.parse_args()

    global verbose
    verbose = args.verbose

    # If the user specified a sorting algorithm, check it's real
    if args.sort:
        if args.sort not in algo_dict:
            print(f"Algorithm not recognised: {args.sort}")
            return 1

    # Get the list, from user input or from a specified file
    print("Welcome to the sorter.\n")
    nums = []
    if not args.input:
        nums = get_list()
    else:
        # Read from file: we take the first line only, and try to parse it as a comma-separated list
        try:
            infile = open(args.input, 'r')
        except:
            print(f"Could not open file: {args.input}")
            return 1
        
        line = infile.readline()
        for num in line.replace(" ", "").split(","):
            try:
                nums.append(int(num))
            except ValueError:
                print(f"Not a number: \"{num}\"")
                return 1
        infile.close()

    # Sort the list
    dir = 1
    if not args.sort:
        instr = input("How would you like to sort this list? ")
        while (instr != "exit"):
            instrs = instr.split()
            if instrs[0] in algo_dict:
                if len(instrs) > 1:
                    if instrs[1] in ["ascending", "descending"]:
                        args.sort = instrs[0]
                        if instrs[1] == "descending":
                            dir = -1
                        break

                args.sort = instrs[0]
                break
            
            instr = input("Option not recognised - try again: ")
    
    elapsed = 0
    start_time = process_time()
    nums = algo_dict[args.sort](nums, dir = dir)
    if args.time:
        elapsed = (process_time() - start_time) * 1000
    
    # Output the sorted list, either to the command line, or to a specified file
    if not args.output:
        print(f"\nSorted list: {nums}")
    else:
        # Write to file
        while os.path.isfile(args.output):
            overwrite = ""
            while overwrite not in ["y", "n"]:
                overwrite = input(f"File {args.output} already exists. Overwrite? [y/n]")
            if overwrite == "n":
                args.output = input("Enter a new output file name: ")
            else:
                break

        with open(args.output, mode="w") as outfile:
            for num in nums:
                outfile.write(str(num))
                outfile.write(", ")
        
        print(f"\nSorted list written to {args.output}.")
    
    if args.time:
        print(f"Time taken: {round(elapsed, 2)} ms.")

if __name__ == "__main__":
    main()