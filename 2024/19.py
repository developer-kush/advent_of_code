import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = 400

dictionary = set(input().split(', '))
input()
words = [input() for _ in range(n)]

def check(word):
    possible = [False]*len(word)
    for i in range(len(word)):
        if word[:i+1] in dictionary: possible[i] = True; continue
        for j in range(i):
            if possible[j] and word[j+1:i+1] in dictionary:
                possible[i] = True
                break
    return possible[-1]

print("Part 1:", sum(check(word) for word in words))

def count(word):
    cnts = [0]*len(word)
    for i in range(len(word)):
        if word[:i+1] in dictionary: cnts[i] += 1

        for j in range(i):
            if word[j+1:i+1] in dictionary:
                cnts[i] += cnts[j]
        
    return cnts[-1]

print("Part 2:", sum(count(word) for word in words))


#-----------------------------------------------------------------------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')