import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

arr = []

while True:
    try: arr.append(list(map(int, input().split())))
    except: break

# Part 1
def isSafe(row):
    for i in range(1, len(row)):
        if not (1<=row[i]-row[i-1]<=3): return False
    return True

print("Part 1:",sum(isSafe(row) or isSafe(row[::-1]) for row in arr))

# Part 2

def isSafe2(row):
    for i in range(len(row)):
        if isSafe(row[:i]+row[i+1:]): return True
    return False

print("Part 2:",sum(isSafe2(row) or isSafe2(row[::-1]) for row in arr))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')