import sys
input = sys.stdin.readline 

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

if n == 1:
    print(l[0])
else:
    dp1 = [l[0],l[1]]+[0]*(n-2)
    dp2 = [0,l[0]+l[1]]+[0]*(n-2)
    dp3 = [0,l[0]]+[0]*(n-2)

    for i in range(2,n):
        dp1[i] = dp3[i-1] + l[i]
        dp2[i] = dp1[i-1] + l[i]
        dp3[i] = max(dp1[i-1],dp2[i-1],dp3[i-1])

    print(max(dp1[n-1],dp2[n-1],dp3[n-1]))