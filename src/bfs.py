from collections import deque

goal = 'E'
wall = '#'
grid = [
    list("#########"),
    list("#G......#"),
    list("#.......#"),
    list("#..#....#"),
    list("#..#E...#"),
    list("#.......#"),
    list("#.......#"),
    list("#.......#"),
    list("#########")
]
width = len(grid)
height = len(grid[0])

def bfs(grid, start):
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[x][y] == goal:
            return path[1:-1]
        for x2, y2 in ((x,y-1), (x,y+1), (x-1,y), (x+1,y)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[x2][y2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
x, y = 1, 1
while True:
    grid[x][y] = '.'
    path = bfs(grid, (x, y))
    if path == []:
        break
    x, y = path[0]
    grid[x][y] = 'G'
    for i in range(width):
        for j in range(height):
            print(grid[i][j], end='')
        print()
    
    
    