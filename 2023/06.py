import sys, time as t
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = t.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------


def get_winnable(tottime, time, dist):
    speed = (tottime-time)*time
    return speed > dist

times = list(map(int, input()[6:].strip().split()))
dists = list(map(int, input()[9:].strip().split()))

tot = 1
for i in range(len(times)):
    tot *= sum(get_winnable(times[i], j, dists[i]) for j in range(1, times[i]))
print("Answer Part 1:", tot)

time = int(''.join(map(str, times)))
dist = int(''.join(map(str, dists)))
res = sum(get_winnable(time, j, dist) for j in range(1, time))
print("Answer Part 2:", res)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(t.perf_counter()-start_time)*1000:.2f} ms to run')