import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

from collections import deque

cnt = 3450
n = m = 71

rows = [['.']*m for _ in range(n)]

byteBreaks = []
for i in range(cnt):
    x, y = map(int, input().split(','))
    byteBreaks.append((x, y))
    if i < 1024:
        rows[x][y] = '#'

q = deque([(0, 0, 0)])
dist = [[-1]*m for _ in range(n)]

while q:
    x, y, d = q.popleft()
    if dist[x][y] != -1: continue
    dist[x][y] = d
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and rows[nx][ny] != '#':
            q.append((nx, ny, d+1))

print("Part 1:", dist[n-1][m-1])


class DSU:
    def __init__(self, cnt):
        self.parent = list(range(cnt))
        self.rank = [0]*cnt
    
    def find(self, x):
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return True
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

    def conn(self, x, y): return self.find(x) == self.find(y)

    def printComponents(self):
        comps = {}
        for i in range(len(self.parent)):
            p = self.find(i)
            if p not in comps: comps[p] = []
            comps[p].append(i)
        return comps

def key(x, y): return x*m + y
def val(key): return divmod(key, m)

dsu = DSU(n*m)
map = [['.']*m for _ in range(n)]
for x, y in byteBreaks: map[x][y] = '#'

st = set(byteBreaks)

for i in range(n):
    for j in range(m):
        if (i, j) in st: continue
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i+dx, j+dy
            if 0 <= ni < n and 0 <= nj < m and not (ni, nj) in st:
                if (ni, nj) in st: continue
                dsu.union(key(i, j), key(ni, nj))

# for k, v in dsu.printComponents().items():
#     print(val(k), v)

# for row in map: print(*row)

for i in range(cnt-1, 0, -1):
    x, y = byteBreaks[i]
    st.remove((x, y))
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in st: dsu.union(key(x, y), key(nx, ny))
    if dsu.conn(0, n*m-1):
        print("Part 2:", f"{x},{y}")
        break



#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')