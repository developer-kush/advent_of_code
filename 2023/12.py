import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------

from functools import lru_cache

def countWays(a, b):
    a = '.'+('.'.join(x for x in a.split('.') if x))

    @lru_cache(500)
    def rec(x, y, level = 0):
        if y <= 0: return int(x == -1 or '#' not in a[:x])
        if x <= 0: return 0

        if a[x-1] == '.': return rec(x-1, y, level+1)

        lastval = b[y-1]

        # no choice
        if a[x-1] == '#':
            if '.' not in a[x-lastval:x]:
                if (x-lastval == 0 or a[x-lastval-1] in '.?'): return rec(x-lastval-1, y-1, level+1)
            return 0
        
        tot = 0
        # choice
        if '.' not in a[x-lastval:x] and (x-lastval == 0 or a[x-lastval-1] in '.?'): tot += rec(x-lastval-1, y-1, level+1)
        tot += rec(x-1, y, level+1)
        
        return tot

    return rec(len(a), len(b))

# n = 9
n = 1000
springs = []
for _ in range(n):
    a, b = input().split()
    springs.append((a, list(map(int, b.split(',')))))

# Answer Part 1
res = [countWays(*spring) for spring in springs]
print("Answer Part 1:", sum(res)) # Expected: 6852
# print(res)

# Answer Part 2
res = [countWays( '?'.join([spring[0]]*5) , spring[1]) for spring in springs]
print("Answer Part 2:", sum(res)) 

#-----------------------------------------------------------------------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')