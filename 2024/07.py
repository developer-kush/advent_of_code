import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

def rec(pos, req, arr):
    if pos == 0: return req == arr[pos]
    if pos < 0: return False
    if rec(pos-1, req-arr[pos], arr): return True
    if rec(pos-1, req/arr[pos], arr): return True
    return False

n = 850
rows = []
for _ in range(n):
    a, *b = input().split()
    a, b = int(a[:-1]), list(map(int, b))
    rows.append((a, b))

print("Part 1:",sum(a*rec(len(b)-1, a, b) for a, b in rows))

def rec(pos, req, orig, arr):
    n = len(arr)
    # if pos > n: return False
    if pos == n: return req == orig
    if pos < n and orig == '': return False
    if req > orig: return False
    
    if rec(pos+1, req+arr[pos], orig, arr): return True
    if rec(pos+1, req*arr[pos], orig, arr): return True
    if rec(pos+1, int(str(req)+str(arr[pos])), orig, arr): return True

    return False

print("Part 2:",sum(a*rec(1, b[0], a, b) for a, b in rows))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')