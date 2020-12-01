with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [int(n) for n in lines]
# O2 complexity
looking_for = 2020
for i in range(len(lines) - 1):
    for j in range(i + 1, len(lines)):
        if lines[i] + lines[j] == looking_for:
            print(f'Two numbers multiplied: {lines[i] * lines[j]}')

# O3 complexity (trading cpu time for developer time, can be done better if we sort)
for i in range(len(lines) - 2):
    for j in range(i + 1, len(lines) - 1):
        for k in range(j + 1, len(lines)):
            if lines[i] + lines[j] + lines[k] == looking_for:
                print(f'Three numbers multiplied: {lines[i] * lines[j] * lines[k]}')

