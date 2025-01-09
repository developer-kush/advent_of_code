import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')

#-----------------------------------------------------------------------


def countReachable(grid, start):
    tot = 0
    visited = set([(start[0], start[1])])
    queue = [start]

    while queue:
        x, y, rem = queue.pop(0)
        if rem%2 == 0: tot += 1
        if rem < 1: continue
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, rem-1))
    
    
    # tot = sum( (abs(start[0]-x)+abs(start[1]-y))%2==0 for x, y in visited)
    
    # for val in visited: print(val)

    return tot

n = 131
moves = 64
grid = [list(input()) for _ in range(n)]
start = [(i,j, moves) for i in range(n) for j in range(n) if grid[i][j] == 'S'][0]

# Answer Part 1
print("Answer Part 1:", countReachable(grid, start))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')