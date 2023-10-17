import sys 
from math import inf 

input = sys.stdin.readline

n = int(input()[:-1])
numbers = list(map(int,input().split()))
counts = list(map(int,input().split()))

ops = []
for i in range(4):
    ops += [i]*counts[i]

visited = set()

max_val = -inf
min_val = inf
used = [0]*(n-1)

def track(used, val, depth):
    global max_val,min_val

    if tuple(used) in visited:
        return

    if depth == n-1:
        max_val = max(max_val,val)
        min_val = min(min_val,val)
        return 
    
    for i in range(n-1):
        if used[i]:
            continue
        used[i] = 1 
        new_val = val
        if ops[i] == 0:
            new_val += numbers[i+1]
        elif ops[i] == 1:
            new_val -= numbers[i+1]
        elif ops[i] == 2:
            new_val *= numbers[i+1]
        elif ops[i] == 3:
            if new_val >= 0:
                new_val //= numbers[i+1]
            else:
                new_val = -(-new_val// numbers[i+1]) 
                
        visited.add(tuple(used))
        track(used,new_val,depth+1)
        used[i] = 0

track(used,numbers[0],0)

print(max_val)
print(min_val)