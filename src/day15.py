from collections import deque
from itertools import count


# lines = open('./input/day15.txt', 'r').read()
# grid = [list(line) for line in lines.strip().split('\n')]
# grid = [
#     list("################################"),
#     list("#########...####################"),
#     list("#########...###########.########"),
#     list("#########G..##########....######"),
#     list("##########..###########...######"),
#     list("#########G...##########...######"),
#     list("#########..G.###########..######"),
#     list("########...#.##########..#######"),
#     list("#######G#..###E######....#######"),
#     list("#######G.....#.######....#######"),
#     list("######...G......##E......#######"),
#     list("####...##.#..G..G.........######"),
#     list("###..........G#####.......####.#"),
#     list("####........G#######...........#"),
#     list("####..G.....#########......#...#"),
#     list("###.........#########........###"),
#     list("##.....G.G..#########......#####"),
#     list("#...G.......#########.........##"),
#     list("#.G.........#########.E.##...###"),
#     list("##.....G.....#######....G#.E...#"),
#     list("##............#####...E.......##"),
#     list("#.G...........E.......#E...##.##"),
#     list("#....G........###########.....##"),
#     list("#......##...#.##################"),
#     list("#.#.........E..##.##############"),
#     list("#.#.......G.......##############"),
#     list("#.###........E....##############"),
#     list("#.####.....###....##############"),
#     list("#.#####......E..################"),
#     list("#######..........###############"),
#     list("#########..####.################"),
#     list("################################")
# ]
grid = [
    list("#######"),
    list("#E..G.#"),
    list("#...#.#"),
    list("#.G.#G#"),
    list("#######")
]

open_cavern = "."
wall = "#"


class Character:
    def __init__(self, role, target, position):
        self.hp = 200
        self.atk = 3
        self.role = role
        self.target = target
        self.position = position
        self.dead = False

    def bfs(self):
        queue = deque([[self.position]])
        seen = set([self.position])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if grid[x][y] == self.target:
                return path[1:-1]
            for x2, y2 in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if grid[x2][y2] != wall and grid[x2][y2] != self.role and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))

    def move(self, character):
        path = self.bfs()
        print(path)
        x, y = self.position
        if path:
            nx, ny = path[0]
            grid[x][y] = open_cavern
            grid[nx][ny] = self.role
            self.position = (nx, ny)
        self.attack(character)

    def attack(self, other):
        x, y = self.position
        targets = {}
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            for i, o in enumerate(other):
                if o.position == (x2, y2) and o.role == self.target and o.dead == False:
                    targets.update({i: o.hp})
        if targets:
            target = min(targets, key=targets.get)
            other[target].hp -= self.atk
            if other[target].hp <= 0:
                x3, y3 = other[target].position
                grid[x3][y3] = open_cavern
                other[target].dead = True


with open('./input/day15.txt', 'r') as lines:
    character = []
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            print(grid[x][y], end='')
        print()

    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char == 'G':
                character.append(Character(char, 'E', (x, y)))
            elif char == 'E':
                character.append(Character(char, 'G', (x, y)))

    for i in range(5):
        character.sort(key=lambda c: (c.position[0], c.position[1]))
        for char in character:
            if not char.dead:
                char.move(character)

        for x in range(len(grid)):
            characters = []
            for y in range(len(grid[0])):
                if grid[x][y] not in '#.':
                    for char in character:
                        if char.position == (x, y) and char.dead == False:
                            characters.append(f"{char.role}({char.hp})")
                print(grid[x][y], end='')
            print('\t\t', end='')
            for c in characters:
                print(c, end=', ')
            print()
        print()

        # if len(set([char.role for char in character if char.dead == False])) == 1:
        #     num = len(character)
        #     print(i)
        #     print(sum([char.hp for char in character if char.dead == False]))
        #     print(i * sum([char.hp for char in character if char.dead == False]))
        #     break
