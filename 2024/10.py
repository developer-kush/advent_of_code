import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = m = 44

rows = [input() for _ in range(n)]

reachablility = [[set() for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if rows[i][j] == '9': reachablility[i][j] = set([(i, j)])

for x in range(8, -1, -1):
    nrc = [[set() for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if rows[i][j] != str(x): continue
            for a, b in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if not (0 <= a < n and 0 <= b < m): continue
                if rows[a][b] != str(x+1): continue
                nrc[i][j] |= reachablility[a][b]

    reachablility = nrc

# for row in reachablility: print(*[len(cell) for cell in row])
print(f"Part 1:",sum(sum([len(cell) for cell in row]) for row in reachablility))


# Part 2

reachablility = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if rows[i][j] == '9': reachablility[i][j] = 1

for x in range(8, -1, -1):
    nrc = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if rows[i][j] != str(x): continue
            for a, b in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if not (0 <= a < n and 0 <= b < m): continue
                if rows[a][b] != str(x+1): continue
                nrc[i][j] += reachablility[a][b]

    reachablility = nrc

print(f"Part 2:",sum(sum(row) for row in reachablility))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')