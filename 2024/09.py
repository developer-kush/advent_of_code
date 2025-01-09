import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------


disk = input()

def rsum(l, r): return (r*(r+1))//2 - (l*(l-1))//2


# Part 1

def part1(disk):
    fileEnds = []
    curr = 0
    for i in range(len(disk)):
        if int(disk[i]) == 0: continue
        if not i&1: fileEnds.append([curr, curr + int(disk[i])-1])
        curr += int(disk[i])

    checksum = 0
    n = len(fileEnds)

    for i in range(n):
        if i >= len(fileEnds): break
        s, e = fileEnds[i]
        # print(f"adding {s}-{e} for {i}")
        checksum += rsum(s, e)*i

        if i+1 >= len(fileEnds): break

        fss = e+1
        fse = fileEnds[i+1][0]-1

        while fileEnds[-1][0] > fss:
            lenfile = fileEnds[-1][1] - fileEnds[-1][0] + 1
            if lenfile <= fse-fss+1:
                # print(f"adding {fss}-{fss-lenfile-1} for {len(fileEnds)-1}")
                checksum += rsum(fss, fss+lenfile-1)*(len(fileEnds)-1)
                fss += lenfile
                fileEnds.pop()
            else:
                covered = fse-fss+1
                fileEnds[-1][-1] -= covered
                # print(f"adding {fss}-{fse} for {len(fileEnds)-1}")
                checksum += rsum(fss, fse)*(len(fileEnds)-1)
                break
    return checksum

print("Part 1:", part1(disk))

# Part 2

def part2(disk):
    fileEnds = []
    curr = 0
    for i in range(len(disk)):
        if int(disk[i]) == 0: continue
        if not i & 1: fileEnds.append([curr, curr + int(disk[i]) - 1])
        curr += int(disk[i])

    freespaces = []
    for i in range(1, len(fileEnds)):
        prev_end = fileEnds[i-1][1]
        curr_start = fileEnds[i][0]
        if prev_end + 1 < curr_start: freespaces.append([curr_start - prev_end - 1, prev_end + 1])
    freespaces.sort(key=lambda x: x[1])

    for i in range(len(fileEnds) - 1, -1, -1):
        s, e = fileEnds[i]
        filesize = e - s + 1

        best_space = None
        for space in freespaces:
            if space[1] + space[0] - 1 < s and space[0] >= filesize:
                best_space = space
                break

        if not best_space: continue

        freesize, freestart = best_space
        fileEnds[i] = [freestart, freestart + filesize - 1]

        freespaces.remove(best_space)
        leftover_size = freesize - filesize
        if leftover_size > 0:
            freespaces.append([leftover_size, freestart + filesize])
            freespaces.sort(key=lambda x: x[1])  # Keep sorted

    checksum = sum(idx * rsum(s, e) for idx, (s, e) in enumerate(fileEnds))
    return checksum


print("Part 2:", part2(disk))



#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')