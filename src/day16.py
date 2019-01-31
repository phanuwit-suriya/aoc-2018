operations = [
    lambda a, b: regs[a] + regs[b],       # addr  0
    lambda a, b: regs[a] + b,             # addi  1
    lambda a, b: regs[a] * regs[b],       # mulr  2
    lambda a, b: regs[a] * b,             # muli  3
    lambda a, b: regs[a] & regs[b],       # banr  4
    lambda a, b: regs[a] & b,             # bani  5
    lambda a, b: regs[a] | regs[b],       # borr  6
    lambda a, b: regs[a] | b,             # bori  7
    lambda a, b: regs[a],                 # setr  8
    lambda a, b: a,                       # seti  9
    lambda a, b: int(a > regs[b]),        # gtir 10
    lambda a, b: int(regs[a] > b),        # gtri 11
    lambda a, b: int(regs[a] > regs[b]),  # gtrr 12
    lambda a, b: int(a == regs[b]),       # eqir 13
    lambda a, b: int(regs[a] == b),       # eqri 14
    lambda a, b: int(regs[a] == regs[b])  # eqrr 15
]

count = 0
opcodes = {k: set(list(range(16))) for k in range(16)}

with open('./input/day16.txt', 'r') as f:
    lines = f.read().split('\n')

for i in range(0, len(lines), 4):
    if lines[i] == '' and lines[i+1] == '':
        break

    regs = {k: int(v) for k, v in enumerate(lines[i+0][9:-1].split(', '))}
    number, A, B, C = [int(num) for num in lines[i+1].split()]
    res_reg = {k: int(v) for k, v in enumerate(lines[i+2][9:-1].split(', '))}

    possible_opcodes = []
    for code, operation in enumerate(operations):
        if operation(A, B) == res_reg[C]:
            possible_opcodes.append(code)
    if len(possible_opcodes) >= 3:
        count += 1
    opcodes[number] = opcodes[number].intersection(set(possible_opcodes))

print(count)

while True:
    for k1, v1 in opcodes.items():
        if len(v1) == 1:
            for k2, v2 in opcodes.items():
                if k1 == k2:
                    continue
                opcodes[k2] = opcodes[k2] - opcodes[k1]
    if sum(len(v) for v in opcodes.values()) == 16:
        break

regs = {0: 0, 1: 0, 2: 0, 3: 0}
for j in range(i, len(lines)):
    if lines[j] == '':
        continue
    number, A, B, C = [int(num) for num in lines[j].split()]
    regs[C] = operations[list(opcodes[number])[0]](A, B)

print(regs[0])
