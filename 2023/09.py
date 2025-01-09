import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------

def extrapolate(values):
    tot = 0
    while any(val for val in values):
        tot += values[-1]
        values = [values[i]-values[i-1] for i in range(1, len(values))]
    return tot

def extrapolate_backwards(values):
    def rec(values):
        if all(not val for val in values): return 0
        return values[0]- rec([values[i]-values[i-1] for i in range(1, len(values))])
    return rec(values)

tot_a = tot_b = 0
for _ in range(200):
    values = list(map(int, input().split()))
    tot_a += extrapolate(list(values))
    tot_b += extrapolate_backwards(list(values))

print("Answer Part 1:",tot_a)
print("Answer Part 2:",tot_b)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')