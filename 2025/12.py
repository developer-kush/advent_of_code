import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

shapes, areas = [], []

for _ in range(6):
    input()
    g = [input() for _ in range(3)]
    input()
    
    cells = [(r,c) for r in range(3) for c in range(3) if g[r][c]=='#']
    areas.append(len(cells))
    
    cands, vars = set(), []
    
    base = [cells]
    for _ in range(3):
        base.append([(c, -r) for r,c in base[-1]])
        
    all_vars = []
    for b in base:
        all_vars.append(b)
        all_vars.append([(r, -c) for r,c in b])
        
    for v in all_vars:
        v.sort()
        r0, c0 = v[0]
        norm = tuple((r-r0, c-c0) for r,c in v)
        if norm not in cands:
            cands.add(norm)
            vars.append(norm)
    shapes.append(vars)

sys.setrecursionlimit(5000)
n = 1000
res = 0

for _ in range(n):
    l, r = input().split(':')
    H, W = map(int, l.split('x'))
    cnts = list(map(int, r.split()))
    
    target = sum(c*a for c,a in zip(cnts, areas))
    if target > H*W: continue
    
    grid = [0]*(H*W)
    
    def solve(idx, cur, wasted):
        while idx < H*W and grid[idx]: idx += 1
        
        if cur == target: return True
        if idx == H*W or target + wasted > H*W: return False
        
        r, c = divmod(idx, W)
        
        for i in range(6):
            if not cnts[i]: continue
            
            for var in shapes[i]:
                undo, ok = [], True
                
                for dr, dc in var:
                    nr, nc = r+dr, c+dc
                    ni = nr*W + nc
                    if 0<=nr<H and 0<=nc<W and not grid[ni]: undo.append(ni)
                    else: ok = False; break
                
                if ok:
                    for u in undo: grid[u] = 1
                    cnts[i] -= 1
                    if solve(idx+1, cur + areas[i], wasted): return True
                    cnts[i] += 1
                    for u in undo: grid[u] = 0
                    
        # skip
        if target + wasted + 1 <= H*W:
             if solve(idx+1, cur, wasted+1): return True
             
        return False

    if solve(0, 0, 0): res += 1

print(res)

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')