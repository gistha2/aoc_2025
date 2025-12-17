from functools import reduce
import operator

def product(iterable):
    return reduce(operator.mul, iterable, 1)

input_file = 'adventofcode.com_2025_day_6_input.txt'

with open(input_file, 'r') as f:
    raw_lines = f.read().splitlines()

max_width = len(raw_lines[0])
grid = [line for line in raw_lines]
height = len(grid)

blocks = []
current_block_cols = []

for x in range(max_width):
    col_slice = [grid[y][x] for y in range(height)]
    
    if all(c == ' ' for c in col_slice):
        if current_block_cols:
            blocks.append(current_block_cols)
            current_block_cols = []
    else:
        current_block_cols.append(col_slice)

if current_block_cols:
    blocks.append(current_block_cols)

grand_total = 0

for block in blocks:
    numbers = []
    op = None
    
    for col in block:
        char_at_bottom = col[-1]
        if char_at_bottom in ('+', '*'):
            op = char_at_bottom
        
        digits = [c for c in col[:-1] if c.isdigit()]
        
        if digits:
            num = int("".join(digits))
            numbers.append(num)

    # Calculate
    if op == '+':
        grand_total += sum(numbers)
    elif op == '*':
        grand_total += product(numbers)

print(grand_total)