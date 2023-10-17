import sys 
from math import inf 
from collections import Counter
input = sys.stdin.readline

n = int(input()[:-1])
numbers = list(map(int,input().split()))
counts = list(map(int,input().split()))

max_val = -inf
min_val = inf

def track(depth,counts,val):
    global max_val,min_val
    if depth == n-1:
        max_val = max(max_val,val)
        min_val = min(min_val,val)

    for op, count in enumerate(counts):
        if count <= 0:
            continue 
        new_val = val
        if op == 0:
            new_val += numbers[depth+1]
        elif op == 1:
            new_val -= numbers[depth+1]
        elif op == 2:
            new_val *= numbers[depth+1]
        elif op == 3:
            if new_val >= 0:
                new_val //= numbers[depth+1]
            else:
                new_val = -(-new_val// numbers[depth+1])

        counts[op] -= 1
        track(depth+1,counts,new_val)
        counts[op] += 1

track(0,counts,numbers[0])

print(max_val)
print(min_val)