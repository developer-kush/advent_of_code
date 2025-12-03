import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

n = 200

banks = [input() for _ in range(n)]

"""
Proof of Correctness:
1. For each position i (from left to right), we select the maximum digit from the valid search range.
   - Valid range: [current_position : remaining_positions_needed]
   - This ensures we have enough digits left to complete the number.

2. We choose the leftmost occurrence of this maximum digit.
   - Choosing leftmost maximizes future options (minimizes deletions).
   - Any later occurrence would unnecessarily constrain subsequent choices.

3. After selecting a digit, we update the search start position to just after the selected digit.
   - This ensures we only consider digits to the right for subsequent positions.
   - Maintains the relative order of digits from the original bank.

Optimality: Since we greedily maximize each digit position from left to right (most significant 
to least significant), and preserve maximum future flexibility, this produces the optimal result.
"""

def max_joltage(batteries, bank):
    curr = ""
    ln = len(bank)
    best = 0
    for i in range(batteries-1, -1, -1):
        mxd = max(bank[best:ln-i])
        mxlp = bank.index(mxd, best)
        best = mxlp+1
        curr += mxd
    return int(curr)

# Part 1
print(sum(max_joltage(2, bank) for bank in banks))

# Part 2
print(sum(max_joltage(12, bank) for bank in banks))

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')