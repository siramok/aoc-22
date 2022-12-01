calories_carried = []
with open('input.txt', 'r') as infile:
    temp = []
    for line in infile:
        if line == '\n':
            calories_carried.append(temp)
            temp = []
        else:
            temp.append(int(line))

elves = []
for calories in calories_carried:
    elves.append(sum(calories))

max_elves = []
for calories in reversed(sorted(elves)[-3:]):
    max_elves.append((elves.index(calories), calories))

total = 0
for elf in max_elves:
    print(f'Elf {elf[0] + 1} is holding {elf[1]} calories')
    total += elf[1]

print(f'The top three elves combined are carrying {total} calories')
