import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = 4177

vals = [input() for _ in range(n)]

# Part 1

curr, res = 50, 0

for val in vals:
    if val[0] == 'L': curr -= int(val[1:])
    else: curr += int(val[1:])
    curr %= 100
    if curr == 0: res += 1
print(res)


# Part 2

curr, res = 50, 0

for val in vals:
    v, d = int(val[1:]), val[0]
    res, v = res + (v//100), v % 100

    orig = curr
    
    if d == 'L': curr -= v
    else: curr += v

    if (curr >= 100) or (curr == 0 or orig != 0 and curr < 0): res += 1

    curr %= 100
print(res)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')