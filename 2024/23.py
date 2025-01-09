import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()

# Author: Kushagra Agarwal < kushagra.agarwal.2709@gmail.com >
#-----------------------------------------------------------------------

from collections import defaultdict

n = 3380
# n = 32
edges = [input().split('-') for _ in range(n)]

# Part 1
graph = defaultdict(set)
for u, v in edges:
    graph[u].add(v)
    graph[v].add(u)

st = set()
for node in graph:
    nes = list(graph[node])
    for i in range(len(nes)):
        for j in range(i+1, len(nes)):
            if nes[i] in graph[nes[j]]:
                st.add(tuple(sorted([node, nes[i], nes[j]])))

print("Part 1:", len(st))

# Part 2

nodes = sorted(graph.keys(), key=lambda x: len(graph[x]))


for _ in range(14):
    ns = set()
    for node in nodes:
        for grp in st:
            grp = set(grp)
            if node in grp: continue
            if not any(ne not in graph[node] for ne in grp):
                ns.add(tuple(sorted(list(grp) + [node])))
    
    if ns == set(): break
    else: st = ns

for grp in st: print(','.join(sorted(grp)))
print("Part 2:", len(st))


#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')