import sys 
input = sys.stdin.readline 

N = int(input())
weights = list(map(int, input().split()))

dp = [set() for _ in range(N+1)]
dp[0].add(0)

for i in range(N):
    weight = weights[i]

    for num in dp[i]:
        dp[i+1].add(num)
        dp[i+1].add(num+weight)
        if num-weight > 0:
            dp[i+1].add(num-weight)
        if weight - num >0:
            dp[i+1].add(weight-num)
    
T = int(input())
nums = list(map(int, input().split()))
answers = []
for num in nums:
    answers.append( "Y" if num in dp[N] else "N")

print(" ".join(answers))
