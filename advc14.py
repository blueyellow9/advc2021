from functools import *
from collections import *
from itertools import *
from math import *
from sys import exit
from dataclasses import dataclass
import numpy as np
import re
from builtins import pow
from heapq import heappop, heappush, heappushpop, heapify, heapreplace
import pyperclip

print ("Welcome to Python Puzzle 2, 2020")

#function to read input file
def read_file(filename):
    with open(filename) as fin:
        data = [i.strip() for i in fin]
    return data

count = 0
instructions = []
coords = []
matrix = []

str = []
#Hold the polymer formula
formula = {}

def main():
    global matrix
    data = read_file("advc14.txt")

    for i, val in enumerate(data):
        if (i == 0):
            template = val
        elif (i > 1):
            str = val.split(' -> ')
            formula[str[0]] = str[1]
        
    #Character count
    #Count each character to start with
    count = {}
    for s in template:
        if (s in count.keys()):
            count[s] += 1
        else:
            count[s] = 1
    #print("Starting  : ", sum(count.values()))

    #The substitutions happen simultaneously
    #Hence maintaining a copy
    pair_count = {}
    pair_copy = {}

    #Creating a dictionaries of all pairs
    l = 0
    while l < len(template)-1:
        pair = template[l]+template[l+1]
        if pair in pair_count.keys():
            pair_count[pair] += 1
        else:
            pair_count[pair] = 1
        l += 1

    for i in range(40):
        #print('#################')
        pair_copy = pair_count.copy()
        #print(pair_copy)
        #algoritm is applied on a copy, but the original is updated
        for key in list(pair_copy):
            if key in formula.keys():
                #print(key, " -> ", formula[key])
                #print("Delete ", key, pair_copy[key] )

                #The process involves removing a pair and adding two new pairs.
                #The new pairs are created after lookup in the formula for polymer

                #1) Remove the pair
                temp = pair_copy[key]
                pair_count[key] = pair_count[key] - temp
                if pair_count[key] == 0:
                    del pair_count[key]

                #Everytime a new character is inserted the count is updated
                if formula[key] in count.keys():
                    count[formula[key]] += temp
                else:
                    count[formula[key]] = 1

                #2)Add top pair
                pair = key[0] + formula[key]
                if pair in pair_count.keys():
                    pair_count[pair] += temp
                else:
                    pair_count[pair] = temp
                #print("Add ",pair, pair_count[pair])

                #3)Add bottom pair
                pair = formula[key] + key[1]
                if pair in pair_count.keys():
                    pair_count[pair] += temp
                else:
                    pair_count[pair] = temp
                #print("Add ",pair, pair_count[pair])

                #one loop is complete
        print("Iteration : ", i, sum(count.values()))

    max_val = count[max(count, key=count.get)]
    min_val = count[min(count, key=count.get)]
    print(max_val, min_val, max_val-min_val)


        

if __name__ == "__main__":
    main()