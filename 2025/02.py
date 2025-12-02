import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

# TODO: A dp or invalid ID building solution will be more optimised
# TODO: Since that won't have to iterate over all the numbers

from collections import Counter
from functools import lru_cache

rows = [list(map(int, rng.split('-'))) for rng in input().split(',')]

part1 = part2 = 0

# Part 1
@lru_cache
def factors(x):
    return [i for i in range(1, (x//2)+1) if x % i == 0]

def checkp1(x):
    x = str(x)
    ln = len(x)
    if ln & 1 : return False
    first, last = x[:ln//2], x[ln//2:]
    return first == last

# Part 2
def checkp2(x):
    # return False
    x = str(x)
    facts = factors(len(x))
    for fact in facts:
        if x[:fact]*(len(x)//fact) == x: return True
    return False


# DRIVER
for l, r in rows:
    for i in range(max(10,l), r+1):
        if checkp1(i): part1 += i
        if checkp2(i): part2 += i

print("Part 1:", part1)
print("Part 2:", part2)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')