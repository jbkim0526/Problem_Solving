import sys 
input = sys.stdin.readline 

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
start = lines[0][0]
end = lines[0][1]
ans = 0

for a,b in lines:
    if a <= end:
        end = max(end,b)
    else:
        ans += end-start 
        start = a 
        end = b

ans += end-start  

print(ans)
