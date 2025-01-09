import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------


from math import gcd
from functools import reduce

dirmap = input()
input()
movemap = {}
for _ in range(754):
    line = input().split('=')
    movemap[line[0].strip()] = line[1].strip('() ').split(', ')
# for key, val in movemap.items(): print(f"[{key}] : {val}")

def dist_find(curr, target):
    cnt = 0
    while not target(curr):
        if dirmap[cnt%len(dirmap)] == 'L': curr = movemap[curr][0]
        else: curr = movemap[curr][1]
        cnt += 1
    return cnt

# Part 1
def key_1(curr): return curr == 'ZZZ'
print('Answer Part 1:', dist_find('AAA', key_1))

# Part 2
def key_2(curr): return curr[-1] == 'Z'
starts = [key for key in movemap.keys() if key[-1] == 'A']
dists = [dist_find(start, key_2) for start in starts]
res = reduce(lambda x,y: (x*y)//gcd(x,y), dists)
print('Answer Part 2:', res)

#------------------------------------------------------------ -----------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')