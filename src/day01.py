import time


def load_data():
    with open('./input/day01.txt', 'r') as f:
        return [int(line) for line in f.read().strip().split('\n')]


def part_one(data):
    return sum(data)


def part_two(data):
    res_freq = 0
    res_set = set()
    while True:
        for freq in data:
            res_freq += freq
            if res_freq in res_set:
                return res_freq
            res_set.add(res_freq)


if __name__ == '__main__':
    data = load_data()
    print(part_one(data))
    print(part_two(data))
