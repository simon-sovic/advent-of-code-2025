import numpy as np

with open('input', 'r') as file:
    grid = np.array([ [ int(ch == '@') for ch in line ] for line in file.read().split('\n') if len(line) > 0 ], dtype=np.byte)


cols, rows = grid.shape
accessible_rolls = 0

for col in range(cols):
    for row in range(rows):
        if grid[row,col] == 0:
            continue
        mincol = max(0, col - 1)
        maxcol = min(cols, col + 2)
        minrow = max(0, row - 1)
        maxrow = min(rows, row + 2)
        accessible_rolls += int(np.sum(grid[minrow:maxrow,mincol:maxcol]) - 1 < 4)


print(accessible_rolls)
