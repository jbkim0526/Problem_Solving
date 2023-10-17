from bisect import bisect_left
import sys 
input = sys.stdin.readline 

N = int(input())
l = list(map(int, input().split()))
dp = [l[0]]
record = [0]
ans = []

for i in range(1,N):
    num = l[i]
    index = bisect_left(dp,num)
    if len(dp) == index:
        record.append(len(dp))
        dp.append(num)
    else:
        dp[index] = num
        record.append(index)

m = len(dp)-1
print(m+1)

for i in range(N-1,-1,-1):
    if m < 0 :
        break
    if record[i] != m:
        continue 
    ans.append(str(l[i]))
    m -= 1

ans.reverse()
print(" ".join(ans))

