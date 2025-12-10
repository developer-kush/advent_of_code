import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = 1000

def isNice(s):
    if any(grp in s for grp in ('ab', 'cd', 'pq', 'xy')): return False
    if all(s[i]!=s[i-1] for i in range(1, len(s))): return False
    return sum(ch in 'aeiou' for ch in s) >= 3


def isNicer(s):
    if all(s[i+1]!=s[i-1] for i in range(1, len(s)-1)): return False
    for i in range(len(s)):
        if s[i:i+2] in s[i+2:]: return True
    return False

part1 = part2 = 0
for i in range(n):
    s = input()
    part1 += isNice(s)
    part2 += isNicer(s)

print("Part 1:", part1)
print("Part 2:", part2)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')