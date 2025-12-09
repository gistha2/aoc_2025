from functools import cache
input_file = 'adventofcode.com_2025_day_7_input.txt' 
#input_file = 'example.txt'
with open(input_file,'r') as f:
    diagram = []
    for line in f:
        diagram.append([c for c in line.strip()])

m = len(diagram)
n = len(diagram[0])
beams = set([])
@cache
def dfs(r,c):
    result = 0
    #Base case
    if r == m:
        return 1
    #Invalid cells
    if r<0 or c<0 or c>=n:
        return 0

    if diagram[r][c] == '^':
        #Split right
        result += dfs(r+1,c+1)
        #Split left
        result += dfs(r+1,c-1)
    else:
        #Continue straight down
        result += dfs(r+1,c)
    
    return result

S = []
for r in range(m):
    for c in range(n):
        if diagram[r][c] == 'S':
            S = [r,c]

print(dfs(S[0],S[1]))