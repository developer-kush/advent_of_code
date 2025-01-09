import sys

sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')


def parta(word):
    word2digit = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    digits = []
    pos = 0
    while pos < len(word):
        if word[pos].isdigit(): digits.append(int(word[pos])); pos+=1; break
        for curr in word2digit:
            if word[pos: pos+len(curr)] == curr: digits.append(word2digit[curr]); pos+=len(curr); break
        else: pos+=1; continue
        break
    pos = len(word) - 1
    while pos >= 0:
        if word[pos].isdigit(): digits.append(int(word[pos])); pos-=1; break
        for curr in word2digit:
            if word[pos-len(curr)+1: pos+1] == curr: digits.append(word2digit[curr]); pos-=len(curr); break
        else: pos-=1; continue
        break

    if len(digits) == 0: return 0
    return int(digits[0]*10+digits[-1])

tot = 0
for _ in range(1000):
    word = input()
    tot += parta(word)

print(tot)