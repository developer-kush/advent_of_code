import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

from collections import defaultdict, deque

with open('_in.txt') as f:
    lines = f.readlines()

breakpoint = lines.index('\n')
conditions = [list(map(int, row[:-1].split('|'))) for row in lines[:breakpoint]]
rows = [list(map(int, row[:-1].split(','))) for row in lines[breakpoint+1:]]

def checkrow(row):
    numindices = {val:i for i, val in enumerate(row)}
    
    for a, b in conditions:
        if a not in numindices or b not in numindices: continue
        if numindices[a] > numindices[b]: return False
    return True

def fixrow(row):
    
    graph = defaultdict(list)
    indeg = defaultdict(int)
    st = set(row)

    for val in st: indeg[val] = 0

    for i, j in conditions:
        if i not in st or j not in st: continue
        graph[j].append(i)
        indeg[i] += 1
        
    starts = deque([i for i in st if indeg[i]==0])
    res = []
    
    while starts:
        node = starts.popleft()
        res.append(node)
        for child in graph[node]:
            indeg[child] -= 1
            if indeg[child] == 0:
                starts.append(child)
    
    return res

# Part 1
tot = 0
for row in rows:
    if checkrow(row):
        tot += row[len(row)//2]

print("Part 1:",tot)

# Part 2
tot = 0
for row in rows:
    if checkrow(row): continue
    rfix = fixrow(row)
    tot += rfix[len(rfix)//2]

print("Part 2:",tot)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')