import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

# Part 1
# def solve(card):
#     st = set(card[0].strip().split())
#     cnt = 0
#     for val in card[1].strip().split():
#         if val in st: cnt += 1
#     if cnt: return 1<<(cnt-1)
#     return 0
# tot = 0
# for _ in range(204):
#     card = input().split(":")[1].strip().split("|")
#     tot += solve(card)
# print("Answer Part 1:", tot)

# Part 2
from collections import Counter

def solve(card):
    st = set(card[0].strip().split())
    cnt = 0
    for val in card[1].strip().split():
        if val in st: cnt += 1
    return cnt

n = 204
freqs = Counter()
for val in range(1, n+1): freqs[val] = 1
for _ in range(1, n+1):
    card = input().split(":")[1].strip().split("|")
    curr = solve(card)
    for i in range(_+1, min(n+1, _+curr+1)): freqs[i] += freqs[_]

# for key, val in freqs.items(): print(key, ":", val)

print("Answer Part 2:", sum(freqs.values()))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')
def autoclear():
    import time
    time.sleep(3)
    import os
    os.system('clear')
autoclear()