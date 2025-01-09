import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

a, b = [], []

while True:
    try:
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    except:
        break

a.sort()
b.sort()
print("Part 1:",sum(abs(a[i]-b[i]) for i in range(len(a))))


# Part 2

from collections import Counter

d = Counter(b)
tot = sum(val*d[val] for val in a)
print("Part 2:",tot)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')