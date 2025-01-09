import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

# Part 1
# def solve_a(n, m, machine):
#     tot = 0
#     for idx, row in enumerate(machine):
#         flag, curr = False, 0
#         for jdx, col in enumerate(row):
#             if not col.isdigit(): 
#                 if flag: tot += curr
#                 flag, curr = False, 0
#                 continue
#             curr = curr*10 + int(col)
#             for x, y in ((idx-1, jdx-1),(idx-1, jdx),(idx-1, jdx+1),(idx, jdx-1),(idx, jdx+1),(idx+1, jdx-1),(idx+1, jdx),(idx+1, jdx+1)):
#                 if not 0<=x<n or not 0<=y<m: continue
#                 if not machine[x][y].isdigit() and machine[x][y] != '.': flag = True
#         if flag: tot += curr
#     return tot

# n = m = 140
# machine = [input() for _ in range(n)]
# print("Answer A:", solve_a(n, m, [row for row in machine]))

from collections import defaultdict

# Part 2
def solve_b(n, m, machine):
    p_nums = defaultdict(dict)
    p_dict = {}
    p_nums_ID = 0

    def save(row, left, right, num):
        nonlocal p_nums_ID
        p_nums_ID += 1
        p_dict[p_nums_ID] = num
        for val in range(left, right+1): p_nums[row][val] = p_nums_ID
    def get_id(row, col): return p_nums[row][col]

    for idx, row in enumerate(machine):
        flag, curr = False, 0
        start = -1
        for jdx, col in enumerate(row):
            if not col.isdigit():
                if flag: save(idx, start, jdx-1, curr)
                flag, curr = False, 0
                continue
            if not jdx or not row[jdx-1].isdigit(): start = jdx
            curr = curr*10 + int(col)
            for x, y in ((idx-1, jdx-1),(idx-1, jdx),(idx-1, jdx+1),(idx, jdx-1),(idx, jdx+1),(idx+1, jdx-1),(idx+1, jdx),(idx+1, jdx+1)):
                if not 0<=x<n or not 0<=y<m: continue
                if not machine[x][y].isdigit() and machine[x][y] != '.': flag = True
        if flag: save(idx, start, jdx, curr)

    # finding gears
    tot = 0
    for idx, row in enumerate(machine):
        for jdx, col in enumerate(row):
            if col != '*': continue
            p_nums_IDS = set()

            for x, y in ((idx-1, jdx-1),(idx-1, jdx),(idx-1, jdx+1),(idx, jdx-1),(idx, jdx+1),(idx+1, jdx-1),(idx+1, jdx),(idx+1, jdx+1)):
                if not 0<=x<n or not 0<=y<m: continue
                if machine[x][y].isdigit(): p_nums_IDS.add(get_id(x, y))
            
            if len(p_nums_IDS) == 2: 
                lst = list(p_nums_IDS)
                tot += p_dict[lst[0]]*p_dict[lst[1]]
    return tot

n = m = 140
machine = [input() for _ in range(n)]
print("Answer B:", solve_b(n, m, [row for row in machine]))

#-----------------------------------------------------------------------
print(f'\n{"-"*40}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')
def autoclear():
    time.sleep(3)
    import os
    os.system('clear')
# autoclear()