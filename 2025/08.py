import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = 1000
k = 1000

nodes = [list(map(int, input().split(','))) for _ in range(n)]

def dist(a, b):
    x, y, z = a
    x2, y2, z2 = b
    return ((x-x2)**2 + (y-y2)**2 + (z-z2)**2)**0.5

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.cost = [1]*n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        self.parent[pv] = pu
        self.cost[pu] += self.cost[pv]
        return True

dsu = DSU(n)

edges = []
for i in range(n):
    for j in range(i+1, n):
        d = dist(nodes[i], nodes[j])
        edges.append((d, i, j))

edges.sort()

cnt = n
for d, x, y in edges[:k]:
    if dsu.find(x) == dsu.find(y): continue
    dsu.union(x, y)
    cnt -= 1
    
pars = set(dsu.find(i) for i in range(n))
costs = [dsu.cost[i] for i in pars if dsu.cost[i]]
costs.sort(reverse=True)

res = costs[0]*costs[1]*costs[2]
print("Part 1:", res)

for _, x, y in edges[k:]:
    if dsu.find(x) == dsu.find(y): continue
    if cnt - 1 == 1:
        print("Part 2:", nodes[x][0] * nodes[y][0])
        break
    dsu.union(x, y)
    cnt -= 1


#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')