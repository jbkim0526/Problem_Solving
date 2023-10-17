import sys 
input = sys.stdin.readline 

t = int(input())

for _ in range(t):
    n = int(input())
    islands = [tuple(map(int,input().split())) for _ in range(n)]
    islands.sort(key = lambda x: -x[1])

    cury, newy = islands[-1][1], 0
    for i in range(n-1,-1,-1):
        x,y = islands[i]
        if y != cury:
            newy += 1
            cury = y
        islands[i] = (x,newy)

    islands.sort(key = lambda x: (x[0]))

    dp = [0]*(2*n)

    def query(l,r):
        l += n ; r += n
        res = 0
        while l < r:
            if l & 1:
                res += dp[l]
                l += 1
            if r & 1:
                r -= 1
                res += dp[r]
            l >>= 1; r >>= 1
        return res 

    def update(x):
        x += n 
        while x >= 1:
            dp[x] += 1
            x >>= 1
            
    ans = 0

    for x,y in islands:
        ans += query(y,n)
        update(y)

    print(ans)