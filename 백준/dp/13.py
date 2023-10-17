import sys 
input = sys.stdin.readline 

N =  int(input())
l =  list(map(int, input().split()))

dp1 = [1]+[0]*(N-1)
dp2 = [1]+[0]*(N-1)
dp3 = [1]+[0]*(N-1)

for i in range(1,N):
    res1 = [0]
    res2 = [0]
    res3 = [0]
    for j in range(i):
        if l[i] > l[j]:
            res1.append(dp1[j])
        if l[i] < l[j]:
            res2.append(dp2[j]) 
            res3.append(dp1[j])
            res3.append(dp3[j])

    dp1[i] = max(res1) + 1
    dp2[i] = max(res2) + 1
    dp3[i] = max(res3) + 1

print(dp1,dp2,dp3)
print(max(dp1[N-1],dp2[N-1],dp3[N-1]))
            
