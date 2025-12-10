import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = 1000

part1 = part2 = 0
for i in range(n):
    a, b, c = map(int, input().split('x'))
    part1 += (((a*b)+(b*c)+(c*a)) << 1 ) + min(a*b, b*c, c*a)
    part2 += ((min(a+b, b+c, a+c)) << 1) + a*b*c
print("Part 1:", part1)  
print("Part 2:", part2)  


#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')