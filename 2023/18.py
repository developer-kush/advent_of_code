import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------

from collections import deque

def getGridSize(moves):
    l = r = u = d = x = y = 0
    for dir, cnt, _ in moves:
        if dir == 'L': y -= cnt
        elif dir == 'R': y += cnt
        elif dir == 'U': x -= cnt
        elif dir == 'D': x += cnt
        l, r, u, d = min(l, y), max(r, y), min(u, x), max(d, x)
    return ((-u, -l), (r-l+1, d-u+1))

def getEnclosedArea(moves):
    (x, y), (m, n) = getGridSize(moves)
    grid = [['.']*(m) for _ in range(n)]
    grid[x][y] = '#'

    for dir, cnt, color in moves:
        if dir == 'L':
            target = y-cnt
            while y > target: y-=1; grid[x][y] = '#'
        elif dir == 'R':
            target = y+cnt
            while y < target: y+=1; grid[x][y] = '#'
        elif dir == 'U':
            target = x-cnt
            while x > target: x-=1; grid[x][y] = '#'
        elif dir == 'D':
            target = x+cnt
            while x < target: x+=1; grid[x][y] = '#'

    q = deque()
    for x in range(n):
        if grid[x][0] == '.':  grid[x][0] = '+'; q.append((x, 0))
        if grid[x][m-1] == '.':  grid[x][m-1] = '+'; q.append((x, m-1))
    for y in range(m):
        if grid[0][y] == '.':  grid[0][y] = '+'; q.append((0, y))
        if grid[n-1][y] == '.':  grid[n-1][y] = '+'; q.append((n-1, y))
    
    while q:
        x, y = q.popleft()
        for a, b in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= a < n and 0 <= b < m and grid[a][b] == '.': 
                grid[a][b] = '+'
                q.append((a, b))
    tot = sum(x.count('+') for x in grid)

    return n*m - tot

def getHex(hexval):
    mapping = {0:'R', 1:'D', 2:'L', 3:'U'}
    return (mapping[int(hexval[5])], int(hexval[:5], 16))

def getShoelace(coords):
    a = b = outline = 0
    for i in range(len(coords)-1):
        a += coords[i][0]*coords[i+1][1]
        b += coords[i][1]*coords[i+1][0]
        outline += abs(coords[i][0]-coords[i+1][0]) + abs(coords[i][1]-coords[i+1][1])
    return ((abs(a-b)+outline+1)>>1)+1

def getEnclosedAreaOptimal(moves):
    coords = [(0, 0)]
    x = y = 0
    for dir, cnt, _ in moves:
        if dir == 'L': y -= cnt
        elif dir == 'R': y += cnt
        elif dir == 'U': x -= cnt
        elif dir == 'D': x += cnt
        coords.append((x, y))
    return getShoelace(coords)

n = 738
moves = []
for _ in range(n):
    dir, cnt, color = input().split()
    cnt = int(cnt)
    moves.append([dir, cnt, color])

# Answer Part 1
print("Answer Part 1:", getEnclosedAreaOptimal(moves))

for idx, (_, _, color) in enumerate(moves): moves[idx][0], moves[idx][1] = getHex(color.strip('(#)'))
# print('moves:', *moves, sep='\n')

# Answer Part 2
print("Answer Part 2:", getEnclosedAreaOptimal(moves))
print(getGridSize(moves))


#-----------------------------------------------------------------------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')