"""
Convert input into a 2D grid of chars (list of lists).
Iterate through all positions and check each '@' cell if it accessible or not and update count.
"""
input_file = 'adventofcode.com_2025_day_4_input.txt'
with open(input_file,'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

count = 0
offsets = [[-1,0],[1,0],[0,-1],[0,1],[-1,1],[1,1],[-1,-1],[1,-1]]  # up, down, left, right, diagonal left up, diagonal right up, diagonal left down, diagonal right down
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        neighbour_paper_count = 0
        if c == '@':
            for offset in offsets:
                ni, nj = i + offset[0], j + offset[1]
                if 0 <= ni < len(lines) and 0 <= nj < len(line):
                    if lines[ni][nj] == '@':
                        neighbour_paper_count += 1
            if neighbour_paper_count < 4:
                count += 1

print(count) 
            
            