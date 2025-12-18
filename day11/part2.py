from functools import cache
input_file = 'adventofcode.com_2025_day_11_input'
example_file = 'example2.txt'
connections = {}
with open(input_file,'r') as f:
    for line in f:
        parts = line.strip().split()
        source = parts[0].strip(':')
        connections[source] = parts[1:]

graph = connections
@cache
def dfs(node,seen_dac, seen_fft):
    n_valid_paths = 0
    if node == 'out':
        if seen_dac and seen_fft:
            return 1
        else:
            return 0
    if node == 'dac':
        seen_dac = True 
    if node == 'fft':
        seen_fft = True
    for neighbour in graph[node]:
        n_valid_paths += dfs(neighbour, seen_dac, seen_fft)

    return n_valid_paths

source = 'svr'
ans = dfs(source,False,False)
print(ans)