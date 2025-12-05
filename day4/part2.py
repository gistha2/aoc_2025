"""
Data Structures

grid: 2D list of chars
degree[i][j]: number of @ neighbors
queue (FIFO)
Phase 1: Precompute neighbor counts
    For every cell (i, j):

    If grid[i][j] == '@':

    Count neighbors and store in degree[i][j]

Phase 2: Initialize queue
    For every @:

    If degree[i][j] < 4, push into queue

Phase 3: BFS Removal Loop

    While queue not empty:

    Pop (i, j)

    If already removed, skip

    Remove it: grid[i][j] = '.'

    Increment total removed

    For each neighbor (ni, nj):

    If still @:

    degree[ni][nj] -= 1

    If degree[ni][nj] < 4:
    queue.append((ni,nj))
"""
input_file = 'adventofcode.com_2025_day_4_input.txt'
with open(input_file,'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

grid = [list(line) for line in lines]  # Convert each line to a list of chars for mutability
n,m = len(grid), len(grid[0])
degree = [[0]*m for _ in range(n)]
offsets = [[-1,0],[1,0],[0,-1],[0,1],[-1,1],[1,1],[-1,-1],[1,-1]]  # up, down, left, right, diagonal left up, diagonal right up, diagonal left down, diagonal right down
queue = [] 
for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            neighbour_paper_count = 0
            for offset in offsets:
                ni, nj = i + offset[0], j + offset[1]
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] == '@':
                        neighbour_paper_count += 1
            degree[i][j] = neighbour_paper_count

for i in range(n):
    for j in range(m):
        if grid[i][j] == '@' and degree[i][j] < 4:
            queue.append((i,j))

total_removed = 0
while queue:
    i,j = queue.pop(0)
    if grid[i][j] == 'x':
        continue
    grid[i][j] = 'x'
    total_removed += 1
    for offset in offsets:
        ni, nj = i + offset[0], j + offset[1]
        if 0 <= ni < n and 0 <= nj < m:
            if grid[ni][nj] == '@':
                degree[ni][nj] -= 1
                if degree[ni][nj] < 4:
                    queue.append((ni,nj))

print(total_removed)
        
