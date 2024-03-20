from math import inf

N = int(input())
numbers = []
ops = []

for i,s in enumerate(input()):
    if i % 2 == 0:
        numbers.append(int(s))
    else:
        ops.append(s)

N= len(numbers)

# dp[i][j] : index i~j 번째 숫자까지 최대
# dp2 : 최소
dp = [[-inf for _ in range(N)] for _ in range(N)]
dp2 = [[inf for _ in range(N)] for _ in range(N)]

# 길이가 1인 것 채우기
for i in range(N):
    dp[i][i] = numbers[i]
    dp2[i][i] = numbers[i]

 
# 길이가 2에서 부터 N까지
for length in range(2,N+1):
    
    for i in range(N):
        j = i+length-1
        if j > N-1:
            break
        #print(i,j)
        # 숫자가 1 ~ length-1 까지
        for l in range(1,length):
            
            # 연산이 - 인경우 dp1 = 최대 - 최소, dp2 = 최소 - 최대
            if ops[i+l-1] == "-":
                dp[i][j] = max(dp[i][j], dp[i][i+l-1]- dp2[i+l][j])
                dp2[i][j] = min(dp2[i][j], dp2[i][i+l-1]-dp[i+l][j])
            # + 가 최대려면 최대 + 최대 , 최소 : 최소 + 최소
            elif ops[i+l-1] == "+":
                dp[i][j] = max(dp[i][j], dp[i][i+l-1] + dp[i+l][j])
                dp2[i][j] = min(dp2[i][j], dp2[i][i+l-1]+ dp2[i+l][j])
            # * 이 최대려면 최대*최대 or 최소*최소, 최소려면 최대*최소 or 최소*최대
            else:
                dp[i][j] = max(dp[i][j], dp[i][i+l-1]*dp[i+l][j],dp2[i][i+l-1]*dp2[i+l][j])
                dp2[i][j] = min(dp2[i][j], dp[i][i+l-1]*dp2[i+l][j],dp2[i][i+l-1]*dp[i+l][j])

print(dp[0][N-1])