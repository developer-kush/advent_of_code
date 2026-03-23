import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

from functools import lru_cache

import sys
sys.setrecursionlimit(500000)

inputs = open('_in.txt', 'r').readlines()
n = len(inputs)

lights = []
for inp in inputs:
    inp = inp.strip('\n')
    f, l = inp.index(' '), inp.index('{')
    lgts, switch, joltage = inp[:f], inp[f+1:l-1], inp[l:]
    lights.append({
        "light": lgts.strip('[]'),
        "switch": [list(map(int, item.strip('()').split(','))) for item in switch.split()], 
        "joltage": list(map(int, joltage.strip('{}').split(',')))
    })
    # print(f"[{lights[-1]["light"]}] [{lights[-1]["switch"]}] [{lights[-1]["joltage"]}]")

def convertLightToNum(light):
    num = 0
    for idx, ch in enumerate(light):
        if ch == '#':
            num |= (1 << idx)
    return num

def convertSwitchToNum(switch):
    num = 0
    for light in switch:
        num |= (1<<light)
    return num

res = 0
for light in lights:
    lgts, switch, joltage = light["light"], light["switch"], light["joltage"]
    
    lnum = convertLightToNum(lgts)
    switches = [convertSwitchToNum(sw) for sw in switch]

    mn = len(switches)
    for i in range(1 << len(switches)):
        curr = 0
        bn = bin(i)[2:].rjust(len(switches), '0')
        for x in range(len(bn)):
            if bn[x] == '1': curr ^= switches[x]
        if curr != lnum: continue
        mn = min(mn, bn.count('1'))
    res += mn
print("Part 1:", res)

# Part 2 
# inf = float('inf')

# @lru_cache
# def rec(pos, joltages):
#     if any(val < 0 for val in joltages): return inf
#     if pos == 0:
#         if all(val == 0 for val in joltages): return 0
#         return inf
    
#     notake = rec(pos-1, joltages)

#     nj = list(joltages)
#     for sw in switch[pos]: nj[sw] -= 1
#     take = rec(pos, tuple(nj)) + 1

#     return min(notake, take)

res2 = 0

from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger, value, PULP_CBC_CMD

for idx, light in enumerate(lights):
    _, switch, joltage = light["light"], light["switch"], light["joltage"]
    k = len(switch)

    # Solve using Linear Programming
    prob = LpProblem("min_sum", LpMinimize)

    vars = [str(i) for i in range(k)]
    vars = {name: LpVariable(name, lowBound=0, cat=LpInteger) for name in vars}
    prob += lpSum(vars.values())

    conditions = {}

    for idx, sw in enumerate(switch):
        for light in sw:
            if light in conditions:
                conditions[light] = conditions[light] + vars[str(idx)]
            else:
                conditions[light] = vars[str(idx)]

    for key, condition in conditions.items(): 
        prob += condition == joltage[key]

    prob.solve(PULP_CBC_CMD(msg=0))
    this = int(value(prob.objective)) 
    
    res2 += this

print("Part 2:", res2)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')