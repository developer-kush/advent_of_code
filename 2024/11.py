import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

from functools import lru_cache
arr = input().split()

@lru_cache(None)
def cnt_inc(x, rem):
    if rem == 0: return 1
    if x == 0: return cnt_inc(1, rem-1)
    if len(str(x))%2 == 0: 
        s = str(x)
        return cnt_inc(int(s[:len(s)//2]), rem-1) + cnt_inc(int(s[len(s)//2:]), rem-1)
    return cnt_inc(x*2024, rem-1)

print("Part 1:", sum(cnt_inc(int(x), 25) for x in arr))

print("Part 2:", sum(cnt_inc(int(x), 75) for x in arr))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')