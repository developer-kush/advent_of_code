import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')

#-----------------------------------------------------------------------

U, R, D, L = 'urdl'
up = lambda x,y: (x-1,y, U)
right = lambda x,y: (x,y+1, R)
down = lambda x,y: (x+1,y, D)
left = lambda x,y: (x,y-1, L)
mapping = {L: left, R: right, U: up, D: down}

from heapq import heappush, heappop

def findMinCost(grid):

    start = (0, 0, 0, U, 0)
    q = [start]

    visited = set()

    while q:
        cost, x, y, dir, turncount = heappop(q)
        if (x, y, dir, turncount) in visited: continue
        visited.add((x, y, dir, turncount))

        if x == n-1 and y == n-1: return cost
        
        positions = []
        if turncount < 2: positions.append(mapping[dir](x,y))
        if dir in (U,D): positions.append(mapping[L](x,y)); positions.append(mapping[R](x,y))
        if dir in (L,R): positions.append(mapping[U](x,y)); positions.append(mapping[D](x,y))

        for ne_x, ne_y, ne_dir in positions:
            if ne_x<0 or ne_x>=n or ne_y<0 or ne_y>=n : continue
            if ne_dir == dir: heappush(q, (cost+grid[x][y], ne_x, ne_y, ne_dir, turncount+1))
            else: heappush(q, (cost+grid[x][y], ne_x, ne_y, ne_dir, 0))

def ultraCrucible(grid):

    q = [(0, 0, 0, R, 0), (0, 0, 0, D, 0)]

    visited = set()
    while q:
        cost, x, y, dir, turncount = heappop(q)
        if (x, y, dir, turncount) in visited: continue
        visited.add((x, y, dir, turncount))

        if x == n-1 and y == n-1 and turncount >= 3: return cost
        
        positions = []
        if turncount < 9: 
            positions.append(mapping[dir](x,y)); 
            
        if turncount >= 3: 
            if dir in (U,D): positions.append(mapping[L](x,y)); positions.append(mapping[R](x,y))
            if dir in (L,R): positions.append(mapping[U](x,y)); positions.append(mapping[D](x,y))

        for ne_x, ne_y, ne_dir in positions:
            if ne_x<0 or ne_x>=n or ne_y<0 or ne_y>=n : continue
            if ne_dir == dir: heappush(q, (cost+grid[x][y], ne_x, ne_y, ne_dir, turncount+1))
            else: heappush(q, (cost+grid[x][y], ne_x, ne_y, ne_dir, 0))

n = 141
grid = [list(map(int, list(input()))) for _ in range(n)]

# Answer Part 1
res = findMinCost(grid)
print("Answer Part 1:", res)

# Answer Part 2
res = ultraCrucible(grid)
print("Answer Part 1:", res)

#-----------------------------------------------------------------------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')