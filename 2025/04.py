import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = 135

grid = [input() for _ in range(n)]

part1 = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != '@': continue
        cnt = 0
        for dx in range(i-1, i+2):
            for dy in range(j-1, j+2):
                if dx == i and dy == j: continue
                if dx < 0 or dx >= n or dy < 0 or dy >= n: continue
                if grid[dx][dy] == '@': cnt += 1
        if cnt < 4: part1 += 1
print("Part1:",part1)

part2 = 0
while True:
    new = [list(row) for row in grid]
    for i in range(n):
        for j in range(n):
            if grid[i][j] != '@': continue
            cnt = 0
            for dx in range(i-1, i+2):
                for dy in range(j-1, j+2):
                    if dx == i and dy == j: continue
                    if dx < 0 or dx >= n or dy < 0 or dy >= n: continue
                    if grid[dx][dy] == '@': cnt += 1
            if cnt < 4: 
                part2 += 1
                new[i][j] = '.'
    if new == grid: break
    grid = new

print("Part2:",part2)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')