import sys
input = sys.stdin.readline

A = input()[:-1]
B = input()[:-1]
dp = [0]*(len(A))

for elem in B:
    cum = 0
    for i in range(len(A)):
        if cum < dp[i]:
            cum = dp[i]
        elif elem == A[i]:
            dp[i] = cum+1

N = max(dp)
print(N)
print(dp)
if N != 0:
    count = 1
    ans = ""
    for i in range(len(A)):
        
        if count > N:
            break
        num = dp[i]
        if num != count:
            continue 
        ans += str(A[i])
        count += 1
    print(ans)


# 반례 : 
# ABCDEF
# BEFDEFACDFABZ