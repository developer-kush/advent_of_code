import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

from collections import deque

n = 496
points = [list(map(int, input().split(','))) for _ in range(n)]

res = 0
for x in range(n):
    for y in range(x+1, n):
        p, q = points[x]
        r, s = points[y]

        area = (abs(p-r)+1)*(abs(q-s)+1)
        res = max(res, area)

print("Part 1:", res)

# ===============================================

xs = sorted(set(x[0] for x in points))
ys = sorted(set(x[1] for x in points))

hmap = {x: i for i, x in enumerate(xs)}
wmap = {x: i for i, x in enumerate(ys)}
h, w = len(xs), len(ys)

grid = [['.']*w for _ in range(h)]
for x, y in points:
    grid[hmap[x]][wmap[y]] = '#'

def fillGrid(a, b):
    global grid, hmap, wmap
    ax, ay = hmap[a[0]], wmap[a[1]]
    bx, by = hmap[b[0]], wmap[b[1]]
    if ax == bx:
        mn, mx = min(ay, by), max(ay, by)
        for i in range(mn, mx+1):
            grid[ax][i] = '#'
    elif ay == by:
        mn, mx = min(ax, bx), max(ax, bx)
        for i in range(mn, mx+1):
            grid[i][ay] = '#'

def floodBorders():
    q = deque()
    vis = [[False]*w for _ in range(h)]

    def insert(x, y):
        if vis[x][y]: return
        if not (0 <= x < h and 0 <= y < w): return
        if grid[x][y] == '#': return
        grid[x][y] = ' '
        vis[x][y] = True
        q.append((x, y))

    for i in range(w): 
        insert(0, i)
        insert(h-1, i)

    for i in range(h):
        insert(i, 0)
        insert(i, w-1)

    while q:
        x, y = q.popleft()
        if grid[x][y] == '#': continue

        grid[x][y] = ' '

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] != '#':
                vis[nx][ny] = True
                grid[x][y] = ' '
                q.append((nx, ny))

def fillIn():
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.': grid[i][j] = '#'

for i in range(n):
    pa = points[i]
    pb = points[i-1]
    fillGrid(pa, pb)
floodBorders()
fillIn()

def safe(a, b):
    (ax, ay), (bx, by) = a, b
    (ax, ay), (bx, by) = (hmap[ax], wmap[ay]), (hmap[bx], wmap[by])

    ax, bx = min(ax, bx), max(ax, bx)
    ay, by = min(ay, by), max(ay, by)

    for i in range(ax, bx+1):
        for j in range(ay, by+1):
            if grid[i][j] != '#': return False
    return True

# for row in grid: print(''.join(row))

res = 0
for x in range(n):
    for y in range(x+1, n):
        if not safe(points[x], points[y]): continue

        p, q = points[x]
        r, s = points[y]
        area = (abs(p-r)+1)*(abs(q-s)+1)

        res = max(res, area)

print("Part 2:", res)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')