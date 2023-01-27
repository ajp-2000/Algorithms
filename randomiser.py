#!/usr/bin/env python3

""" Write a list of random integers to a specified output file, seperated by commas and spaces, generated within
certain parameters."""

import argparse
import os.path
import random

def main():
    # Parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("min", help = "Lowest integer value", type = int)
    parser.add_argument("max", help = "Highest integer value", type = int)
    parser.add_argument("count", help = "Number of values to write", type = int)
    parser.add_argument("output", help = "File to write to")
    args = parser.parse_args()

    # Open the output file
    while os.path.isfile(args.output):
            overwrite = ""
            while overwrite not in ["y", "n"]:
                overwrite = input(f"File {args.output} already exists. Overwrite? [y/n]")
            if overwrite == "n":
                args.output = input("Enter a new output file name: ")
            else:
                break

    with open(args.output, mode="w") as outfile:
        for i in range(args.count - 1):
            outfile.write(str(random.randint(args.min, args.max)))
            outfile.write(", ")
        outfile.write(str(random.randint(args.min, args.max)))
        
        print("Written.")

if __name__ == "__main__":
    main()