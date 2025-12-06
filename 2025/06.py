import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = 4

inps = [input() for _ in range(n)]
ops = input().split()

def prod(arr):
    res = arr[0]
    for i in range(1, len(arr)): res *= arr[i]
    return res

def solve(inps):
    res = 0
    for idx, row in enumerate(inps):
        row = list(map(int, row))
        if ops[idx] == '+': res += sum(row)
        else: res += prod(row)
    return res


# Part 1
def format_inp(inps):
    return list(zip(*[row.split() for row in inps]))

print("Part 1: ", solve(format_inp(inps)))

# Part 2

def format_inp(inps):
    tp = list(zip(*inps))
    joined = ["".join(item).strip() for item in tp]
    res = []
    row = []
    for item in joined:
        if item: row.append(int(item))
        else:
            res.append(row)
            row = []
    res.append(row)
    return res

print("Part 2: ", solve(format_inp(inps)))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')