from collections import deque

def C(i):
    return dp[i - 1] - psum[i]

N, K = map(int, input().split())
A = [0]  # Padding to make indices match
A += [int(input()) for _ in range(N)]
psum = [0] * (N + 1)
for i in range(1, N + 1):
    psum[i] = psum[i - 1] + A[i]

dp = [0] * (N + 1)
dq = deque()

for i in range(1, N + 1):
    while dq and dq[0] < i - K:
        dq.popleft()
    while dq and C(dq[-1]) <= C(i):
        dq.pop()
    dq.append(i)
    dp[i] = psum[i] + C(dq[0])
    if i <= K:
        dp[i] = max(dp[i], psum[i])

print(dp[N])