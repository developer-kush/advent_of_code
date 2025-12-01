import sys

sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')

# Part 1
s = input()
res = s.count('(') - s.count(')')
print("Part 1:", res)

# Part 2
res = 0
for i in range(len(s)):
    if s[i] == '(':  res += 1
    else: res -= 1

    if res < 0:
        print("Part 2:", i+1)
        break