from functools import reduce
import operator

def product(iterable):
    return reduce(operator.mul,iterable,1)

input_file = 'adventofcode.com_2025_day_6_input.txt'
with open(input_file,'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

n = len([c for c in lines[0].split()])
stacks = [[] for _ in range(n)]
for i, line in enumerate(lines):
    chars = line.split()
    for j, c in enumerate(chars):
        if c.isnumeric():
            stacks[j].append(int(c))
        else:
            stacks[j].append(c)

result = 0
for stack in stacks:
    if stack[-1] == '+':
        result += sum(stack[:len(stack)-1])
    elif stack[-1] == '*':
        result += product(stack[:len(stack)-1])

print(result)