import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

with open('_in.txt', 'r') as f: data = f.readlines()
data = [row.replace('\n', '') for row in data]

n, m = len(data), len(data[0])

tot = 0
for i in range(n):
    for j in range(m):
        for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            flag = True
            x, y = i, j
            for ch in 'XMAS':
                if not (0 <= x < n and 0 <= y < m): flag = False; break
                if data[x][y]!=ch: flag = False; break
                x += di
                y += dj
            if flag: tot += 1
print("Part 1:",tot)

from collections import Counter
tot = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        if data[i][j] != 'A': continue
        chars = data[i-1][j-1] + data[i-1][j+1] + data[i+1][j-1] + data[i+1][j+1]
        if data[i-1][j-1] == data[i+1][j+1] or data[i-1][j+1] == data[i+1][j-1]: continue
        if list(Counter(chars).values()) == [2, 2] and 'M' in chars and 'S' in chars:
            tot += 1
print("Part 2:",tot)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')