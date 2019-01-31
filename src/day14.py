recipes = "554401"
scoreboard = "37"
elf1, elf2 = 0, 1
while recipes not in scoreboard[-10:]:
    elf1_score = int(scoreboard[elf1])
    elf2_score = int(scoreboard[elf2])
    scoreboard += str(elf1_score + elf2_score)
    elf1 = (elf1 + elf1_score + 1) % len(scoreboard)
    elf2 = (elf2 + elf2_score + 1) % len(scoreboard)
    if len(scoreboard) == int(recipes) + 10:
        print(scoreboard[int(recipes):int(recipes)+10])

print(scoreboard.index(recipes))