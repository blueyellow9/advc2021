import numpy as np
import re
from collections import defaultdict
print ("Welcome to Python Puzzle 2, 2020")

#function to read input file
def read_file(filename):
    with open(filename) as fin:
        data = [i.strip() for i in fin]
    return data

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

    current_position = t
    if (current_position == "end"):
        #print("Path taken: " + path)
        count = count + 1
        return

    if current_position in paths.keys():
        for destination in paths[current_position]:
                if destination == "start":
                    visited[destination] = 1
                #for upper case big caves you can visit as many times as you want
                elif destination.isupper():
                    travel(path, current_position, destination, paths, visited.copy())
                #if any small cave as been visited twice, skip
                elif "smallcaves_twice" not in visited.keys():
                    travel(path, current_position, destination, paths, visited.copy())
                #if the small cave has not peen visited or been visited only once
                elif destination not in visited.keys():
                    travel(path, current_position, destination, paths, visited.copy())

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