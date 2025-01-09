import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------


from functools import lru_cache

n = 5 
from itertools import permutations
codes = [input() for _ in range(n)]

def valid(path, x, y, tx, ty, dirmode = False):
    for c in path:
        if c == '^': x -= 1
        elif c == 'v': x += 1
        elif c == '<': y -= 1
        elif c == '>': y += 1

        if not dirmode and (x, y) == (3, 0): return False
        if dirmode and (x, y) == (0, 0): return False

    return (x, y) == (tx, ty)

def numerical(path, ways):
    positions = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
        '0': (3, 1), 'A': (3, 2)
    }
    res = 0
    x, y = 3, 2
    for c in path:
        tx, ty = positions[c]
        moves = ""
        if x > tx: moves += '^'*(x-tx)
        elif x < tx: moves += 'v'*(tx-x)
        if y > ty: moves += '<'*(y-ty)
        elif y < ty: moves += '>'*(ty-y)
        perms = set(map(lambda x: ''.join(x), list(permutations(moves))))
        perms = [perm for perm in perms if valid(perm, x, y, tx, ty)]
        curr = min(directional(perm+'A', ways) for perm in perms)
        res += curr
        x, y = tx, ty
    return res

@lru_cache(None)
def directional(path, ways):
    positions = {
                     '^': (0, 1), 'A': (0, 2),
        '<': (1, 0), 'v': (1, 1), '>': (1, 2)
    }
    res = 0
    x, y = 0, 2
    for c in path:
        tx, ty = positions[c]
        moves = ""
        if x > tx: moves += '^'*(x-tx)
        elif x < tx: moves += 'v'*(tx-x)
        if y > ty: moves += '<'*(y-ty)
        elif y < ty: moves += '>'*(ty-y)
        perms = set(map(lambda x: ''.join(x), list(permutations(moves))))
        perms = [perm for perm in perms if valid(perm, x, y, tx, ty, dirmode = True)]
        if ways == 1:
            curr = min(dcost(perm+'A') for perm in perms if valid(perm, x, y, tx, ty))
        else:
            curr = min(directional(perm+'A', ways-1) for perm in perms)
        res += curr
        x, y = tx, ty
    return res

def dcost(path):
    positions = {
        '^': (0, 1), 'A': (0, 2),
        '<': (1, 0), 'v': (1, 1), '>': (1, 2)
    }
    x, y = 0, 2
    res = 0
    for c in path:
        tx, ty = positions[c]
        res += abs(x-tx) + abs(y-ty) + 1
        x, y = tx, ty
    return res

# =================== DRIVER CODE =======================

tot = 0
for code in codes:
    cost = numerical(code, ways = 1)
    tot += cost*int(code[:-1])
    # tot += cost(code, int(code[:-1]))
print("Part 1:", tot)


tot = 0
for code in codes:
    cost = numerical(code, ways = 24)
    tot += cost*int(code[:-1])
print("Part 2:", tot)



#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')