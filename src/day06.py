import time

import numpy as np


def load_data():
    with open('./input/day06.txt', 'r') as f:
        return np.asarray([tuple(list(map(int, line.split(',')))) for line in f.read().strip().split('\n')])


def manhattan_distance(a, b, c, d):
    return abs(a - c) + abs(b - d)


def part_one(data):
    max_x = data[:, 0].max()
    max_y = data[:, 1].max()
    grid = np.full((max_x, max_y), 0, dtype=int)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            distance = np.asarray([manhattan_distance(i, j, x, y) for x, y in data])
            grid[i][j] = np.where(distance == distance.min())[0] if len(np.where(distance == distance.min())[0]) == 1 else 50
    my_set = set(grid[0, :] + grid[max_x-1, :]).union(set(grid[:, 0] + grid[:, max_y-1]))
    my_list = list(set(list(range(0, 50))).difference(my_set))
    return max([(grid == num).sum() for num in my_list])


def part_two(data):
    max_x = data[:, 0].max()
    max_y = data[:, 1].max()
    grid = np.full((max_x, max_y), 0, dtype=int)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            distance = np.asarray([manhattan_distance(i, j, x, y) for x, y in data])
            grid[i][j] = sum(distance)
    return (grid < 10000).sum()


if __name__ == '__main__':
    data = load_data() 
    print(part_one(data))
    print(part_two(data))
