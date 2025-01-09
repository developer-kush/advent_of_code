import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = m = 50
wh = [list(input()) for _ in range(n)]
input()
moves = input()

movebreakup = [[moves[0], 0]]
for i in moves:
    if movebreakup[-1][0] == i: movebreakup[-1][1] += 1
    else: movebreakup.append([i, 1])

newwh = [wh[i][:] for i in range(n)]

x, y = None, None
for i in range(n):
    for j in range(n):
        if wh[i][j] == '@': 
            x, y = i, j
            break
    if x is not None: break

dirmap = { '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1) }

# print("Before")
# for row in newwh: print(*row)
# print(x, y)
# print("---")

for dir, cnt in movebreakup:
    # print(dir, cnt)
    dx, dy = dirmap[dir]
    nx, ny = x + dx, y + dy
    curr = 0
    while newwh[nx][ny] != '#' and curr < cnt:
        if newwh[nx][ny] =='.': curr += 1
        if curr >= cnt: break
        nx, ny = nx + dirmap[dir][0], ny + dirmap[dir][1]

    cursorx, cursory = nx, ny
    if newwh[nx][ny] == '#': cursorx, cursory = nx-dx, ny-dy

    nx, ny = nx-dx, ny-dy
    while (nx, ny) != (x, y):
        if newwh[nx][ny] in 'O':
            newwh[nx][ny], newwh[cursorx][cursory] = newwh[cursorx][cursory], newwh[nx][ny]
            cursorx, cursory = cursorx-dx, cursory-dy
        nx, ny = nx-dx, ny-dy
    newwh[x][y], newwh[cursorx][cursory] = newwh[cursorx][cursory], newwh[x][y]
    x, y = cursorx, cursory

    # for row in newwh: print(*row)
    # print(x, y)

    # print("---")

cost = 0
for i in range(n):
    for j in range(n):
        if newwh[i][j] == 'O': cost += i*100+j

print("Part 1:", cost)

# ======================================================================

# Part 2

from collections import Counter

newwh = [[x*2 if (x not in '@O') else x+'.' if x == '@' else '[]' for x in wh[i]] for i in range(n)]
newwh = [list(''.join(x)) for x in newwh]

def canMove(x, y, dir):
    if newwh[x][y] == '.': return True
    if newwh[x][y] == '#': return False
    yl = yr = y
    if newwh[x][y] == ']': yl-=1
    if newwh[x][y] == '[': yr+=1
    if not newwh[x+dir][yl]=='.' and not canMove(x+dir, yl, dir): return False
    if not newwh[x+dir][yr]=='.' and not canMove(x+dir, yr, dir): return False
    return True

def doMove(x, y, dir):
    if newwh[x][y] not in '[]': return
    yl = yr = y
    if newwh[x][y] == ']': yl-=1
    if newwh[x][y] == '[': yr+=1
    if newwh[x+dir][yl] == ']': doMove(x+dir, yl, dir)
    if newwh[x+dir][yr] in '[]': doMove(x+dir, yr, dir)
    if not newwh[x+dir][yr]=='.' and not canMove(x+dir, yr): return False
    
    newwh[x+dir][yl], newwh[x][yl] = newwh[x][yl], newwh[x+dir][yl]
    newwh[x+dir][yr], newwh[x][yr] = newwh[x][yr], newwh[x+dir][yr]

x, y = None, None
for i in range(n):
    for j in range(n):
        if newwh[i][j] == '@': 
            x, y = i, j
            break
    if x is not None: break

dirmap = { '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1) }

# print("Before")
# for row in newwh: print(*row)
# print(x, y)
# print("---")

for dir, cnt in movebreakup:
    # print(dir, cnt)
    dx, dy = dirmap[dir]

    if dir in '<>':
        nx, ny = x + dx, y + dy
        curr = 0
        while newwh[nx][ny] != '#' and curr < cnt:
            if newwh[nx][ny] == '.': curr += 1
            if curr >= cnt: break
            nx, ny = nx + dx, ny + dy

        cursorx, cursory = nx, ny
        if newwh[nx][ny] == '#': cursorx, cursory = nx-dx, ny-dy

        nx, ny = nx-dx, ny-dy
        while (nx, ny) != (x, y):
            if newwh[nx][ny] in '[]':
                newwh[nx][ny], newwh[cursorx][cursory] = newwh[cursorx][cursory], newwh[nx][ny]
                cursorx, cursory = cursorx-dx, cursory-dy
            nx, ny = nx-dx, ny-dy
        newwh[x][y], newwh[cursorx][cursory] = newwh[cursorx][cursory], newwh[x][y]
        x, y = cursorx, cursory

    else:
        for _ in range(cnt):
            if canMove(x, y, dx): 
                doMove(x+dx, y, dx)
                # print("Can:", x, y, x+dx, "-", dx, dy)
                newwh[x][y], newwh[x+dx][y] = newwh[x+dx][y], newwh[x][y]
                x, y = x+dx, y
            else: break

# for row in newwh: print(*row)
# print(x, y)
# print("---")

cost = 0
for i in range(n):
    for j in range(2*n):
        if newwh[i][j] == '[': cost += i*100+j

print("Part 2:", cost)

    

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')