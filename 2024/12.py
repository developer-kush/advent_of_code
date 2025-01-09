import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = m = 140

from collections import Counter

rows = [input() for _ in range(n)]

# Part 1

marked = [[False]*m for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        if marked[i][j]: continue
        area = peri = 0

        queue = [(i, j)]
        marked[i][j] = True

        while queue:
            x, y = queue.pop()
            area += 1
            for u, v in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if (0 <= u < n and 0 <= v < m) and rows[u][v] == rows[i][j]:
                    if marked[u][v]: continue
                    marked[u][v] = True
                    queue.append((u, v))
                else: peri += 1
        
        res += area*peri        

print("Part 1:", res)

# Part 1

marked = [[False]*m for _ in range(n)]
res = 0
for p in range(n):
    for q in range(m):
        if marked[p][q]: continue
        area = 0
        perigrp = []
        queue = [(p, q)]
        marked[p][q] = True

        while queue:
            x, y = queue.pop()
            area += 1
            for md, u, v in [(0, x+1, y), (1, x-1, y), (2, x, y+1), (3, x, y-1)]:
                if (0 <= u < n and 0 <= v < m) and rows[u][v] == rows[p][q]:
                    if marked[u][v]: continue
                    marked[u][v] = True
                    queue.append((u, v))
                else:
                    perigrp.append((md, x, y))

        peri = 0
        grped = {md: [] for md in range(4)}
        for md, x, y in perigrp:
            grped[md].append((x, y))

        for md in grped:
            if md in (2, 3): mat = sorted([row[::-1] for row in grped[md]])
            else: mat = sorted(grped[md])
                
            peri += 1
            for i in range(1, len(mat)):
                if not (mat[i][0] == mat[i-1][0] and mat[i][1] == mat[i-1][1]+1): peri += 1

        res += area*peri

print("Part 2:", res)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')