# 결국 모든 경우를 검사하는 것이지만, 
# memorization을 활용하면 가지가 현저하게 줄어들게 됨 

from collections import defaultdict
from math import inf
import sys
sys.setrecursionlimit(200000)

def solution(numbers):
    
    W = [
        [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6], 
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5], 
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4], 
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5], 
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3], 
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2], 
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4], 
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2], 
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1], 
        ]
    n = len(numbers)
    dp = [dict() for _ in range(n)]
    numbers = list(int(x) for x in numbers)
    
    def solve(i, left, right):
        print(i, left,right)
        if i == n:
            return 0
        if (left,right) in dp[i]:
            return dp[i][(left,right)]
        w = inf
        num = numbers[i]
        if num != right:
            w = min(w, solve(i+1, num, right) + W[left][num])
        if num != left:
            w = min(w, solve(i+1, left, num) + W[right][num])
        dp[i][(left,right)] = w
        return w
    
    return solve(0, 4, 6)

print(solution("1756"))