import numpy as np
import re
print ("Welcome to Python Puzzle 2, 2020")

PW_REGEX = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

matrix = []
array = []
low_points = []

WIDTH = 1000
DEPTH = 1000
def create_array(ROWS, COLS):
    global matrix
    for i in range(COLS):
        array.append(0)
    for j in range(ROWS):
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
    #print(count)

def part1(matrix, ROWS, COLS):
    count = 0
    global low_points
    for i in range(ROWS):
        for j in range(COLS):
            if i > 0:
                up = matrix[i-1][j]
            else:
                up = 99
            if j > 0:
                left = matrix[i][j-1]
            else:
                left = 99
            if i == ROWS-1:
                down = 99
            else:
                down = matrix[i+1][j]
            if j == COLS-1:
                right = 99
            else:
                right = matrix[i][j+1]
            if (matrix[i][j] < up and matrix[i][j] < down and matrix[i][j] < right and matrix[i][j]< left):
                low_points.append((i,j))
                count = count + matrix[i][j]  + 1
    return count

def part2(matrix, low_points, ROWS, COLS):
    #np array to store the basins
    #Result for the example would look as below
    #Each basin represnted by an id
    #[1 1 0 0 0 2 2 2 2 2] 
    #[1 0 3 3 3 0 2 0 2 2] 
    #[0 3 3 3 3 3 0 4 0 2] 
    #[3 3 3 3 3 0 4 4 4 0] 
    #[0 3 0 0 0 4 4 4 4 4] 
    
    ids = np.zeros((ROWS,COLS),dtype=int)
    cur_id = 1
    #print(low_points) These were already identfied in part1
    #every low_point has a basin
    for row, col in low_points:
        #create a stack and a set to keep track of visited earlier
        stack = [(row,col)]
        visited = set()
        while (len(stack) > 0):
            row, col = stack.pop()
            if (row, col) in visited:
                continue
            visited.add((row,col))
            #unique id to group the basins (basin0, basin2, basin2 etc)
            ids[row,col] = cur_id 

            #Add the adjacent positions(max of 4) to stack on two conditions 
            #1. not equal to 9
            #2. not already present in stack
            #Also take care of the borders (up, down, left, right)

            #up
            if row > 0:
                if matrix[row-1][col] < 9:
                    stack.append((row-1,col))
            #left
            if col > 0:
                if matrix[row][col-1] < 9:
                    stack.append((row,col-1))
            #down
            if row < ROWS-1:
                if matrix[row+1][col] < 9:
                    stack.append((row+1,col))
            #right
            if col < COLS-1:
                if matrix[row][col+1] < 9:
                    stack.append((row,col+1))
        #once stack becomes empty search for next basin
        cur_id += 1
    #print(ids)

    sizes = [0] * cur_id
    for i in ids.flatten():
        if (i > 0): #do not count 0s
            sizes[i] = sizes[i] + 1
    sizes.sort()
    #print(sizes)
    #Return multiplication of last 3
    return sizes[-1] * sizes[-2] * sizes[-3]

def main():
    #with open("advc3.txt", "rb") as fin:
    with open("advc9_ex.txt") as fin:
        data = [i.strip() for i in fin]
    
    #Convert the data into a matrix
    ROWS = len(data)
    COLS = len(data[0])
    create_array(ROWS, COLS)
    for i in range(len(data)):
        for j in range(len(data[0])):
            matrix[i][j] = int(data[i][j])
    #print(matrix)


    print(part1(matrix, ROWS, COLS))
    #print(len(low_points))
    print(part2(matrix,low_points, ROWS, COLS))

if __name__ == "__main__":
    main()