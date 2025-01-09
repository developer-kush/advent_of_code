import sys, time
sys.stdin = open('_in.txt', 'r')
start_time = time.perf_counter()
#-----------------------------------------------------------------------

a = int(input()[12:])
b = int(input()[12:])
c = int(input()[12:])
input()
instructions = list(map(int, input()[9:].split(',')))

def program(a, b, c, instructions):

    res = []

    ip = 0
    while ip < len(instructions)-1:
        opcode, operand = instructions[ip], instructions[ip+1]

        if operand == 4: operand = a
        elif operand == 5: operand = b
        elif operand == 6: operand = c

        if opcode == 0: a = a // (1<<operand)
        elif opcode == 1: b = b ^ operand
        elif opcode == 2: b = operand % 8
        elif opcode == 3: 
            if a != 0:
                ip = operand
                ip -= 2
        elif opcode == 4: b = b ^ c
        elif opcode == 5: res.append(operand%8)
        elif opcode == 6: b = a // (1<<operand)
        elif opcode == 7: c = a // (1<<operand)
        ip += 2

    return res

print("Part 1:",','.join(map(str, program(a, b, c, instructions))))

# Part 2

def move(A):
    B = (A % 8) ^ 7
    C = A // (1<<B)
    A = A // 8
    return (B ^ 7 ^ C) % 8

def rec(A, col=0):
    if As: return
    if move(A) != instructions[-(col + 1)]: return
    if col == len(instructions) - 1: As.append(A); return
    else:
        for B in range(8): 
            rec(A * 8 + B, col + 1)
            if As: return

As = []
for a in range(8):
    rec(a)
print("Part 2:",As[0])

#-----------------------------------------------------------------------
print(f'\n{"-"*50}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')