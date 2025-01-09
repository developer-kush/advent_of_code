import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n, m = 130, 130
mat = []
for _ in range(n):
    row = list(input())
    mat.append(row)

x, y, dir = None, None, None

lefts = [[-1]*m for _ in range(n)]
ups = [[-1]*m for _ in range(n)]
rights = [[m]*m for _ in range(n)]
downs = [[n]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if mat[i][j] in '^>v<':
            x, y = i, j
            dir = '^>v<'.index(mat[i][j])
        if mat[i][j] == '#': lefts[i][j], ups[i][j] = j, i
        else:
            if i: ups[i][j] = ups[i-1][j]
            if j: lefts[i][j] = lefts[i][j-1]

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if mat[i][j] == '#': rights[i][j], downs[i][j] = j, i
        else:
            if i < n-1: downs[i][j] = downs[i+1][j]
            if j < m-1: rights[i][j] = rights[i][j+1]

# Part 1

xmain, ymain, dirmain = x, y, dir

tot = 0
resmat = [['.']*m for _ in range(n)]
resmat[x][y] = 'X'
while True:
    # print(x, y, dir)
    if dir == 0:
        tidx = ups[x][y]
        for i in range(x, tidx, -1): resmat[i][y] = 'X'
        if tidx == -1: break
        x = tidx + 1
    if dir == 1:
        tidx = rights[x][y]
        for j in range(y, tidx): resmat[x][j] = 'X'
        if tidx == m: break
        y = tidx - 1
    if dir == 2:
        tidx = downs[x][y]
        for i in range(x, tidx): resmat[i][y] = 'X'
        if tidx == n: break
        x = tidx - 1
    if dir == 3:
        tidx = lefts[x][y]
        for j in range(y, tidx, -1): resmat[x][j] = 'X'
        if tidx == -1: break
        y = tidx + 1

    dir = (dir+1)%4

tot = sum(''.join(row).count('X') for row in resmat)
print("Part 1:",tot)

# Part 2

from bisect import insort, bisect_left, bisect_right

hors = [[-1] for _ in range(n)]
vers = [[-1] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if mat[i][j] == '#':
            hors[i].append(j)
            vers[j].append(i)

for i in range(n): hors[i].append(m)
for j in range(m): vers[j].append(n)

def check_if_passes(x, y, dir, debug = False):
    st = set()

    while True:
        if (x, y, dir) in st: return False
        st.add((x, y, dir))

        if dir == 0:
            tidx = vers[y][bisect_left(vers[y], x)-1]
            if tidx == -1: break
            x = tidx + 1
        if dir == 1:
            tidx = hors[x][bisect_right(hors[x], y)]
            if tidx == m: break
            y = tidx - 1
        if dir == 2:
            tidx = vers[y][bisect_right(vers[y], x)]
            if tidx == n: break
            x = tidx - 1
        if dir == 3:
            tidx = hors[x][bisect_left(hors[x], y)-1]
            if tidx == -1: break
            y = tidx + 1
        
        dir = (dir+1)%4
    return True

tot = 0
for i in range(n):
    for j in range(m):
        
        if (i, j) == (xmain, ymain): continue 
        if mat[i][j] == '#': continue

        insort(hors[i], j)
        insort(vers[j], i)

        chk = check_if_passes(xmain, ymain, dirmain)
        tot += (1-chk)
            
        hors[i].remove(j)
        vers[j].remove(i)
        
print("Part 2:", tot)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')