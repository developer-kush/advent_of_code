import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------

def are1afar(a, b):
    tot = 0
    for ra, rb in zip(a, b):
        tot += sum(x != y for x, y in zip(ra, rb))
    return tot == 1
    
def getMirror(grid):
    for i in range(1, len(grid)):
        a, b = grid[:i][::-1], grid[i:]
        n = min(len(a), len(b))
        a, b = a[:n], b[:n]
        if a == b: return 100*i
    grid = [''.join(x) for x in zip(*grid)]
    for i in range(1, len(grid)):
        a, b = grid[:i][::-1], grid[i:]
        n = min(len(a), len(b))
        a, b = a[:n], b[:n]
        if a == b: return i
    return 0

def fixSmudgeScore(grid):
    for i in range(1, len(grid)):
        a, b = grid[:i][::-1], grid[i:]
        n = min(len(a), len(b))
        a, b = a[:n], b[:n]
        if are1afar(a, b): return 100*i
    grid = [''.join(x) for x in zip(*grid)]

    for i in range(1, len(grid)):
        a, b = grid[:i][::-1], grid[i:]
        n = min(len(a), len(b))
        a, b = a[:n], b[:n]
        if are1afar(a, b): return i
    
    return 0

grids = []
grid = []
while True:
    try:
        curr = input()
        if curr == '': grids.append(grid); grid = []
        else: grid.append(curr)
    except EOFError: break
grids.append(grid)

# Answer Part 1
print("Answer Part 1:", sum([getMirror(grid) for grid in grids]))

# Answer Part 2
print("Answer Part 1:", sum([fixSmudgeScore(grid) for grid in grids]))

#-----------------------------------------------------------------------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')