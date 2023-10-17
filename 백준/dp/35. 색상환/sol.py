import sys 
input = sys.stdin.readline 

n,k  = int(input()),int(input())

# dp1: 첫번째를 선택 dp2: 첫번쨰를 선택x
dp1 = [[0 for _ in range(k+1)] for _ in range(n)]
dp2 = [[0 for _ in range(k+1)] for _ in range(n)]

for i in range(n):
    dp1[i][1] = 1
for i in range(1,n):
    dp2[i][1] = i

for j in range(2,k+1):
    for i in range(2,n):    
        dp1[i][j] = (dp1[i-2][j-1] + dp1[i-1][j]) % 1000000003
        dp2[i][j] = (dp2[i-2][j-1] + dp2[i-1][j]) % 1000000003

print((dp1[n-2][k]+dp2[n-1][k]) % 1000000003)





 






    



