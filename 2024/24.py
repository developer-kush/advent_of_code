import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()

# Author: Kushagra Agarwal < kushagra.agarwal.2709@gmail.com >
#-----------------------------------------------------------------------

n_wires = 90
n_conn = 222

xnum = ynum = 0

wire = {}
for _ in range(n_wires):
    x, y = input().split(':')
    y = int(y.strip())
    wire[x] = y
    
input()
conns = {}
for _ in range(n_conn):
    a,b,c,d,e = input().split()
    conns[e] = (b, a, c)
    
xnum = ynum = 0

def getZ(wire, conn):
    global xnum, ynum
    
    vis = set()
    def getStatus(w):
        if w in vis: return wire[w]
        vis.add(w)

        if w in wire: return wire[w]
        a,b,c = conns[w]
        b = getStatus(b)
        c = getStatus(c)
        if a == 'AND': res = int(b and c)
        if a == 'XOR': res = int(b ^ c)
        if a == 'OR': res = int(b or c)
        wire[w] = res
        return res
    
    p1 = 0
    for w in (list(conns) + list(wire)):
        if w[0] != 'z':
            if w[0] == 'x':
                if not getStatus(w): continue 
                move = int(w[1:])
                xnum |= (1<<move)
            if w[0] == 'y':
                if not getStatus(w): continue 
                move = int(w[1:])
                ynum |= (1<<move)
            continue 
        
        if not getStatus(w): continue
        move = int(w[1:])
        p1 |= (1<<move)
    return p1

cpy = dict(wire)
res = getZ(cpy, conns)
print("Part 1:", res)

# Part 2

hz = max(key for key in conns if key[0]=="z")

bad = set()
for res, (op, op1, op2) in conns.items():
    if res[0] == "z" and op != "XOR" and res != hz: bad.add(res)

    if (
        op == "XOR"
        and res[0] not in ["x", "y", "z"]
        and op1[0] not in ["x", "y", "z"]
        and op2[0] not in ["x", "y", "z"]
    ): bad.add(res)

    if op == "AND" and "x00" not in [op1, op2]:
        for subres, (subop, subop1, subop2) in conns.items():
            if (res == subop1 or res == subop2) and subop != "OR":
                bad.add(res); break
    
    if op == "XOR":
        for subres, (subop, subop1, subop2) in conns.items():
            if (res == subop1 or res == subop2) and subop == "OR":
                bad.add(res); break

print("Part 2:",",".join(sorted(bad)))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')