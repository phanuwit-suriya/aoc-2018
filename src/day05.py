import time
from collections import deque


def load_data():
    with open('./input/day05.txt', 'r') as f:
        return deque(list(f.read().strip()))


def react(data):
    polymer = ['dummy']
    polymer.append(data.popleft())
    while len(data) != 0:
        temp = data.popleft()
        if polymer[-1].lower() == temp.lower():
            if (polymer[-1].isupper() and temp.islower()) or (polymer[-1].islower() and temp.isupper()):
                polymer.pop()
            else:
                polymer.append(temp)
        else:
            polymer.append(temp)
    return ''.join(polymer[1:])


def part_one(polymer):
    return len(polymer)


def part_two(polymer):
    shortest = len(polymer)
    for lc, uc in zip('abcdefghijklmnopqrstuvwxuz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        length = len(react(deque(list(polymer.replace(lc, '').replace(uc, '')))))
        if length < shortest:
            shortest = length
    return shortest


if __name__ == '__main__':
    data = load_data()
    polymer = react()
    print(part_one(polymer))
    print(part_two(polymer))
