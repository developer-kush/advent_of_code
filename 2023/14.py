import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------

def tilt_north_load(grid):
    tot = 0
    for j in range(len(grid[0])):
        lastpos = 0
        for i in range(n):
            if grid[i][j] == 'O': 
                tot += n - lastpos
                lastpos += 1
            elif grid[i][j] == '#': lastpos = i + 1
    return tot

def north_load(grid):
    return sum(row.count('O')*(n-i) for i, row in enumerate(grid))

def spin_grid(grid):
    for j in range(n):
        lastpos = 0
        for i in range(n):
            if grid[i][j] == 'O':
                grid[i][j], grid[lastpos][j] = grid[lastpos][j], grid[i][j]
                lastpos += 1
            elif grid[i][j] == '#': lastpos = i+1
    for i in range(n):
        lastpos = 0
        for j in range(n):
            if grid[i][j] == 'O':
                grid[i][j], grid[i][lastpos] = grid[i][lastpos], grid[i][j]
                lastpos += 1
            elif grid[i][j] == '#': lastpos = j+1
    for j in range(n):
        lastpos = n-1
        for i in range(n-1, -1, -1):
            if grid[i][j] == 'O':
                grid[i][j], grid[lastpos][j] = grid[lastpos][j], grid[i][j]
                lastpos -= 1
            elif grid[i][j] == '#': lastpos = i-1
    for i in range(n):
        lastpos = n-1
        for j in range(n-1,-1,-1):
            if grid[i][j] == 'O':
                grid[i][j], grid[i][lastpos] = grid[i][lastpos], grid[i][j]
                lastpos -= 1
            elif grid[i][j] == '#': lastpos = j-1
    return grid

def key(grid): return ''.join(''.join(row) for row in grid)

def spin_grid_n_times(spins, grid):
    seendict = {}

    for cnt in range(spins):
        if key(grid) in seendict: break
        seendict[key(grid)] = cnt
        grid = spin_grid(grid)
    else: return grid
    
    currkey = seendict[key(grid)]
    dist = cnt - currkey

    for k, v in seendict.items():
        if v == currkey+((spins-cnt)%dist): return [k[i*n:((i+1)*n)] for i in range(n)]
    return grid

n = 100
grid = [list(input()) for _ in range(n)]

# Answer Part 1
print("Answer Part 1: ", tilt_north_load(grid))

# Answer Part 2
grid = spin_grid_n_times(1000000000, grid)
print("Answer Part 2: ", north_load(grid))

#-----------------------------------------------------------------------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')