def find(s, ch):
    return [i + 5 for i, ltr in enumerate(s) if ltr == ch]


with open('./input/day12.txt', 'r') as lines:
    parts = lines.read().strip().split('\n')
    initial_state = '.' * 3 + parts[0][15:] + '.' * 11
    rules = {condition[:5]: condition[-1] for condition in parts[2:]}

    print(f"00: {initial_state}")
    for g in range(20):
        next_state = ''
        for i in range(len(initial_state)):
            if initial_state[i-2:i+3] in rules.keys():
                next_state += rules[initial_state[i-2:i+3]]
            else:
                next_state += '.'
        initial_state =  next_state
        print(f"{g + 1:02d}: {initial_state}")
    print(sum(find(initial_state, '#')))
