import numpy as np
import re
print ("Welcome to Python Puzzle 2, 2020")

PW_REGEX = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

matrix = []
array = []

WIDTH = 1000
DEPTH = 1000
for i in range(WIDTH):
    array.append(0)
for j in range(DEPTH):
    matrix.append(array.copy())

#print(matrix)

def part2(data):
    count = 0
    for line in data:
        match = PW_REGEX.search(line)
        assert match is not None

        a,b,c,d = match.groups()

        x1 = int(a)
        y1 = int(b)
        x2 = int(c)
        y2 = int(d)
        #print(str(x1) + " " + str(y1) + " " + " " + str(x2) + " " + str(y2))
        count = count + 1

        #There are four different types of lines that can be traced
        #Horizontal, vertical, 
        # upward slope to right, upward slope to left, 
        # downward slope to right, downward slope to left

        #Vertical line
        if (y1 == y2):
            if (x2 > x1):
               for l in range(x1,x2+1):
                   #print(str(x1) + " " + str(l))
                   matrix[y1][l] = matrix[y1][l] + 1
            else:
               for l in range(x2,x1+1):
                   #print(str(x1) + " " + str(l))
                   matrix[y1][l] = matrix[y1][l] + 1

        else:
            #Horizontal line
            if (x1 == x2):
                if (y2 > y1):
                    for l in range(y1,y2+1):
                        matrix[l][x1] = matrix[l][x1] + 1
                else:
                    for l in range(y2,y1+1):
                        matrix[l][x1] = matrix[l][x1] + 1
            else: 
                #Sloping upwards left to right
                if (x1 > x2 and y1 < y2):
                    matrix[y1][x1] = matrix[y1][x1] + 1
                    l = x1
                    m = y1
                    while (l > x2):
                       l = l-1
                       m = m+1
                       matrix[m][l] = matrix[m][l] + 1
                else:
                    #sloping downwards left to right
                    if (x1 < x2 and y1 < y2):
                        matrix[y1][x1] = matrix[y1][x1] + 1
                        l = x1
                        m = y1
                        while (l < x2):
                           l = l+1
                           m = m+1
                           matrix[m][l] = matrix[m][l] + 1
                    else:
                        #sloping upwards right to left
                        if (x1 > x2 and y1 > y2):
                            matrix[y1][x1] = matrix[y1][x1] + 1
                            l = x1
                            m = y1
                            while (l > x2):
                               l = l-1
                               m = m-1
                               matrix[m][l] = matrix[m][l] + 1
                        else:
                            #sloping downwards right to left
                            if (x1 < x2 and y1 > y2):
                                matrix[y1][x1] = matrix[y1][x1] + 1
                                l = x1
                                m = y1
                                while (l < x2):
                                   l = l+1
                                   m = m-1
                                   matrix[m][l] = matrix[m][l] + 1

    count = 0
    for i in range(DEPTH):
        for j in range(WIDTH):
            if (matrix[i][j] >= 2):
                count = count + 1
    #for i in range(DEPTH):
    #    print(matrix[i])
    print(count)

def main():
    #with open("advc3.txt", "rb") as fin:
    with open("advc5.txt") as fin:
        data = [i.strip() for i in fin]

    part2(data)

if __name__ == "__main__":
    main()