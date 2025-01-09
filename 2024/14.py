
import sys, time
stdin = sys.stdin
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

import os
import time

robocnt = 500
n, m = 101, 103

robots = []

for _ in range(robocnt):
    p, v = input().split()
    px, py = map(int, p[2:].split(','))
    vx, vy = map(int, v[2:].split(','))
    robots.append((px, py, vx, vy))

# Part 1

def part_one(time_elapsed):

    a = b = c = d = 0

    mx, my = n//2, m//2

    for px, py, vx, vy in robots:
        nx = (px + vx*time_elapsed)%n
        ny = (py + vy*time_elapsed)%m

        if nx == mx or ny == my: continue
        # sample_mat[ny][nx] += 1

        if nx < mx and ny < my: a += 1
        if nx > mx and ny < my: b += 1
        if nx < mx and ny > my: c += 1
        if nx > mx and ny > my: d += 1

    # print(a, b, c, d)

    # for row in sample_mat:
    #     print(*row)

    return a*b*c*d
    
    
print("Part 1:", part_one(100))

# Part 2

def part_two(time_elapsed):

    cnt = 0

    sample_mat = [[0]*m for _ in range(n)]

    for px, py, vx, vy in robots:
        nx = (px + vx*time_elapsed)%n
        ny = (py + vy*time_elapsed)%m

        if abs(nx - n//2) < 1: cnt += 1

        sample_mat[nx][ny] += 1

    # os.system('clear')
    for row in sample_mat:
        row = ['.' if val == 0 else '#' for val in row]
        print(''.join(row))
    print("Iteration:", time_elapsed)
    
    return cnt

part_two(6668)


#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')