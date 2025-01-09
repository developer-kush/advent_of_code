import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os; os.system('clear')
#-----------------------------------------------------------------------

def flow(system, taskflows):
    for taskflow in taskflows.split(','):
        if ':' not in taskflow: return taskflow
        taskflow, res = taskflow.split(':')
        if taskflow[1] == '<':
            if system[taskflow[0]] < int(taskflow[2:]): return res
        else:
            if system[taskflow[0]] > int(taskflow[2:]): return res

def findAcceptedSystemsTotal(workflows, systems):
    tot = 0
    for idx, system in enumerate(systems):
        res = 'in'
        while res not in 'AR': res = flow(system, workflows[res])
        if res == 'A': tot += sum(system.values())
    return tot

def findingSystemPossibilities(workflow, system, success_systems = []):
    if workflow in list('AR'): 
        if workflow == 'A': success_systems.append(system)
        return success_systems
    flow = workflows[workflow]
    for taskflow in flow.split(','):
        if ':' not in taskflow: findingSystemPossibilities(taskflow, dict(system), success_systems); break
        taskflow, res = taskflow.split(':')
        prop, value = taskflow[0], int(taskflow[2:])
        if taskflow[1] == '<':
            findingSystemPossibilities(res, {**system, prop:[system[prop][0], min(system[prop][1], value-1)]}, success_systems)
            system[prop][0] = max(system[prop][0], value+1)
        else:
            findingSystemPossibilities(res, {**system, prop:[max(system[prop][0], value+1), system[prop][1]]}, success_systems)
            system[prop][1] = min(system[prop][1], value)
    return success_systems

workflows = {}

while curr:=input():
    name, taskflows = curr.strip('}').split('{')
    workflows[name] =taskflows

systems = []

while True:
    try: 
        curr = input().strip('}{').split(',')
        systems.append({name:int(val) for name, val in map(
            lambda x: x.split('='), curr
        )})
    except EOFError: break

# Answer Part 1
print("Answer Part 1:", findAcceptedSystemsTotal(workflows, systems))

# Answer Part 2
success_systems = findingSystemPossibilities('in', {key:[1, 4000] for key in 'xmas'})
tot = 0
for system in success_systems:
    print(list(system.values()))
    if any(value[1]<value[0] for value in system.values()): continue
    curr = 1
    for value in system.values(): curr *= (value[1]-value[0]+1)
    tot += curr
print("Answer Part 2:", tot)

# 43543382751500
# 167409079868000
# 256000000000000

#-----------------------------------------------------------------------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')