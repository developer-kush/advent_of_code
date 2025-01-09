import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

with open('_in.txt', 'r') as f: data = ''.join(f.readlines())

import re
pattern = r"mul\(\d+,\d+\)"

tot = 0
for x in re.findall(pattern, data):
    a, b = map(int, x[4:-1].split(','))
    tot += a*b
print("Part 1:",tot)

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
tot = 0
flag = True
for x in re.findall(pattern, data):
    if x == "do()": flag = True
    elif x == "don't()": flag = False
    elif flag: 
        a, b = map(int, x[4:-1].split(','))
        tot += a*b
print("Part 2:",tot)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')