input_file = 'adventofcode.com_2025_day_11_input'
example_file = 'example.txt'
connections = {}
with open(input_file,'r') as f:
    for line in f:
        parts = line.strip().split()
        source = parts[0].strip(':')
        connections[source] = parts[1:]

print(connections)

def dfs(node,graph):
    n_valid_paths = 0
    if node == 'out':
        return 1
    for neighbour in graph[node]:
        n_valid_paths += dfs(neighbour, graph)

    return n_valid_paths

ans = dfs('you',connections)
print(ans)