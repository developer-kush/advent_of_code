import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = 187
ranges = [list(map(int, input().split('-'))) for _ in range(n)]
input()
m = 1188-188
points = [int(input()) for _ in range(m)]


def merge_intervals(arr):
    arr.sort(key=lambda x: x[0])
    merged = []
    for interval in arr:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

mr = merge_intervals(ranges)

ridx = part1 = 0
for point in sorted(points):
    while ridx < len(mr) and point > mr[ridx][1]: ridx += 1
    if ridx == len(mr): break
    if point >= mr[ridx][0] and point <= mr[ridx][1]: part1 += 1
print("Part 1:",part1)
        
part2 = sum(r-l+1 for l,r in mr)
print("Part 2:",part2)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')