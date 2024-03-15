import sys
from math import inf
input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))
numbers.append(inf)
numbers.append(-inf)
numbers.sort()

M = int(input())
checks = list(map(int,input().split()))

for i in range(M):
    left,right = 0,N+1
    while left+1 < right:
        mid = (left + right) // 2
        if numbers[mid] > checks[i]:
            right = mid
        else:
            left = mid 
    if numbers[left] == checks[i]:
        print(1)
    else:
        print(0)





