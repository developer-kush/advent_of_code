import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

from collections import defaultdict

n = m = 50
grouped_positions = defaultdict(list)

mat = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if mat[i][j] != '.': grouped_positions[mat[i][j]].append((i, j))

# Part 1

antinodes = set()

for k, v in grouped_positions.items():
    if len(v) <= 1: continue
    for i in range(1,len(v)):
        for j in range(i):
            ax, ay = v[i]
            bx, by = v[j]

            dx, dy = ax-bx, ay-by
            
            for nx, ny in [(ax+dx, ay+dy), (bx-dx, by-dy)]:
                if not (0 <= nx < n and 0 <= ny < m): continue
                antinodes.add((nx, ny))

print("Part 1:", len(antinodes))

# Part 2

antinodes = set()
for k, v in grouped_positions.items():
    if len(v) <= 1: continue
    for node in v: antinodes.add(node)
    for i in range(1,len(v)):
        for j in range(i):
            ax, ay = v[i]
            bx, by = v[j]

            dx, dy = ax-bx, ay-by

            nx, ny = ax+dx, ay+dy
            while 0 <= nx < n and 0 <= ny < m:
                antinodes.add((nx, ny))
                nx, ny = nx+dx, ny+dy
            
            nx, ny = bx-dx, by-dy
            while 0 <= nx < n and 0 <= ny < m:
                antinodes.add((nx, ny))
                nx, ny = nx-dx, ny-dy

print("Part 2:", len(antinodes))


#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')