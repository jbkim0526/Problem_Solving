import sys
input = sys.stdin.readline 

N = int(input())
l = list(map(int,input().split()))

dp = [-1]

for target in l:
    if target > dp[-1]:
        dp.append(target)
    else:
        left = 0
        right = len(dp)-1

        while left < right:
            mid = (left+right)//2
            if dp[mid] < target:
                left = mid+1
            else:
                right = mid
        dp[left] = target
print(len(dp)-1)


            