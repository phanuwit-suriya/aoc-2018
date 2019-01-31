import time


def load_data():
    with open('./input/day02.txt', 'r') as f:
        return [line for line in f.read().strip().split('\n')]


def counter(id):
    return {char: id.count(char) for char in 'abcdefghijklmnopqrstuvwxyz'}


def part_one(data):
    two = 0
    three = 0
    for id in data:
        id = counter(id)
        # id = dict(Counter(id))
        if {k: v for k, v in id.items() if v == 2}:
            two += 1
        if {k: v for k, v in id.items() if v == 3}:
            three += 1
    return two * three


def part_two(data):
    for count, first in enumerate(data, start=1):
        for second in data[count:]:
            match = ''
            score = 0
            for c_first, c_second in zip(first, second):
                if c_first == c_second:
                    match += c_first
                    score += 1
                    if score == len(first) - 1:
                        return match


if __name__ == '__main__':
    data = load_data()
    print(part_one(data))
    print(part_two(data))
