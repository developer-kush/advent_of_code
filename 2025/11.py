import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = 596
# n = 13

from collections import defaultdict, deque, Counter
from functools import lru_cache

graph = defaultdict(list)
for _ in range(n):
    node, edges = input().split(':')
    edges = edges.strip().split()
    graph[node] = edges

def paths(st, to, iga='', igb=''):
    vis = set()

    paths = Counter()
    paths[st] = 1
    q = deque([st])

    while q:
        node = q.popleft()

        if node in vis: continue
        vis.add(node)
        
        if node == to or node == iga or node == igb: continue

        nes = graph[node]
        for ne in nes:
            paths[ne] += paths[node]
            q.append(ne)
        paths[node] = 0
    return paths[to]

print("Part 1:", paths('you', 'out'))

# Part 2
st, end, ig1, ig2 = 'svr', 'out', 'fft', 'dac'

@lru_cache(None)
def rec(u, fig1, fig2):
    if u == end:
        return int(fig1 and fig2)

    if u == ig1: fig1 = True
    if u == ig2: fig2 = True

    return sum(rec(v, fig1, fig2) for v in graph[u])

print("Part 2:", rec(st, False, False))


#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')