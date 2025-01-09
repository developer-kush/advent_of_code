import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------

from collections import Counter

def getInterstellarDistance(mat, expansion_rate = 0):
    rmap, cmap = [0]*n , [0]*n
    r = c = 0
    for idx, row in enumerate(mat):
        rmap[idx] = idx+r
        if '#' not in row: r += expansion_rate
    
    mat = [''.join(x) for x in zip(*mat)]
    for idx, row in enumerate(mat):
        cmap[idx] = idx+c
        if '#' not in row: c += expansion_rate
    mat = [''.join(x) for x in zip(*mat)]

    galaxies = []
    for i in range(n):
        for j in range(n):
            if mat[i][j] == '#': galaxies.append((rmap[i], cmap[j]))
    
    tot = 0
    for idx, (x, y) in enumerate(galaxies):
        for x2, y2 in galaxies[idx+1:]:
            tot += abs(x-x2) + abs(y-y2)
    return tot
        

n = 140
mat = [input() for _ in range(n)]

# Answer Part 1
print("Answer Part 1:", getInterstellarDistance(mat, expansion_rate=1))

# Answer Part 2
print("Answer Part 2:", getInterstellarDistance(mat, expansion_rate=999_999))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')