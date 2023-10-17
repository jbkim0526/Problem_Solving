import sys
input = sys.stdin.readline 

N = int(input())

l = []
dp = [-1]
res = 0

for i in range(N):
    l.append(tuple(map(int, input().split())))

l.sort()

for _ , target in l:
    if target > dp[-1]:
        dp.append(target)
    else:
        left = 0
        right = len(dp)-1
        while left < right:
            mid = (left +right) // 2
            if dp[mid] < target:
                left = mid+1
            else:
                right = mid
        dp[left] = target

print(N - len(dp)+1)