import time

import numpy as np


def load_data():
    with open('./input/day03.txt', 'r') as f:
        table = str.maketrans(dict.fromkeys('#@,:x', ' '))
        data = [line.translate(table).split() for line in f.read().strip().split('\n')]
        data = [(d[0], int(d[1]), int(d[2]), int(d[3]), int(d[4])) for d in data]
        return data


def claimed_fabric(data):
    fabric = np.full((1000, 1000), '.', dtype=object)
    for claim in data:
        id, x, y, w, h = claim
        fabric[x:x+w, y:y+h] = np.where(fabric[x:x+w, y:y+h] == '.', str(id), 'X')
    return fabric


def part_one(fabric):
    return (fabric == 'X').sum()


def part_two(data, fabric):
    for claim in data:
        id, x, y, w, h = claim
        if ((fabric[x:x+w, y:y+h] == str(id))).all():
            return id


if __name__ == '__main__':
    data = load_data()
    fabric = claimed_fabric(data)
    print(part_one(fabric))
    print(part_two(data, fabric))
