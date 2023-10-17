import sys 
from math import factorial,gcd
input = sys.stdin.readline 

n = int(input())
numbers = [input()[:-1] for _ in range(n)]
k = int(input())
dp = [dict() for _ in range(n)]

def track(depth,num,status):
    if depth == n:
        return 0 if (int(num) % k) else 1

    if status in dp[depth]:
        return dp[depth][status]

    ans = 0
    for i in range(n):
        # 이미 사용한 숫자는 pass
        if status & (1<<i):
            continue
        # 해당 숫자를 현 위치에 사용했을 때 최소값을 더해줌.
        ans += track(depth+1,num+numbers[i], status|(1<<i))

    # 현재의 위치까지 사용한 숫자가 이것일 때 
    dp[depth][status] = ans 
    return ans

count = track(0,'',0)
total = factorial(n)
d = gcd(count,total)
print(count,total)
print(str(count//d)+"/"+str(total//d))



        

    