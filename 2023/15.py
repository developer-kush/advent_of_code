import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------

def HASH(string):
    res = 0
    for c in string: res = ((res+ord(c))*17)%256
    return res

def HASHMAP(strings):
    res = [[{}, []] for _ in range(256)]

    for string in strings:
        if string[-1]=='-':
            box = HASH(string[:-1])
            if string[:-1] in res[box][0]: 
                del res[box][0][string[:-1]]
                res[box][1].remove(string[:-1])
        else:
            key, val = string.split('=')
            box = HASH(key)
            if key not in res[box][1]: res[box][1].append(key)
            res[box][0][key] = int(val)
    return res

def focusing_power(strings):
    hashmap = HASHMAP(strings)

    res = 0
    for idx, (lenses, order) in enumerate(hashmap):
        for jdx, lens in enumerate(order):
            res += (idx+1)*(jdx+1)*lenses[lens]

    return res

strings = input().split(',')

# Answer Part 1
res = sum(map(HASH, strings))
print("Answer Part 1:", res)

# Answer Part 2
print("Answer Part 2:", focusing_power(strings))

#-----------------------------------------------------------------------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')