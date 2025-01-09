import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------

from collections import deque
L, R, U, D = list('lrud')

def Countpath(grid, start = (0, 0, R)):

    visited = set([start])
    q = deque([start])
    
    up = lambda x,y: (x-1,y, U)
    right = lambda x,y: (x,y+1, R)
    down = lambda x,y: (x+1,y, D)
    left = lambda x,y: (x,y-1, L)

    mapping = {L: left, R: right, U: up, D: down}
    check = {
        L: lambda x, y: (y>0) and ((x, y-1, L) not in visited), 
        R: lambda x, y: (y+1<len(grid[0])) and ((x, y+1, R) not in visited), 
        U: lambda x, y: (x>0) and ((x-1, y, U) not in visited),
        D: lambda x, y: (x+1<len(grid)) and ((x+1, y, D) not in visited)
    }

    while q:
        x, y, dir = q.popleft()
        
        # if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]): continue
        
        if grid[x][y] == '.':
            if check[dir](x,y): q.append(mapping[dir](x,y)); visited.add(mapping[dir](x,y))

        if grid[x][y] == '|':
            if dir in (U,D) and check[dir](x,y): q.append(mapping[dir](x,y)); visited.add(mapping[dir](x,y))
            else:
                if check[U](x,y): q.append(mapping[U](x,y)); visited.add(mapping[U](x,y))
                if check[D](x,y): q.append(mapping[D](x,y)); visited.add(mapping[D](x,y))

        if grid[x][y] == '-':
            if dir in (L,R) and check[dir](x,y): q.append(mapping[dir](x,y)); visited.add(mapping[dir](x,y))
            else:
                if check[L](x,y): q.append(mapping[L](x,y)); visited.add(mapping[L](x,y))
                if check[R](x,y): q.append(mapping[R](x,y)); visited.add(mapping[R](x,y))

        if grid[x][y] == '/':
            dir = {L: D, R: U, U: R, D: L}[dir]
            if check[dir](x,y): q.append(mapping[dir](x,y)); visited.add(mapping[dir](x,y))
        if grid[x][y] == '\\':
            dir = {L: U, R: D, U: L, D: R}[dir]
            if check[dir](x,y): q.append(mapping[dir](x,y)); visited.add(mapping[dir](x,y))

    visited_cells = set((x,y) for x,y,_ in visited)

    # heatmap = [['.']*n for _ in range(n)]
    # for u, v in visited_cells:
    #     try: heatmap[u][v] = '#'
    #     except: pass
    # for row in heatmap: print(*row)

    return len(visited_cells)
        
n = 110
grid = [input() for _ in range(n)]

# Answer Part 1
print("Answer Part 1:", Countpath(grid))

# Answer Part 2
starts = []
for i in range(n):
    starts.append((i, 0, R))
    starts.append((i, len(grid[0])-1, L))
for j in range(len(grid[0])):
    starts.append((0, j, D))
    starts.append((n-1, j, U))
print("Answers Part 2:", max(Countpath(grid, start) for start in starts))

#-----------------------------------------------------------------------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')