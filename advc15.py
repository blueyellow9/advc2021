from functools import *
from collections import *
import heapq
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

def read_file(filename):
    with open(filename) as fin:
        data = [i.strip() for i in fin]
    return data

#Move horizontally and vertically
rows = [-1, 0, 0, 1]
cols = [0, -1, 1, 0]

#does the horizontal and vertical movements fall within the matrix?
def isValid(x,y,N,M,tiles=1):
    return (0 <= x <= N*tiles-1 and 0 <= y <= M*tiles-1)

matrix = []
visited = set()
cost = defaultdict(int)

#cost for part 1
#def get_risk(x,y,N,M,tiles):
#    return matrix[x][y]

#cost for part 2
def get_risk(x,y, N, M,tiles=1):
    global matrix
    if (tiles == 1):
        return matrix[x][y]
    c = matrix[x%N][y%M] + x // N + y // M 
    c = (c - 1)%9 + 1
    return c 

def find_path(N,M,tiles=1):
    global cost, matrix, visited, rows, cols
    nodes = [(0,0,0,[])] #starting node left top corner
    heapq.heapify(nodes)

    while(len(nodes) > 0):
        #store cost, row and column position and path taken in the heap
        c, row, col, path = heapq.heappop(nodes)
        #print("Current node ", row, col, c, path)
        if (row,col) in visited:
            continue
        visited.add((row,col))
        cost[(row,col)] = c
        p = path.copy()
        #Update the path for the next elements
        p.append([row, col])

        #if bottom right element of matrix, done
        if (row == N*tiles-1 and col == M*tiles-1):
            #print the final path if needed
            #print(p)
            break

        #from current node look, left, right, up, down
        for k in range(len(rows)):
            rr = rows[k] + row
            cc = cols[k] + col

            if not isValid(rr, cc, N, M,tiles):
                continue
            #print("Adding node ", rr, cc, c+matrix[rr][cc])
            #Add the node to queue, the cost of the node is cost of the
            #previous node + cost of the node itself
            heapq.heappush(nodes, (c+get_risk(rr,cc,N,M,tiles), rr, cc,p.copy()))
        #print(len(nodes))
    return

def main():
    #data = read_file("advc15_ex.txt")
    data = read_file("advc15.txt")
    N = len(data)
    M = len(data[0])
    for i in range(N):
        arr = []
        for j in range(M):
            arr.append(int(data[i][j]))
        matrix.append(arr)

    #matrix = [
    #    [4, 4, 6, 5, 5, 1, 1, 1, 7, 4],
    #    [3, 6, 2, 4, 6, 5, 7, 2, 6, 6],
    #    [1, 3, 6, 1, 1, 1, 7, 1, 4, 5],
    #    [7, 5, 6, 3, 1, 3, 3, 1, 1, 7],
    #    [3, 4, 6, 4, 7, 2, 6, 5, 4, 4],
    #    [3, 2, 5, 1, 2, 5, 1, 2, 3, 4],
    #    [4, 2, 2, 2, 5, 2, 3, 7, 7, 3],
    #    [7, 2, 4, 3, 5, 2, 2, 3, 6, 3],
    #    [5, 1, 4, 2, 6, 4, 6, 7, 3, 7],
    #    [1, 4, 1, 7, 5, 3, 6, 5, 3, 4]
    #]
    N = len(matrix)
    M = len(matrix[0])

    tiles = 5 #Change the number of times here, keept this to 1 for part 1
    find_path(N,M,tiles)
    print(cost[N*tiles-1,M*tiles-1])

if __name__ == "__main__":
    main()