import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

from collections import Counter

inp = input()

# Part 1
x = y = 0
houses = Counter()
houses[(0, 0)] = 1

for c in inp:
    match c:
        case '^': x += 1
        case 'v': x -= 1
        case '<': y -= 1
        case '>': y += 1
    houses[(x, y)] += 1

print("Part 1:",len(houses))

# Part 2
sx = sy = rx = ry = 0
houses = Counter()
houses[(0, 0)] = 1

for i, c in enumerate(inp):
    match c:
        case '^':
            if i & 1: sx += 1
            else: rx += 1
        case 'v': 
            if i & 1: sx -= 1
            else: rx -= 1
        case '<': 
            if i & 1: sy -= 1
            else: ry -= 1
        case '>': 
            if i & 1: sy += 1
            else: ry += 1
    houses[(sx, sy)] += 1
    houses[(rx, ry)] += 1

print("Part 2:",len(houses))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')