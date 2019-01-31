from collections import defaultdict, deque

with open('./input/day09.txt', 'r') as line:
    parts = line.read().split()
    max_players, last_marble = int(parts[0]), int(parts[6])
    players = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble * 100 + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            players[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

        if marble == last_marble:
            print(f"Part one: {max(players.values()) if players else 0}")
    print(f"Part two: {max(players.values()) if players else 0}")
