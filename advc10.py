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
            l = item[0]
            item = item[1:]
            if l in ['(','[','{','<']:
                arr.append(l)
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
        if (error == 0 and len(arr) > 0):
            completion = ''
            comp_points = 0
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
    print(points)
    print(comp[mid-1])

    
if __name__ == "__main__":
    main()