import sys 
from math import factorial,gcd
input = sys.stdin.readline 

n = int(input())
numbers = [int(input()) for _ in range(n)]
k = int(input())

# 현재 r = j 일때 숫자 i를 쓰면 다음 r 
remainders = [[(j*10**len(str(numbers[i]))+numbers[i]) % k for j in range(k)] for i in range(n)]
dp = [[0 for _ in range(k)] for _ in range(1<<n)]
dp[0][0] = 1

for status in range(1<<n):
    for i in range(n):
        if status & (1<<i):
            continue 
        # 현재 status 만큼의 숫자를 썼고 -> 아직 안 쓴 숫자 i를 찾았음.
        # 현재의 나머지가 0~k-1인 모든 경우에 대해서 i를 사용함
        
        for j in range(k):
            dp[status|(1<<i)][remainders[i][j]] += dp[status][j]

# 모든 숫자를 쓴 status에서 r = 0인 개수가 count
count = dp[(1<<n)-1][0]
total = factorial(n)
d = gcd(count,total)
print(str(count//d)+"/"+str(total//d))



        

    