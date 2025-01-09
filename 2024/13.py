import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------


from functools import lru_cache

machines = []
inf = float('inf')

while True:
    try:
        a = input().split(',')
        b = input().split(',')
        p = input().split(',')
        ax, ay = int(a[0][12:]), int(a[1][3:])
        bx, by = int(b[0][12:]), int(b[1][3:])
        px, py = int(p[0][9:]), int(p[1][3:])
        machines.append((ax, ay, bx, by, px, py))
        input()
    except: break
    
def gcd(x, y):
    while y: x, y = y, x%y
    return x

def lcm(x, y): return x*y//gcd(x, y)

def part_one():
    res = 0
    
    for ax, ay, bx, by, px, py in machines:
        
        mn = inf
        # remove x
        lcm1 = lcm(ax, ay)
        amulfac = lcm1//ax
        tax, tbx, tpx = ax*amulfac, bx*amulfac, px*amulfac
        bmulfac = lcm1//ay
        tay, tby, tpy = ay*bmulfac, by*bmulfac, py*bmulfac

        b = tbx-tby
        c = tpx-tpy

        y = c/b
        if y == int(y):
            x = (tpx - y*tbx)/tax
            if x != int(x): continue
            if x >= 0 and y >= 0: mn = min(mn, 3*x+y)

        # remove y
        lcm2 = lcm(bx, by)
        amulfac = lcm2//bx
        tax, tbx, tpx = ax*amulfac, bx*amulfac, px*amulfac
        bmulfac = lcm2//by
        tay, tby, tpy = ay*bmulfac, by*bmulfac, py*bmulfac

        a = tax-tay
        c = tpx-tpy

        x = c/a
        if x == int(x):
            y = (tpy - x*tay)/tby
            if y != int(y): continue
            if x >= 0 and y >= 0: mn = min(mn, 3*x+y)

        if mn != inf: res += mn
    
    return int(res) 

print("Part 1:", part_one())

# Part 2

def gcd(x, y):
    while y: x, y = y, x%y
    return x

def lcm(x, y): return x*y//gcd(x, y)

def part_two():
    res = 0
    
    for ax, ay, bx, by, px, py in machines:
        px, py = px+10000000000000, py+10000000000000
        
        mn = inf
        # remove x
        lcm1 = lcm(ax, ay)
        amulfac = lcm1//ax
        tax, tbx, tpx = ax*amulfac, bx*amulfac, px*amulfac
        bmulfac = lcm1//ay
        tay, tby, tpy = ay*bmulfac, by*bmulfac, py*bmulfac

        b = tbx-tby
        c = tpx-tpy

        y = c/b
        if y == int(y):
            x = (tpx - y*tbx)/tax
            if x != int(x): continue
            if x >= 0 and y >= 0: mn = min(mn, 3*x+y)

        # remove y
        lcm2 = lcm(bx, by)
        amulfac = lcm2//bx
        tax, tbx, tpx = ax*amulfac, bx*amulfac, px*amulfac
        bmulfac = lcm2//by
        tay, tby, tpy = ay*bmulfac, by*bmulfac, py*bmulfac

        a = tax-tay
        c = tpx-tpy

        x = c/a
        if x == int(x):
            y = (tpy - x*tay)/tby
            if y != int(y): continue
            if x >= 0 and y >= 0: mn = min(mn, 3*x+y)

        if mn != inf: res += mn
    
    return int(res)   

print("Part 2:", part_two())

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')