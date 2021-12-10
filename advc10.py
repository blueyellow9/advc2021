import numpy as np
import re
print ("Welcome to Python Puzzle 9, 2021")

PW_REGEX = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

def main():
    #with open("advc3.txt", "rb") as fin:
    with open("advc10.txt") as fin:
        data = [i.strip() for i in fin]
    points = 0
    comp = []
    for item in data:
        arr = []
        error = 0
        while (len(item)> 0 and error == 0):
            #Pop the first character from line
            l = item[0]
            item = item[1:]
            #if it is a open parantheses, push to array
            if l in ['(','[','{','<']:
                arr.append(l)
            #else if it is a closed parantheses pop an entry from array,
            #then compare that both paraentheses match (), [], {}, <>
            #if dont match flag error and exit after computing the points
            elif(l in [')', '}', ']', '>']):
                t = arr.pop()
                if l == ')':
                    if t in ['[', '{', '<']:
                        points = points + 3
                        error = 1
                if l == ']':
                    if t in ['(', '{', '<']:
                        points = points + 57
                        error = 1
                if l == '}':
                    if t in ['(', '[', '<']:
                        points = points + 1197
                        error = 1
                if l == '>':
                    if t in ['(', '[', '{']:
                        points = points + 25137
                        error = 1
        #if this point is reached without error flag the array should be 
        #either empty or an incomplete string
        if (error == 0 and len(arr) > 0):
            completion = ''
            comp_points = 0
            #for the incomplete string, for each entry from the end of string
            #compute the matching parantheses score
            for l in reversed(arr):
                if l == '(':
                    comp_points = comp_points*5 + 1
                if l == '[':
                    comp_points = comp_points*5 + 2
                if l == '{':
                    comp_points = comp_points*5 + 3
                if l == '<':
                    comp_points = comp_points*5 + 4
            comp.append(comp_points)
    comp.sort()
    mid = int((len(comp)+1)/2)
    #Solution to part1
    print(points)
    #Solution to part2
    print(comp[mid-1])

    
if __name__ == "__main__":
    main()