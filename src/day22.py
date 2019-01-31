import networkx as nx

with open('./input/day22.txt', 'r') as f:
    lines = [line for line in f.read().strip().split('\n')]
    depth = int(lines[0][7:])
    target = tuple(map(int, lines[1][8:].split(',')))
    depth = 510
    target = (10, 10)
    mx, my = target

grid = {}
for x in range(mx + 6):
    for y in range(my + 6):
        if (x, y) == (0, 0) or (x, y) == target:
            grid[(x, y)] = depth % 20183
        elif x == 0 or y == 0:
            grid[(x, y)] = ((y * 48271) + depth) % 20183 if x == 0 else ((x * 16807) + depth) % 20183
        else:
            grid[(x, y)] = ((grid[(x, y-1)] * grid[(x-1, y)]) + depth) % 20183

ngrid = {}
for x in range(mx + 6):
    for y in range(my + 6):
        ngrid[(x, y)] = {0: 0, 1: 1, 2: 2}[grid[(x, y)] % 3]

total = sum(ngrid[(i, j)] for i in range(mx + 1) for j in range(my + 1))
print(total)


def dijkstra(grid):
    G = nx.Graph()
    for x, y in grid.keys():
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                X, Y = x + dx, y + dy
                if 0 <= X < my + 6 and 0 <= Y < mx + 6:
                    if grid[(X, Y)] == grid[(x, y)]:
                        G.add_edge((X, Y), (x, y), weight=1)
                    else:
                        G.add_edge((X, Y), (x, y), weight=7)
    print(nx.dijkstra_path_length(G, (0, 0), (10, 10)))
    print(nx.dijkstra_path(G, (0, 0), (10, 10)))
    print(' A')


equipment = {0: ['climbing_gear', 'torch'], 1: ['climbing_gear', 'neither'], 2: ['torch', 'neither']}

dijkstra(ngrid)


            















# for y in range(my + 6):
#     for x in range(mx + 6):
#         if (x, y) == target:
#             print('T', end='')
#         else:
#             print(ngrid[(x, y)], end='')
#     print()