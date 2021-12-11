import numpy as np
import re
import time
print ("Welcome to Python Puzzle 11, 2021")

PW_REGEX = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
ROW = 0
COLS = 0
matrix = []
count = 0

#flashed = current state of flashing
#x,y = coordinate
def flash(flashed, x, y):
    global count
    #if already flashed then nothing needs to be done for this step
    if flashed[x][y] == 0:
        #if any of the cells flashed update the neighbour cells
        if (matrix[x][y] == 9):
            matrix[x][y] = 0
            flashed[x][y] = 1
            #Keep track of flash count
            count = count + 1
            update_neighbours(flashed, x,y)
        #else just increment the value
        else:
            matrix[x][y] = matrix[x][y] + 1

#if any of the cells flashed update the neighbour cells
#Note: flash will call update_neighbours
#and update_neighbours will call flash to update the individual cells.
#This is inherently recursive, one calling the other
def update_neighbours(flashed, x, y):
    global matrix
    global ROWS, COLS
    #print("Updating neighbours of " + str(x) + " " + str(y))

    #Solve for internal cells, 4 edges and 4 corners

    #All internal cells have 8 neighbours
    if (x > 0 and y > 0 and x < ROWS-1 and y < COLS-1):
            flash(flashed, x, y-1)
            flash(flashed, x, y+1)
            flash(flashed, x-1, y)
            flash(flashed, x-1, y+1)
            flash(flashed, x-1, y-1)
            flash(flashed, x+1, y)
            flash(flashed, x+1, y-1)
            flash(flashed, x+1, y+1)

    #All edges excluding corners have five neighbours
    elif (x == 0 and y > 0 and y < COLS-1):
            flash(flashed, x, y-1)
            flash(flashed, x, y+1)
            flash(flashed, x+1, y)
            flash(flashed, x+1, y-1)
            flash(flashed, x+1, y+1)

    #5
    elif (x > 0 and y > 0 and x == ROWS-1 and y < COLS-1):
            flash(flashed, x, y-1)
            flash(flashed, x, y+1)
            flash(flashed, x-1, y)
            flash(flashed, x-1, y+1)
            flash(flashed, x-1, y-1)

    #5
    elif (x > 0 and y == 0 and x < ROWS-1 and y < COLS-1):
            flash(flashed, x, y+1)
            flash(flashed, x-1, y)
            flash(flashed, x-1, y+1)
            flash(flashed, x+1, y)
            flash(flashed, x+1, y+1)

    #5
    elif (x > 0 and y > 0 and x < ROWS-1 and y == COLS-1):
            flash(flashed, x, y-1)
            flash(flashed, x-1, y)
            flash(flashed, x-1, y-1)
            flash(flashed, x+1, y)
            flash(flashed, x+1, y-1)

    #all corners have only three neighbours
    elif (x == 0 and y == 0):
            flash(flashed, x, y+1)
            flash(flashed, x+1, y)
            flash(flashed, x+1, y+1)

    elif (x == 0 and y == COLS-1):
            flash(flashed, x, y-1)
            flash(flashed, x+1, y)
            flash(flashed, x+1, y-1)

    elif (y == 0 and x == ROWS-1):
            flash(flashed, x, y+1)
            flash(flashed, x-1, y)
            flash(flashed, x-1, y+1)

    elif (x == ROWS-1 and y == COLS-1):
            flash(flashed, x, y-1)
            flash(flashed, x-1, y)
            flash(flashed, x-1, y-1)

#a single step defined by the puzzle
def time_step(flashed):
    global ROWS, COLS
    global matrix
    for i in range(ROWS):
        for j in range(COLS):
            #Checking and incrementing every cells
            #Optionally incrementing the neighbouring cells if the current cell flashed
            #A flash is an overflow from 9 to 0
            flash(flashed, i, j)

def main():
    global ROWS, COLS
    global matrix
    start = time.time()
    #with open("advc3.txt", "rb") as fin:
    with open("advc11_ex.txt") as fin:
        data = [i.strip() for i in fin]

    ROWS = len(data)
    COLS = len(data[0])
    #Storing the current status of flashing when going through each element
    #Will be cleared at the start of each step
    flashed = np.zeros((ROWS, COLS), int)

    for i in range(ROWS):
        array = []
        for j in range(COLS):
            array.append(int(data[i][j]))
        matrix.append(array.copy())

    #print(np.array(matrix))
    for t in range(1000):
        flashed = np.zeros((ROWS, COLS), int)
        time_step(flashed)
        if (t == 99):
            print("Count after 100 steps = " + str(count))
        if (np.sum(flashed) == ROWS * COLS):
            print("All flash at " + str(t+1))
            break
    print("Time : " + str(time.time() -start))

    
if __name__ == "__main__":
    main()