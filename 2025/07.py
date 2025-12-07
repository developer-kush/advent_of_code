import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

from collections import Counter

n = 141

start = input().index('S')
rows = [input() for _ in range(n)]

# Part 1
st = { start }
part1 = 0
for _, row in enumerate(rows):
    for idx, ch in enumerate(row):
        if ch == '.': continue
        if idx in st: 
            part1 += 1
            st.remove(idx)
            st.add(idx+1)
            st.add(idx-1)
print("Part 1:", part1)


# Part 2
st = Counter({ start : 1 })
for _, row in enumerate(rows):
    for idx, ch in enumerate(row):
        if ch == '.': continue
        if idx in st: 
            st[idx-1] += st[idx]
            st[idx+1] += st[idx] 
            st[idx] = 0

print("Part 2:", sum(st.values()))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')