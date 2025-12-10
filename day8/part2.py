from math import sqrt
from heapq import heappush, heappop

input_file = 'adventofcode.com_2025_day_8_input.txt'
positions = []
with open(input_file,'r') as f:
    for line in f:
        positions.append(tuple(int(val) for val in line.strip().split(',')))

def euclidean_distance(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

# Build min-heap of all pairs
heap = []
N = len(positions)
for i in range(N):
    for j in range(i+1, N):
        heappush(heap, (euclidean_distance(positions[i], positions[j]), (i, j)))

# DSU
parent = list(range(N))
size = [1] * N  # size instead of rank, since you want component sizes

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py:
        return 0 
    if size[py] > size[px]:
        px, py = py, px
    parent[py] = px
    size[px] += size[py]
    return 1

# Take up to 1000 smallest pairs
components = N
while heap:
    _, (a, b) = heappop(heap)
    merge = union(a,b)
    if merge:
        components -= 1
        if components == 1:
            print(positions[a][0]*positions[b][0])
            break 
