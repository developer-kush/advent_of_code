import sys, time
sys.stdin = open('_in.txt', 'r')
sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------

from collections import deque

def areNeighbors(a, b):
    (p, q), (x, y) = a, b
    if p == x:
        q, y = min(q, y), max(q, y)
        aval, bval = grid[p][q], grid[x][y] 
        if aval in 'S-FL': return bval in 'J7-'
        if bval in 'S-J7': return aval in 'LF-'
    if q == y: 
        p, x = min(p, x), max(p, x)
        aval, bval = grid[p][q], grid[x][y] 
        if aval in 'S|7F': return bval in 'J|L'
        if bval in 'S|': return aval in '7|F'
    return False

def cleanGrid(grid, start):
    res = [['*']*n for _ in range(n)]
    visited = set([start])
    q = deque([start])
    while q:
        x, y = q.popleft()
        res[x][y] = grid[x][y] 
        for ne in ((x+1, y), (x, y+1), (x-1,y), (x, y-1)):
            if ne[0] < 0 or ne[0] >= n or ne[1] < 0 or ne[1] >= n: continue
            if ne in visited: continue
            if not areNeighbors((x, y), ne): continue
            visited.add(ne)
            q.append(ne)

    x, y = start
    ne = []
    if x-1 >= 0 and grid[x-1][y] in '7F|': ne.append(1)
    if x+1 < n and grid[x+1][y] in 'JL|': ne.append(2)
    if y-1 >= 0 and grid[x][y-1] in 'LF-':  ne.append(3)
    if y+1 < n and grid[x][y-1] in 'J7-': ne.append(4)

    res[x][y] = {(1, 2): '|', (2, 3): '7', (3, 4): '-', (1, 3):'J', (1, 4):'L', (2, 4):'F'}[tuple(sorted(ne))]
    
    return res

def enclosedCount(grid):
    first =  {'L':'010', 'F':'000', 'J':'010', '7':'000', '|':'010', '-':'000', '*':'000', 'S': '111'}
    second = {'L':'011', 'F':'011', 'J':'110', '7':'110', '|':'010', '-':'111', '*':'000', 'S': '111'}
    third =  {'L':'000', 'F':'010', 'J':'000', '7':'010', '|':'010', '-':'000', '*':'000', 'S': '111'}

    for row in grid: print(''.join(row))

    newgrid = []
    for row in grid:
        curr = ""
        for col in row: curr += first[col]
        newgrid.append(curr.replace('1', '.')); curr = ""
        for col in row: curr += second[col]
        newgrid.append(curr.replace('1', '.')); curr = ""
        for col in row: curr += third[col]
        newgrid.append(curr.replace('1', '.'))

    for row in newgrid: print(row)
        
    grid = newgrid

    q = deque()
    for i in range(n): 
        if grid[i][0]=='0': q.append((i, 0)); 
        if grid[i][3*n-1]=='0': q.append((i, 3*n-1))
    for j in range(1, 3*n-2):
        if grid[0][j]=='0': q.append((0, j)); 
        if grid[3*n-1][j]=='0': q.append((3*n-1, j))
    visited = set()
    covered = set()
    while q: 
        x, y = q.popleft()
        visited.add((x,y))
        visited.add((x, y))
        covered.add((x//3, y//3))
        for ne in ((x+1, y), (x, y+1), (x-1,y), (x, y-1)):
            if ne[0] < 0 or ne[0] >= 3*n or ne[1] < 0 or ne[1] >= 3*n: continue
            if ne in visited: continue
            if newgrid[ne[0]][ne[1]]!='0': continue
            covered.add((ne[0]//3, ne[1]//3))
            q.append(ne)
            visited.add(ne)
    return n*n - len(covered)


n = 140
grid = [input() for _ in range(n)]
start = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 'S'][0]
grid = cleanGrid(grid, start)

# Part 1
res1 = sum(sum(char!='*' for char in row) for row in grid)
print("Answer Part 1:",res1>>1)

# Part 2
print("Answer Part 2:",enclosedCount(grid))

#-----------------------------------------------------------------------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')