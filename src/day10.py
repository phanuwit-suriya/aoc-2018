import re
import time

import matplotlib.pyplot as plt
import numpy as np

with open('./input/day10.txt', 'r') as lines:
    points = [tuple(map(int, re.findall(r'-?\d+', line))) for line in lines]
    stop_criteria = 1000000
    i = 0

    while True:
        minx = min(x + i * vx for (x, _, vx, _) in points)
        maxx = max(x + i * vx for (x, _, vx, _) in points)
        miny = min(y + i * vy for (_, y, _, vy) in points)
        maxy = max(y + i * vy for (_, y, _, vy) in points)
        pos_x, pos_y = [], []
        if maxx - minx + maxy - miny > stop_criteria:
            for x, y, vx, vy in points:
                x = x + (i - 1) * vx
                y = y + (i - 1) * vy
                pos_x.append(x)
                pos_y.append(y)
            break
        stop_criteria = maxx - minx + maxy - miny
        i += 1
    plt.scatter(pos_x, pos_y, color='black')
    plt.gca().invert_yaxis()
    plt.show()
