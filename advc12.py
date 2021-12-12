import numpy as np
import re
from collections import defaultdict
print ("Welcome to Python Puzzle 2, 2020")

#Regular expressions that need to be matched
PW_REGEX = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

#Empty matrix
matrix = []

#function to read input file
def read_file(filename):
    with open(filename) as fin:
        data = [i.strip() for i in fin]
    return data

#initialize a WxD matrix with values 0
def create_matrix(matrix, WIDTH, DEPTH):
    array = []
    for i in range(WIDTH):
        array.append(0)
    for j in range(DEPTH):
        matrix.append(array.copy())

def get_adjcs(WIDTH, DEPTH, x, y, mode=0):
    adjs = []
    if (mode == 0):
        #horizontal vertical and diagonal
        adjs_list = [[0,-1], [0,1], [-1,-1], [-1,0], [-1,1], [1,-1], [1,0], [1,1]]
    else:
        #only horizontal and vertical
        adjs_list = [[0,-1], [0,1], [-1,0], [1,0]]
    for i in adjs_list:
        rr,cc = x+i[0], y+i[1]
        if (rr >= 0 and rr < DEPTH and cc >= 0 and cc < WIDTH):
            adjs.append([rr,cc])
    return adjs

count = 0

def travel(path, f, t, paths, visited):
    global count
    path = path + '-' + t
    if t.islower():
        if t in visited.keys():
            visited[t] = visited[t] + 1
            visited["smallcaves_twice"] = 1
        else:
            visited[t] = 1

    pos = t
    if (pos == "end"):
        #print("Path taken: " + path)
        count = count + 1
        return

    if pos in paths.keys():
        for item in paths[pos]:
                if item == "start":
                    visited[item] = 1
                #for upper case big caves you can visit as many times as you want
                elif item.isupper():
                    travel(path, pos, item, paths, visited.copy())
                #if any small cave as been visited twice, skip
                elif "smallcaves_twice" not in visited.keys():
                    travel(path, pos, item, paths, visited.copy())
                #if the small cave has not peen visited or been visited only once
                elif item not in visited.keys():
                    travel(path, pos, item, paths, visited.copy())

def main():
    paths = {}
    visited = {}
    data = read_file("advc12.txt")
    #print(data)
    for i in data:
        x = i.split('-')
        if x[0] not in paths.keys():
            paths[x[0]] = [x[1]]
        else: 
            paths[x[0]].append(x[1])

        if x[1] not in paths.keys():
            paths[x[1]] = [x[0]]
        else: 
            if x[0] not in paths[x[1]]:
                paths[x[1]].append(x[0])

    print(paths)

    for dest in paths["start"]: 
        travel("start", "start", dest, paths, visited.copy())
    print(count)

if __name__ == "__main__":
    main()