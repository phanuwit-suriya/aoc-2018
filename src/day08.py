from collections import deque


with open('./input/day08.txt', 'r') as data:
    data = [int(num) for num in data.read().strip('\n').split(' ')]

def parse_data(data):
    children, metadata = data[:2]
    data = data[2:]
    scores = []
    totals = 0
    for i in range(children):
        total, score, data = parse_data(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metadata])

    if children == 0:
        return (totals, sum(data[:metadata]), data[metadata:])
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metadata] if k > 0 and k <= len(scores)),
            data[metadata:]
        )

total, value, remaining = parse_data(data)
print(total, value)



