import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------

from collections import Counter

def getgrp(card, new_rule=False):
    ctr = Counter(card)
    if len(ctr) == 1: return 7
    if new_rule: 
        jval = card.count('a')
        del ctr['a']

    mapping = {
        (5, ): 7,
        (4, 1): 6,
        (3, 2): 5,
        (3, 1, 1): 4,
        (2, 2, 1): 3,
        (2, 1, 1, 1): 2,
        (1, 1, 1, 1, 1): 1
    }
    hand = sorted(ctr.values(), reverse=True)
    if new_rule: hand[0]+=jval
    return mapping[tuple(hand)]

def sortkey_a(card):
    card = card[0]
    replacemap = "23456789TJQKA"
    for i in range(len(replacemap)): card = card.replace(replacemap[i], chr(97+i))
    
    return [
        getgrp(card),
        card
    ]

def sortkey_b(card):
    card = card[0]
    replacemap = "J23456789TQKA"
    for i in range(len(replacemap)): card = card.replace(replacemap[i], chr(97+i))
    return [
        getgrp(card, new_rule=True),
        card
    ]

cards = []
for _ in range(1000): cards.append(input().split())
cards = sorted(cards, key=sortkey_a)

# print([card[0] for card in cards])
# print(*[[sortkey(card),card[0]] for card in cards], sep='\n')

# Part 1
print("Answer Part 1:",sum(i*int(cards[i-1][-1]) for i in range(1, len(cards)+1)))

# Part 2
cards = sorted(cards, key=sortkey_b)
print("Answer Part 2:",sum(i*int(cards[i-1][-1]) for i in range(1, len(cards)+1)))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')