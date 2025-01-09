import sys, time
sys.stdin = open('_in.txt', 'r')
# sys.stdout = open('_out.txt', 'w')
start_time = time.perf_counter()
import os
os.system('clear')

#-----------------------------------------------------------------------


def getLocation(seed, stages):
    for stage in stages:
        for key, val in stage.items():
            if key[0] <= seed <= key[1]: seed += val; break
    return seed

def mergeIntervals(intervals):
    res = []
    intervals.sort()
    curr = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= curr[1]+1: curr[1] = max(curr[1], intervals[i][1])
        else: res.append(curr); curr = intervals[i]
    res.append(curr)
    return res

def getMinLocationInterval(intervals, stages):
    def stageTransform(intervals, stage):
        res = []
        n = len(intervals)
        curr = 0
        for key, val in stage.items():
            start, end = key
            while curr<n and intervals[curr][1] < start: res.append(list(intervals[curr])); curr += 1
            while curr<n and intervals[curr][0] < start:
                res.append([intervals[curr][0], start-1])
                intervals[curr][0] = start
            while curr<n and intervals[curr][1] <= end:
                res.append([intervals[curr][0]+val, intervals[curr][1]+val])
                curr += 1
            while curr<n and intervals[curr][0] <= end:
                res.append([intervals[curr][0]+val, end+val])
                intervals[curr][0] = end+1
        while curr<n: res.append(list(intervals[curr])); curr += 1
        return res
    
    for stage in stages: 
        intervals = mergeIntervals(stageTransform(intervals, stage))
    return intervals[0][0]

def sort_dict(d):
    res = {}
    for key in sorted(d.keys()): res[key] = d[key]
    return res


# INPUT
seeds = list(map(int, input()[7:].strip().split()))
stages = []
input()
for _ in range(7):
    input()
    stages.append({})
    while True: 
        try: curr = input()
        except: break
        if not curr: break
        dest, src, cnt = map(int, curr.split())
        stages[-1][(src, src+cnt-1)] = dest-src

# Part 1
print("Answer Part 1:",min([getLocation(seed, stages) for seed in seeds]))

# Part 2
intervals = mergeIntervals([[seeds[i<<1], (seeds[i<<1]+seeds[(i<<1)+1]-1)] for i in range(len(seeds)>>1)])
stages = [sort_dict(stage) for stage in stages]
print("Answer Part 2:", getMinLocationInterval(intervals, stages))

#-----------------------------------------------------------------------
print(f'\n{"-"*30}\n\033[92mTook {(time.perf_counter()-start_time)*1000:.2f} ms to run')
def autoclear(): import time, os; time.sleep(5); os.system('clear')
# autoclear()