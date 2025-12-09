"""
1. Parse the grid, find the column of the starting S.

This gives you the initial set:

active = {S_col}

2. For each row from top → bottom:

For each column c in active:

If grid[r][c] == '.':
→ beam continues downward at same column

If grid[r][c] == '^':
→ count ONE split
→ do NOT include c in next-row beams (beam stops)
→ add c-1 and c+1 to next-row beams if within bounds

3. Move to next row with updated active set.
4. Total number of splits = your answer.
"""

input_file = 'adventofcode.com_2025_day_7_input.txt' 
with open(input_file,'r') as f:
    diagram = []
    for line in f:
        diagram.append([c for c in line.strip()])

m = len(diagram)
n = len(diagram[0])
beams = set([])
splits = 0
for r in range(m):
    for c in range(n):
        if diagram[r][c] == 'S':
            beams.add((c))

for r in range(m):
    new_beams = set()
    for c in beams:
        if diagram[r][c] == '^':        
            splits += 1
            if c-1>=0:
                new_beams.add(c-1)
            if c+1<n:
                new_beams.add(c+1)
        else:
            new_beams.add(c)
    beams = new_beams
print(splits)