import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = m = 15
threshold = 50
cheatsize = 20
grid = [list(input()) for _ in range(n)]

from collections import deque

sx, sy, tx, ty = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S': sx, sy = i, j
        if grid[i][j] == 'T': tx, ty = i, j

# Shortest Path
def bfs(sx, sy, tx, ty):
    q = deque([(sx, sy, 0)])
    visited = [[False]*m for _ in range(n)]
    visited[sx][sy] = True

    while q:
        x, y, d = q.popleft()
        grid[x][y] = d
        if x == tx and y == ty: return d
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                q.append((nx, ny, d+1))
    
    return d

shortest = bfs(sx, sy, tx, ty)
to_d = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '#': grid[i][j] = '.'; to_d[i][j] = '.'
        else: to_d[i][j] = shortest-grid[i][j]

tot = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        if sum(val=='.' for val in (grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1])) < 2: continue
        for frx, fry in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if grid[frx][fry] == '.': continue
            for tox, toy in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if grid[tox][toy] == '.': continue
                ndist = grid[frx][fry] + to_d[tox][toy]
                if shortest-ndist > threshold:
                    tot += 1

print("Part 1:",tot)

tot = 0
for frx in range(1, n-1):
    for fry in range(1, m-1):
        if grid[frx][fry] == '.': continue
        for tox in range(max(1, frx-cheatsize-1), min(n-1, frx+cheatsize+2)):
            for toy in range(max(1, fry-cheatsize-1), min(m-1, fry+cheatsize+2)):
                if grid[tox][toy] == '.': continue
                man_dist = abs(frx-tox) + abs(fry-toy)
                if man_dist > cheatsize: continue
                ndist = grid[frx][fry] + to_d[tox][toy] + man_dist-1

                if shortest-ndist > threshold: tot += 1

print("Part 2:",tot)

print("---------")
print("DEBUG")
for row in grid: 
    print(*[str(x).rjust(2) for x in row])
print("----")
for row in to_d: 
    print(*[str(x).rjust(2) for x in row])

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')