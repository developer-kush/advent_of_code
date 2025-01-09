import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = 1771
nums = [int(input()) for _ in range(n)]

def simulate(num):
    MOD = 16777216
    for _ in range(2000):
        num = (num ^ (num << 6))%MOD
        num = (num ^ (num >> 5))%MOD
        num = (num ^ (num << 11))%MOD
        
    return num

print("Part 1:",sum(simulate(num) for num in nums))

from collections import Counter

def simulate(num):
    MOD = 16777216
    nums = []
    for _ in range(2000):
        num = (num ^ (num << 6))%MOD
        num = (num ^ (num >> 5))%MOD
        num = (num ^ (num << 11))%MOD
        nums.append(num%10)
    return nums

scmap = Counter()
for num in nums:
    st = set()
    prices = simulate(num)
    for i in range(4, len(prices)):
        s = tuple(prices[x]-prices[x-1] for x in range(i-3, i+1))
        if s in st: continue
        st.add(s)
        scmap[s] += prices[i]

print("Part 2:", max(scmap.values()))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')