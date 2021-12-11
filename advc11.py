import numpy as np
import re
print ("Welcome to Python Puzzle 11, 2021")

PW_REGEX = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
ROW = 0
COLS = 0
matrix = []
count = 0

def flash(flashed, x, y):
    global count
    if flashed[x][y] == 0:
        if (matrix[x][y] == 9):
            matrix[x][y] = 0
            flashed[x][y] = 1
            count = count + 1
            update_neighbours(flashed, x,y)
        else:
            matrix[x][y] = matrix[x][y] + 1

def update_neighbours(flashed, x, y):
    global matrix
    global ROWS, COLS

    #has 8 neighbours
    #print("Updating neighbours of " + str(x) + " " + str(y))
    if (x > 0 and y > 0 and x < ROWS-1 and y < COLS-1):
            flash(flashed, x, y-1)
            flash(flashed, x, y+1)
            flash(flashed, x-1, y)
            flash(flashed, x-1, y+1)
            flash(flashed, x-1, y-1)
            flash(flashed, x+1, y)
            flash(flashed, x+1, y-1)
            flash(flashed, x+1, y+1)

    elif (x == 0 and y > 0 and y < COLS-1):
            flash(flashed, x, y-1)
            flash(flashed, x, y+1)
            flash(flashed, x+1, y)
            flash(flashed, x+1, y-1)
            flash(flashed, x+1, y+1)

    elif (x > 0 and y > 0 and x == ROWS-1 and y < COLS-1):
            flash(flashed, x, y-1)
            flash(flashed, x, y+1)
            flash(flashed, x-1, y)
            flash(flashed, x-1, y+1)
            flash(flashed, x-1, y-1)

    elif (x > 0 and y == 0 and x < ROWS-1 and y < COLS-1):
            flash(flashed, x, y+1)
            flash(flashed, x-1, y)
            flash(flashed, x-1, y+1)
            flash(flashed, x+1, y)
            flash(flashed, x+1, y+1)

    elif (x > 0 and y > 0 and x < ROWS-1 and y == COLS-1):
            flash(flashed, x, y-1)
            flash(flashed, x-1, y)
            flash(flashed, x-1, y-1)
            flash(flashed, x+1, y)
            flash(flashed, x+1, y-1)

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

def time_step(flashed):
    global ROWS, COLS
    global matrix
    for i in range(ROWS):
        for j in range(COLS):
            flash(flashed, i, j)

def main():
    global ROWS, COLS
    global matrix
    #with open("advc3.txt", "rb") as fin:
    with open("advc11_ex.txt") as fin:
        data = [i.strip() for i in fin]

    ROWS = len(data)
    COLS = len(data[0])
    flashed = np.zeros((ROWS, COLS), int)

    for i in range(ROWS):
        array = []
        for j in range(COLS):
            array.append(int(data[i][j]))
        matrix.append(array.copy())

    res = np.array(matrix)
    #print(res)

    #print(np.array(matrix))
    for t in range(1000):
        flashed = np.zeros((ROWS, COLS), int)
        time_step(flashed)
        if (t == 99):
            print("Count after 100 steps = " + str(count))
        if (np.sum(flashed) == ROWS * COLS):
            print("All flash at " + str(t+1))
            break

    
if __name__ == "__main__":
    main()