import re
from itertools import count
import time


def get_neighbors(grid, i, j):
    return [grid[i + dx][j + dy]
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            if 0 <= j + dy < len(grid[0])
            and 0 <= i + dx < len(grid)
            and not dx == dy == 0]


def open_ground(neighbors, n=3):
    return sum(1 for elem in neighbors if elem == '|') >= n


def trees(neighbors, n=3):
    return sum(1 for elem in neighbors if elem == '#') >= n


def lumberyard(neighbors):
    return open_ground(neighbors, 1) and trees(neighbors, 1)


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print()
    print()


start = time.time()

with open('./input/day18.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    grid = [list(line) for line in lines]
    mx, my = (len(grid), len(grid[0]))

snapshots = []
for t in count(1):
    new_grid = [[None for _ in range(mx)] for _ in range(my)]
    for x in range(mx):
        for y in range(my):
            neighbors = get_neighbors(grid, x, y)
            if grid[x][y] == '.':
                new_grid[x][y] = '|' if open_ground(neighbors) else grid[x][y]
            elif grid[x][y] == '|':
                new_grid[x][y] = '#' if trees(neighbors) else grid[x][y]
            elif grid[x][y] == '#':
                new_grid[x][y] = grid[x][y] if lumberyard(neighbors) else '.'
    grid = new_grid

    snapshot = '\n'.join(''.join(row) for row in grid)
    if snapshot in snapshots:
        i = snapshots.index(snapshot)
        print("Found %d as a repeat of %d" % (t, 1+i))
        period = t - (1+i)
        while (i+1) % period != 1000000000 % period:
            i += 1
        # print(snapshots[i])
        count1 = len(re.findall('[|]', snapshots[i]))
        count2 = len(re.findall('[#]', snapshots[i]))
        print((i+1, count1, count2))
        print(count1 * count2)
        break
    snapshots.append(snapshot)

    if t == 10:
        count1 = len(re.findall('[|]', snapshot))
        count2 = len(re.findall('[#]', snapshot))
        print((t, count1, count2))
        print(count1 * count2)

print(time.time() - start)
