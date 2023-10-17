from math import gcd
from collections import defaultdict 

def solution(n, cores):
    answer = 0
    cycle = []
    lcm = 1
    for core in cores:
        lcm = lcm*core // gcd(lcm,core)

    for i in range(lcm+1):
        for core in cores:
            if i % core != 0:
                continue 
            cycle.append(core)

    return cycle[n % len(cycle)-1]