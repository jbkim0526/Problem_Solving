import sys 
from math import inf 
from itertools import permutations
input = sys.stdin.readline

n = int(input()[:-1])
numbers = list(map(int,input().split()))
counts = list(map(int,input().split()))

ops = []
for i in range(4):
    ops += [i]*counts[i]
s = set(permutations(ops))

max_val = -inf
min_val = inf

for elem in s:
    eq = ""
    val = numbers[0]
    for i in range(1,n):
        if elem[i-1] == 0:
            val += numbers[i]
        elif elem[i-1] == 1:
            val -= numbers[i]
        elif elem[i-1] == 2:
            val *= numbers[i]
        elif elem[i-1] == 3:
            if val >= 0:
                val //= numbers[i]
            else:
                val = -(-val // numbers[i]) 

    max_val = max(max_val,val)
    min_val = min(min_val,val)

print(max_val)
print(min_val)