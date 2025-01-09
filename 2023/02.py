import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

# Part 1
# def solve(s):
#     s = s.split(';')
#     for game in s:
#         game = game.strip().split(',')
#         for val, mode in map(lambda x:x.split(), game):
#             if mode=='red' and int(val)>12: return False
#             if mode=='green' and int(val)>13: return False
#             if mode=='blue' and int(val)>14: return False
#     return True

# tot = 0
# for _ in range(100):
#     s = input().split(':')
#     if solve(s[1].strip()): tot += int(s[0][5:])
# print("Answer:", tot)

# Part 2
from collections import Counter
def solve(s):
    s = s.split(';')
    ctr = Counter()
    for game in s:
        game = game.strip().split(',')
        for val, mode in map(lambda x:x.split(), game):
            ctr[mode] = max(ctr[mode], int(val))
    return ctr['red']*ctr['green']*ctr['blue']

tot = 0
for _ in range(100):
    s = input().split(':')
    tot += solve(s[1].strip())
print("Answer:", tot)


#-----------------------------------------------------------------------
print(f'\n{"-"*50}\nTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')