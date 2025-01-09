import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = m = 141
maze = [input() for _ in range(n)]

from heapq import *
from functools import lru_cache

# Part 1

sx, sy = None, None

for i in range(n):
    for j in range(m):
        if maze[i][j] == 'S': sx, sy = i, j; break
    if sx is not None: break

vis = set([])
q = [(0, sx, sy, 0)]

mncost = float('inf')
tx = ty = None

while q:
    while q and tuple(q[0][1:]) in vis: heappop(q)
    d, x, y, dir = heappop(q)
    vis.add((x, y, dir))

    if maze[x][y] == 'E':
        mncost = d
        tx, ty = x, y
        print("Part 1:", d)
        break

    for u, v, w in [(x+1, y, 1), (x-1, y, 3), (x, y+1, 0), (x, y-1, 2)]:
        if not (0 <= u < n and 0 <= v < m): continue
        if maze[u][v] == '#': continue
        if (u, v, w) in vis: continue

        if w != dir: heappush(q, (d+1000, x, y, w))
        if w == dir: heappush(q, (d+1, u, v, w))

# Part 2

import sys
sys.setrecursionlimit(50000)

sx, sy = None, None

for i in range(n):
    for j in range(m):
        if maze[i][j] == 'S': sx, sy = i, j; break
    if sx is not None: break

vis = set([])
q = [(0, sx, sy, 0)]

mncost = float('inf')
tx = ty = None
tilemincost = [[[float('inf')]*4 for _ in range(m)] for _ in range(n)]

cnt = 0

while q:
    cnt += 1
    
    while q and tuple(q[0][1:]) in vis: heappop(q)
    if not q: break

    d, x, y, dir = heappop(q)
    # print(d, x, y, dir)
    vis.add((x, y, dir))
    tilemincost[x][y][dir] = min(tilemincost[x][y][dir], d)

    if maze[x][y] == 'E': mncost = min(mncost, d)

    for u, v, w in [(x+1, y, 1), (x-1, y, 3), (x, y+1, 0), (x, y-1, 2)]:
        if not (0 <= u < n and 0 <= v < m): continue
        if maze[u][v] == '#': continue
        if (u, v, w) in vis: continue

        if w != dir: heappush(q, (d+1000, x, y, w))
        if w == dir: heappush(q, (d+1, u, v, w))

for i in range(n):
    for j in range(m):
        if maze[i][j] == '#':
            tilemincost[i][j] = [-1]*4


maze = [list(row) for row in maze]

@lru_cache(None)
def rec(x, y, dir, rem_cost):
    if not (0 <= x < n and 0 <= y < m): return False
    if maze[x][y] == '#': return False
    if rem_cost < mncost-tilemincost[x][y][dir]: return False
    if rem_cost < 0: return False

    if maze[x][y] == 'E': return True

    res = False

    for u, v, w in [(x+1, y, 1), (x-1, y, 3), (x, y+1, 0), (x, y-1, 2)]:
        if rec(u, v, w, rem_cost-(1 if dir==w else 1001)): res = True

    if res: maze[x][y] = '0'
    return res

rec(sx, sy, 0, mncost)

tot = 0
for i in range(n):
    for j in range(m):
        if maze[i][j] in 'E0': tot += 1

print("Part 2:", tot)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')