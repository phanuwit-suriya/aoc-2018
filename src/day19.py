from pprint import pprint


operations = {
    'addr': lambda a, b: regs[a] + regs[b],
    'addi': lambda a, b: regs[a] + b,
    'mulr': lambda a, b: regs[a] * regs[b],
    'muli': lambda a, b: regs[a] * b,
    'banr': lambda a, b: regs[a] & regs[b],
    'bani': lambda a, b: regs[a] & b,
    'borr': lambda a, b: regs[a] | regs[b],
    'bori': lambda a, b: regs[a] | b,
    'setr': lambda a, b: regs[a],
    'seti': lambda a, b: a,
    'gtir': lambda a, b: int(a > regs[b]),
    'gtri': lambda a, b: int(regs[a] > b),
    'gtrr': lambda a, b: int(regs[a] > regs[b]),
    'eqir': lambda a, b: int(a == regs[b]),
    'eqri': lambda a, b: int(regs[a] == b),
    'eqrr': lambda a, b: int(regs[a] == regs[b])
}


with open('./input/day19.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    init_ip = int(lines[0].split()[1])
    lines = lines[1:]
    instructions = [v.split() for v in lines]

    regs = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    ip = regs[init_ip]

    while ip < len(instructions):
        regs[init_ip] = ip
        instruction, A, B, C = instructions[ip]
        regs[int(C)] = operations[instruction](int(A), int(B))
        ip = regs[init_ip]
        ip += 1
    print(regs)
