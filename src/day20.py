import networkx as nx


with open('./input/day20.txt', 'r') as f:
    path = f.read().strip()[1:-1]
    grid = nx.Graph()
    pos = {0}
    stack = []
    starts, ends = {0}, set()

    for dir in path:
        if dir in 'NESW':
            # move in a given direction: add all edges and update our current positions
            direction = {'N': 1, 'E': 1j, 'S': -1, 'W': -1j}[dir]
            grid.add_edges_from((p, p + direction) for p in pos)
            pos = {p + direction for p in pos}
        elif dir == '(':
            # start of groupp: add current positions as start of a new group
            stack.append((starts, ends))
            starts, ends = pos, set()
        elif dir == '|':
            # an alternate: update possible ending points, and restart the group
            ends.update(pos)
            pos = starts
        elif dir == ')':
            # end of group: finish current group, add current positions as possible ensd
            pos.update(ends)
            starts, ends = stack.pop()

# find the shortest path lengths from the starting room to all other rooms
lengths = nx.algorithms.shortest_path_length(grid, 0)

print(max(lengths.values()))
print(sum(1 for length in lengths.values() if length >= 1000))
