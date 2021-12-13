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

#use np.hsplit and np.vsplit to slit the array
#while splitting array has to be split into equal halves. if array is not being split into equal halves,
#pad the array so that split can happen. The padding will be ignored later on since the pads wont have any #
#use np.flip to flip the array vertically or horizontally as needed
#Then add locally defined function to add the matrices to create the transparency overlap
def fold_horizontal(y):
    global matrix
    matrix = np.array(matrix)

    l = len(matrix)
    extra = (y)*2+1 - l #Check if padding is needed
    r = ['.' for i in range(len(matrix[0]))]
    if extra > 0:
        for i in range(extra):
            matrix = np.vstack([matrix,r])

    #Delete the row or column where the split happens
    matrix = np.delete(matrix, y, 0)
    matrices = np.vsplit(matrix, 2)

    matrices[0] = np.array(matrices[0])
    matrices[1] = np.array(matrices[1])

    matrices[1] = np.flip(matrices[1],0)

    matrix = add_matrices(matrices[0], matrices[1])
    return

def fold_vertical(x):
    global matrix
    matrix = np.array(matrix)

    l = len(matrix[0])
    extra = (x)*2+1 - l
    if (extra > 0):
        matrix = np.c_[matrix, np.ones(len(matrix))]

    #Delete the row or column where the split happens
    matrix = np.delete(matrix, x, 1)
    matrices = np.hsplit(matrix, 2)

    matrices[0] = np.array(matrices[0])
    matrices[1] = np.array(matrices[1])

    matrices[1] = np.flip(matrices[1],1)

    matrix = add_matrices(matrices[0], matrices[1])
    return

def add_matrices(mat1, mat2):
    global matrix
    mat = mat1.copy()
    count = 0
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            if mat1[i][j] == '#' or mat2[i][j] == '#':
                mat[i][j] = '#'
                count = count + 1
            else:
                mat[i][j] = '.'
    return mat

def main():
    global matrix
    data = read_file("advc13.txt")
    for i in data:
        if (i == ''):
            continue
        if (i.startswith('fold')):
            instructions.append(i)
        else:
            coords.append(i)

    COLS = 0
    ROWS = 0
    for i, field in enumerate(coords):
        (x,y) = field.split(',')
        coords[i] = (int(x), int(y))
        if (int(x) > COLS): COLS = int(x)
        if (int(y) > ROWS): ROWS = int(y)
    ROWS = ROWS + 1
    COLS = COLS + 1

    arr = ['.' for i in range(COLS)]
    matrix = [arr.copy() for i in range(ROWS)]

    for i, field in enumerate(coords):
        row = field[0]
        col = field[1]
        #matrix[col] = matrix[col][0:row] + '#' + matrix[col][row+1:]
        matrix[col][row] = '#'

    for i in instructions:
        cmd = i.split(' ')
        if len(cmd) == 3:
            dir,pos = cmd[2].split('=')
            #print(dir,pos)
            if (dir == 'y'):
                #print(cmd, " for matrix ", len(matrix), len(matrix[0]))
                fold_horizontal(int(pos))
            elif (dir == 'x'):
                #print(cmd, " for matrix ", len(matrix), len(matrix[0]))
                fold_vertical(int(pos))

    #Print the final matrix to reveal the answer
    for i in range(len(matrix)):
        string = ''
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#':
                string += '#'
            else:
                string += ' '
        print(string)

if __name__ == "__main__":
    main()