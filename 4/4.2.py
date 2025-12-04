import numpy as np

with open('input', 'r') as file:
    grid = np.array([ [ int(ch == '@') for ch in line ] for line in file.read().split('\n') if len(line) > 0 ], dtype=np.byte)


cols, rows = grid.shape

def get_accessible_rolls() -> list[tuple[int, int]]:
    accessible_rolls = []
    for col in range(cols):
        for row in range(rows):
            if grid[row,col] == 0:
                continue
            mincol = max(0, col - 1)
            maxcol = min(cols, col + 2)
            minrow = max(0, row - 1)
            maxrow = min(rows, row + 2)
            if np.sum(grid[minrow:maxrow,mincol:maxcol]) - 1 < 4:
                accessible_rolls.append((row, col))
    return accessible_rolls


removable_rolls_count = 0

removable_rolls = get_accessible_rolls()
while len(removable_rolls) > 0:
    removable_rolls_count += len(removable_rolls)
    for row, col in removable_rolls:
        grid[row,col] = 0
    removable_rolls = get_accessible_rolls()

print(removable_rolls_count)
